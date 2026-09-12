"""Positive and negative HGSS branches missed by neutral smoke boards."""
import unittest
from unittest.mock import AsyncMock, patch
from tests import test_hgss_rules as fixtures
from tests.test_hgss_rules import definition
from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.session.effects import EffectContext, full_stack
from spirit.tools.effect_smoke import P1, P2


class EdgeTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add
    ctx = fixtures.HgssRulesTests.ctx

    def neutral(self, pokemon):
        pokemon.set_attribute(AttrID.WEAKNESS_TYPES, [])
        pokemon.set_attribute(AttrID.RESISTANCE_TYPES, PokemonTypes.UNSET.value)

    async def test_copied_self_damage_uses_actual_attackers_weakness(self):
        rig, e = self.rig('HGSS4.Mew_97')
        attack = definition('HGSS3.Drifblim_12').abilities[0]
        ctx = EffectContext(rig.session, P1, e['target'], attack)
        before = ctx.source.get_attribute(AttrID.HP)
        await attack.effect(ctx)
        self.assertEqual(before - ctx.source.get_attribute(AttrID.HP), 40)

    async def test_portrait_accepts_supporter_without_condition(self):
        rig, e, ctx = self.ctx('HGSS3.Smeargle_8', 'Portrait')
        for card in list(ctx.hand(P2)):
            rig.to_area(card, P2, 'deck')
        supporter = definition('HGSS1.Bill_89')
        card = self.add(rig, supporter, P2, 'hand')
        before = ctx.hand_size()
        with patch.object(supporter, 'condition', None):
            await ctx.ability.effect(ctx)
        self.assertEqual(ctx.hand_size() - before, 2)
        self.assertIn(card, ctx.hand(P2))

    async def test_dimension_transfer_heads_and_tails(self):
        for heads in (False, True):
            rig, e, ctx = self.ctx('HGSS4.PorygonZ_7', 'Dimension Transfer')
            for card in list(ctx.discard_pile()):
                rig.to_area(card, P1, 'hand')
            item = self.add(rig, definition('HGSS2.PlusPower_80'), P1, 'discard')
            ctx.flip_coins = AsyncMock(return_value=[heads])
            ctx.reveal_cards = AsyncMock()
            await ctx.ability.effect(ctx)
            if heads:
                self.assertIs(ctx.deck_top(1)[0], item)
                ctx.reveal_cards.assert_awaited_once_with([item])
            else:
                self.assertIn(item, ctx.discard_pile())
                ctx.reveal_cards.assert_not_awaited()

    async def test_enraged_assault_only_damaged_own_vespiquen(self):
        for damaged in (False, True):
            rig, e, ctx = self.ctx('HGSS3.Combee_44', 'Enraged Assault')
            self.neutral(ctx.defender)
            bee = self.add(rig, definition('HGSS3.Vespiquen_23'), P1, 'bench')
            bee.set_attribute(AttrID.HP, ctx.max_hp(bee) - 10 * damaged)
            before = ctx.defender.get_attribute(AttrID.HP)
            await ctx.ability.effect(ctx)
            self.assertEqual(before - ctx.defender.get_attribute(AttrID.HP), 80 if damaged else 20)
            self.assertEqual('Poisoned' in (ctx.defender.get_attribute(AttrID.SPECIAL_CONDITIONS) or []), damaged)

    async def test_ninja_fang_requires_undamaged_defender(self):
        for damaged in (False, True):
            rig, e, ctx = self.ctx('HGSS3.Gliscor_4', 'Ninja Fang')
            self.neutral(ctx.defender)
            ctx.defender.set_attribute(AttrID.HP, ctx.max_hp(ctx.defender) - 10 * damaged)
            await ctx.ability.effect(ctx)
            self.assertEqual('Paralyzed' in (ctx.defender.get_attribute(AttrID.SPECIAL_CONDITIONS) or []), not damaged)

    async def test_illumisile_requires_illumise_and_hits_selected_bench(self):
        for present in (False, True):
            rig, e, ctx = self.ctx('HGSS4.Volbeat_82', 'Illumisile')
            if present:
                self.add(rig, definition('HGSS4.Illumise_64'), P1, 'bench')
            target = ctx.opponent_bench()[0]
            before = target.get_attribute(AttrID.HP)
            ctx.choose_pokemon = AsyncMock(return_value=target)
            await ctx.ability.effect(ctx)
            self.assertEqual(before - target.get_attribute(AttrID.HP), 30 if present else 0)
            if not present:
                ctx.choose_pokemon.assert_not_awaited()

    async def test_pheromone_poison_requires_benched_female(self):
        for pid in (P1, P2):
            rig, e, ctx = self.ctx('HGSS4.Nidoran_70', 'Pheromone Poison')
            self.add(rig, definition('HGSS4.Nidoran_69'), pid, 'bench')
            await ctx.ability.effect(ctx)
            self.assertEqual('Poisoned' in (ctx.defender.get_attribute(AttrID.SPECIAL_CONDITIONS) or []), pid == P1)

    async def test_tentavolve_only_immediately_after_evolution(self):
        for this_turn in (False, True):
            rig, e, ctx = self.ctx('HGSS4.Tentacruel_50', 'Tentavolve')
            basic = self.add(rig, definition('HGSS4.Tentacool_80'), P1, 'hand')
            rig.attach(basic, ctx.source)
            rig.session.turn_state.entered_play_turn[ctx.source.entity_id] = rig.session.turn_state.turn_number - (not this_turn)
            await ctx.ability.effect(ctx)
            states = ctx.defender.get_attribute(AttrID.SPECIAL_CONDITIONS) or []
            self.assertEqual('Poisoned' in states, this_turn)
            self.assertEqual('Paralyzed' in states, this_turn)

    async def test_fury_cutter_all_coin_totals(self):
        for heads, amount in enumerate((20, 40, 60, 120)):
            rig, e, ctx = self.ctx('HGSS4.Kricketune_24', 'Fury Cutter')
            self.neutral(ctx.defender)
            ctx.defender.set_attribute(AttrID.HP, 200)
            ctx.flip_coins = AsyncMock(return_value=[True] * heads + [False] * (3 - heads))
            await ctx.ability.effect(ctx)
            self.assertEqual(ctx.defender.get_attribute(AttrID.HP), 200 - amount)

    async def test_destructive_tsunami_affects_exactly_coin_chosen_side(self):
        for heads in (False, True):
            rig, e, ctx = self.ctx('COL.Kyogre_12', 'Destructive Tsunami')
            pokemon = ctx.my_pokemon_in_play() + ctx.opponent_pokemon_in_play()
            for p in pokemon:
                self.neutral(p)
            before = {p.entity_id: p.get_attribute(AttrID.HP) for p in pokemon}
            ctx.flip_coins = AsyncMock(return_value=[heads])
            await ctx.ability.effect(ctx)
            for p in pokemon:
                self.assertEqual(before[p.entity_id] - p.get_attribute(AttrID.HP),
                                 40 if p.owning_player_id == (P2 if heads else P1) else 0)

    async def test_healing_items_reject_undamaged_field(self):
        for path in ('HGSS1.MoomooMilk_94', 'HGSS2.LifeHerb_79'):
            rig, e = self.rig(path, 'trainer')
            card = definition(path)
            self.assertFalse(card.condition(rig.board, P1, e['target']), path)
            active = rig.board.active_pokemon(P1)
            active.set_attribute(AttrID.HP, active.get_attribute(AttrID.HP) - 10)
            self.assertTrue(card.condition(rig.board, P1, e['target']), path)

    async def test_tropical_tidal_wave_discards_only_coin_chosen_side(self):
        for heads in (False, True):
            rig, e = self.rig('Promo_HGSS.TropicalTidalWave_18', 'trainer')
            ctx = EffectContext(rig.session, P1, e['target'], None)
            tools = []
            for pid in (P1, P2):
                card = self.add(rig, definition('HGSS3.Defender_72'), pid, 'hand')
                rig.attach(card, rig.board.active_pokemon(pid))
                tools.append(card)
            ctx.flip_coins = AsyncMock(return_value=[heads])
            await definition('Promo_HGSS.TropicalTidalWave_18').effect(ctx)
            for card in tools:
                self.assertEqual(card in ctx.discard_pile(card.owning_player_id),
                                 card.owning_player_id == (P2 if heads else P1))

    async def test_take_away_returns_whole_stacks_and_user_promotes_first(self):
        rig, e, ctx = self.ctx('HGSS3.Drifblim_12', 'Take Away')
        stacks = {P1: full_stack(ctx.source), P2: full_stack(ctx.defender)}
        rig.session._promote_new_active = AsyncMock(return_value=True)
        await ctx.ability.effect(ctx)
        for pid, cards in stacks.items():
            for card in cards:
                self.assertIn(card, ctx.deck(pid))
        self.assertEqual([call.args[0] for call in rig.session._promote_new_active.call_args_list], [P1, P2])

    async def test_lost_world_requires_six_opposing_pokemon_and_own_turn(self):
        rig, e = self.rig('COL.LostWorld_81', 'trainer')
        ability = definition('COL.LostWorld_81').ability
        state = rig.session.turn_state
        state.active_player_id = P1
        for i in range(6):
            self.assertFalse(ability.condition(rig.board, P1, e['target']))
            self.add(rig, self.filler, P2, 'lostZone')
        self.assertTrue(ability.condition(rig.board, P1, e['target']))
        ctx = EffectContext(rig.session, P1, e['target'], ability)
        ctx.win_game = AsyncMock()
        await ability.effect(ctx)
        ctx.win_game.assert_awaited_once_with('Lost World')
        state.in_checkup = True
        self.assertFalse(ability.condition(rig.board, P1, e['target']))
        state.in_checkup = False
        state.active_player_id = P2
        self.assertFalse(ability.condition(rig.board, P1, e['target']))
        self.assertFalse(ability.condition(rig.board, P2, e['target']))

    async def test_condition_immunities_are_specific(self):
        from spirit.game.attributes import SpecialConditions
        cases = [('Promo_HGSS.Hoothoot_5', 'Asleep', 'Poisoned'),
                 ('HGSS4.Rapidash_8', 'Confused', 'Poisoned'),
                 ('HGSS2.Steelix_87', 'Poisoned', None)]
        for path, blocked, allowed in cases:
            rig, e = self.rig(path)
            ctx = EffectContext(rig.session, P2, rig.board.active_pokemon(P2), None)
            await ctx.apply_special_condition(e['target'], SpecialConditions[blocked.upper()])
            self.assertNotIn(blocked, e['target'].get_attribute(AttrID.SPECIAL_CONDITIONS) or [])
            if allowed:
                await ctx.apply_special_condition(e['target'], SpecialConditions[allowed.upper()])
                self.assertIn(allowed, e['target'].get_attribute(AttrID.SPECIAL_CONDITIONS) or [])

    async def test_luster_float_only_latios_and_requires_own_latias(self):
        from spirit.game.session.passives import effective_retreat_cost
        rig, e = self.rig('Promo_HGSS.Latios_11')
        target = e['target']
        target.set_attribute(AttrID.RETREAT_COST, 3)
        ally = rig.board.pokemon_in_play(P1)[1]
        ally.set_attribute(AttrID.RETREAT_COST, 3)
        self.assertEqual(effective_retreat_cost(rig.board, target), 3)
        self.add(rig, definition('Promo_HGSS.Latias_10'), P2, 'bench')
        self.assertEqual(effective_retreat_cost(rig.board, target), 3)
        self.add(rig, definition('Promo_HGSS.Latias_10'), P1, 'bench')
        self.assertEqual(effective_retreat_cost(rig.board, target), 0)
        # The rig's first bencher is another Latios; use a plain ally instead.
        ally = self.add(rig, self.filler, P1, 'bench')
        ally.set_attribute(AttrID.RETREAT_COST, 3)
        self.assertEqual(effective_retreat_cost(rig.board, ally), 3)

    async def test_boost_gas_and_free_flight_ignore_non_energy_attachments(self):
        from spirit.game.session.passives import effective_retreat_cost
        for path, empty, attached in [('HGSS2.Pupitar_38', 3, 0), ('HGSS4.Yanma_84', 0, 3)]:
            rig, e = self.rig(path)
            source = e['target']
            for energy in list(rig.board.attached_energies(source)):
                rig.to_area(energy, P1, 'hand')
            source.set_attribute(AttrID.RETREAT_COST, 3)
            tool = self.add(rig, definition('HGSS3.Defender_72'), P1, 'hand')
            rig.attach(tool, source)
            self.assertEqual(effective_retreat_cost(rig.board, source), empty)
            energy = rig.pull_guid(P1, self.energies[PokemonTypes.WATER.value])
            rig.attach(energy, source)
            self.assertEqual(effective_retreat_cost(rig.board, source), attached)

    async def test_insight_updates_cost_when_hand_counts_change(self):
        from spirit.game.session.passives import effective_attack_cost
        rig, e = self.rig('HGSS4.Yanmega_98')
        for pid in (P1, P2):
            for card in list(rig.board.find_player_area(pid, 'hand').children):
                rig.to_area(card, pid, 'deck')
        self.assertEqual(effective_attack_cost(rig.board, e['target'], {'Colorless': 3}), {})
        self.add(rig, self.filler, P1, 'hand')
        self.assertEqual(effective_attack_cost(rig.board, e['target'], {'Colorless': 3}), {'Colorless': 3})

    async def test_trick_reveal_needs_at_least_one_nonempty_hand(self):
        rig, e, ctx = self.ctx('COL.MrMime_29', 'Trick Reveal')
        for pid in (P1, P2):
            for card in list(ctx.hand(pid)):
                rig.to_area(card, pid, 'deck')
        self.assertFalse(ctx.ability.condition(rig.board, P1, ctx.source))
        self.add(rig, self.filler, P2, 'hand')
        self.assertTrue(ctx.ability.condition(rig.board, P1, ctx.source))

    async def test_berserk_requires_damage_and_only_boosts_its_holder(self):
        from spirit.game.session.passives import compute_damage
        rig, e = self.rig('HGSS2.Ursaring_89')
        target = rig.board.active_pokemon(P2)
        self.neutral(target)
        self.assertEqual(compute_damage(rig.board, e['target'], target, 30).amount, 30)
        e['target'].set_attribute(AttrID.HP, e['target'].get_attribute(AttrID.HP) - 10)
        self.assertEqual(compute_damage(rig.board, e['target'], target, 30).amount, 90)
        ally = self.add(rig, self.filler, P1, 'bench')
        self.assertEqual(compute_damage(rig.board, ally, target, 30).amount, 30)

    async def test_take_away_last_pokemon_on_both_sides_is_a_tie(self):
        from spirit.game.session.game_session import SuddenDeath
        rig, e, ctx = self.ctx('HGSS3.Drifblim_12', 'Take Away')
        for pid in (P1, P2):
            for pokemon in list(rig.board.find_player_area(pid, 'bench').children):
                rig.to_area(pokemon, pid, 'deck')
        rig.session.end_game = AsyncMock()
        with self.assertRaises(SuddenDeath):
            await ctx.ability.effect(ctx)
        rig.session.end_game.assert_not_awaited()

    async def test_simultaneous_win_conditions_are_compared_before_ending(self):
        from spirit.game.session.game_session import SuddenDeath
        rig, e = self.rig('HGSS3.Drifblim_12')
        rig.session.end_game = AsyncMock()
        for pid in (P1, P2):
            rig.board.prizes_dealt[pid] = 6
            for card in list(rig.board.find_player_area(pid, 'prizePile').children):
                rig.to_area(card, pid, 'hand')
        with self.assertRaises(SuddenDeath):
            await rig.session._resolve_simultaneous_win_conditions()
        rig.session.end_game.assert_not_awaited()
        for pokemon in list(rig.board.pokemon_in_play(P2)):
            rig.to_area(pokemon, P2, 'discard')
        await rig.session._resolve_simultaneous_win_conditions()
        self.assertEqual(rig.session.end_game.call_args.args[0], P1)

    async def test_sudden_death_returns_all_cards_and_deals_one_prize(self):
        rig, e = self.rig('HGSS3.Drifblim_12')
        self.add(rig, self.filler, P1, 'lostZone')
        rig.session.turn_state.turn_number = 12
        e['target'].set_attribute(AttrID.HP, 10)
        ctx = EffectContext(rig.session, P1, e['target'], None)
        before = {}
        for pid in (P1, P2):
            before[pid] = set()
            for zone in ('hand', 'deck', 'discard', 'lostZone', 'prizePile', 'activePokemonArea', 'bench'):
                for card in rig.board.find_player_area(pid, zone).children:
                    before[pid].update(c.entity_id for c in full_stack(card))
        await rig.session._reset_sudden_death_round()
        for pid in (P1, P2):
            self.assertEqual({c.entity_id for c in ctx.deck(pid)}, before[pid])
            self.assertEqual(rig.board.pokemon_in_play(pid), [])
        self.assertEqual(rig.session.turn_state.turn_number, 0)
        self.assertIs(rig.board.turn_state, rig.session.turn_state)
        self.assertEqual(e['target'].get_attribute(AttrID.HP), ctx.max_hp(e['target']))
        rig.session.first_player_id = P1
        await rig.session._deal_prize_cards()
        for pid in (P1, P2):
            self.assertEqual(len(rig.board.find_player_area(pid, 'prizePile').children), 1)
