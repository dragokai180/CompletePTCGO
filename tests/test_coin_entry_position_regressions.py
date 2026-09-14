"""Coin gates, entry timing, and Active-only powers use real card definitions."""
import unittest
from unittest.mock import AsyncMock, patch

from tests import test_hgss_rules as fixtures
from tests.test_hgss_rules import definition
from spirit.game.attributes import AttrID
from spirit.game.data_utils import Triggers
from spirit.game.session.effects import EffectContext
from spirit.game.session.legal_actions import _ability_entries
from spirit.tools.effect_smoke import P1, P2


class CoinEntryPositionTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add
    ctx = fixtures.HgssRulesTests.ctx

    async def test_per_head_searches_flip_before_search_and_allow_failure(self):
        for path in ['HGSS2.DualBall_72', 'COL.DualBall_78',
                     'SM1.TimerBall_134', 'SM11.StadiumNav_208']:
            for heads in range(3):
                with self.subTest(path=path, heads=heads):
                    rig, entities = self.rig(path, 'trainer')
                    ctx = EffectContext(rig.session, P1, entities['target'], None)
                    order = []
                    async def flip(*args):
                        order.append('flip')
                        return [i < heads for i in range(2)]
                    async def search(*args, **kwargs):
                        order.append('search')
                        self.assertEqual(kwargs['count'], heads)
                        self.assertEqual(kwargs['minimum'], 0)
                        self.assertTrue(kwargs['reveal_result'])
                        return []
                    ctx.flip_coins = AsyncMock(side_effect=flip)
                    ctx.search_deck = AsyncMock(side_effect=search)
                    ctx.shuffle_deck = AsyncMock()
                    await definition(path).effect(ctx)
                    self.assertEqual(order, ['flip', 'search'] if heads else ['flip'])
                    self.assertEqual(ctx.flip_coins.call_args.args[0], 2)

    async def test_both_heads_searches_do_nothing_on_one_head(self):
        for path in ['SV2.DeliveryDrone_178', 'ZSV10PT5.EnergyCoin_81']:
            for heads in range(3):
                rig, entities = self.rig(path, 'trainer')
                ctx = EffectContext(rig.session, P1, entities['target'], None)
                ctx.flip_coins = AsyncMock(return_value=[i < heads for i in range(2)])
                ctx.search_deck = AsyncMock(return_value=[])
                ctx.shuffle_deck = AsyncMock()
                await definition(path).effect(ctx)
                ctx.flip_coins.assert_awaited_once()
                self.assertEqual(ctx.search_deck.await_count, int(heads == 2))
                if heads == 2:
                    self.assertEqual(ctx.search_deck.call_args.kwargs['count'], 1)
                    self.assertEqual(ctx.search_deck.call_args.kwargs['minimum'],
                                     1 if 'DeliveryDrone' in path else 0)

    async def test_public_recoveries_count_heads(self):
        for path, target_path in [('SM7.LureBall_138', 'HGSS1.Raichu_10'),
                                  ('SM9.Electrocharger_139', 'SM8.Electropower_172')]:
            for heads in [0, 1, 2]:
                rig, entities = self.rig(path, 'trainer')
                ctx = EffectContext(rig.session, P1, entities['target'], None)
                for card in list(ctx.discard_pile()):
                    rig.to_area(card, P1, 'deck')
                cards = [self.add(rig, definition(target_path), P1, 'discard') for _ in range(2)]
                ctx.flip_coins = AsyncMock(return_value=[i < heads for i in range(3 if 'LureBall' in path else 2)])
                ctx.choose_cards = AsyncMock(return_value=cards[:heads])
                await definition(path).effect(ctx)
                ctx.flip_coins.assert_awaited_once()
                self.assertEqual(sum(c not in ctx.discard_pile() for c in cards), heads)
                if heads:
                    self.assertEqual(ctx.choose_cards.call_args.args[1], heads)

    async def test_portrait_is_blocked_on_bench_in_menu_and_resolution(self):
        for path in ['HGSS3.Smeargle_8', 'COL.Smeargle_21']:
            rig, entities, ctx = self.ctx(path, 'Portrait')
            self.assertTrue(ctx.ability.condition(rig.board, P1, ctx.source))
            rig.to_area(ctx.source, P1, 'bench')
            self.assertFalse(ctx.ability.condition(rig.board, P1, ctx.source))
            self.assertFalse(_ability_entries(rig.board, rig.session.turn_state,
                             P1, rig.session.game_id, [ctx.source]))
            ctx.reveal_hand = AsyncMock(return_value=[])
            await ctx.ability.effect(ctx)
            ctx.reveal_hand.assert_not_awaited()

    async def test_celebration_wind_prompt_follows_entry_not_a_later_click(self):
        rig, entities, ctx = self.ctx('HGSS2.Shaymin_8', 'Celebration Wind')
        source = ctx.source
        rig.to_area(source, P1, 'hand')
        order = []
        async def played(*args, **kwargs):
            self.assertIn(source, rig.board.find_player_area(P1, 'bench').children)
            order.append('entered')
        async def confirm(effect_ctx, *args, **kwargs):
            self.assertIs(effect_ctx.source, source)
            self.assertIn(source, rig.board.find_player_area(P1, 'bench').children)
            order.append('prompt')
            return False
        rig.session._send_play_sequence = AsyncMock(side_effect=played)
        with patch.object(EffectContext, 'ask_yes_no', confirm), \
             patch.object(EffectContext, 'move_energy_freely', new_callable=AsyncMock) as move:
            await rig.session._execute_play_basic(P1, source)
            move.assert_not_awaited()
        self.assertEqual(order, ['entered', 'prompt'])
        self.assertTrue(ctx.ability.has_trigger(Triggers.ON_PLAY))
        self.assertFalse(_ability_entries(rig.board, rig.session.turn_state,
                         P1, rig.session.game_id, [source]))

    async def test_other_active_power_is_also_guarded_without_blocking_bench_bonuses(self):
        from spirit.game.card_effects.standard_era import ability_position_allowed
        rig, entities, ctx = self.ctx('HGSS4.Celebi_92', 'Forest Breath')
        rig.to_area(ctx.source, P1, 'bench')
        ctx.attach_energy = AsyncMock()
        ctx.choose_cards = AsyncMock()
        await ctx.ability.effect(ctx)
        ctx.choose_cards.assert_not_awaited()
        ctx.attach_energy.assert_not_awaited()
        # Tasting's Active clause increases its benefit; it is not a cost.
        self.assertTrue(ability_position_allowed(rig.board, P1, ctx.source,
            'Once during your turn, you may draw a card. If this Pokémon is your Active Pokémon, draw 1 more card.'))
