"""Printed costs, Mega ex evolution, and damage versus attack effects."""
import unittest
from unittest.mock import AsyncMock, Mock

from tests import test_hgss_rules as fixtures
from tests.test_hgss_rules import definition
from spirit.game.attributes import AttrID, SpecialConditions
from spirit.game.data_utils import Ability, Attack, CARD_DEFS_BY_GUID
from spirit.game.session.effects import EffectContext
from spirit.game.session.passives import Passive
from spirit.game.card_effects.standard_era import _mandatory_hand_discard_cost, _search_predicate
from spirit.tools.effect_smoke import P1, P2


class ModernCostsAndShieldsTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx
    add = fixtures.HgssRulesTests.add

    COST_CARDS = (
        'SV05.MortysConviction_155', 'SV09.IrissFightingSpirit_149',
        'SV065.EarthenVessel_96', 'SV085.TechnoRadar_130',
    )

    async def test_another_card_cost_is_paid_before_drawing_or_searching(self):
        for path in self.COST_CARDS:
            with self.subTest(card=path):
                rig, e = self.rig(path, 'trainer')
                source = e['target']
                # Trainer resolution removes the played card from the hand.
                rig.to_area(source, P1, 'discard')
                ctx = EffectContext(rig.session, P1, source, None)
                events = []
                original = ctx.discard_from_hand
                async def pay(*args, **kwargs):
                    events.append('cost')
                    return await original(*args, **kwargs)
                ctx.discard_from_hand = AsyncMock(side_effect=pay)
                ctx.choose_cards = AsyncMock(side_effect=lambda pool, count, **kw: pool[:count])
                async def draw(*args, **kwargs):
                    events.append('draw')
                async def search(*args, **kwargs):
                    events.append('search')
                    return []
                ctx.draw_cards = AsyncMock(side_effect=draw)
                ctx.draw_until = AsyncMock(side_effect=draw)
                ctx.search_deck = AsyncMock(side_effect=search)
                before = len(ctx.hand())
                await definition(path).effect(ctx)
                self.assertEqual(events[0], 'cost')
                self.assertEqual(len(events), 2)
                ctx.discard_from_hand.assert_awaited_once()
                self.assertEqual(len(ctx.hand()), before - 1)

    async def test_missing_cost_prevents_play_and_stops_resolution(self):
        for path in self.COST_CARDS:
            with self.subTest(card=path):
                rig, e = self.rig(path, 'trainer')
                source = e['target']
                for card in list(rig.board.find_player_area(P1, 'hand').children):
                    if card is not source:
                        rig.to_area(card, P1, 'discard')
                self.assertFalse(definition(path).condition(rig.board, P1, source))
                rig.to_area(source, P1, 'discard')
                ctx = EffectContext(rig.session, P1, source, None)
                ctx.discard_from_hand = AsyncMock(return_value=[])
                ctx.draw_cards = AsyncMock()
                ctx.draw_until = AsyncMock()
                ctx.search_deck = AsyncMock()
                await definition(path).effect(ctx)
                ctx.draw_cards.assert_not_awaited()
                ctx.draw_until.assert_not_awaited()
                ctx.search_deck.assert_not_awaited()

    def test_optional_and_post_draw_discards_are_not_upfront_costs(self):
        for text in ('you may discard another card from your hand. if you do, draw 3 cards.',
                     'draw 3 cards. discard another card from your hand.',
                     'discard up to 2 cards from your hand. draw that many cards.'):
            self.assertIsNone(_mandatory_hand_discard_cost(text))
        self.assertEqual(_mandatory_hand_discard_cost(
            'you can use this card only if you discard another card from your hand. draw 3 cards.'), (1, 'card'))

    async def test_techno_radar_filters_future_pokemon(self):
        rig, e, ctx = self.ctx('BW1.Snivy_1', 'Tackle')
        future = self.add(rig, definition('SV05.IronCrownex_81'), P1, 'deck')
        pred = _search_predicate('search your deck for up to 2 future pokémon, reveal them')
        self.assertTrue(pred(future))
        self.assertFalse(pred(ctx.attacker))

    async def test_morty_needs_opponents_bench_and_a_nonempty_deck(self):
        path = 'SV05.MortysConviction_155'
        rig, e = self.rig(path, 'trainer')
        source = e['target']
        self.assertTrue(definition(path).condition(rig.board, P1, source))
        for pokemon in list(rig.board.find_player_area(P2, 'bench').children):
            rig.to_area(pokemon, P2, 'discard')
        self.assertFalse(definition(path).condition(rig.board, P1, source))
        self.add(rig, self.filler, P2, 'bench')
        for card in list(rig.board.find_player_area(P1, 'deck').children):
            rig.to_area(card, P1, 'discard')
        self.assertFalse(definition(path).condition(rig.board, P1, source))

    async def test_iris_checks_hand_size_after_paying_cost(self):
        path = 'SV09.IrissFightingSpirit_149'
        rig, e = self.rig(path, 'trainer')
        source = e['target']
        for card in list(rig.board.find_player_area(P1, 'hand').children):
            if card is not source:
                rig.to_area(card, P1, 'discard')
        for _ in range(6):
            self.add(rig, self.filler, P1, 'hand')
        self.assertTrue(definition(path).condition(rig.board, P1, source))
        self.add(rig, self.filler, P1, 'hand')
        self.assertFalse(definition(path).condition(rig.board, P1, source))

    async def test_all_modern_mega_printings_keep_turn_on_evolution(self):
        rig, e, ctx = self.ctx('BW1.Snivy_1', 'Tackle')
        rig.session._validated_target = Mock(return_value=ctx.attacker.entity_id)
        rig.session.perform_evolution = AsyncMock(return_value=True)
        modern = [d for d in list(CARD_DEFS_BY_GUID.values()) if 'SV_Mega' in (getattr(d, 'subtypes', ()) or ())]
        self.assertGreater(len(modern), 20)
        for card_def in modern:
            with self.subTest(card=card_def.display_name, set=card_def.set_code, number=card_def.collector_number):
                card = self.add(rig, card_def, P1, 'hand')
                self.assertFalse(await rig.session._execute_evolve(P1, card, {}, [ctx.attacker.entity_id]))

    async def test_xy_mega_rule_and_spirit_link_are_preserved(self):
        rig, e, ctx = self.ctx('BW1.Snivy_1', 'Tackle')
        rig.session._validated_target = Mock(return_value=ctx.attacker.entity_id)
        rig.session.perform_evolution = AsyncMock(return_value=True)
        mega = self.add(rig, definition('XY4.MManectricEX_24'), P1, 'hand')
        self.assertTrue(await rig.session._execute_evolve(P1, mega, {}, [ctx.attacker.entity_id]))
        link = self.add(rig, definition('XY4.ManectricSpiritLink_100'), P1, 'hand')
        rig.attach(link, ctx.attacker)
        self.assertFalse(await rig.session._execute_evolve(P1, mega, {}, [ctx.attacker.entity_id]))

    async def test_chaotic_pain_is_blocked_but_attack_damage_is_not(self):
        rig, e, ctx = self.ctx('ME55.Gengarex_90', 'Chaotic Pain')
        empoleon = self.add(rig, definition('ME2.Empoleonex_70'), P2, 'bench')
        hp = empoleon.get_attribute(AttrID.HP)
        ctx.choose_pokemon = AsyncMock(return_value=empoleon)
        await ctx.ability.effect(ctx)
        self.assertEqual(empoleon.get_attribute(AttrID.HP), hp)
        await ctx.set_damage_counters(empoleon, 20)
        self.assertEqual(empoleon.get_attribute(AttrID.HP), hp)
        self.assertFalse(await ctx.apply_special_condition(empoleon, SpecialConditions.POISONED))
        self.assertEqual(await ctx.deal_damage(40, empoleon), 40)
        rig.session.turn_state.abilities_disabled_through_turn = rig.session.turn_state.turn_number
        await ctx.ability.effect(ctx)
        self.assertEqual(empoleon.get_attribute(AttrID.HP), hp - 170)

    async def test_emperor_does_not_block_ability_counters(self):
        rig, e, ctx = self.ctx('ME55.Gengarex_90', 'Chaotic Pain')
        target = self.add(rig, definition('ME2.Empoleonex_70'), P2, 'bench')
        ability_ctx = EffectContext(rig.session, P1, ctx.attacker, Ability(title='Test Ability'))
        self.assertEqual(await ability_ctx.deal_damage(30, target, as_counters=True), 30)

    async def test_protection_covers_energy_removal_devolution_and_stack_moves(self):
        for action in ('hand', 'deck', 'discard', 'lost'):
            with self.subTest(action=action):
                rig, e, ctx = self.ctx('ME55.Gengarex_90', 'Chaotic Pain')
                target = self.add(rig, definition('ME2.Empoleonex_70'), P2, 'bench')
                energy = self.add(rig, definition('BW1.MetalEnergy_112'), P2, 'hand')
                rig.attach(energy, target)
                self.assertEqual(await ctx.discard_energy_from(target, 1), [])
                rig.session.perform_devolution = AsyncMock()
                self.assertEqual(await ctx.devolve_pokemon(target), [])
                rig.session.perform_devolution.assert_not_awaited()
                from spirit.game.session.effects import full_stack
                moves = {'hand': ctx.put_in_hand, 'deck': ctx.shuffle_into_deck,
                         'discard': ctx.discard_cards, 'lost': ctx.move_to_lost_zone}
                await moves[action](full_stack(target))
                self.assertIn(target, ctx.opponent_bench())
                self.assertIn(energy, ctx.attached_energies(target))
                # The same Ability cannot prevent rule-based KO cleanup.
                target.set_attribute(AttrID.HP, 0)
                await ctx.discard_cards(full_stack(target))
                self.assertIn(target, ctx.discard_pile(P2))
                self.assertIn(energy, ctx.discard_pile(P2))

    async def test_protection_prevents_retreat_lock_and_temporary_riders(self):
        rig, e, ctx = self.ctx('ME55.Gengarex_90', 'Chaotic Pain')
        target = self.add(rig, definition('ME2.Empoleonex_70'), P2, 'bench')
        rig.session.turn_state.lock_retreat = Mock()
        ctx.lock_retreat(target)
        rig.session.turn_state.lock_retreat.assert_not_called()
        from spirit.game.card_effects.bw_era import _BWTurnShield
        before = len(rig.board.temporary_passives)
        ctx.add_temporary_passive(target, _BWTurnShield(amount=10))
        self.assertEqual(len(rig.board.temporary_passives), before)

    async def test_counter_only_shield_does_not_prevent_removing_counters(self):
        class CounterShield(Passive):
            def blocks_damage_counters(self, target, carrier):
                return target is carrier
        rig, e, ctx = self.ctx('ME55.Gengarex_90', 'Chaotic Pain')
        target = self.add(rig, definition('BW1.Snivy_1'), P2, 'bench')
        ctx.add_temporary_passive(target, CounterShield())
        target.set_attribute(AttrID.HP, 20)
        await ctx.set_damage_counters(target, 5)
        self.assertEqual(target.get_attribute(AttrID.HP), 20)
        await ctx.set_damage_counters(target, 1)
        self.assertEqual(target.get_attribute(AttrID.HP), ctx.max_hp(target) - 10)

    async def test_energy_and_type_scoped_team_shields(self):
        cases = [('SV3.Toedscruelex_22', 'energy'), ('XY11.MagearnaEX_75', 'metal'),
                 ('DM.Flygon_39', 'dragon'), ('SV10.TeamRocketsArticuno_51', 'rocket')]
        for path, mode in cases:
            with self.subTest(card=path):
                rig, e, ctx = self.ctx('ME55.Gengarex_90', 'Chaotic Pain')
                shield = self.add(rig, definition(path), P2, 'bench')
                target_path = {'rocket': 'SV10.TeamRocketsArticuno_51', 'dragon': 'BW6.Gible_87'}.get(mode, 'BW1.Snivy_1')
                target = self.add(rig, definition(target_path), P2, 'bench')
                if mode in ('energy', 'metal'):
                    self.assertFalse(ctx.effects_blocked(target))
                    tool = self.add(rig, definition('BW9.FloatStone_99'), P2, 'hand')
                    rig.attach(tool, target)
                    self.assertFalse(ctx.effects_blocked(target))
                    energy = self.add(rig, definition('BW1.MetalEnergy_112'), P2, 'hand')
                    rig.attach(energy, target)
                self.assertTrue(ctx.effects_blocked(target))
                unrelated = self.add(rig, definition('BW1.Snivy_1'), P2, 'bench')
                self.assertFalse(ctx.effects_blocked(unrelated))
                self.assertFalse(ctx.effects_blocked(ctx.attacker))

    async def test_bench_and_active_requirements_on_shields(self):
        rig, e, ctx = self.ctx('ME55.Gengarex_90', 'Chaotic Pain')
        pokemon = self.add(rig, definition('SV06.Poltchageist_20'), P2, 'bench')
        self.assertTrue(ctx.effects_blocked(pokemon))
        self.assertEqual(await ctx.deal_damage(20, pokemon), 0)
        rig.to_area(ctx.defender, P2, 'bench')
        rig.to_area(pokemon, P2, 'activePokemonArea')
        self.assertFalse(ctx.effects_blocked(pokemon))
        suicune = self.add(rig, definition('XY9.Suicune_30'), P2, 'bench')
        self.assertFalse(ctx.effects_blocked(pokemon))
        rig.to_area(pokemon, P2, 'bench')
        rig.to_area(suicune, P2, 'activePokemonArea')
        self.assertTrue(ctx.effects_blocked(pokemon))
        self.assertTrue(ctx.effects_blocked(suicune))

    async def test_source_restricted_damage_and_effect_protection_match(self):
        cases = [('SL.Hoopa_55', 'BW7.KeldeoEX_49', 'BW1.Snivy_1'),
                 ('XY12.Mew_53', 'BW1.Servine_3', 'BW1.Snivy_1'),
                 ('SV08.Miloticex_42', 'SV06.TealMaskOgerponex_25', 'BW1.Snivy_1'),
                 ('BW9.LatiasEX_112', 'ME2.Empoleonex_70', 'BW1.Snivy_1')]
        for target_path, yes_path, no_path in cases:
            for attacker_path, protected in ((yes_path, True), (no_path, False)):
                with self.subTest(target=target_path, attacker=attacker_path):
                    rig, e, ctx = self.ctx('ME55.Gengarex_90', 'Chaotic Pain')
                    target = self.add(rig, definition(target_path), P2, 'bench')
                    attacker = self.add(rig, definition(attacker_path), P1, 'bench')
                    attack_ctx = EffectContext(rig.session, P1, attacker, Attack(title='Test', damage=10))
                    self.assertEqual(attack_ctx.effects_blocked(target), protected)
                    self.assertEqual(await attack_ctx.deal_damage(10, target), 0 if protected else 10)

    async def test_force_canceler_only_blocks_gx_and_requires_active(self):
        rig, e, ctx = self.ctx('ME55.Gengarex_90', 'Chaotic Pain')
        shield = self.add(rig, definition('SM10.CelesteelaGX_163'), P2, 'bench')
        target = ctx.defender
        gx = Attack(title='Test-GX', gx=True, damage=20)
        gx_ctx = EffectContext(rig.session, P1, ctx.attacker, gx)
        self.assertFalse(gx_ctx.effects_blocked(target))
        rig.to_area(target, P2, 'bench')
        rig.to_area(shield, P2, 'activePokemonArea')
        self.assertTrue(gx_ctx.effects_blocked(target))
        self.assertFalse(ctx.effects_blocked(target))
        self.assertEqual(await gx_ctx.deal_damage(20, target), 0)
        self.assertEqual(await ctx.deal_damage(20, target), 20)
