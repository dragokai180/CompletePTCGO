"""Prize-only effects run on an actual face-down Prize take, not a swap."""
import unittest
from unittest.mock import AsyncMock, patch

from tests import test_hgss_rules as fixtures
from spirit.game.session.effects import EffectContext
from spirit.game.session.legal_actions import trainer_condition_met
from spirit.tools.effect_smoke import P1


class PrizeTakeTriggerTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    def prize_first(self, rig, card):
        board = rig.board
        hand = board.find_player_area(P1, 'hand')
        prizes = board.find_player_area(P1, 'prizePile')
        if card.parent is prizes:
            board.move_card(card.entity_id, hand.entity_id)
        self.assertTrue(board.move_card(card.entity_id, prizes.entity_id, 0))
        return prizes

    async def test_dream_ball_taken_as_prize_plays_and_benches_from_deck(self):
        rig, entities = self.rig('SWSH7.DreamBall_146', 'trainer')
        card = entities['target']
        definition = fixtures.definition('SWSH7.DreamBall_146')
        self.assertFalse(trainer_condition_met(definition.condition, rig.board, P1, card))
        self.prize_first(rig, card)
        target = self.add(rig, fixtures.definition('BW1.Snivy_1'), P1, 'deck')
        rig.session.send_game_sequence = AsyncMock()
        with patch.object(EffectContext, 'ask_yes_no', new_callable=AsyncMock,
                          return_value=True), \
             patch.object(EffectContext, 'search_deck', new_callable=AsyncMock,
                          return_value=[target]) as search:
            await rig.session._take_prizes(P1, 1)
        self.assertEqual(card._containing_area_name(), 'discard')
        self.assertEqual(target._containing_area_name(), 'bench')
        self.assertEqual(rig.session.turn_state.prizes_taken[P1], 1)
        self.assertTrue(search.await_args.args[0](target))

    async def test_greedy_dice_only_plays_on_prize_take_and_heads_takes_another(self):
        rig, entities = self.rig('XY11.GreedyDice_102', 'trainer')
        card = entities['target']
        definition = fixtures.definition('XY11.GreedyDice_102')
        self.assertFalse(trainer_condition_met(definition.condition, rig.board, P1, card))
        self.prize_first(rig, card)
        rig.session.send_game_sequence = AsyncMock()
        with patch.object(EffectContext, 'ask_yes_no', new_callable=AsyncMock,
                          return_value=True), \
             patch.object(EffectContext, 'flip_coins', new_callable=AsyncMock,
                          return_value=[True]) as coin:
            await rig.session._take_prizes(P1, 1)
        coin.assert_awaited_once()
        self.assertEqual(card._containing_area_name(), 'discard')
        self.assertEqual(rig.session.turn_state.prizes_taken[P1], 2)

    async def test_prize_pokemon_enter_bench_and_get_correct_bonus(self):
        for path, title, heads in (
                ('SM7.Jirachi_97', 'Wish Upon a Star', None),
                ('SV035.Chansey_113', 'Lucky Bonus', True),
                ('SV035.Chansey_113', 'Lucky Bonus', False)):
            with self.subTest(card=path, heads=heads):
                rig, _ = self.rig(path)
                card = self.add(rig, fixtures.definition(path), P1, 'prizePile')
                self.prize_first(rig, card)
                rig.session.send_game_sequence = AsyncMock()
                with patch.object(EffectContext, 'ask_yes_no', new_callable=AsyncMock,
                                  return_value=True), \
                     patch.object(EffectContext, 'flip_coins', new_callable=AsyncMock,
                                  return_value=[heads]) as coin:
                    await rig.session._take_prizes(P1, 1)
                self.assertEqual(card._containing_area_name(), 'bench')
                self.assertEqual(rig.session.turn_state.prizes_taken[P1],
                                 1 if heads is False else 2)
                if heads is None:
                    coin.assert_not_awaited()
                else:
                    coin.assert_awaited_once()

    async def test_treasure_energy_attaches_only_when_taken_face_down_on_owners_turn(self):
        rig, entities = self.rig('SWSH7.TreasureEnergy_165', 'energy')
        card = entities['target']
        self.prize_first(rig, card)
        pokemon = rig.board.active_pokemon(P1)
        rig.session.send_game_sequence = AsyncMock()
        with patch.object(EffectContext, 'ask_yes_no', new_callable=AsyncMock,
                          return_value=True):
            await rig.session._take_prizes(P1, 1)
        self.assertIn(card, rig.board.attached_energies(pokemon))
        self.assertEqual(rig.session.turn_state.prizes_taken[P1], 1)

    async def test_face_up_prize_does_not_play_greedy_dice(self):
        rig, entities = self.rig('XY11.GreedyDice_102', 'trainer')
        card = entities['target']
        self.prize_first(rig, card)
        card.publicly_revealed = True
        rig.session.send_game_sequence = AsyncMock()
        with patch.object(EffectContext, 'ask_yes_no', new_callable=AsyncMock) as ask:
            await rig.session._take_prizes(P1, 1)
        ask.assert_not_awaited()
        self.assertEqual(card._containing_area_name(), 'hand')

    async def test_daisys_help_draws_then_shows_own_hidden_prizes(self):
        rig, entities = self.rig('SV035.DaisysHelp_158', 'trainer')
        ctx = EffectContext(rig.session, P1, entities['target'], None)
        before = len(ctx.hand())
        hidden = list(rig.board.find_player_area(P1, 'prizePile').children)
        ctx.reveal_cards = AsyncMock()

        await fixtures.definition('SV035.DaisysHelp_158').effect(ctx)

        self.assertEqual(len(ctx.hand()), before + 2)
        ctx.reveal_cards.assert_awaited_once_with(hidden, to_player=P1)

    async def test_lt_surges_bargain_lets_opponent_decide(self):
        for agrees in (True, False):
            with self.subTest(agrees=agrees):
                rig, entities = self.rig('ME1.LtSurgesBargain_120', 'trainer')
                ctx = EffectContext(rig.session, P1, entities['target'], None)
                rig.session.send_game_sequence = AsyncMock()
                ctx.ask_yes_no = AsyncMock(return_value=agrees)
                before_hand = len(ctx.hand())

                await fixtures.definition('ME1.LtSurgesBargain_120').effect(ctx)

                ctx.ask_yes_no.assert_awaited_once_with(
                    'May each player take a Prize card?', player_id=ctx.opponent_id)
                self.assertEqual(rig.session.turn_state.prizes_taken.get(P1, 0),
                                 int(agrees))
                self.assertEqual(rig.session.turn_state.prizes_taken.get(ctx.opponent_id, 0),
                                 int(agrees))
                if agrees:
                    self.assertEqual(len(ctx.hand()), before_hand + 1)
                else:
                    self.assertEqual(len(ctx.hand()), before_hand + 4)

    async def test_gladion_swap_does_not_trigger_dream_ball(self):
        rig, entities = self.rig('SM4.Gladion_95', 'trainer')
        dream = self.add(rig, fixtures.definition('SWSH7.DreamBall_146'),
                         P1, 'prizePile')
        source = entities['target']
        active_trainer = rig.board.find_global_area('activeTrainer')
        self.assertTrue(rig.board.move_card(source.entity_id,
                                            active_trainer.entity_id))
        rig.session.prompt_prize_reveal_pick = AsyncMock(return_value=dream.entity_id)
        rig.session.send_game_sequence = AsyncMock()
        rig.session._execute_play_trainer = AsyncMock()
        ctx = EffectContext(rig.session, P1, source, None)
        await fixtures.definition('SM4.Gladion_95').effect(ctx)
        self.assertEqual(dream._containing_area_name(), 'hand')
        rig.session._execute_play_trainer.assert_not_awaited()
        self.assertEqual(rig.session.turn_state.prizes_taken.get(P1, 0), 0)


if __name__ == '__main__':
    unittest.main()
