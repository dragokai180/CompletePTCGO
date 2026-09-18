"""Atomic Lost Zone instructions shared by historical/reprinted cards.

Return True only after handling a complete attack, so generic searches,
damage formulas, and coin riders cannot reinterpret the same instruction.
"""
import random
import re

from spirit.game.attributes import PokemonTypes, SpecialConditions
from spirit.game.data_utils import subtypes_for
from spirit.game.session.effects import is_energy_card, is_pokemon_card
from spirit.game.session.passives import Passive


async def move_energy_units_to_lost_zone(ctx, energies, amount):
    """Lose attached Energy value, not a fixed number of physical cards."""
    from spirit.game.session.legal_actions import energy_provided_count
    energies = list(energies)
    if not energies or amount <= 0:
        return []
    if sum(energy_provided_count(e, ctx.board) for e in energies) <= amount:
        picks = energies  # Resolve as much as possible, including copied attacks.
    else:
        ids = await ctx.session.prompt_energy_unit_picker(
            ctx.player_id, ctx.attacker.entity_id, energies, amount,
            'Choose Energy to put in the Lost Zone')
        picks = [e for e in energies if e.entity_id in ids]
    await ctx.move_to_lost_zone(picks)
    return picks


class _LostAttackKnockouts(Passive):
    """A replacement for KOs caused by this resolution, never later attacks."""
    def __init__(self, attack_ctx):
        self.attack_ctx = attack_ctx

    def knockout_destination_for(self, pokemon, ctx, carrier):
        if ctx is self.attack_ctx and pokemon.owning_player_id != ctx.player_id \
                and pokemon.entity_id in ctx.attack_damage and not ctx.effects_blocked(pokemon):
            return 'lostZone'
        return None

    knockout_attachment_destination = knockout_destination_for


def hand_energy_payment(text):
    return re.search(
        r'you may put (\d+) (grass|fire|water|lightning|psychic|fighting|darkness|metal|fairy) '
        r'energy cards from your hand in the lost zone\. if you do,', text)


def payment_candidates(cards, match):
    from spirit.game.card_effects.pokemon import energy_provides_type
    kind = getattr(PokemonTypes, match[2].upper()).value
    return [c for c in cards if is_energy_card(c) and energy_provides_type(c, kind)]


async def resolve_lost_zone_ability(ctx, text):
    payment = hand_energy_payment(text)
    if not payment or "your opponent's active pokémon is now paralyzed" not in text:
        return False
    count = int(payment[1])
    cards = payment_candidates(ctx.hand(), payment)
    if len(cards) < count or ctx.opponent_active() is None:
        ctx.suppress_announce = True
        return True
    if not await ctx.ask_yes_no(f'Use {ctx.ability.title}?'):
        ctx.suppress_announce = True
        return True
    picks = await ctx.choose_cards(cards, count, minimum=count,
                                   prompt='Choose Energy cards to put in the Lost Zone')
    if len(picks) != count:
        return True
    await ctx.move_to_lost_zone(picks)
    if all(c in ctx.lost_zone() for c in picks):
        await ctx.apply_special_condition(ctx.opponent_active(), SpecialConditions.PARALYZED)
    return True


async def resolve_lost_zone_attack(ctx, text, printed):
    if 'lost zone' not in text:
        return False

    search = re.fullmatch(
        r'search your deck for (?:1|a) pokémon and put it in the lost zone\. '
        r'(?:shuffle your deck afterward|then, shuffle your deck)\.', text)
    if search:
        picks = await ctx.search_deck(is_pokemon_card, 1, minimum=0,
                                      prompt='Choose a Pokémon to put in the Lost Zone')
        await ctx.move_to_lost_zone(picks)
        await ctx.shuffle_deck()
        return True

    count_damage = re.fullmatch(
        r'(?:this attack does|does(?: \d+ damage plus)?) (\d+) (more )?damage for each '
        r'of your pokémon(?:, except [^,]+ pokémon,)? in the lost zone\.', text)
    if count_damage:
        cards = [c for c in ctx.lost_zone() if is_pokemon_card(c)]
        if 'except' in text:
            cards = [c for c in cards if not any('prism' in s.casefold()
                     for s in (subtypes_for(c.archetype_id) or []))]
        await ctx.deal_damage((printed if count_damage[2] else 0) + int(count_damage[1]) * len(cards))
        return True

    if text.startswith('choose 1 pokémon from your hand and put it in the lost zone.'):
        cards = [c for c in ctx.hand() if is_pokemon_card(c)]
        picks = await ctx.choose_cards(cards, 1, minimum=1,
            prompt='Choose a Pokémon to put in the Lost Zone') if cards else []
        if picks:
            await ctx.move_to_lost_zone(picks)
            if all(c in ctx.lost_zone() for c in picks):
                await ctx.deal_damage(printed)
        return True

    if text == "choose 1 card from your opponent's hand without looking and put it in the lost zone.":
        if printed:
            await ctx.deal_damage(printed)
        cards = list(ctx.hand(ctx.opponent_id))
        if cards:
            await ctx.move_to_lost_zone([random.choice(cards)])
        return True

    if text.startswith('flip a coin. if heads, choose 1 energy card attached to 1 of your opponent') \
            and text.endswith('and put it in the lost zone.'):
        if printed:
            await ctx.deal_damage(printed)
        if (await ctx.flip_coins(1, ctx.ability.title))[0]:
            cards = [e for p in ctx.opponent_pokemon_in_play() for e in ctx.attached_energies(p)]
            picks = await ctx.choose_cards(cards, 1, minimum=1,
                prompt='Choose an Energy to put in the Lost Zone') if cards else []
            await ctx.move_to_lost_zone(picks)
        return True

    if text == ('flip a coin. if heads, the defending pokémon is now paralyzed. '
                'if tails, put 1 energy card attached to the defending pokémon in the lost zone.'):
        if printed:
            await ctx.deal_damage(printed)
        if (await ctx.flip_coins(1, ctx.ability.title))[0]:
            await ctx.apply_special_condition(ctx.defender, SpecialConditions.PARALYZED)
        else:
            cards = list(ctx.attached_energies(ctx.defender))
            picks = await ctx.choose_cards(cards, 1, minimum=1,
                prompt='Choose an Energy to put in the Lost Zone') if cards else []
            await ctx.move_to_lost_zone(picks)
        return True

    # Lost Boomerang-GX: choose distinct targets; only damage KOs are redirected.
    multi_ko = re.match(r'this attack does (\d+) damage to (\d+) of your opponent\'s pokémon\.', text)
    if multi_ko and 'if a pokémon is knocked out by this damage' in text \
            and 'put that pokémon and all cards attached to it in the lost zone' in text:
        targets = list(ctx.opponent_pokemon_in_play())
        count = min(int(multi_ko[2]), len(targets))
        picks = await ctx.choose_cards(targets, count, minimum=count,
                                      prompt='Choose Pokémon to damage') if count else []
        ctx.add_temporary_passive(ctx.attacker, _LostAttackKnockouts(ctx),
                                  ctx.session.turn_state.turn_number)
        for target in picks:
            await ctx.deal_damage(int(multi_ko[1]), target=target,
                                  ignore_weakness=True, ignore_resistance=True)
        return True
    return False
