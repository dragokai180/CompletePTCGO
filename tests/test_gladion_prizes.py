"""Gladion uses the Prize fan and keeps the chosen card private."""
import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures

from spirit.game.attributes import GameSequence
from spirit.game.prizes import face_down_prizes
from spirit.game.session.effects import EffectContext
from spirit.network.message_names import OutboundMsg
from spirit.tools.effect_smoke import P1, P2


class GladionPrizeTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig

    async def test_played_gladion_swaps_prize_and_closes_private_fan(self):
        rig, entities = self.rig('SM4.Gladion_95', 'trainer')
        source = entities['target']
        prize_area = rig.board.find_player_area(P1, 'prizePile')
        chosen = prize_area.children[1]
        original_count = len(prize_area.children)
        active_trainer = rig.board.find_global_area('activeTrainer')
        self.assertTrue(rig.board.move_card(source.entity_id,
                                            active_trainer.entity_id))
        ctx = EffectContext(rig.session, P1, source, None)
        rig.session.prompt_prize_reveal_pick = AsyncMock(
            return_value=chosen.entity_id)
        rig.session.send_game_sequence = AsyncMock()

        await fixtures.definition('SM4.Gladion_95').effect(ctx)

        self.assertIn(chosen, ctx.hand())
        self.assertIn(source, prize_area.children)
        self.assertEqual(len(prize_area.children), original_count)
        self.assertEqual(len(face_down_prizes(rig.board, P1)), original_count)
        self.assertEqual(rig.session.turn_state.prizes_taken.get(P1, 0), 0)
        offer = rig.session.prompt_prize_reveal_pick.await_args
        self.assertEqual(offer.kwargs['minimum'], 1)
        self.assertEqual(set(offer.args[2]), set(offer.args[3]))
        calls = rig.session.send_game_sequence.await_args_list
        self.assertTrue(any(call.args[1] == GameSequence.WITH_OPEN_PRIZE_CARDS
                            and call.args[0] == [rig.session.players[P1]]
                            for call in calls))
        self.assertTrue(any(call.args[1] == GameSequence.WITH_OPEN_PRIZE_CARDS
                            and call.args[0] == [rig.session.players[P2]]
                            for call in calls))
        self.assertFalse(any(
            call.args[0] == [rig.session.players[P2]]
            and message['name'] == OutboundMsg.ENTITY_INTRODUCED.value
            and message['value']['entityID'] == chosen.entity_id
            for call in calls for message in call.args[2]
        ))

    async def test_unplayed_gladion_has_no_effect(self):
        rig, entities = self.rig('SM4.Gladion_95', 'trainer')
        ctx = EffectContext(rig.session, P1, entities['target'], None)
        rig.session.prompt_prize_reveal_pick = AsyncMock()
        await fixtures.definition('SM4.Gladion_95').effect(ctx)
        rig.session.prompt_prize_reveal_pick.assert_not_awaited()

    async def test_prize_fan_requires_gladions_pick(self):
        rig, _ = self.rig('SM4.Gladion_95', 'trainer')
        prize = rig.board.find_player_area(P1, 'prizePile').children[0]
        player = object()
        rig.session.players[P1] = player
        rig.session.send_game_sequence = AsyncMock()
        rig.session.prompt_selection_message = AsyncMock(return_value={
            'selection': {'targetResponses': [
                {'entityList': [prize.entity_id]},
            ]},
        })

        picked = await rig.session.prompt_prize_reveal_pick(
            P1, 'gladion-source', [prize.entity_id], [prize.entity_id],
            minimum=1, prompt='Choose a Prize card',
        )

        self.assertEqual(picked, prize.entity_id)
        offer = rig.session.prompt_selection_message.await_args.args[2]
        info = next(iter(offer['targetMap'].values()))[0]
        self.assertTrue(offer['forced'])
        self.assertTrue(info['forced'])
        self.assertEqual(info['minimumToSelect'], 1)
        self.assertEqual(info['validTargets'], [prize.entity_id])

    async def test_normal_supporter_play_keeps_gladion_in_prizes(self):
        rig, entities = self.rig('SM4.Gladion_95', 'trainer')
        source = entities['target']
        chosen = rig.board.find_player_area(P1, 'prizePile').children[0]
        rig.session.prompt_prize_reveal_pick = AsyncMock(
            return_value=chosen.entity_id)
        rig.session.send_game_sequence = AsyncMock()

        await rig.session._execute_play_trainer(P1, source)

        self.assertIn(chosen, rig.board.find_player_area(P1, 'hand').children)
        self.assertIn(source, rig.board.find_player_area(P1, 'prizePile').children)
        self.assertNotIn(source, rig.board.find_player_area(P1, 'discard').children)


if __name__ == '__main__':
    unittest.main()
