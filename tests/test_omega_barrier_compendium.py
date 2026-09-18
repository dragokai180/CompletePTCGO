"""Regression scenarios from the Compendium's seven Omega Barrier rulings.

https://compendium.pokegym.net/category/4-abilities/omega-barrier/
"""
import unittest
from unittest.mock import AsyncMock, patch
from tests import test_hgss_rules as fixtures
from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.session.effects import EffectContext
from spirit.game.session.legal_actions import (
    compute_legal_actions, trainer_condition_met, tool_attachment_targets,
)
from spirit.game.session.passives import def_for, effective_attack_cost, compute_damage
from spirit.tools.effect_smoke import P1, P2


class OmegaBarrierCompendiumTests(unittest.IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls):
        fixtures.HgssRulesTests.setUpClass()
        cls.fixture = fixtures.HgssRulesTests()

    def add(self, rig, path, owner=P2, zone='bench'):
        return self.fixture.add(rig, fixtures.definition(path), owner, zone)

    def setup_trainer(self, path):
        rig, e = self.fixture.rig('BW1.Snivy_1')
        trainer = self.add(rig, path, P1, 'hand')
        ctx = EffectContext(rig.session, P1, trainer, None)
        ctx.is_trainer_effect = True
        return rig, e, ctx, def_for(trainer.archetype_id)

    def active(self, rig, pokemon, owner=P2):
        rig.to_area(rig.board.active_pokemon(owner), owner, 'bench')
        rig.to_area(pokemon, owner, 'activePokemonArea')

    async def test_avery_player_discards_selected_barrier_stacks(self):
        for protected in (False, True):
            with self.subTest(protected=protected):
                rig, e, ctx, card = self.setup_trainer('SWSH6.Avery_130')
                victims = [self.add(rig, 'Promo_XY.Regirock_49' if protected else 'BW1.Snivy_1') for _ in range(2)]
                self.add(rig, 'BW1.Snivy_1')
                self.assertEqual(len(ctx.opponent_bench()), 5)
                energy = self.add(rig, 'BW1.FightingEnergy_110', P2, 'hand')
                rig.attach(energy, victims[0])
                # A finite chooser avoids hanging the audit if no card moves.
                ctx.choose_pokemon = AsyncMock(side_effect=[*victims, None])
                hand_before = ctx.hand_size()
                await card.effect(ctx)
                self.assertEqual(ctx.hand_size(), hand_before + 3)
                self.assertEqual(ctx.choose_pokemon.call_args_list[0].kwargs['player_id'], P2)
                self.assertEqual(len(ctx.opponent_bench()), 3)
                for target in [*victims, energy]:
                    self.assertIn(target, ctx.discard_pile(P2))

    async def test_cyrus_player_shuffles_unselected_barrier_stack(self):
        for protected in (False, True):
            with self.subTest(protected=protected):
                rig, e, ctx, card = self.setup_trainer('SM5.Cyrus_120')
                e['target'].set_attribute(AttrID.POKEMON_TYPES, [PokemonTypes.WATER.value])
                keep = list(ctx.opponent_bench())
                target = self.add(rig, 'Promo_XY.Regirock_49' if protected else 'BW1.Snivy_1')
                energy = self.add(rig, 'BW1.FightingEnergy_110', P2, 'hand')
                rig.attach(energy, target)
                self.assertTrue(trainer_condition_met(card.condition, rig.board, P1, ctx.source))
                ctx.choose_cards = AsyncMock(return_value=keep)
                await card.effect(ctx)
                ctx.choose_cards.assert_awaited()
                self.assertEqual(ctx.choose_cards.call_args.kwargs['player_id'], P2)
                self.assertEqual(ctx.opponent_bench(), keep)
                self.assertIn(target, ctx.deck(P2))
                self.assertIn(energy, ctx.deck(P2))

    async def test_target_whistle_can_bench_barrier_from_discard(self):
        rig, e, ctx, card = self.setup_trainer('XY4.TargetWhistleTeamFlareGear_106')
        target = self.add(rig, 'Promo_XY.Regirock_49', P2, 'discard')
        self.assertTrue(trainer_condition_met(card.condition, rig.board, P1, ctx.source))
        async def pick(pool, *args, **kwargs):
            self.assertIn(target, pool)
            return [target]
        ctx.choose_cards = AsyncMock(side_effect=pick)
        await card.effect(ctx)
        self.assertIn(target, ctx.opponent_bench())
        self.assertNotIn(target, ctx.my_bench())
        self.assertTrue(ctx._trainer_blocked(target))

    async def test_captivating_poke_puff_can_bench_barrier_from_hand(self):
        for protected in (False, True):
            with self.subTest(protected=protected):
                rig, e, ctx, card = self.setup_trainer('XY11.CaptivatingPokPuff_99')
                target = self.add(rig, 'Promo_XY.Regirock_49' if protected else 'BW1.Snivy_1', P2, 'hand')
                self.assertTrue(trainer_condition_met(card.condition, rig.board, P1, ctx.source))
                # Preserve effect processing; only replace the visual hand browser.
                ctx.reveal_hand = AsyncMock(return_value=list(ctx.hand(P2)))
                ctx.choose_cards = AsyncMock(return_value=[target])
                ctx.choose_pokemon = AsyncMock(return_value=target)
                await card.effect(ctx)
                ctx.reveal_hand.assert_awaited_once()
                self.assertIn(target, ctx.opponent_bench())
                self.assertNotIn(target, ctx.hand(P2))

    async def test_lysandre_shields_selected_bencher_not_old_active(self):
        for active_protected, bench_protected in ((False, False), (True, False), (False, True), (True, True)):
            with self.subTest(active=active_protected, bench=bench_protected):
                rig, e, ctx, card = self.setup_trainer('XY2.Lysandre_90')
                if active_protected:
                    self.active(rig, self.add(rig, 'XY5.PrimalGroudonEX_86'))
                old_active = ctx.opponent_active()
                target = self.add(rig, 'Promo_XY.Regirock_49' if bench_protected else 'BW1.Snivy_1')
                ctx.choose_pokemon = AsyncMock(return_value=target)
                await card.effect(ctx)
                self.assertIs(ctx.opponent_active(), old_active if bench_protected else target)

    async def test_escape_rope_shields_old_active_not_selected_bencher(self):
        for active_protected, bench_protected in ((False, False), (True, False), (False, True), (True, True)):
            with self.subTest(active=active_protected, bench=bench_protected):
                rig, e, ctx, card = self.setup_trainer('BW8.EscapeRope_120')
                if active_protected:
                    self.active(rig, self.add(rig, 'XY5.PrimalGroudonEX_86'))
                old_active = ctx.opponent_active()
                target = self.add(rig, 'Promo_XY.Regirock_49' if bench_protected else 'BW1.Snivy_1')
                own = ctx.my_bench()[0]
                async def pick(pool, *args, **kwargs):
                    return target if kwargs.get('player_id') == P2 else own
                ctx.choose_pokemon = AsyncMock(side_effect=pick)
                await card.effect(ctx)
                self.assertIs(ctx.my_active(), own)
                self.assertIs(ctx.opponent_active(), old_active if active_protected else target)

    async def test_tool_f_can_attach_to_opposing_ex_with_barrier(self):
        for path in ('XY4.HeadRingerTeamFlareHyperGear_97', 'XY4.JammingNetTeamFlareHyperGear_98'):
            for protected in (False, True):
                with self.subTest(path=path, protected=protected):
                    rig, e, ctx, card = self.setup_trainer(path)
                    target = self.add(rig, 'XY5.PrimalGroudonEX_86' if protected else 'XY5.GroudonEX_85')
                    actions = compute_legal_actions(rig.board, rig.session.turn_state, P1, rig.session.game_id)
                    entries = [a for a in actions if a['entityID'] == ctx.source.entity_id]
                    valid = [v for a in entries for info in a.get('targetInfoLst', []) for v in info.get('validTargets', [])]
                    self.assertIn(target.entity_id, valid)
                    self.assertNotIn(e['target'].entity_id, valid)
                    entry = next(a for a in entries if target.entity_id in str(a['targetInfoLst']))
                    await rig.session._execute_attach_tool(P1, ctx.source, entry, [target.entity_id])
                    self.assertIs(ctx.source.parent, target)

    async def test_tool_f_effect_itself_not_blocked_by_barrier(self):
        for path, damage in [('XY4.HeadRingerTeamFlareHyperGear_97', False), ('XY4.JammingNetTeamFlareHyperGear_98', True)]:
            with self.subTest(path=path):
                rig, e, ctx, card = self.setup_trainer(path)
                target = self.add(rig, 'XY5.PrimalGroudonEX_86')
                self.active(rig, target)
                rig.attach(ctx.source, target)
                self.assertFalse(ctx._trainer_blocked(target))
                if damage:
                    result = compute_damage(rig.board, target, e['target'], 100, ignore_weakness=True, ignore_resistance=True)
                    self.assertEqual(result.amount, 80)
                else:
                    result = effective_attack_cost(rig.board, target, {PokemonTypes.FIGHTING.value: 4})
                    self.assertEqual(sum(result.values()), 5)

    async def test_tool_f_rejects_invalid_and_stale_targets(self):
        rig, e, ctx, card = self.setup_trainer('XY4.HeadRingerTeamFlareHyperGear_97')
        own_ex = self.add(rig, 'XY5.GroudonEX_85', P1)
        modern_ex = self.add(rig, 'SV1.Gardevoirex_86')
        double = self.add(rig, 'XY7.MTyranitarEX_43')
        self.assertIn(double, tool_attachment_targets(rig.board, P1, ctx.source))
        actions = compute_legal_actions(rig.board, rig.session.turn_state, P1, rig.session.game_id)
        entry = next(a for a in actions if a['entityID'] == ctx.source.entity_id)
        occupied = self.add(rig, 'BW9.FloatStone_99', P2, 'hand')
        rig.attach(occupied, double)
        targets = tool_attachment_targets(rig.board, P1, ctx.source)
        for invalid in (own_ex, modern_ex, double, e['target']):
            self.assertNotIn(invalid, targets)
        # Even theta Double's spare Tool slot does not satisfy Tool F's rule.
        await rig.session._execute_attach_tool(P1, ctx.source, entry, [double.entity_id])
        self.assertIn(ctx.source, ctx.hand())

    async def test_ordinary_tools_still_only_attach_to_own_pokemon(self):
        rig, e, ctx, card = self.setup_trainer('BW9.FloatStone_99')
        opponent_ex = self.add(rig, 'XY5.PrimalGroudonEX_86')
        targets = tool_attachment_targets(rig.board, P1, ctx.source)
        self.assertIn(e['target'], targets)
        self.assertNotIn(opponent_ex, targets)
        self.assertTrue(all(p.owning_player_id == P1 for p in targets))

    async def test_player_directed_scope_restores_shields_and_keeps_global_checks(self):
        rig, e, ctx, card = self.setup_trainer('SWSH6.Avery_130')
        target = self.add(rig, 'Promo_XY.Regirock_49')
        self.assertTrue(ctx._trainer_blocked(target))
        with self.assertRaisesRegex(ValueError, 'selection failed'):
            with ctx.trainer_effect_on_player(P2):
                self.assertFalse(ctx._trainer_blocked(target))
                with ctx.trainer_effect_on_player(P1):
                    self.assertTrue(ctx._trainer_blocked(target))
                self.assertFalse(ctx._trainer_blocked(target))
                with patch('spirit.game.session.effects.trainer_effects_blocked', return_value=True) as shield:
                    self.assertTrue(ctx._trainer_blocked(target))
                    shield.assert_called_once_with(rig.board, P2, ctx.source, None)
                raise ValueError('selection failed')
        self.assertTrue(ctx._trainer_blocked(target))


if __name__ == '__main__':
    unittest.main()
