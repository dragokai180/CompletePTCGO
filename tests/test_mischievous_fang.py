"""Rattata's optional on-play Tool removal resolves through the play action."""

import unittest
from unittest.mock import AsyncMock, patch

from spirit.game.session.effects import EffectContext
from spirit.tools.effect_smoke import P1, P2
from tests import test_hgss_rules as fixtures


class MischievousFangTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    async def test_play_from_hand_discards_only_opposing_active_tools_when_accepted(self):
        rig, entities = self.rig('XY12.Rattata_66')
        rattata = self.add(rig, fixtures.definition('XY12.Rattata_66'), P1, 'hand')
        active = entities['p2_active']
        benched = rig.board.find_player_area(P2, 'bench').children[0]
        active_tools = [
            self.add(rig, fixtures.definition(path), P2, 'hand')
            for path in ('XY9.FightingFuryBelt_99', 'BW9.FloatStone_99')
        ]
        bench_tool = self.add(rig, fixtures.definition('XY1.MuscleBand_121'), P2, 'hand')
        own_tool = self.add(rig, fixtures.definition('XY1.MuscleBand_121'), P1, 'hand')
        for tool in active_tools:
            rig.attach(tool, active)
        rig.attach(bench_tool, benched)
        rig.attach(own_tool, entities['p1_active'])

        with patch.object(EffectContext, 'ask_yes_no', AsyncMock(return_value=True)) as ask:
            await rig.session._execute_play_basic(P1, rattata)

        ask.assert_awaited_once_with('Use Mischievous Fang?')
        self.assertIn(rattata, rig.board.find_player_area(P1, 'bench').children)
        discard = rig.board.find_player_area(P2, 'discard').children
        for tool in active_tools:
            self.assertIn(tool, discard)
        self.assertIn(bench_tool, benched.children)
        self.assertIn(own_tool, entities['p1_active'].children)

    async def test_declining_keeps_opposing_active_tool(self):
        rig, entities = self.rig('XY12.Rattata_66')
        rattata = self.add(rig, fixtures.definition('XY12.Rattata_66'), P1, 'hand')
        tool = self.add(rig, fixtures.definition('XY9.FightingFuryBelt_99'), P2, 'hand')
        rig.attach(tool, entities['p2_active'])

        with patch.object(EffectContext, 'ask_yes_no', AsyncMock(return_value=False)) as ask:
            await rig.session._execute_play_basic(P1, rattata)

        ask.assert_awaited_once_with('Use Mischievous Fang?')
        self.assertIn(rattata, rig.board.find_player_area(P1, 'bench').children)
        self.assertIn(tool, entities['p2_active'].children)

    async def test_putting_rattata_from_deck_on_bench_does_not_trigger(self):
        rig, entities = self.rig('XY12.Rattata_66')
        rattata = self.add(rig, fixtures.definition('XY12.Rattata_66'), P1, 'deck')
        tool = self.add(rig, fixtures.definition('XY9.FightingFuryBelt_99'), P2, 'hand')
        rig.attach(tool, entities['p2_active'])
        ctx = EffectContext(rig.session, P1, entities['p1_active'], None)

        with patch.object(EffectContext, 'ask_yes_no', AsyncMock()) as ask:
            self.assertTrue(await ctx.bench_pokemon(rattata))

        ask.assert_not_awaited()
        self.assertIn(tool, entities['p2_active'].children)


if __name__ == '__main__':
    unittest.main()
