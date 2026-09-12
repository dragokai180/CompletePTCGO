"""Explicit HGSS compound attacks that cannot be inferred clause by clause.

Dispatch uses the printed attack's set, so copying one preserves its rules.
Simple attacks still use the shared interpreter and its board primitives.
"""
import re
import random

from spirit.game.attributes import AttrID, AbilityTypes, PokemonTypes, SpecialConditions, CLIENT_SPECIAL_CONDITION_NAMES
from spirit.game.session.passives import Passive
from spirit.game.legend import is_legend, complementary_halves
from spirit.game.session.effects import is_energy_card, is_supporter_card, is_pokemon_card, is_trainer_card, is_item_card, is_basic_pokemon, is_basic_energy, full_stack
from spirit.game.card_effects.pokemon import energy_provides_type


class PsychicLock(Passive):
    def __init__(self, player_id):
        self.player_id = player_id

    def blocks_ability(self, pokemon, ability, carrier):
        return pokemon.owning_player_id == self.player_id and ability is not None \
            and ability.ability_type == AbilityTypes.POKE_POWER


class Afterimage(Passive):
    async def damage_interceptor(self, ctx, calc, target, carrier):
        if target is carrier and calc.is_attack and calc.attacker is not None \
                and calc.attacker.owning_player_id != carrier.owning_player_id:
            if (await ctx.flip_coins(1, 'Afterimage Strike', source=carrier,
                                     player_id=carrier.owning_player_id))[0]:
                return 0
        return None


async def resolve_hgss_attack(ctx, text, printed):
    if getattr(ctx.ability, 'printed_set_code', None) not in (
            'HGSS1', 'HGSS2', 'HGSS3', 'HGSS4', 'COL', 'Promo_HGSS'):
        return False
    title = ctx.ability.title
    source = ctx.attacker
    from spirit.game.card_effects.bw_era import _energy_count, _name, _is_type
    if title == 'Psychic Lock':
        await ctx.deal_damage(printed)
        ctx.add_temporary_player_passive(ctx.opponent_id, PsychicLock(ctx.opponent_id),
                                         ctx.session.turn_state.turn_number + 1)
        return True
    if title == 'Afterimage Strike':
        await ctx.deal_damage(printed)
        ctx.add_passive_through_opponents_turn(source, Afterimage())
        return True
    if title == 'Mach Wind':
        from spirit.game.card_effects.bw_era import _BWTemporaryCombatRule
        await ctx.deal_damage(printed)
        ctx.add_passive_through_own_next_turn(source, _BWTemporaryCombatRule(retreat_zero=True))
        return True
    if title == 'Take Away':
        defender = ctx.defender
        await ctx.shuffle_into_deck(full_stack(source))
        await ctx.shuffle_into_deck(full_stack(defender), player_id=ctx.opponent_id)
        await ctx.flush_choreography()
        await ctx.session._resolve_simultaneous_win_conditions()
        # Unlike a simultaneous KO, this attack explicitly asks its user first.
        for pid in (ctx.player_id, ctx.opponent_id):
            await ctx.session._promote_new_active(pid)
        return True
    if title in ('Ember', 'Fireworks', 'Shock Bolt', 'Scorching Wing') and 'if tails' in text:
        await ctx.deal_damage(printed)
        if not (await ctx.flip_coins(1, title))[0]:
            kind = PokemonTypes.LIGHTNING if 'lightning energy' in text else PokemonTypes.FIRE if 'fire energy' in text else None
            predicate = (lambda e: energy_provides_type(e, kind.value)) if kind else None
            if 'discard all' in text:
                await ctx.discard_cards([e for e in ctx.attached_energies(source)
                                        if predicate is None or predicate(e)])
            else:
                await ctx.discard_energy_units_from(source, 1, predicate=predicate, partial=True)
        return True
    if title in ('Hydro Launcher', 'Torrent Blade'):
        from spirit.game.session.passives import energy_provided_options
        pool = [e for e in ctx.attached_energies(source)
                if any(PokemonTypes.WATER.value in option for option in energy_provided_options(ctx.board, e))]
        selected, remaining = [], 2
        while pool and remaining > 0:
            picks = await ctx.choose_cards(pool, 1, prompt='Choose Water Energy to return')
            if not picks:
                break
            card = picks[0]
            pool.remove(card)
            selected.append(card)
            remaining -= max((o.count(PokemonTypes.WATER.value)
                              for o in energy_provided_options(ctx.board, card)), default=0)
        await ctx.put_in_hand(selected, reveal=False)
        targets = ctx.opponent_bench() if title == 'Torrent Blade' else ctx.opponent_pokemon_in_play()
        target = await ctx.choose_pokemon(targets, 'Choose a Pokemon to damage') if targets else None
        if target:
            await ctx.deal_damage(100, target=target, apply_modifiers=(target is ctx.defender))
        return True
    if title in ('Snowy Present', 'Green Draw'):
        count = sum(_energy_count(ctx, p, 'water') for p in ctx.my_pokemon_in_play()) \
            if title == 'Snowy Present' else sum(_is_type(p, PokemonTypes.GRASS) for p in ctx.my_pokemon_in_play())
        await ctx.draw_cards(count)
        return True
    if title in ('Vengeance', 'Evoblast', 'Miasma Wind', 'Poltergeist'):
        if title == 'Vengeance':
            amount = printed + 10 * sum(is_pokemon_card(p) and _is_type(p, PokemonTypes.DARKNESS)
                                       for p in ctx.discard_pile())
        elif title == 'Evoblast':
            amount = printed + 10 * sum(p.get_attribute(AttrID.EVOLUTION_LOGIC_FROM) in
                ('Eevee', 'com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name')
                for p in ctx.my_pokemon_in_play())
        elif title == 'Miasma Wind':
            amount = 50 * len(set(ctx.defender.get_attribute(AttrID.SPECIAL_CONDITIONS) or []))
        else:
            cards = await ctx.reveal_hand(ctx.opponent_id, ctx.player_id)
            amount = 30 * sum(is_trainer_card(card) for card in cards)
        await ctx.deal_damage(amount)
        return True
    if title == 'Thunder Shot':
        for target in ctx.opponent_pokemon_in_play():
            if ctx.attached_energies(target):
                await ctx.deal_damage(50, target=target, apply_modifiers=(target is ctx.defender))
        return True
    if title in ('Plasma Arrow', 'Feint Attack', 'Bebop Punch', 'Illumisile'):
        if title == 'Illumisile' and not any(_name(p) == 'Illumise' for p in ctx.my_pokemon_in_play()):
            return True
        pool = ctx.opponent_bench() if title == 'Illumisile' else ctx.opponent_pokemon_in_play()
        target = await ctx.choose_pokemon(pool, 'Choose a Pokemon to damage') if pool else None
        if target:
            amount = 30
            if title == 'Plasma Arrow':
                amount = 20 * _energy_count(ctx, target)
            elif title == 'Bebop Punch':
                amount = 0
                while (await ctx.flip_coins(1, title))[0]:
                    amount += 50
            ignore = title in ('Feint Attack', 'Plasma Arrow')
            await ctx.deal_damage(amount, target=target, apply_modifiers=(target is ctx.defender),
                                  ignore_weakness=ignore, ignore_resistance=ignore,
                                  ignore_target_effects=(title == 'Feint Attack'))
        return True
    if title == 'Eruption':
        cards = ctx.deck_top(1) + ctx.deck_top(1, ctx.opponent_id)
        amount = 20 * sum(is_energy_card(card) for card in cards)
        await ctx.discard_cards(cards)
        await ctx.deal_damage(amount)
        return True
    if title == 'Pheromone Poison':
        await ctx.deal_damage(printed)
        if any(_name(p) == 'Nidoran ♀' for p in ctx.my_bench()):
            await ctx.apply_special_condition(ctx.defender, SpecialConditions.POISONED)
        return True
    if title == 'Tentavolve':
        await ctx.deal_damage(printed)
        state = ctx.session.turn_state
        if state.entered_play_turn.get(source.entity_id) == state.turn_number \
                and any(_name(p) == 'Tentacool' for p in full_stack(source)[1:]):
            for condition in (SpecialConditions.PARALYZED, SpecialConditions.POISONED):
                await ctx.apply_special_condition(ctx.defender, condition)
        return True
    if title == 'Poison Effect':
        poisoned = CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.POISONED] in (
            source.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])
        await ctx.deal_damage(printed + (60 if poisoned else 0))
        if poisoned:
            await ctx.cure_condition(source, SpecialConditions.POISONED)
        return True
    if title == 'Infinite Wind':
        await ctx.deal_damage(printed)
        if any(_name(p) == 'Latios' for p in ctx.my_bench()):
            for pokemon in ctx.my_bench():
                await ctx.heal(20, pokemon)
        return True
    if title == 'Strip Bare':
        await ctx.deal_damage(printed)
        if all(await ctx.flip_coins(2, title)):
            await ctx.discard_cards(list(ctx.hand(ctx.opponent_id)))
        return True
    if title in ('Astonish', 'Sharpen Claws'):
        await ctx.deal_damage(printed)
        if title == 'Sharpen Claws':
            count = sum(await ctx.flip_coins(3, title))
        elif 'flip a coin' in text:
            count = int((await ctx.flip_coins(1, title))[0])
        else:
            count = 2
        hand = list(ctx.hand(ctx.opponent_id))
        picks = random.sample(hand, min(count, len(hand)))
        if title == 'Sharpen Claws':
            await ctx.discard_cards(picks)
        elif picks:
            await ctx.reveal_cards(picks, to_player=ctx.player_id)
            await ctx.shuffle_into_deck(picks, player_id=ctx.opponent_id)
        return True
    if title == 'Green Call':
        count = sum(await ctx.flip_coins(2, title))
        if count:
            cards = await ctx.search_deck(lambda p: is_pokemon_card(p) and _is_type(p, PokemonTypes.GRASS), count)
            await ctx.put_in_hand(cards)
            await ctx.shuffle_deck()
        return True
    if title == 'Static Electricity':
        count = sum(_name(p) == 'Mareep' for p in ctx.my_pokemon_in_play() + ctx.opponent_pokemon_in_play())
        cards = await ctx.search_deck(lambda c: is_energy_card(c) and
            energy_provides_type(c, PokemonTypes.LIGHTNING.value), count)
        for card in cards:
            await ctx.attach_energy(card, source)
        await ctx.shuffle_deck()
        return True
    if title == 'Playground':
        from spirit.game.session.passives import effective_bench_capacity
        for pid in (ctx.player_id, ctx.opponent_id):
            bench = ctx.board.find_player_area(pid, 'bench')
            room = max(0, effective_bench_capacity(ctx.board, pid) - len(bench.children))
            if room and ctx.deck(pid) and await ctx.ask_yes_no('Search for Basic Pokemon?', player_id=pid):
                cards = await ctx.search_deck(is_basic_pokemon, room, player_id=pid)
                for card in cards:
                    await ctx.bench_pokemon(card)
                await ctx.shuffle_deck(pid)
        await ctx.apply_special_condition(source, SpecialConditions.ASLEEP)
        return True
    if title == 'Solar Suggestion':
        remaining = 4
        while remaining:
            pool = [p for p in ctx.my_pokemon_in_play() if p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p)]
            donor = await ctx.choose_pokemon(pool, 'Choose a Pokemon to move counters from', optional=True) if pool else None
            if donor is None:
                break
            count = min(remaining, (ctx.max_hp(donor) - donor.get_attribute(AttrID.HP, 0)) // 10)
            chosen = await ctx.choose('How many damage counters?', [str(n) for n in range(1, count + 1)]) + 1
            moved = await ctx.move_damage_counters(donor, ctx.opponent_pokemon_in_play(), max_count=chosen)
            if not moved:
                break
            remaining -= moved
        return True
    if title == "Moon's Invite":
        # Each original counter is available once; moving counters onto a
        # later donor must not make that donor's initial quota larger.
        available = {p.entity_id: (ctx.max_hp(p) - p.get_attribute(AttrID.HP, 0)) // 10
                     for p in ctx.opponent_pokemon_in_play()}
        while True:
            pool = [p for p in ctx.opponent_pokemon_in_play() if available.get(p.entity_id, 0) > 0]
            donor = await ctx.choose_pokemon(pool, 'Choose a Pokemon to move counters from', optional=True) if pool else None
            if donor is None:
                break
            count = available.pop(donor.entity_id)
            chosen = await ctx.choose('How many damage counters?', [str(n) for n in range(count + 1)])
            if chosen:
                await ctx.move_damage_counters(donor, ctx.opponent_pokemon_in_play(), max_count=chosen)
        return True
    if title == 'Cosmic Cyclone':
        pool = [e for p in ctx.my_pokemon_in_play() for e in ctx.attached_energies(p)
                if energy_provides_type(e, PokemonTypes.WATER.value)]
        chosen = await ctx.choose_cards(pool, len(pool), minimum=0,
                                        prompt='Choose Water Energy to shuffle away') if pool else []
        from spirit.game.session.passives import energy_provided_options
        value = sum(max((option.count(PokemonTypes.WATER.value)
                         for option in energy_provided_options(ctx.board, e)), default=0) for e in chosen)
        await ctx.deal_damage(20 * value)
        await ctx.shuffle_into_deck(chosen)
        return True
    if title == 'Everyone Explode Now':
        from spirit.game.card_effects.bw_era import _name
        pool = [p for p in ctx.my_pokemon_in_play() if _name(p) in ('Pineco', 'Forretress')]
        await ctx.deal_damage(30 * len(pool))
        for pokemon in pool:
            await ctx.deal_damage(30, target=pokemon, apply_modifiers=False)
        return True
    if title == 'Enraged Assault':
        from spirit.game.card_effects.bw_era import _name
        boosted = any(_name(p) == 'Vespiquen' and p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p) for p in ctx.my_bench())
        await ctx.deal_damage(printed + (60 if boosted else 0))
        if boosted:
            await ctx.apply_special_condition(ctx.defender, SpecialConditions.POISONED)
        return True
    if title == 'Ninja Fang':
        clean = ctx.defender.get_attribute(AttrID.HP) == ctx.max_hp(ctx.defender)
        dealt = await ctx.deal_damage(printed)
        if clean and dealt:
            await ctx.apply_special_condition(ctx.defender, SpecialConditions.PARALYZED)
        return True
    if title == 'Startling Trip':
        await ctx.deal_damage(printed)
        target = ctx.defender if (await ctx.flip_coins(1, title))[0] else source
        await ctx.apply_special_condition(target, SpecialConditions.CONFUSED)
        return True
    if title == 'Big Yawn':
        await ctx.deal_damage(printed)
        for target in (source, ctx.defender):
            await ctx.apply_special_condition(target, SpecialConditions.ASLEEP)
        return True
    if title == 'Fury Cutter':
        heads = sum(await ctx.flip_coins(3, title))
        await ctx.deal_damage(printed + (0, 20, 40, 100)[heads])
        return True
    if title == 'Bench Manipulation':
        coins = await ctx.flip_coins(len(ctx.opponent_bench()), title, player_id=ctx.opponent_id)
        await ctx.deal_damage(40 * sum(not c for c in coins), ignore_weakness=True, ignore_resistance=True)
        return True
    if title == 'Destructive Tsunami':
        pool = ctx.opponent_pokemon_in_play() if (await ctx.flip_coins(1, title))[0] else ctx.my_pokemon_in_play()
        for target in pool:
            await ctx.deal_damage(40, target=target, apply_modifiers=(target is ctx.defender))
        return True
    if title == 'Volcano Stomp':
        await ctx.deal_damage(printed)
        pid = ctx.opponent_id if (await ctx.flip_coins(1, title))[0] else ctx.player_id
        await ctx.discard_cards(ctx.deck_top(4, pid))
        return True
    if title == 'Top Burner':
        from spirit.game.card_effects.bw_era import _energy_count
        await ctx.discard_cards(ctx.deck_top(_energy_count(ctx, source, 'fire'), ctx.opponent_id))
        if not (await ctx.flip_coins(1, title))[0]:
            await ctx.discard_cards([e for e in ctx.attached_energies(source)
                                    if energy_provides_type(e, PokemonTypes.FIRE.value)])
        return True
    if title == 'Distorted Wave':
        await ctx.heal(10, ctx.defender)
        await ctx.deal_damage(printed)
        return True
    if title == 'Legend Ceremony':
        first = await ctx.search_deck(is_legend, 1, minimum=0,
                                       prompt='Choose a LEGEND half')
        if first:
            second = await ctx.search_deck(lambda card: complementary_halves(first[0], card),
                1, minimum=0, prompt='Choose the other LEGEND half')
            await ctx.put_in_hand(first + second)
        await ctx.shuffle_deck()
        return True
    if title == 'Plead':
        if await ctx.ask_yes_no('Allow your opponent to draw 2 cards?', player_id=ctx.opponent_id):
            await ctx.draw_cards(2)
        else:
            await ctx.deal_damage(20)
        return True
    if title == 'Selfish Draw':
        cards = ctx.deck_top(1)
        if cards:
            await ctx.reveal_cards(cards, to_player=ctx.player_id)
            if await ctx.ask_yes_no('Put this card into your hand?'):
                await ctx.put_in_hand(cards, reveal=False)
            else:
                await ctx.discard_cards(cards)
                await ctx.draw_cards(1)
        return True
    if title == 'Future Sight':
        side = await ctx.choose('Choose a deck', ['Your deck', "Opponent's deck"])
        await ctx.reorder_deck_top(5, player_id=ctx.player_id if side == 0 else ctx.opponent_id)
        return True
    if title == 'Mountain Eater':
        pid = ctx.opponent_id if "opponent's deck" in text else ctx.player_id
        cards = ctx.deck_top(1, pid)
        if cards:
            await ctx.discard_cards(cards)
            await ctx.heal(20, source)
        return True
    if title == 'Recover':
        kind = re.search(r'discard (?:an|a) (\w+) energy', text)
        ptype = getattr(PokemonTypes, kind.group(1).upper(), None) if kind else None
        predicate = (lambda card: energy_provides_type(card, ptype.value)) if ptype else None
        paid = await ctx.discard_energy_units_from(source, 1, predicate=predicate)
        if paid:
            amount = re.search(r'remove (\d+) damage counters', text)
            await ctx.heal(int(amount.group(1)) * 10 if amount else ctx.max_hp(source), source)
        return True
    if title in ('Leech Life', 'Giga Drain'):
        dealt = await ctx.deal_damage(printed)
        await ctx.heal(dealt, source)
        return True
    if title == 'Energy Bloom':
        await ctx.deal_damage(printed)
        for pokemon in ctx.my_pokemon_in_play():
            if ctx.attached_energies(pokemon):
                await ctx.heal(30, pokemon)
        return True
    if title == 'Fresh-Picked Fruit':
        candidates = [p for p in ctx.my_bench() if p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p)]
        target = await ctx.choose_pokemon(candidates, 'Choose a Benched Pokemon to heal') if candidates else None
        if target:
            await ctx.heal(60, target)
        return True
    if title == 'Underwater Dive':
        heads = sum(await ctx.flip_coins(2, title))
        await ctx.heal(30 * heads, source)
        return True
    if title == 'Happy Punch':
        await ctx.deal_damage(printed)
        if (await ctx.flip_coins(1, title))[0]:
            await ctx.heal(30, source)
        return True
    if title == 'Suspicious Beam β':
        await ctx.deal_damage(printed)
        from spirit.game.data_utils import def_for
        if not any((def_for(e.archetype_id).display_name or '') == 'Rainbow Energy'
                   for e in ctx.attached_energies(source)):
            await ctx.deal_damage(20, target=source, apply_modifiers=True)
            await ctx.apply_special_condition(source, SpecialConditions.CONFUSED)
        return True
    if title == 'Tripping Headbutt':
        heads = (await ctx.flip_coins(1, title))[0]
        pool = ctx.opponent_pokemon_in_play() if heads else ctx.my_pokemon_in_play()
        target = await ctx.choose_pokemon(pool, 'Choose a Pokemon to damage') if pool else None
        if target:
            await ctx.deal_damage(30, target=target, apply_modifiers=(target is ctx.defender))
        return True
    return False


def hgss_transfer_options(board, player_id, source, title):
    """Shared candidates for the button's legality and the actual movement."""
    rules = {'Wash Out': PokemonTypes.WATER, 'Voltage Increase': PokemonTypes.LIGHTNING,
             'Leaf Trans': PokemonTypes.GRASS, 'Magical Trans': PokemonTypes.PSYCHIC}
    if title not in rules:
        return None
    from spirit.game.session.passives import energy_provided_options
    pokemon = list(board.pokemon_in_play(player_id))
    active = board.active_pokemon(player_id)
    donors = [p for p in pokemon if p is not active] if title == 'Wash Out' else pokemon
    targets = [active] if title == 'Wash Out' else [source] if title == 'Voltage Increase' else pokemon
    targets = [p for p in targets if p is not None]
    kind = rules[title].value
    def predicate(energy):
        return any(kind in option for option in energy_provided_options(board, energy))
    donors = [p for p in donors if any(t is not p for t in targets)
              and any(predicate(e) for e in board.attached_energies(p))]
    return donors, targets, predicate


async def resolve_hgss_power(ctx, text):
    if getattr(ctx.ability, 'printed_set_code', None) not in (
            'HGSS1', 'HGSS2', 'HGSS3', 'HGSS4', 'COL', 'Promo_HGSS'):
        return False
    title = ctx.ability.title
    transfer = hgss_transfer_options(ctx.board, ctx.player_id, ctx.source, title)
    if transfer is not None:
        donors, targets, predicate = transfer
        await ctx.move_energy_freely(donors, targets, predicate=predicate,
                                    max_count=1, prompt='Choose Energy to move')
        return True
    hand_acceleration = {'Rain Dance': PokemonTypes.WATER, 'Water Acceleration': PokemonTypes.WATER,
                         'Forest Breath': PokemonTypes.GRASS, 'Self-Generation': PokemonTypes.LIGHTNING}
    if title in hand_acceleration:
        from spirit.game.session.passives import effective_pokemon_types
        kind = hand_acceleration[title].value
        pool = [c for c in ctx.hand() if energy_provides_type(c, kind)]
        count = 2 if title == 'Self-Generation' else 1
        chosen = await ctx.choose_cards(pool, count, minimum=0 if count == 2 else None,
                                        prompt='Choose Energy to attach') if pool else []
        targets = [ctx.source] if title in ('Water Acceleration', 'Self-Generation') else ctx.my_pokemon_in_play()
        if title == 'Rain Dance':
            targets = [p for p in targets if PokemonTypes.WATER.value in effective_pokemon_types(ctx.board, p)]
        for energy in chosen:
            target = targets[0] if len(targets) == 1 else await ctx.choose_pokemon(
                targets, 'Choose a Pokemon') if targets else None
            if target is not None:
                await ctx.attach_energy(energy, target, counts_as_attachment=True)
        return True
    if title == 'Active Volcano':
        cards = ctx.deck_top(1)
        if cards:
            await ctx.discard_cards(cards)
            if is_energy_card(cards[0]) and energy_provides_type(cards[0], PokemonTypes.FIRE.value):
                await ctx.attach_energy(cards[0], ctx.source)
        return True
    if title == 'Portrait':
        from spirit.game.card_effects.bw_era import _choose_one, _use_trainer_effect_as_attack
        from spirit.game.data_utils import def_for
        from spirit.game.session.legal_actions import trainer_condition_met
        cards = await ctx.reveal_hand(ctx.opponent_id, ctx.player_id)
        supporters = []
        for card in cards:
            if not is_supporter_card(card):
                continue
            condition = getattr(def_for(card.archetype_id), 'condition', None)
            if condition is None or trainer_condition_met(condition, ctx.board, ctx.player_id, card):
                supporters.append(card)
        chosen = await _choose_one(ctx, supporters, 'Choose a Supporter effect') if supporters else None
        if chosen is not None:
            await _use_trainer_effect_as_attack(ctx, chosen)
        return True
    return False


def hgss_power_condition(board, player_id, source, text):
    from spirit.game.data_utils import def_for
    definition = def_for(getattr(source, 'archetype_id', None))
    if getattr(definition, 'set_code', None) not in (
            'HGSS1', 'HGSS2', 'HGSS3', 'HGSS4', 'COL', 'Promo_HGSS'):
        return None
    phrases = {
        'move a water energy attached to 1 of your benched': 'Wash Out',
        'move a lightning energy attached to 1 of your pokémon to raichu': 'Voltage Increase',
        'move a grass energy attached to 1 of your pokémon': 'Leaf Trans',
        'move a psychic energy attached to 1 of your pokémon': 'Magical Trans',
    }
    for phrase, title in phrases.items():
        if phrase in text:
            donors, targets, _ = hgss_transfer_options(board, player_id, source, title)
            return bool(donors and targets)
    if 'move all fighting energy attached to your active' in text:
        active = board.active_pokemon(player_id)
        return active is not None and source is not active and any(
            energy_provides_type(e, PokemonTypes.FIGHTING.value) for e in board.attached_energies(active))
    if 'discard the top card of your deck' in text and 'attach it to slugma' in text:
        return bool(board.find_player_area(player_id, 'deck').children)
    if 'choose a water pokémon on your bench and switch it with your active' in text:
        from spirit.game.session.passives import effective_pokemon_types
        return any(p is not board.active_pokemon(player_id)
                   and PokemonTypes.WATER.value in effective_pokemon_types(board, p)
                   for p in board.pokemon_in_play(player_id))
    if 'both you and your opponent reveal your hands' in text:
        return any(board.find_player_area(pid, 'hand').children for pid in board.player_ids)
    return None


def lost_world_condition(board, player_id, source=None):
    state = getattr(board, 'turn_state', None)
    if state is not None and (state.in_checkup or state.active_player_id != player_id):
        return False
    opponent = next(pid for pid in board.player_ids if pid != player_id)
    area = board.find_player_area(opponent, 'lostZone')
    return area is not None and sum(is_pokemon_card(card) for card in area.children) >= 6


async def lost_world(ctx):
    if lost_world_condition(ctx.board, ctx.player_id, ctx.source):
        await ctx.win_game('Lost World')


async def resolve_hgss_trainer(ctx):
    from spirit.game.data_utils import def_for
    definition = def_for(ctx.source.archetype_id)
    if getattr(definition, 'set_code', None) not in (
            'HGSS1', 'HGSS2', 'HGSS3', 'HGSS4', 'COL', 'Promo_HGSS'):
        return False
    name = definition.display_name
    if name == 'Tropical Tidal Wave':
        pid = ctx.opponent_id if (await ctx.flip_coins(1, name))[0] else ctx.player_id
        cards = [card for pokemon in ctx.board.pokemon_in_play(pid)
                 for card in full_stack(pokemon)[1:] if is_item_card(card)]
        await ctx.discard_cards(cards)
        stadium = ctx.stadium_in_play()
        if stadium is not None and stadium.owning_player_id == pid:
            await ctx.discard_stadium()
        return True
    if name == "Emcee's Chatter":
        await ctx.draw_cards(3 if (await ctx.flip_coins(1, name))[0] else 2)
        return True
    if name == "Cheerleader's Cheer":
        await ctx.draw_cards(3)
        if await ctx.ask_yes_no('Draw a card?', player_id=ctx.opponent_id):
            await ctx.draw_cards(1, player_id=ctx.opponent_id)
        return True
    if name == 'Judge':
        for pid in (ctx.player_id, ctx.opponent_id):
            await ctx.shuffle_into_deck(list(ctx.hand(pid)), player_id=pid)
        for pid in (ctx.player_id, ctx.opponent_id):
            await ctx.draw_cards(4, player_id=pid)
        return True
    if name == 'Life Herb':
        if (await ctx.flip_coins(1, name))[0]:
            candidates = [p for p in ctx.my_pokemon_in_play() if p.get_attribute(AttrID.SPECIAL_CONDITIONS)
                          or p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p)]
            target = await ctx.choose_pokemon(candidates, 'Choose a Pokemon to heal') if candidates else None
            if target:
                await ctx.heal(60, target)
                await ctx.cure_all_conditions(target)
        return True
    if name in ('Fisherman', 'Energy Returner'):
        pool = [c for c in ctx.discard_pile() if is_basic_energy(c)]
        count = min(4, len(pool))
        cards = await ctx.choose_cards(pool, count, minimum=count, prompt='Choose Basic Energy') if count else []
        if name == 'Fisherman':
            await ctx.put_in_hand(cards)
        else:
            await ctx.reveal_cards(cards)
            await ctx.shuffle_into_deck(cards)
        return True
    if name in ('Energy Exchanger', 'Pokémon Communication'):
        predicate = is_energy_card if name == 'Energy Exchanger' else is_pokemon_card
        pool = [c for c in ctx.hand() if c is not ctx.source and predicate(c)]
        chosen = await ctx.choose_cards(pool, 1, prompt='Choose a card to return to your deck') if pool else []
        if chosen:
            await ctx.reveal_cards(chosen)
            await ctx.put_on_top_of_deck(chosen[0])
            cards = await ctx.search_deck(predicate, 1)
            await ctx.put_in_hand(cards)
            await ctx.shuffle_deck()
        return True
    return False
