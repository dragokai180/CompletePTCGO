"""TAG TEAM GX effects whose bonus requires Energy beyond the attack cost."""
import re

from spirit.game.attributes import AttrID, PokemonTypes, SpecialConditions
from spirit.game.data_utils import subtypes_for
from spirit.game.session.effects import EffectContext, full_stack, is_basic_energy, is_energy_card, is_pokemon_card, is_trainer_card
from spirit.game.session.legal_actions import attack_cost_satisfied
from spirit.game.session.passives import Passive, effective_attack_cost, effective_bench_capacity


def extra_energy_satisfied(ctx, text):
    clause = re.search(
        r"if this pok[eé]mon has at least (.+?) attached(?: to it)? "
        r"\(in addition to this attack's cost\)", text.lower())
    if not clause:
        return False
    cost = effective_attack_cost(ctx.board, ctx.attacker, {
        getattr(kind, 'value', kind): count
        for kind, count in (ctx.ability.cost or {}).items()
    }, attack=ctx.ability)
    extras = re.findall(r"(\d+) extra (?:(\w+) )?energy", clause.group(1))
    if 'extra fire, water, and lightning energy' in clause.group(1):
        extras = [('1', 'fire'), ('1', 'water'), ('1', 'lightning')]
    for count, kind in extras:
        ptype = getattr(PokemonTypes, (kind or 'colorless').upper())
        cost[ptype.value] = cost.get(ptype.value, 0) + int(count)
    return bool(extras) and attack_cost_satisfied(
        cost, ctx.attached_energies(ctx.attacker), ctx.board)


class _SurviveHeroism(Passive):
    async def damage_interceptor(self, ctx, calc, target, carrier):
        if target is carrier and calc.is_attack and calc.is_opposing:
            hp = carrier.get_attribute(AttrID.HP, 0)
            if calc.amount >= hp:
                return max(0, hp - 10)
        return None


TITLES = {
    'Magical Miracle-GX', 'Dark Union-GX', 'Acme of Heroism-GX',
    'Nasty Goo Mix-GX', 'Beast Game-GX', 'Gigafall-GX', 'Lightning Ride-GX',
    'Tropical Hour-GX', 'Thrilling Times-GX', 'Bubble Launcher-GX',
    'Puffy Smashers-GX', 'Chaotic Order-GX', 'Supreme Puff-GX',
    'Horror House-GX', 'Aero Unit-GX',
    'Crimson Flame Pillar-GX', 'Cross Division-GX', 'Dark Moon-GX',
    'Double Blaze-GX', 'Evergreen-GX', 'Full Metal Wall-GX', 'GG End-GX',
    'Megaton Friends-GX', 'Miraculous Duo-GX', 'Pale Moon-GX',
    'Sky Legends-GX', 'Solar Plant-GX', 'Tag Bolt-GX', 'Towering Splash-GX',
}


async def resolve_tag_team_gx(ctx):
    title = ctx.ability.title
    if title not in TITLES:
        return False
    boosted = extra_energy_satisfied(ctx, ctx.ability.game_text)
    damage = ctx.ability.damage or 0
    if title == 'Thrilling Times-GX':
        flips = await ctx.flip_coins(10 if boosted else 1, title)
        damage += 100 * sum(flips)
    elif title == 'Lightning Ride-GX':
        damage += 100 if boosted else 0
    elif title == 'Bubble Launcher-GX':
        damage += 150 if boosted else 0
    elif title == 'Double Blaze-GX':
        damage += 100 if boosted else 0
    if damage:
        if title == 'Double Blaze-GX':
            await ctx.deal_damage(damage, ignore_target_effects=boosted)
        else:
            await ctx.deal_damage(damage)

    if title == 'Magical Miracle-GX' and boosted:
        await ctx.shuffle_into_deck(list(ctx.hand(ctx.opponent_id)), player_id=ctx.opponent_id)
    elif title == 'Dark Union-GX':
        candidates = [c for c in ctx.discard_pile()
                      if is_pokemon_card(c)
                      and PokemonTypes.DARKNESS.value in (c.get_attribute(AttrID.POKEMON_TYPES) or [])
                      and {'GX', 'EX'}.intersection(subtypes_for(c.archetype_id) or [])]
        count = min(2, len(candidates),
                    max(0, effective_bench_capacity(ctx.board, ctx.player_id) - len(ctx.my_bench())))
        picks = await ctx.choose_cards(candidates, count, minimum=count,
                                       prompt="Choose Darkness Pokémon-GX or Pokémon-EX") if count else []
        for pokemon in picks:
            if await ctx.bench_pokemon(pokemon) and boosted:
                energies = [c for c in ctx.discard_pile() if is_energy_card(c)]
                n = min(2, len(energies))
                chosen = await ctx.choose_cards(energies, n, minimum=n,
                                                prompt="Choose 2 Energy cards to attach") if n else []
                for energy in chosen:
                    await ctx.attach_energy(energy, pokemon)
    elif title == 'Acme of Heroism-GX' and boosted:
        ctx.add_passive_through_opponents_turn(ctx.attacker, _SurviveHeroism())
    elif title == 'Nasty Goo Mix-GX':
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.PARALYZED)
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.POISONED, poison_counters=15 if boosted else 1)
    elif title == 'Beast Game-GX':
        ctx.add_extra_prize_watcher(
            attacker_predicate=lambda p: p is ctx.attacker,
            target_predicate=lambda p: p is ctx.defender,
            prizes=3 if boosted else 1)
    elif title == 'Gigafall-GX' and boosted:
        await ctx.discard_cards(ctx.deck_top(15, ctx.opponent_id))
    elif title == 'Lightning Ride-GX':
        bench = list(ctx.my_bench())
        target = await ctx.choose_pokemon(bench, "Choose your new Active Pokémon") if bench else None
        if target is not None:
            await ctx.switch_active(ctx.player_id, target)
    elif title == 'Tropical Hour-GX' and boosted:
        cards = [e for p in ctx.opponent_pokemon_in_play() if not ctx.effects_blocked(p)
                 for e in ctx.attached_energies(p)]
        await ctx.shuffle_into_deck(cards, player_id=ctx.opponent_id)
    elif title == 'Bubble Launcher-GX':
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.PARALYZED)
    elif title == 'Puffy Smashers-GX':
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.ASLEEP)
        bench = list(ctx.opponent_bench())
        if boosted and bench:
            target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon")
            if target is not None:
                await ctx.deal_damage(200, target=target, ignore_weakness=True, ignore_resistance=True)
    elif title == 'Chaotic Order-GX':
        area = ctx.board.find_player_area(ctx.player_id, 'prizePile')
        prizes = list(area.children) if area else []
        await ctx.reveal_cards(prizes)
        for card in prizes:
            card.publicly_revealed = True
        if boosted:
            await ctx.take_prizes(2)
    elif title == 'Supreme Puff-GX':
        ctx.take_extra_turn()
        if boosted:
            cards = [c for p in ctx.opponent_bench() if not ctx.effects_blocked(p) for c in full_stack(p)]
            await ctx.shuffle_into_deck(cards, player_id=ctx.opponent_id)
    elif title == 'Horror House-GX':
        ctx.lock_plays(ctx.opponent_id, lambda card: True)
        if boosted:
            await ctx.draw_until(7)
            await ctx.draw_until(7, player_id=ctx.opponent_id)
    elif title in ('Aero Unit-GX', 'Crimson Flame Pillar-GX'):
        energies = [c for c in ctx.discard_pile() if is_basic_energy(c)]
        n = min(5, len(energies))
        chosen = await ctx.choose_cards(energies, n, minimum=n,
                                        prompt="Choose Basic Energy cards") if n else []
        for energy in chosen:
            target = await ctx.choose_pokemon(ctx.my_pokemon_in_play(), "Choose a Pokémon")
            if target is not None:
                await ctx.attach_energy(energy, target)
        if boosted and title == 'Aero Unit-GX':
            from spirit.game.card_effects.bw_era import _BWTurnShield
            ctx.add_passive_through_opponents_turn(ctx.attacker, _BWTurnShield(prevent_all=True))
        elif boosted:
            await ctx.apply_special_condition(ctx.defender, SpecialConditions.BURNED)
            await ctx.apply_special_condition(ctx.defender, SpecialConditions.CONFUSED)
    elif title == 'Cross Division-GX':
        await ctx.place_damage_counters(20 if boosted else 10, ctx.opponent_pokemon_in_play())
    elif title == 'Dark Moon-GX':
        ctx.lock_plays(ctx.opponent_id, is_trainer_card)
        if boosted:
            await ctx.knock_out(ctx.defender)
    elif title == 'Evergreen-GX':
        await ctx.heal(ctx.max_hp(ctx.attacker), ctx.attacker)
        if boosted:
            await ctx.shuffle_into_deck(list(ctx.discard_pile()))
    elif title == 'Full Metal Wall-GX':
        from spirit.game.card_effects.bw_era import _BWPlayerCombatRule
        ctx.add_temporary_player_passive(ctx.player_id, _BWPlayerCombatRule(
            ctx.player_id, damage_reduction=30,
            damage_reduction_types={PokemonTypes.METAL.value}), None)
        if boosted and not ctx.effects_blocked(ctx.defender):
            await ctx.discard_cards(list(ctx.attached_energies(ctx.defender)))
    elif title == 'GG End-GX':
        pool = list(ctx.opponent_pokemon_in_play())
        n = min(2 if boosted else 1, len(pool))
        chosen = await ctx.choose_cards(pool, n, minimum=n, prompt="Choose Pokémon to discard")
        for pokemon in chosen:
            if not ctx.effects_blocked(pokemon):
                await ctx.discard_cards(full_stack(pokemon))
    elif title == 'Megaton Friends-GX' and boosted:
        await ctx.draw_until(10)
    elif title == 'Miraculous Duo-GX' and boosted:
        for pokemon in ctx.my_pokemon_in_play():
            await ctx.heal(ctx.max_hp(pokemon), pokemon)
    elif title == 'Pale Moon-GX':
        if not ctx.effects_blocked(ctx.defender):
            marker = Passive()
            target = ctx.defender
            ctx.add_passive_through_opponents_turn(target, marker)
            def still_defending(board):
                return board.active_pokemon(ctx.opponent_id) is target and any(
                    entry.passive is marker for entry in board.temporary_passives)
            async def finish(session):
                delayed = EffectContext(session, ctx.player_id, ctx.attacker, None)
                await delayed.knock_out(target)
                if delayed._messages:
                    await session._flush_effect_runs(delayed)
                if delayed.knockouts:
                    await session.resolve_knockouts(delayed)
            ctx.schedule_at_checkup(1, finish, guard=still_defending)
        if boosted and not ctx.effects_blocked(ctx.defender):
            await ctx.discard_cards(list(ctx.attached_energies(ctx.defender)))
    elif title == 'Sky Legends-GX':
        # Retain the original attacking card in ctx even after its stack leaves play.
        await ctx.shuffle_into_deck(full_stack(ctx.attacker))
        if boosted:
            pool = list(ctx.opponent_pokemon_in_play())
            n = min(3, len(pool))
            chosen = await ctx.choose_cards(pool, n, minimum=n, prompt="Choose 3 Pokémon")
            for pokemon in chosen:
                await ctx.deal_damage(110, target=pokemon)
    elif title == 'Solar Plant-GX':
        for pokemon in list(ctx.opponent_pokemon_in_play()):
            await ctx.deal_damage(50, target=pokemon)
        if boosted:
            for pokemon in ctx.my_pokemon_in_play():
                await ctx.heal(ctx.max_hp(pokemon), pokemon)
    elif title == 'Tag Bolt-GX' and boosted:
        pool = list(ctx.opponent_bench())
        target = await ctx.choose_pokemon(pool, "Choose a Benched Pokémon") if pool else None
        if target is not None:
            await ctx.deal_damage(170, target=target)
    elif title == 'Towering Splash-GX' and boosted:
        for pokemon in list(ctx.opponent_bench()):
            await ctx.deal_damage(100, target=pokemon)
    return True
