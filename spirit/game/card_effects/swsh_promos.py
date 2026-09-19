"""Compound promo effects whose targets/quantities need explicit resolution."""
import random

from spirit.game.attributes import AttrID, PokemonTypes as T
from spirit.game.data_utils import subtypes_for, Triggers
from spirit.game.session.effects import is_basic_energy, is_basic_pokemon, is_pokemon_card, is_supporter_card
from spirit.game.session.passives import Passive, effective_pokemon_types, effective_bench_capacity, energy_provided_options


async def teapot(ctx):
    if ctx.source is not ctx.my_active() or ctx.damage_amount <= 0 \
            or ctx.damaged_by is None or ctx.damaged_by.owning_player_id == ctx.player_id:
        return
    hand = ctx.hand(ctx.opponent_id)
    if hand:
        chosen = random.choice(hand)
        await ctx.reveal_cards([chosen])
        await ctx.put_on_bottom_of_deck(chosen)


class ProtectiveDNA(Passive):
    def modify_damage_taken(self, calc, carrier):
        if calc.is_attack and calc.is_opposing and calc.attacker is not None \
                and calc.target.owning_player_id == carrier.owning_player_id \
                and 'VSTAR' in subtypes_for(calc.attacker.archetype_id):
            calc.amount = max(0, calc.amount - 30)


async def twinkle_gathering(ctx):
    kinds = {kind for p in ctx.my_pokemon_in_play() for kind in effective_pokemon_types(ctx.board, p)}
    picked = await ctx.search_deck(count=len(kinds), minimum=0)
    await ctx.put_in_hand(picked)
    await ctx.shuffle_deck()


async def mixed_call(ctx):
    groups = await ctx.search_deck_groups([
        (is_pokemon_card, 1, 'Pokémon'), (is_supporter_card, 1, 'Supporter')])
    await ctx.put_in_hand([c for group in groups for c in group], reveal=True)
    await ctx.shuffle_deck()


async def promo_acceleration(ctx):
    title = ctx.ability.title
    await ctx.deal_damage()
    kind = T.WATER if title == 'Grand Falls' else T.LIGHTNING
    predicate = is_basic_energy if title == 'Flight Up' else lambda e: any(
        kind.value in option for option in energy_provided_options(ctx.board, e))
    if title == 'Grand Falls':
        picks = await ctx.search_deck(predicate, 3)
    else:
        pool = [e for e in ctx.discard_pile() if predicate(e)]
        picks = await ctx.choose_cards(pool, 3, minimum=0)
    targets = ctx.my_bench() if title in ('Grand Falls', 'Flight Up') else ctx.my_pokemon_in_play()
    fixed = None
    for energy in picks:
        target = fixed or (await ctx.choose_pokemon(targets, 'Choose a Pokémon') if targets else None)
        if target is None:
            break
        await ctx.attach_energy(energy, target)
        if title != 'Grand Falls':
            fixed = target
    if title == 'Grand Falls':
        await ctx.shuffle_deck()


async def pursuit_claw(ctx):
    target = await ctx.choose_pokemon(ctx.opponent_bench(), 'Choose a Benched Pokémon')
    if target is not None:
        await ctx.deal_damage(20 * ((ctx.max_hp(target) - target.get_attribute(AttrID.HP, 0)) // 10),
                              target, apply_modifiers=False)


async def psychic_javelin(ctx):
    await ctx.deal_damage()
    targets = [p for p in ctx.opponent_bench() if any(
        s in subtypes_for(p.archetype_id) for s in ('V', 'VMAX', 'VSTAR', 'V-UNION'))]
    if targets:
        target = await ctx.choose_pokemon(targets, 'Choose a Benched Pokémon V')
        if target is not None:
            await ctx.deal_damage(60, target, apply_modifiers=False)


async def pulling_currents(ctx):
    viewed = await ctx.reveal_hand(ctx.opponent_id, ctx.player_id)
    pool = [c for c in viewed if is_basic_pokemon(c) and ctx.can_bench_pokemon(c)]
    free = max(0, effective_bench_capacity(ctx.board, ctx.opponent_id) - len(ctx.opponent_bench()))
    picks = await ctx.choose_cards(pool, min(2, free), minimum=0, display_cards=viewed)
    for card in picks:
        await ctx.bench_pokemon(card)


async def coin_draw(ctx):
    heads = 0
    while (await ctx.flip_coins(1))[0]:
        heads += 1
    await ctx.draw_cards(heads)


def configure_promo(card):
    callbacks = {'Twinkle Gathering': twinkle_gathering, 'Mixed Call': mixed_call,
                 'Flight Up': promo_acceleration, 'Tail Charge': promo_acceleration,
                 'Grand Falls': promo_acceleration, 'Pursuit Claw': pursuit_claw,
                 'Psychic Javelin': psychic_javelin, 'Pulling Currents': pulling_currents,
                 'Flaring Dash': coin_draw, 'Shake and Gather': coin_draw}
    for ability in card.abilities:
        if '1 VSTAR Power' in ability.game_text:
            ability.vstar = True
        if ability.title == 'Crystal Star':
            ability.locks_next_turn = False
        if ability.title in callbacks:
            ability.effect = callbacks[ability.title]
        elif ability.title == 'Teapot of Surprises':
            ability.passive = None
            ability.effect = teapot
            ability.trigger = Triggers.ON_DAMAGED_BY_ATTACK
        elif ability.title == 'Protective DNA':
            ability.passive = ProtectiveDNA()
