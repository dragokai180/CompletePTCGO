"""Recon Directive's card movement and hidden reorder use short catch-up estimates."""
import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures
from spirit.game.attributes import GameSequence
from spirit.game.session.constants import SEQUENCE_DURATION_SECONDS
from spirit.network.message_names import OutboundMsg
from spirit.tools.effect_smoke import P1


class ReconDirectivePacingTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx

    async def test_recon_directive_moves_one_card_and_reorders_without_extra_animation(self):
        rig, _, ctx = self.ctx('SV06.Drakloak_129', 'Recon Directive')
        chosen, other = ctx.deck_top(2)
        ctx.choose_cards = AsyncMock(return_value=[chosen])

        await ctx.ability.effect(ctx)

        self.assertIn(chosen, ctx.hand())
        self.assertIs(ctx.deck()[0], other)
        runs = ctx.bracket_runs_for(P1, GameSequence.POKE_ABILITY.value)
        self.assertEqual([name for name, _ in runs], [
            GameSequence.POKE_ABILITY.value,
            GameSequence.GROUPED_MOVE.value,
        ])
        self.assertEqual(
            [msg['value']['entityID'] for msg in runs[0][1]
             if msg['name'] == OutboundMsg.ENTITY_MOVED.value],
            [chosen.entity_id],
        )
        self.assertEqual(
            [msg['name'] for msg in runs[1][1]],
            [OutboundMsg.PILE_REORDERED.value],
        )

        rig.session.choreography_pauses = True
        rig.session._client_caught_up_at.clear()
        rig.session._note_client_animation(GameSequence.ATTACK, [P1])
        for name, messages in runs:
            rig.session._note_client_animation(name, [P1], messages)
        self.assertLess(
            rig.session._client_catchup_remaining(P1),
            SEQUENCE_DURATION_SECONDS['Attack'] + 1.0,
        )


if __name__ == '__main__':
    unittest.main()
