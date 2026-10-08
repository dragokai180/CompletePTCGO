"""A multi-card deck mill should not create two playback sequences per card."""
import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures
from spirit.game.attributes import GameSequence
from spirit.network.message_names import OutboundMsg
from spirit.tools.effect_smoke import P1, P2


class DeckMillAnimationTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx

    async def test_legacy_star_mills_seven_cards_in_two_sequences(self):
        rig, _, ctx = self.ctx('SWSH12.RegidragoVSTAR_136', 'Legacy Star')
        top = ctx.deck_top(7)
        self.assertEqual(len(top), 7)
        ctx.choose_cards = AsyncMock(return_value=[])

        await ctx.ability.effect(ctx)

        self.assertTrue(set(top).issubset(ctx.discard_pile()))
        for viewer in (P1, P2):
            runs = ctx.bracket_runs_for(viewer)
            self.assertEqual([name for name, _ in runs], [
                GameSequence.SERIAL_SEQUENCE.value,
                GameSequence.GROUPED_MOVE.value,
            ])
            intros = [msg for msg in runs[0][1]
                      if msg['name'] == OutboundMsg.ENTITY_INTRODUCED.value]
            moves = [msg for msg in runs[1][1]
                     if msg['name'] == OutboundMsg.ENTITY_MOVED.value]
            self.assertEqual([msg['value']['entityID'] for msg in intros],
                             [card.entity_id for card in top])
            self.assertEqual([msg['value']['entityID'] for msg in moves],
                             [card.entity_id for card in top])


if __name__ == '__main__':
    unittest.main()
