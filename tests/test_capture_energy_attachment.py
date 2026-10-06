"""Capture Energy searches only when it is attached from the hand."""

import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures
from spirit.game.session.effects import (
    EffectContext, resolve_activated_ability, resolve_energy_on_attach,
)
from spirit.tools.effect_smoke import P1


class CaptureEnergyAttachmentTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    async def test_manual_attachment_benches_searched_basic(self):
        for path in ('SWSH2.CaptureEnergy_171', 'SWSH3.CaptureEnergy_201'):
            with self.subTest(path=path):
                rig, entities = self.rig(path, 'energy')
                energy = entities['target']
                target = entities['p1_active']
                # The smoke deck contains many Basic Pokemon of its filler type.
                basic = next(c for c in rig.board.find_player_area(P1, 'deck').children
                             if c.archetype_id.lower() == self.filler.guid.lower())
                bench = rig.board.find_player_area(P1, 'bench')
                before = len(bench.children)
                rig.session.prompt_card_chooser = AsyncMock(
                    return_value=[basic.entity_id])

                rig.attach(energy, target)
                ctx = await resolve_energy_on_attach(
                    rig.session, P1, energy, target)

                self.assertIsNotNone(ctx)
                self.assertIn(basic, bench.children)
                self.assertEqual(len(bench.children), before + 1)
                rig.session.prompt_card_chooser.assert_awaited_once()

    async def test_crazy_code_attachment_triggers_capture_search(self):
        rig, entities = self.rig('SM10.PorygonZ_157')
        source = entities['target']
        ability = next(a for a in fixtures.definition('SM10.PorygonZ_157').abilities
                       if a.title == 'Crazy Code')
        energy = self.add(rig, fixtures.definition('SWSH2.CaptureEnergy_171'),
                          P1, 'hand')
        basic = next(c for c in rig.board.find_player_area(P1, 'deck').children
                     if c.archetype_id.lower() == self.filler.guid.lower())
        bench = rig.board.find_player_area(P1, 'bench')
        before = len(bench.children)
        rig.session.prompt_entity_picker = AsyncMock(
            side_effect=lambda pid, sid, cards, *args, **kwargs:
                [cards[0].entity_id])
        rig.session.prompt_card_chooser = AsyncMock(
            return_value=[basic.entity_id])

        await resolve_activated_ability(rig.session, P1, source, ability)

        self.assertNotIn(energy, rig.board.find_player_area(P1, 'hand').children)
        self.assertIn(basic, bench.children)
        self.assertEqual(len(bench.children), before + 1)
        rig.session.prompt_card_chooser.assert_awaited_once()

    async def test_attaching_capture_from_discard_does_not_search(self):
        rig, entities = self.rig('SM10.PorygonZ_157')
        source = entities['target']
        energy = self.add(rig, fixtures.definition('SWSH2.CaptureEnergy_171'),
                          P1, 'discard')
        bench = rig.board.find_player_area(P1, 'bench')
        before = len(bench.children)
        rig.session.prompt_card_chooser = AsyncMock()
        ctx = EffectContext(rig.session, P1, source, None)

        self.assertTrue(await ctx.attach_energy(energy, source))

        self.assertEqual(len(bench.children), before)
        rig.session.prompt_card_chooser.assert_not_awaited()

    async def test_capture_can_fill_an_expanded_bench(self):
        rig, entities = self.rig('SWSH2.CaptureEnergy_171', 'energy')
        energy = entities['target']
        bench = rig.board.find_player_area(P1, 'bench')
        for _ in range(3):
            self.add(rig, self.filler, P1, 'bench')
        self.assertEqual(len(bench.children), 5)
        stadium = self.add(rig, fixtures.definition('XY6.SkyField_89'),
                           P1, 'hand')
        rig.board.move_card(
            stadium.entity_id,
            rig.board.find_global_area('activeStadium').entity_id)
        basic = next(c for c in rig.board.find_player_area(P1, 'deck').children
                     if c.archetype_id.lower() == self.filler.guid.lower())
        rig.session.prompt_card_chooser = AsyncMock(
            return_value=[basic.entity_id])

        rig.attach(energy, entities['p1_active'])
        await resolve_energy_on_attach(
            rig.session, P1, energy, entities['p1_active'])

        self.assertIn(basic, bench.children)
        self.assertEqual(len(bench.children), 6)


if __name__ == '__main__':
    unittest.main()
