"""Devolution follows the cards actually in the stack, including Rare Candy."""

import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures
from spirit.game.card_effects.pokemon import devolvable, devolve_depth
from spirit.game.session.effects import EffectContext, devolution_chain
from spirit.game.session.passives import evolution_blocked
from spirit.tools.effect_smoke import P1, P2


class DevolutionRareCandyTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    async def candy_stack(self, rig):
        basic = self.add(rig, fixtures.definition('BW1.Snivy_1'), P1, 'bench')
        stage2 = self.add(rig, fixtures.definition('BW1.Serperior_5'), P1, 'hand')
        self.assertTrue(await rig.session.perform_evolution(P1, stage2, basic))
        self.assertEqual(devolution_chain(stage2), [stage2, basic])
        return basic, stage2

    async def test_devolution_spray_returns_rare_candy_stage_and_locks_basic(self):
        for path in ('BW6.DevolutionSpray_113',
                     'XY10.DevolutionSpray_95', 'XY12.DevolutionSpray_76'):
            with self.subTest(card=path):
                rig, entries = self.rig(path, 'trainer')
                basic, stage2 = await self.candy_stack(rig)
                ctx = EffectContext(rig.session, P1, entries['target'], None)
                rig.session.turn_state.turn_number = 4
                ctx.choose_pokemon = AsyncMock(return_value=stage2)
                await fixtures.definition(path).effect(ctx)

                self.assertIn(basic, ctx.my_bench())
                self.assertIn(stage2, ctx.hand())
                self.assertTrue(evolution_blocked(rig.board, P1, basic))
                for candy_path in ('CZ.RareCandy_141', 'SWSH1.RareCandy_180',
                                   'PGO.RareCandy_69'):
                    self.assertFalse(fixtures.definition(candy_path).condition(
                        rig.board, P1))
                stage1 = self.add(rig, fixtures.definition('BW1.Servine_3'), P1, 'hand')
                self.assertFalse(await rig.session.perform_evolution(P1, stage1, basic))
                self.assertIn(stage1, ctx.hand())
                rig.session.turn_state.begin_turn(P2, rig.board)
                self.assertFalse(evolution_blocked(rig.board, P1, basic))

    async def test_spray_z_and_direct_devolution_use_actual_stack_depth(self):
        rig, entries = self.rig('SM10.DevolutionSprayZ_166', 'trainer')
        basic, stage2 = await self.candy_stack(rig)
        self.assertTrue(devolvable(stage2))
        self.assertEqual(devolve_depth(stage2), 1)
        ctx = EffectContext(rig.session, P1, entries['target'], None)
        rig.session.turn_state.turn_number = 4
        ctx.choose_pokemon = AsyncMock(return_value=stage2)
        ctx.choose = AsyncMock()
        await fixtures.definition('SM10.DevolutionSprayZ_166').effect(ctx)
        ctx.choose.assert_not_awaited()
        self.assertIn(basic, ctx.my_bench())
        self.assertIn(stage2, ctx.deck())
        self.assertTrue(evolution_blocked(rig.board, P1, basic))

        other = self.add(rig, fixtures.definition('BW1.Snivy_1'), P2, 'bench')
        evolved = self.add(rig, fixtures.definition('BW1.Serperior_5'), P2, 'hand')
        self.assertTrue(await rig.session.perform_evolution(P2, evolved, other))
        self.assertEqual(devolve_depth(evolved), 1)
        opposing_ctx = EffectContext(rig.session, P1, entries['target'], None)
        removed = await opposing_ctx.devolve_pokemon(evolved)
        self.assertEqual(removed, [evolved])
        self.assertIn(other, opposing_ctx.opponent_bench())
        self.assertIn(evolved, opposing_ctx.hand(P2))

    async def test_attached_pokemon_tool_is_not_an_evolution_stage(self):
        rig, _ = self.rig('BW1.Snivy_1')
        basic = self.add(rig, fixtures.definition('BW1.Snivy_1'), P1, 'bench')
        shedinja = self.add(rig, fixtures.definition('SM8.Shedinja_95'), P1, 'hand')
        rig.attach(shedinja, basic)
        self.assertFalse(devolvable(basic))
        self.assertEqual(devolve_depth(basic), 0)
        self.assertIsNone(await rig.session.perform_devolution(basic))
        self.assertIs(shedinja.parent, basic)

    async def test_downgrading_beam_can_devolve_rare_candy_stage(self):
        rig, entries = self.rig('SWSH11.PorygonZ_142')
        basic = self.add(rig, fixtures.definition('BW1.Snivy_1'), P2, 'bench')
        stage2 = self.add(rig, fixtures.definition('BW1.Serperior_5'), P2, 'hand')
        self.assertTrue(await rig.session.perform_evolution(P2, stage2, basic))
        attack = next(a for a in fixtures.definition('SWSH11.PorygonZ_142').abilities
                      if a.title == 'Downgrading Beam')
        ctx = EffectContext(rig.session, P1, entries['target'], attack)
        ctx.choose_pokemon = AsyncMock(return_value=stage2)
        ctx.choose = AsyncMock()
        await attack.effect(ctx)
        ctx.choose.assert_not_awaited()
        self.assertIn(basic, ctx.opponent_bench())
        self.assertIn(stage2, ctx.deck(P2))

    async def test_strange_timepiece_requires_evolved_psychic_target(self):
        rig, _ = self.rig('ME1.StrangeTimepiece_128', 'trainer')
        trainer = fixtures.definition('ME1.StrangeTimepiece_128')
        basic = self.add(rig, fixtures.definition('BW1.Snivy_1'), P1, 'bench')
        evolved = self.add(rig, fixtures.definition('BW1.Servine_3'), P1, 'hand')
        self.assertTrue(await rig.session.perform_evolution(P1, evolved, basic))
        self.assertFalse(trainer.condition(rig.board, P1))
        psychic = self.add(rig, fixtures.definition('BW11.Ralts_59'), P1, 'bench')
        kirlia = self.add(rig, fixtures.definition('BW11.Kirlia_60'), P1, 'hand')
        self.assertTrue(await rig.session.perform_evolution(P1, kirlia, psychic))
        self.assertTrue(trainer.condition(rig.board, P1))


if __name__ == '__main__':
    unittest.main()
