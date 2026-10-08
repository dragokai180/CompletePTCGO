"""Effects naming face-down Prizes cannot target cards already turned up."""
import unittest
from unittest.mock import AsyncMock, patch

from tests import test_hgss_rules as fixtures
from spirit.game.attributes import GameSequence, PokemonTypes
from spirit.game.data_utils import def_for
from spirit.game.session.effects import EffectContext
from spirit.game.prizes import shuffle_face_down_prizes
from spirit.network.message_names import OutboundMsg
from spirit.tools.effect_smoke import P1, P2


class FaceDownPrizeTargetTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx
    add = fixtures.HgssRulesTests.add

    async def test_shuffle_dance_offers_only_face_down_opposing_prizes(self):
        rig, entities, ctx = self.ctx('SWSH3.GalarianMrRime_36', 'Shuffle Dance')
        prizes = rig.board.find_player_area(P2, 'prizePile').children
        prizes[0].publicly_revealed = True
        self.assertTrue(ctx.ability.condition(rig.board, P1, entities['target']))
        rig.session._prompt_prize_pick = AsyncMock(return_value=[])
        await ctx.ability.effect(ctx)
        offered = rig.session._prompt_prize_pick.await_args.args[1]
        self.assertNotIn(prizes[0].entity_id, offered)
        self.assertEqual(len(offered), len(prizes) - 1)

        for prize in prizes:
            prize.publicly_revealed = True
        self.assertFalse(ctx.ability.condition(rig.board, P1, entities['target']))

    async def test_hisuian_heavy_ball_inspects_only_face_down_prizes(self):
        rig, entities = self.rig('SWSH10.HisuianHeavyBall_146', 'trainer')
        prizes = rig.board.find_player_area(P1, 'prizePile').children
        prizes[0].publicly_revealed = True
        face_up_id = prizes[0].entity_id
        ctx = EffectContext(rig.session, P1, entities['target'], None)
        rig.session.prompt_prize_reveal_pick = AsyncMock(return_value=None)
        rig.session.send_game_sequence = AsyncMock()

        await fixtures.definition('SWSH10.HisuianHeavyBall_146').effect(ctx)

        offered = rig.session.prompt_prize_reveal_pick.await_args.args[2]
        self.assertNotIn(face_up_id, offered)
        self.assertEqual(len(offered), len(prizes) - 1)

    async def test_bother_bot_turns_up_only_a_face_down_prize(self):
        rig, entities = self.rig('SV10.TeamRocketsBotherBot_172', 'trainer')
        prizes = rig.board.find_player_area(P2, 'prizePile').children
        prizes[0].publicly_revealed = True
        ctx = EffectContext(rig.session, P1, entities['target'], None)
        rig.session._prompt_prize_pick = AsyncMock(
            return_value=[prizes[1].entity_id])
        rig.session.send_game_sequence = AsyncMock()

        async def decline_after_reveal(_prompt):
            hand_ids = {card.entity_id for card in ctx.hand(P2)}
            revealed = {
                message['value']['entityID']
                for call in rig.session.send_game_sequence.await_args_list
                for message in call.args[2]
                if message['name'] == OutboundMsg.ENTITY_INTRODUCED.value
            }
            self.assertTrue(revealed & hand_ids)
            return False

        ctx.ask_yes_no = AsyncMock(side_effect=decline_after_reveal)

        await fixtures.definition('SV10.TeamRocketsBotherBot_172').effect(ctx)

        offered = rig.session._prompt_prize_pick.await_args.args[1]
        self.assertNotIn(prizes[0].entity_id, offered)
        self.assertEqual(len(offered), len(prizes) - 1)
        self.assertTrue(prizes[1].publicly_revealed)
        self.assertTrue(any(
            call.args[1] == GameSequence.WITH_OPEN_PRIZE_CARDS
            for call in rig.session.send_game_sequence.await_args_list
        ))

    async def test_code_check_inspects_only_face_down_opposing_prizes(self):
        rig, entities, ctx = self.ctx('SM3.Porygon_103', 'Code Check')
        prizes = rig.board.find_player_area(P2, 'prizePile').children
        prizes[0].publicly_revealed = True
        rig.session._prompt_prize_pick = AsyncMock(return_value=[])
        rig.session.send_game_sequence = AsyncMock()

        await ctx.ability.effect(ctx)

        offered = rig.session._prompt_prize_pick.await_args.args[1]
        self.assertNotIn(prizes[0].entity_id, offered)
        self.assertEqual(len(offered), len(prizes) - 1)

    async def test_face_up_prize_does_not_fire_face_down_take_trigger(self):
        rig, _ = self.rig('SWSH7.DreamBall_146', 'trainer')
        prize = rig.board.find_player_area(P1, 'prizePile').children[0]
        prize.publicly_revealed = True
        rig.session.send_game_sequence = AsyncMock()
        rig.session._fire_triggered_abilities = AsyncMock()

        await rig.session._take_prizes(P1, 1)

        rig.session._fire_triggered_abilities.assert_not_awaited()

    async def test_shuffle_preserves_revealed_prize_and_randomizes_hidden_slots(self):
        rig, entities = self.rig('SM7.BeastBall_125', 'trainer')
        prizes = rig.board.find_player_area(P1, 'prizePile').children
        revealed = prizes[1]
        revealed.publicly_revealed = True
        hidden_before = [card.entity_id for card in prizes if card is not revealed]

        with patch('spirit.game.prizes.random.shuffle', side_effect=lambda cards: cards.reverse()):
            shuffled = shuffle_face_down_prizes(rig.board, P1)

        self.assertIs(prizes[1], revealed)
        self.assertTrue(revealed.publicly_revealed)
        self.assertEqual([card.entity_id for card in shuffled], hidden_before[::-1])
        self.assertEqual([card.entity_id for card in prizes if card is not revealed],
                         hidden_before[::-1])
        for index, card in enumerate(prizes):
            if card is not revealed:
                self.assertEqual(card.board_slot, index)

        ctx = EffectContext(rig.session, P1, entities['target'], None)
        with patch('spirit.game.prizes.random.shuffle', side_effect=lambda cards: cards.reverse()):
            await ctx.shuffle_prizes()
        self.assertIs(prizes[1], revealed)
        self.assertTrue(revealed.publicly_revealed)

    async def test_attacks_turn_only_hidden_prizes_up_before_damage(self):
        cases = (
            ('SV065.Cresselia_21', 'Crescent Purge', None, 80),
            ('SM10.Blacephalon_32', 'Blazer', 'fire', 50),
            ('Promo_XY.Umbreon_96', 'Lunatic Sense', 'pokemon', 60),
        )
        for path, title, prize_kind, bonus in cases:
            with self.subTest(attack=path):
                rig, _, ctx = self.ctx(path, title)
                prizes = rig.board.find_player_area(P1, 'prizePile').children
                revealed = prizes[0]
                revealed.publicly_revealed = True
                if prize_kind == 'fire':
                    chosen = self.add(
                        rig, def_for(self.energies[PokemonTypes.FIRE.value]),
                        P1, 'prizePile')
                elif prize_kind == 'pokemon':
                    chosen = self.add(
                        rig, fixtures.definition('BW1.Snivy_1'),
                        P1, 'prizePile')
                else:
                    chosen = prizes[1]
                ctx.ask_yes_no = AsyncMock(return_value=True)
                rig.session._prompt_prize_pick = AsyncMock(
                    return_value=[chosen.entity_id])
                rig.session.send_game_sequence = AsyncMock()
                ctx.reveal_cards = AsyncMock()
                ctx.deal_damage = AsyncMock(return_value=0)

                await ctx.ability.effect(ctx)

                offered = rig.session._prompt_prize_pick.await_args.args[1]
                self.assertNotIn(revealed.entity_id, offered)
                self.assertTrue(chosen.publicly_revealed)
                ctx.reveal_cards.assert_awaited_once_with([chosen])
                self.assertTrue(any(
                    call.args[1] == GameSequence.WITH_OPEN_PRIZE_CARDS
                    for call in rig.session.send_game_sequence.await_args_list
                ))
                self.assertEqual(ctx.deal_damage.await_args.args[0],
                                 ctx.ability.damage + bonus)

    async def test_optional_prize_turn_can_be_declined_without_damage_bonus(self):
        rig, _, ctx = self.ctx('SV065.Cresselia_21', 'Crescent Purge')
        prizes = rig.board.find_player_area(P1, 'prizePile').children
        ctx.ask_yes_no = AsyncMock(return_value=False)
        rig.session._prompt_prize_pick = AsyncMock()
        ctx.deal_damage = AsyncMock(return_value=0)

        await ctx.ability.effect(ctx)

        rig.session._prompt_prize_pick.assert_not_awaited()
        self.assertFalse(any(prize.publicly_revealed for prize in prizes))
        self.assertEqual(ctx.deal_damage.await_args.args[0], ctx.ability.damage)

    async def test_wrong_prize_type_gives_no_damage_bonus(self):
        rig, _, ctx = self.ctx('SM10.Blacephalon_32', 'Blazer')
        prize = rig.board.find_player_area(P1, 'prizePile').children[0]
        rig.session._prompt_prize_pick = AsyncMock(
            return_value=[prize.entity_id])
        rig.session.send_game_sequence = AsyncMock()
        ctx.reveal_cards = AsyncMock()
        ctx.deal_damage = AsyncMock(return_value=0)

        await ctx.ability.effect(ctx)

        self.assertTrue(prize.publicly_revealed)
        self.assertEqual(ctx.deal_damage.await_args.args[0], ctx.ability.damage)


if __name__ == '__main__':
    unittest.main()
