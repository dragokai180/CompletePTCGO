"""Printed rules for the main 30th Celebration set (30C / ME55).

Unusual clauses are explicit here. Ordinary coin flips, conditions and simple
damage use the existing rules helpers, not a second rules-text interpreter.
"""
from spirit.game.attributes import AttrID, PokemonTypes, SpecialConditions
from spirit.game.data_utils import Attack, Activations, Triggers, def_for, subtypes_for
from spirit.game.card_effects.bw_era import _name, _energy_count, _BWTurnShield
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.session.effects import (
    full_stack, is_basic_energy, is_basic_pokemon, is_energy_card,
    is_item_card, is_pokemon_card, is_pokemon_tool, is_stadium_card,
    is_supporter_card,
)
from spirit.game.session.passives import (
    Passive, effective_max_hp, effective_pokemon_types, effective_bench_capacity,
    energy_provided_options, healing_blocked,
)


def area(entity):
    parent = getattr(entity, 'parent', None)
    return parent.get_attribute(AttrID.NAME) if parent is not None else None


def board_for(entity):
    root = entity
    while getattr(root, 'parent', None) is not None:
        root = root.parent
    return getattr(root, '_board_state', None)


def energy_units(board, pokemon, kind):
    return sum(max((option.count(kind.value) for option in energy_provided_options(board, e)), default=0)
               for e in board.attached_energies(pokemon))


def basic_of(card, kind):
    return is_basic_energy(card) and energy_provides_type(card, kind.value)


def damage_on(board, pokemon):
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0))


class CelebrationPassive(Passive):
    def __init__(self, title):
        self.title = title

    def max_hp_bonus(self, pokemon, carrier):
        if self.title == 'Scale Up' and pokemon is carrier:
            board = board_for(carrier)
            if board is not None and energy_units(board, carrier, PokemonTypes.GRASS) >= 6:
                return 250
        return 0

    def modify_weakness(self, calc, carrier):
        if self.title == 'Supereffective Pheromones' and calc.to_active:
            if any(_name(p) == 'Volbeat' for p in calc.board.pokemon_in_play(carrier.owning_player_id)):
                calc.weakness_multiplier = 3

    def modify_damage_dealt(self, calc, carrier):
        if self.title == 'Lonely Gaze' and area(carrier) == 'activePokemonArea' \
                and calc.is_attack and calc.attacker is not None \
                and calc.attacker.owning_player_id != carrier.owning_player_id \
                and area(calc.attacker) == 'activePokemonArea':
            calc.amount = max(0, calc.amount - 20)

    def prevents_damage(self, calc, carrier):
        return self.title == 'Keep Hidden' and calc.target is carrier \
            and area(carrier) == 'bench' and calc.is_attack and calc.is_opposing

    def blocks_attack_effects(self, target, carrier):
        return self.title == 'Keep Hidden' and target is carrier and area(carrier) == 'bench'

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if self.title == 'Nighttime Byway' and area(carrier) == 'bench' \
                and pokemon.owning_player_id == carrier.owning_player_id \
                and area(pokemon) == 'activePokemonArea':
            return max(0, cost - 2)
        return cost

    def prevents_healing(self, target, carrier):
        return self.title == 'Life-Locked' and area(target) == 'activePokemonArea' \
            and target.owning_player_id != carrier.owning_player_id

    def granted_attacks(self, board, pokemon, carrier):
        if self.title != 'Memory Helix' or pokemon is not carrier:
            return []
        return [a for p in board.pokemon_in_play(carrier.owning_player_id)
                if area(p) == 'bench'
                for a in getattr(def_for(p.archetype_id), 'abilities', [])
                if isinstance(a, Attack)]

    async def after_attack_damage(self, ctx, carrier):
        if self.title != 'Counterattack Grouping':
            return
        damaged = [ctx.board.get_entity(eid) for eid in ctx.attack_damage_active]
        if ctx.attacker.owning_player_id == carrier.owning_player_id or not any(
                p is not None and p.owning_player_id == carrier.owning_player_id
                and _name(p) in ('Wishiwashi', 'Wishiwashi ex') for p in damaged):
            return
        # Use an Ability context: these are counters, not attack damage, and
        # source-sensitive protections must see the defending Wishiwashi.
        from spirit.game.session.effects import EffectContext
        ability = next(a for a in def_for(carrier.archetype_id).abilities if a.title == self.title)
        reaction = EffectContext(ctx.session, carrier.owning_player_id, carrier, ability)
        await reaction.deal_damage(30, ctx.attacker, as_counters=True)
        ctx.knockouts.extend(p for p in reaction.knockouts if p not in ctx.knockouts)
        await ctx.session._flush_effect_runs(reaction)


class LightningWeakness(Passive):
    def modify_weakness(self, calc, carrier):
        if calc.target is carrier:
            calc.weak_types = [PokemonTypes.LIGHTNING.value]
            calc.weakness_multiplier = 2


class AttackBan(Passive):
    def blocks_attacks(self, pokemon, carrier):
        return pokemon is carrier


BIRD_TYPES = {'Fiery Flapping': PokemonTypes.FIRE,
              'Frosty Flapping': PokemonTypes.WATER,
              'Flash-Pop Flapping': PokemonTypes.LIGHTNING}


def ability_condition(title):
    def condition(board, pid, source=None):
        if source not in board.pokemon_in_play(pid):
            return False
        if title in BIRD_TYPES:
            names = {_name(p) for p in board.pokemon_in_play(pid)}
            return {'Articuno', 'Zapdos', 'Moltres'} <= names and any(
                basic_of(c, BIRD_TYPES[title]) for c in board.find_player_area(pid, 'hand').children)
        if title == 'Sunrise':
            return area(source) == 'bench' and bool(board.find_player_area(pid, 'deck').children)
        if title == 'Guiding Dance':
            return bool(board.find_player_area(pid, 'deck').children)
        if title == 'Share Happiness':
            return any(damage_on(board, p) and not healing_blocked(board, p)
                       for p in board.pokemon_in_play(pid))
        return True
    return condition


async def ability_effect(ctx):
    title = ctx.ability.title
    if title in BIRD_TYPES:
        if not ability_condition(title)(ctx.board, ctx.player_id, ctx.source):
            return
        chosen = await ctx.choose_cards([c for c in ctx.hand() if basic_of(c, BIRD_TYPES[title])], 1,
                                        prompt='Choose a basic Energy to attach')
        if chosen:
            await ctx.attach_energy(chosen[0], ctx.source, counts_as_attachment=True)
    elif title in ('Guiding Dance', 'Sunrise'):
        if not ability_condition(title)(ctx.board, ctx.player_id, ctx.source):
            return
        if title == 'Guiding Dance' and not (await ctx.flip_coins(1))[0]:
            return
        picks = await ctx.search_deck(is_pokemon_card if title == 'Guiding Dance'
                                     else lambda c: basic_of(c, PokemonTypes.METAL),
                                     count=1 if title == 'Guiding Dance' else 2)
        if title == 'Guiding Dance':
            await ctx.put_in_hand(picks, reveal=True)
        else:
            for c in picks:
                await ctx.attach_energy(c, ctx.source)
        await ctx.shuffle_deck()
    elif title == 'Share Happiness':
        pool = [p for p in ctx.my_pokemon_in_play() if damage_on(ctx.board, p)
                and not healing_blocked(ctx.board, p)]
        target = await ctx.choose_pokemon(pool, 'Choose a Pokémon to heal')
        if target is not None:
            await ctx.heal(30, target)
    elif title == 'Fainting Spell':
        if ctx.ko_from_attack and ctx.ko_attacker is not None and (await ctx.flip_coins(1))[0]:
            await ctx.knock_out(ctx.ko_attacker)
    elif title == 'Good Sleep':
        if 'Asleep' in (ctx.source.get_attribute(AttrID.SPECIAL_CONDITIONS) or []):
            await ctx.heal(10000, ctx.source)


async def attach_selected(ctx, cards, one_target=False):
    target = None
    for c in cards:
        if target is None or not one_target:
            target = await ctx.choose_pokemon(ctx.my_pokemon_in_play(), 'Choose a Pokémon to attach the Energy to')
        if target is not None:
            await ctx.attach_energy(c, target)


async def search_to_hand(ctx, predicate, count=1, minimum=0):
    picks = await ctx.search_deck(predicate, count=count, minimum=minimum,
                                  reveal_result=predicate is not None)
    await ctx.put_in_hand(picks, reveal=predicate is not None)
    await ctx.shuffle_deck()


async def attack_effect(ctx):
    title = ctx.ability.title
    if title == 'Energy Gift':
        picks = await ctx.search_deck(is_basic_energy, count=2)
        await attach_selected(ctx, picks)
        await ctx.shuffle_deck()
    elif title == 'Sacred Breath':
        await ctx.discard_cards(list(ctx.attached_energies(ctx.attacker)))
        target = await ctx.choose_pokemon(ctx.my_bench(), 'Choose a Benched Pokémon to heal')
        if target is not None:
            await ctx.heal(10000, target)
    elif title == 'Cheerful Flame':
        await ctx.deal_damage(70 * ctx.prizes_taken())
    elif title in ('Laser Flame', 'Nitro Thunder'):
        kind = 'lightning' if title == 'Laser Flame' else 'fire'
        await ctx.deal_damage(80 + (80 if _energy_count(ctx, ctx.attacker, kind) else 0))
    elif title == 'Ferry Across':
        await search_to_hand(ctx, is_supporter_card)
    elif title == 'Geonavigation':
        await search_to_hand(ctx, is_stadium_card, 2)
    elif title == 'Wormhole':
        await ctx.deal_damage(100)
        chosen = await ctx.choose_pokemon(ctx.my_bench(), 'Choose your new Active Pokémon')
        if chosen is not None and await ctx.switch_active(ctx.player_id, chosen):
            other = await ctx.choose_pokemon(ctx.opponent_bench(), 'Choose your new Active Pokémon', player_id=ctx.opponent_id)
            if other is not None:
                await ctx.switch_active(ctx.opponent_id, other)
    elif title == 'Stealthy Slash':
        target = await ctx.choose_pokemon(ctx.opponent_pokemon_in_play(), 'Choose a Pokémon to attack')
        if target is not None:
            await ctx.deal_damage(3 * damage_on(ctx.board, target), target)
    elif title == 'Pika Chain':
        await ctx.deal_damage(40 * sum(_name(p) in ('Pikachu', 'Pikachu ex') for p in ctx.my_pokemon_in_play()))
    elif title == 'Overwriting Bolt':
        target = ctx.defender
        await ctx.deal_damage(10)
        if target is not None and not ctx.effects_blocked(target):
            ctx.add_passive_through_own_next_turn(target, LightningWeakness())
    elif title == 'Charge-Up Dash':
        count = await ctx.flip_until_tails()
        if count:
            picks = await ctx.search_deck(lambda c: basic_of(c, PokemonTypes.LIGHTNING), count=count)
            for c in picks:
                await ctx.attach_energy(c, ctx.attacker)
        await ctx.shuffle_deck()
    elif title == 'Tropical Vibes':
        await ctx.apply_special_condition(ctx.attacker, SpecialConditions.ASLEEP)
        await ctx.draw_until(6)
    elif title == 'Fighting Lightning':
        await ctx.deal_damage(20 + (80 if ctx.defender is not None and 'ex' in subtypes_for(ctx.defender.archetype_id) else 0))
    elif title == 'Pika-Pika Parade':
        room = max(0, effective_bench_capacity(ctx.board, ctx.player_id) - len(ctx.my_bench()))
        picks = await ctx.search_deck(lambda c: is_basic_pokemon(c) and ctx.can_bench_pokemon(c), count=room)
        for c in picks:
            await ctx.bench_pokemon(c)
        await ctx.shuffle_deck()
    elif title == 'Zip-Zap Frenzy':
        while True:
            pool = [c for c in ctx.hand() if is_basic_energy(c)]
            if not pool:
                break
            chosen = await ctx.choose_cards(pool, 1, minimum=0, submit_on_pick=True,
                                            prompt='Choose a basic Energy, or Done')
            if not chosen:
                break
            target = await ctx.choose_pokemon(ctx.my_pokemon_in_play(), 'Choose a Pokémon')
            if target is None or not await ctx.attach_energy(chosen[0], target, counts_as_attachment=True):
                break
    elif title == 'Select a Snack':
        cards = list(ctx.deck_top(3))
        await ctx.discard_cards(cards)
        chosen = await ctx.choose_cards([c for c in cards if c in ctx.discard_pile()], 1,
                                        prompt='Choose one of the cards just discarded')
        await ctx.put_in_hand(chosen, reveal=True)
    elif title == 'Empower':
        chosen = await ctx.choose_cards([c for c in ctx.discard_pile() if is_basic_energy(c)], 2, minimum=0,
                                        prompt='Choose up to 2 basic Energy')
        await attach_selected(ctx, chosen, one_target=True)
    elif title == 'Photon Bullets':
        for p in list(ctx.opponent_pokemon_in_play()):
            if 'ex' in subtypes_for(p.archetype_id):
                await ctx.deal_damage(50, p)
    elif title == 'Miraculous Shine':
        for p in list(ctx.opponent_pokemon_in_play()):
            if not ctx.effects_blocked(p):
                await ctx.devolve_pokemon(p, steps=1, destination='hand')
    elif title == 'Solar Beatdown':
        await ctx.deal_damage(30 * len(ctx.my_pokemon_in_play()))
    elif title == 'Colorful Harmony':
        kinds = {kind for p in ctx.my_pokemon_in_play() for c in ctx.attached_energies(p)
                 if is_basic_energy(c) for option in energy_provided_options(ctx.board, c) for kind in option}
        await ctx.deal_damage(50 * len(kinds))
    elif title == 'Comforting Aroma':
        p = await ctx.choose_pokemon(ctx.my_bench(), 'Choose a Benched Pokémon to heal')
        if p is not None:
            await ctx.heal(80, p)
    elif title == 'Midnight Ray':
        await ctx.deal_damage(20 + 20 * sum(is_energy_card(c) for c in ctx.discard_pile()))
    elif title == 'Strolls So Much':
        if (await ctx.flip_coins(1))[0]:
            await search_to_hand(ctx, None, minimum=1)
    elif title == 'Quaking Fist':
        await ctx.deal_damage(60)
        ctx.require_trainer_flip(ctx.opponent_id)
    elif title == 'Counter':
        await ctx.deal_damage(10 + ctx.damage_taken_last_turn(ctx.attacker))
    elif title == 'Chaotic Pain':
        target = await ctx.choose_pokemon(ctx.opponent_pokemon_in_play(), 'Choose a Pokémon for 13 damage counters')
        if target is not None:
            await ctx.deal_damage(130, target, as_counters=True)
    elif title == 'Lunatic Claw':
        await ctx.deal_damage(100 + (140 if ctx.defender is not None and damage_on(ctx.board, ctx.defender) else 0))
    elif title == 'Three-Headed Bite':
        heads = sum(await ctx.flip_coins(3))
        if ctx.defender is not None and not ctx.effects_blocked(ctx.defender):
            await ctx.discard_energy_from(ctx.defender, heads)
    elif title == 'Treasure Rush':
        await ctx.deal_damage(10 * ctx.hand_size())
    elif title == 'Wish Granter':
        await ctx.draw_until(7)
    elif title == 'Kaboom Needles':
        for p in list(ctx.opponent_pokemon_in_play()):
            await ctx.deal_damage(50, p)
        await ctx.deal_damage(130, ctx.attacker, apply_modifiers=False)
    elif title == 'Fend Off':
        if ctx.defender is not None and not ctx.effects_blocked(ctx.defender):
            await ctx.discard_cards([c for c in ctx.defender.children if is_pokemon_tool(c)])
        await ctx.deal_damage(20)
    elif title == 'Celebration':
        if ctx.hand_size() == 30:
            taken = await ctx.take_prizes(2)
            if taken:
                await ctx.shuffle_into_deck(list(ctx.hand()))
    elif title == 'Booming Call':
        room = max(0, effective_bench_capacity(ctx.board, ctx.player_id) - len(ctx.my_bench()))
        pool = [c for c in ctx.discard_pile() if is_pokemon_card(c)
                and PokemonTypes.DRAGON.value in (c.get_attribute(AttrID.POKEMON_TYPES) or [])
                and ctx.can_bench_pokemon(c)]
        picks = await ctx.choose_cards(pool, min(3, room), minimum=0, prompt='Choose up to 3 Dragon Pokémon')
        for c in picks:
            await ctx.bench_pokemon(c)
    elif title == 'Surprisingly Transform':
        if (await ctx.flip_coins(1))[0]:
            picks = await ctx.search_deck(is_pokemon_card, count=1)
            if picks:
                await ctx.identity_swap(ctx.attacker, picks[0], destination='deck', transfer=True)
            await ctx.shuffle_deck()
    elif title == 'Fetch and Hide':
        await ctx.reveal_hand(ctx.opponent_id)
        picks = await ctx.choose_cards([c for c in ctx.hand(ctx.opponent_id) if is_item_card(c)], 1,
                                        prompt='Choose an Item to put at the bottom of their deck')
        for c in picks:
            await ctx.put_on_bottom_of_deck(c)
    elif title == 'Bouncy Circle':
        await ctx.deal_damage(30 * sum(ctx.max_hp(p) == 30 for p in ctx.my_bench()))
    elif title == 'Swirling Resentment':
        if ctx.defender is not None:
            counters = max(0, ctx.defender.get_attribute(AttrID.HP, 0) - 50) // 10
            await ctx.deal_damage(counters * 10, ctx.defender, as_counters=True)
    elif title == 'Gnaw Together':
        count = sum(_name(p) == 'Maushold' for p in ctx.my_pokemon_in_play())
        heads = sum(await ctx.flip_coins(count))
        await ctx.discard_cards(list(ctx.deck_top(2 * heads, ctx.opponent_id)))
    else:
        await common_attack(ctx)


CONDITIONS = {
    'Hypnosis': SpecialConditions.ASLEEP, 'Poison Powder': SpecialConditions.POISONED,
    'Singe': SpecialConditions.BURNED,
}
COIN_CONDITIONS = {'Thunder Shock', 'Ice Beam', 'Body Slam'}
RECOIL = {'Volt Tackle': 30, 'Slight Intrusion': 10, 'Thunder': 30, 'Thundering Lightning': 60}
HEAL = {'Mega Drain': 50, 'Nap': 30, 'Aurora Gain': 30}
DRAW = {'Nightime Stroll', 'Rapid Draw', 'Pay Day'}
SPLASH = {'Spark': 20, 'Electrobullet': 20, 'Aura Sphere': 60}
DISCARD = {'Fire Spin': (2, None), 'Psydrive': (1, None),
           'Electro Drift': (2, PokemonTypes.LIGHTNING), 'Collision Course': (2, PokemonTypes.FIGHTING)}
COMMON_ATTACKS = {
    *CONDITIONS, *COIN_CONDITIONS, *RECOIL, *HEAL, *DRAW, *SPLASH, *DISCARD,
    'Luring Glow', 'Rally Back', 'Hide', 'Well-Hidden', 'Agility', 'Wild Kick',
    'Surprise Attack', 'Call for Family', 'Hail', 'Hydro Pump', 'Peer At',
    'Find a Friend', 'Energized Tail', 'Scurry About', 'Targeted Spark', 'Iron Tail',
    'Get Some Air', 'Play Rough', 'Quick Attack', 'Store Up', 'Lightning Crash',
    'Angry Bolt', 'Rage', 'Thunderbolt', 'Sunsteel Strike', 'Thunderous Bolt',
    'Psychic Powers', 'Psychic', 'Teleportation Burst', 'Mysterious Signal',
    'Float Up', 'Eerie Glow', 'Stiffen', 'Shield Press', 'Break Ground', 'Growl',
    'Retaliate', 'Clumsily Clutch', 'Nitpick', 'Swift', 'Reversed Clock',
    'Hardened Blade', 'Slashing Strike', 'Triple Smash', 'Dragon Pulse', 'Screech',
    'Collapse', 'Elemental Blast', 'Shoot Meteors',
}


async def common_attack(ctx):
    """Small, explicit recurring effects; selectors keep private/public rules."""
    title, printed = ctx.ability.title, ctx.ability.damage
    if title in CONDITIONS or title in COIN_CONDITIONS:
        await ctx.deal_damage(printed)
        condition = CONDITIONS.get(title, SpecialConditions.PARALYZED)
        if title not in COIN_CONDITIONS or (await ctx.flip_coins(1))[0]:
            await ctx.apply_special_condition(ctx.defender, condition)
    elif title in RECOIL:
        await ctx.deal_damage(printed)
        await ctx.deal_damage(RECOIL[title], ctx.attacker, apply_modifiers=False)
    elif title in HEAL:
        await ctx.deal_damage(printed)
        await ctx.heal(HEAL[title], ctx.attacker)
    elif title in DRAW:
        await ctx.deal_damage(printed)
        await ctx.draw_cards(1)
    elif title in SPLASH:
        await ctx.deal_damage(printed)
        p = await ctx.choose_pokemon(ctx.opponent_bench(), 'Choose a Benched Pokémon to attack')
        if p is not None:
            await ctx.deal_damage(SPLASH[title], p, apply_modifiers=False)
    elif title in DISCARD:
        await ctx.deal_damage(printed)
        count, kind = DISCARD[title]
        await ctx.discard_energy_units_from(ctx.attacker, count,
            predicate=(lambda c: energy_provides_type(c, kind.value)) if kind is not None else None,
            partial=True)
    elif title in ('Thunderbolt', 'Sunsteel Strike'):
        await ctx.deal_damage(printed)
        await ctx.discard_cards(list(ctx.attached_energies(ctx.attacker)))
    elif title in ('Lightning Crash', 'Shoot Meteors', 'Targeted Spark'):
        if title != 'Targeted Spark':
            cards = [c for c in ctx.attached_energies(ctx.attacker)
                     if title == 'Shoot Meteors' or energy_provides_type(c, PokemonTypes.LIGHTNING.value)]
            await ctx.discard_cards(cards)
        p = await ctx.choose_pokemon(ctx.opponent_pokemon_in_play(), 'Choose a Pokémon to attack')
        if p is not None:
            await ctx.deal_damage({'Lightning Crash': 90, 'Shoot Meteors': 120, 'Targeted Spark': 20}[title], p)
    elif title in ('Luring Glow', 'Scurry About', 'Teleportation Burst'):
        await ctx.deal_damage(printed)
        other = title == 'Luring Glow'
        pool = ctx.opponent_bench() if other else ctx.my_bench()
        chosen = await ctx.choose_pokemon(pool, 'Choose the new Active Pokémon', optional=title == 'Teleportation Burst')
        if chosen is not None:
            await ctx.switch_active(ctx.opponent_id if other else ctx.player_id, chosen)
    elif title in ('Rally Back', 'Retaliate'):
        await ctx.deal_damage(printed + ((90 if title == 'Rally Back' else 100) if ctx.kos_by_attack_last_turn() else 0))
    elif title in ('Hide', 'Well-Hidden', 'Agility'):
        heads = (await ctx.flip_coins(1))[0]
        await ctx.deal_damage(printed)
        if heads:
            ctx.add_passive_through_opponents_turn(ctx.attacker, _BWTurnShield(prevent_all=True))
    elif title in ('Wild Kick', 'Surprise Attack'):
        if (await ctx.flip_coins(1))[0]:
            await ctx.deal_damage(printed)
    elif title in ('Quick Attack', 'Play Rough'):
        await ctx.deal_damage(printed + (20 if (await ctx.flip_coins(1))[0] else 0))
    elif title in ('Iron Tail', 'Triple Smash'):
        heads = await ctx.flip_until_tails() if title == 'Iron Tail' else sum(await ctx.flip_coins(3))
        await ctx.deal_damage(printed * heads)
    elif title == 'Call for Family':
        room = max(0, effective_bench_capacity(ctx.board, ctx.player_id) - len(ctx.my_bench()))
        picks = await ctx.search_deck(lambda c: is_basic_pokemon(c) and ctx.can_bench_pokemon(c), count=min(2, room))
        for c in picks:
            await ctx.bench_pokemon(c)
        await ctx.shuffle_deck()
    elif title == 'Hail':
        for p in list(ctx.opponent_pokemon_in_play()):
            await ctx.deal_damage(30, p)
    elif title == 'Hydro Pump':
        await ctx.deal_damage(printed + 30 * _energy_count(ctx, ctx.attacker, 'water'))
    elif title == 'Psychic':
        await ctx.deal_damage(printed + 40 * _energy_count(ctx, ctx.defender))
    elif title in ('Angry Bolt', 'Rage'):
        await ctx.deal_damage(printed + damage_on(ctx.board, ctx.attacker))
    elif title == 'Peer At':
        await ctx.reveal_hand(ctx.opponent_id)
    elif title in ('Find a Friend', 'Energized Tail'):
        await search_to_hand(ctx, is_pokemon_card if title == 'Find a Friend' else is_energy_card)
    elif title == 'Get Some Air':
        await ctx.cure_all_conditions(ctx.attacker)
    elif title in ('Store Up', 'Reversed Clock'):
        pool = [c for c in ctx.discard_pile() if is_basic_energy(c) or title == 'Reversed Clock' and is_pokemon_card(c)]
        picks = await ctx.choose_cards(pool, 2 if title == 'Store Up' else 3, minimum=0,
                                      prompt='Choose cards to recover')
        if title == 'Store Up':
            await ctx.put_in_hand(picks, reveal=True)
        else:
            await ctx.shuffle_into_deck(picks)
    elif title in ('Thunderous Bolt', 'Psychic Powers'):
        await ctx.deal_damage(printed)
        ctx.add_passive_through_own_next_turn(ctx.attacker, AttackBan())
    elif title == 'Mysterious Signal':
        ctx.extra_prizes += 1
        await ctx.deal_damage(printed)
    elif title == 'Float Up':
        await ctx.deal_damage(printed)
        if await ctx.ask_yes_no('Shuffle this Pokémon and all attached cards into your deck?'):
            await ctx.shuffle_into_deck(full_stack(ctx.attacker))
    elif title == 'Eerie Glow':
        await ctx.deal_damage(printed)
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.BURNED)
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.CONFUSED)
    elif title in ('Stiffen', 'Shield Press'):
        await ctx.deal_damage(printed)
        ctx.add_passive_through_opponents_turn(ctx.attacker, _BWTurnShield(60 if title == 'Stiffen' else 50))
    elif title == 'Break Ground':
        await ctx.deal_damage(printed)
        for p in list(ctx.my_bench()):
            await ctx.deal_damage(20, p, apply_modifiers=False)
    elif title == 'Growl':
        if ctx.defender is not None and not ctx.effects_blocked(ctx.defender):
            ctx.add_passive_through_opponents_turn(ctx.defender, _BWTurnShield(30, outgoing=True))
    elif title == 'Clumsily Clutch':
        heads = (await ctx.flip_coins(1))[0]
        await ctx.deal_damage(printed)
        if heads and ctx.defender is not None and not ctx.effects_blocked(ctx.defender):
            ctx.lock_retreat(ctx.defender)
    elif title == 'Nitpick':
        await ctx.shuffle_into_deck(list(ctx.hand(ctx.opponent_id)), ctx.opponent_id)
        await ctx.draw_cards(4, ctx.opponent_id)
    elif title == 'Swift':
        await ctx.deal_damage(printed, ignore_target_effects=True, ignore_weakness=True, ignore_resistance=True)
    elif title == 'Hardened Blade':
        await ctx.deal_damage(printed + (40 if any(is_pokemon_tool(c) for c in full_stack(ctx.attacker)[1:]) else 0))
    elif title == 'Slashing Strike':
        await ctx.deal_damage(printed)
        ctx.session.turn_state.lock_attack(ctx.attacker.entity_id, ctx.ability.ability_id)
    elif title == 'Dragon Pulse':
        await ctx.deal_damage(printed)
        await ctx.discard_cards(list(ctx.deck_top(2)))
    elif title == 'Screech':
        if ctx.defender is not None and not ctx.effects_blocked(ctx.defender):
            ctx.add_passive_through_own_next_turn(ctx.defender, _BWTurnShield(30, increase=True))
    elif title == 'Collapse':
        await ctx.deal_damage(printed)
        await ctx.apply_special_condition(ctx.attacker, SpecialConditions.ASLEEP)
    elif title == 'Elemental Blast':
        await ctx.deal_damage(printed)
        for kind in (PokemonTypes.FIRE, PokemonTypes.WATER, PokemonTypes.LIGHTNING):
            await ctx.discard_energy_units_from(ctx.attacker, 1,
                predicate=lambda c, k=kind: energy_provides_type(c, k.value), partial=True)
    else:
        raise ValueError(f'Unmapped 30C effect: {title}')


CUSTOM_ATTACKS = {
    'Energy Gift', 'Sacred Breath', 'Cheerful Flame', 'Laser Flame', 'Nitro Thunder',
    'Ferry Across', 'Geonavigation', 'Wormhole', 'Stealthy Slash', 'Pika Chain',
    'Overwriting Bolt', 'Charge-Up Dash', 'Tropical Vibes', 'Fighting Lightning',
    'Pika-Pika Parade', 'Zip-Zap Frenzy', 'Select a Snack', 'Empower', 'Photon Bullets',
    'Miraculous Shine', 'Solar Beatdown', 'Colorful Harmony', 'Comforting Aroma',
    'Midnight Ray', 'Strolls So Much', 'Quaking Fist', 'Counter', 'Chaotic Pain',
    'Lunatic Claw', 'Three-Headed Bite', 'Treasure Rush', 'Wish Granter',
    'Kaboom Needles', 'Fend Off', 'Celebration', 'Booming Call',
    'Surprisingly Transform', 'Fetch and Hide', 'Bouncy Circle',
    'Swirling Resentment', 'Gnaw Together',
}
PASSIVES = {'Scale Up', 'Supereffective Pheromones', 'Lonely Gaze', 'Keep Hidden',
            'Nighttime Byway', 'Life-Locked', 'Memory Helix', 'Counterattack Grouping'}
ACTIVATED = {*BIRD_TYPES, 'Guiding Dance', 'Sunrise', 'Share Happiness'}


def configure(card):
    for a in card.abilities:
        if isinstance(a, Attack):
            if a.title in CUSTOM_ATTACKS or a.title in COMMON_ATTACKS:
                a.effect = attack_effect
        elif a.title in PASSIVES:
            a.effect = None
            a.trigger = None
            a.passive = CelebrationPassive(a.title)
        elif a.title in ACTIVATED:
            a.effect = ability_effect
            a.passive = None
            a.trigger = None
            a.activation = Activations.ONCE_PER_TURN
            a.condition = ability_condition(a.title)
        elif a.title in ('Fainting Spell', 'Good Sleep'):
            a.effect = ability_effect
            a.passive = None
            a.trigger = Triggers.ON_KNOCKED_OUT if a.title == 'Fainting Spell' else Triggers.BETWEEN_TURNS
