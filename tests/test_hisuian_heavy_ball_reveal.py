"""Hisuian Heavy Ball reveals only the chosen Prize to the opponent."""
import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures
from spirit.game.attributes import GameSequence
from spirit.game.card_effects.trainers import hisuian_heavy_ball
from spirit.game.session.effects import EffectContext
from spirit.network.message_names import OutboundMsg
from spirit.tools.effect_smoke import P1, P2


class HisuianHeavyBallRevealTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    async def test_selected_basic_is_publicly_revealed_before_the_prize_swap(self):
        rig, entities = self.rig('SWSH10.HisuianHeavyBall_146', 'trainer')
        source = entities['target']
        chosen = self.add(rig, self.filler, P1, 'prizePile')
        prize_area = rig.board.find_player_area(P1, 'prizePile')
        other_prizes = {card.entity_id for card in prize_area.children if card is not chosen}
        ctx = EffectContext(rig.session, P1, source, None)
        rig.session.prompt_prize_reveal_pick = AsyncMock(return_value=chosen.entity_id)
        rig.session.send_game_sequence = AsyncMock()

        await hisuian_heavy_ball(ctx)

        calls = rig.session.send_game_sequence.call_args_list
        reveal_at = next(i for i, call in enumerate(calls)
                         if any(message['name'] == OutboundMsg.REVEAL_CARD_TO_ALL_EFFECT.value
                                for message in call.args[2]))
        reveal_call = calls[reveal_at]
        self.assertEqual(reveal_call.args[0], [rig.session.players[P2]])
        self.assertEqual(reveal_call.args[1], GameSequence.GROUPED_MOVE)
        self.assertEqual(reveal_call.args[2][0]['value']['entityID'], chosen.entity_id)
        self.assertEqual(calls[reveal_at - 1].args[0], [rig.session.players[P2]])
        self.assertEqual(calls[reveal_at - 1].args[2][0]['name'],
                         OutboundMsg.ENTITY_INTRODUCED.value)
        self.assertTrue(any(call.args[1] == GameSequence.WITH_OPEN_PRIZE_CARDS
                            for call in calls[reveal_at + 1:]))
        opponent_reveals = [message['value']['entityID']
                            for call in calls if call.args[0] == [rig.session.players[P2]]
                            for message in call.args[2]
                            if message['name'] == OutboundMsg.REVEAL_CARD_TO_ALL_EFFECT.value]
        self.assertEqual(opponent_reveals, [chosen.entity_id])
        self.assertFalse(other_prizes.intersection(opponent_reveals))
        self.assertIn(chosen, rig.board.find_player_area(P1, 'hand').children)
        self.assertIn(source, prize_area.children)

    async def test_declining_does_not_reveal_a_prize(self):
        rig, entities = self.rig('SWSH10.HisuianHeavyBall_146', 'trainer')
        ctx = EffectContext(rig.session, P1, entities['target'], None)
        rig.session.prompt_prize_reveal_pick = AsyncMock(return_value=None)
        rig.session.send_game_sequence = AsyncMock()

        await hisuian_heavy_ball(ctx)

        self.assertFalse(any(
            message['name'] == OutboundMsg.REVEAL_CARD_TO_ALL_EFFECT.value
            for call in rig.session.send_game_sequence.call_args_list
            for message in call.args[2]
        ))
