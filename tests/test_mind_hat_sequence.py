"""Mind Hat shows the opponent's discard before the player's choice."""

import unittest

from tests import test_hgss_rules as fixtures
from spirit.tools.effect_smoke import P1, P2


class MindHatSequenceTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    ctx = fixtures.HgssRulesTests.ctx
    rig = fixtures.HgssRulesTests.rig

    async def test_opponents_card_is_revealed_and_flushed_before_own_prompt(self):
        _, _, ctx = self.ctx('SWSH2.Hatterene_85', 'Mind Hat')
        events = []
        discarded = []
        original_flush = ctx.flush_choreography
        original_wait = ctx.session._wait_for_client_catchup

        async def flush():
            events.append('flush')
            self.assertTrue(any(
                viewer == P1 and message['name'] == 'RevealCardToAllEffect'
                for viewer, message, _ in ctx._messages
            ))
            await original_flush()

        async def wait(player_id):
            events.append('wait')
            self.assertEqual(player_id, P1)
            await original_wait(player_id)

        async def choose(cards, count, *, minimum, prompt, player_id):
            events.append(player_id)
            self.assertEqual(count, 1)
            self.assertIsNone(minimum)
            if player_id == P1:
                self.assertEqual(events, [P2, 'flush', 'wait', P1])
                self.assertIn(discarded[0], ctx.discard_pile(P2))
                self.assertFalse(ctx._messages)
            else:
                discarded.append(cards[0])
            return cards[:1]

        ctx.flush_choreography = flush
        ctx.session._wait_for_client_catchup = wait
        ctx.choose_cards = choose
        await ctx.ability.effect(ctx)

        self.assertEqual(events, [P2, 'flush', 'wait', P1])
        self.assertIn(discarded[0], ctx.discard_pile(P2))


if __name__ == '__main__':
    unittest.main()
