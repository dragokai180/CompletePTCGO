"""Contrary follows the owner of each flip and the opponent's turn."""
import unittest
from types import SimpleNamespace
from unittest.mock import AsyncMock, patch

from tests import test_hgss_rules as fixtures
from spirit.game.data_utils import Attack
from spirit.game.session.effects import EffectContext
from spirit.game.session.passives import forced_coin_result
from spirit.tools.effect_smoke import P1, P2


class ContraryCoinOverrideTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig

    def context(self, rig, player_id):
        attacker = rig.board.active_pokemon(player_id)
        return EffectContext(rig.session, player_id, attacker,
                             Attack(title='Coin attack', damage=20))

    async def test_opponents_attack_coins_are_tails_even_if_random_is_heads(self):
        rig, _ = self.rig('Promo_XY.Malamar_58')
        rig.session.turn_state.begin_turn(P2, rig.board)
        self.assertIs(forced_coin_result(rig.board, P2), False)

        ctx = self.context(rig, P2)
        with patch('spirit.game.session.effects.random.choice', return_value=0):
            results = await ctx.flip_coins(2, 'Coin attack')

        self.assertEqual(results, [False, False])
        self.assertEqual(ctx.coin_results, [1, 1])

    async def test_defenders_coin_and_owners_coin_are_not_overridden(self):
        rig, entities = self.rig('Promo_XY.Malamar_58')
        rig.session.turn_state.begin_turn(P2, rig.board)
        self.assertIsNone(forced_coin_result(rig.board, P1))
        ctx = self.context(rig, P2)

        with patch('spirit.game.session.effects.random.choice', return_value=0):
            result = await ctx.flip_coins(
                1, 'Defense', source=entities['target'], player_id=P1)
        self.assertEqual(result, [True])

        rig.session.turn_state.begin_turn(P1, rig.board)
        self.assertIsNone(forced_coin_result(rig.board, P2))
        with patch('spirit.game.session.effects.random.choice', return_value=0):
            result = await self.context(rig, P1).flip_coins(1, 'Own attack')
        self.assertEqual(result, [True])

    async def test_benched_malamar_does_not_force_tails(self):
        rig, entities = self.rig('Promo_XY.Malamar_58')
        rig.to_area(entities['target'], P1, 'bench')
        rig.session.turn_state.begin_turn(P2, rig.board)
        self.assertIsNone(forced_coin_result(rig.board, P2))

        with patch('spirit.game.session.effects.random.choice', return_value=0):
            results = await self.context(rig, P2).flip_coins(1, 'Coin attack')
        self.assertEqual(results, [True])

    async def test_chosen_heads_cannot_override_contrary(self):
        rig, _ = self.rig('Promo_XY.Malamar_58')
        rig.session.turn_state.begin_turn(P2, rig.board)
        rig.session.turn_state.forced_coin_result = True

        with patch('spirit.game.session.effects.random.choice', return_value=0):
            results = await self.context(rig, P2).flip_coins(1, 'Coin attack')

        self.assertEqual(results, [False])
        self.assertIsNone(rig.session.turn_state.forced_coin_result)

    async def test_attack_reroll_is_still_tails(self):
        rig, _ = self.rig('Promo_XY.Malamar_58')
        rig.session.turn_state.begin_turn(P2, rig.board)
        ctx = self.context(rig, P2)
        ctx.ask_yes_no = AsyncMock(return_value=True)
        ctx._queue_coin_results = AsyncMock()

        with patch('spirit.game.session.effects.attack_coin_reroll_offered',
                   return_value=True), patch(
                       'spirit.game.session.effects.random.choice', return_value=0):
            results = await ctx.flip_coins(2, 'Coin attack')

        self.assertEqual(results, [False, False])
        self.assertTrue(rig.session.turn_state.attack_coin_reroll_used)

    async def test_turn_flips_outside_effect_context_are_tails(self):
        rig, entities = self.rig('Promo_XY.Malamar_58')
        rig.session.turn_state.begin_turn(P2, rig.board)
        attacker = entities['p2_active']

        with patch('spirit.game.session.game_session.random.choice',
                   return_value=0), patch.object(
                       rig.session, 'send_game_sequence', new_callable=AsyncMock
                   ), patch.object(
                       rig.session, 'choreo_pause', new_callable=AsyncMock
                   ), patch.object(
                       rig.session, '_apply_raw_damage', new_callable=AsyncMock,
                       return_value=False) as damage:
            self.assertFalse(await rig.session._resolve_attack_attempt_flip(
                P2, attacker, 'Smokescreen'))
            self.assertFalse(await rig.session._resolve_confusion_flip(P2, attacker))
            self.assertFalse(await rig.session._resolve_attach_tax_flip(
                P2, SimpleNamespace(entity_id='missing'), entities['target']))

        damage.assert_awaited_once()


if __name__ == '__main__':
    unittest.main()
