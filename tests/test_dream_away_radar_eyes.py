"""Coin-gated shuffle attacks and top-deck pick attacks."""

import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures
from spirit.tools.effect_smoke import P1, P2


class DreamAwayRadarEyesTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx

    async def test_dream_away_only_shuffles_on_heads(self):
        for heads in (False, True):
            with self.subTest(heads=heads):
                rig, _, ctx = self.ctx('SM8.TapuFini_151', 'Dream Away')
                defender = ctx.defender
                ctx.flip_coins = AsyncMock(return_value=[heads])
                await ctx.ability.effect(ctx)
                ctx.flip_coins.assert_awaited_once_with(1, 'Dream Away')
                self.assertEqual(defender in ctx.deck(P2), heads)
                self.assertEqual(ctx.opponent_active() is defender, not heads)

    async def test_coin_gated_active_bounce(self):
        for path, title in (
            ('SM1.Pinsir_6', 'Roof Fling'),
            ('SV3.Floatzel_49', 'Swirling Tail'),
        ):
            for heads in (False, True):
                with self.subTest(path=path, heads=heads):
                    _, _, ctx = self.ctx(path, title)
                    defender = ctx.defender
                    ctx.flip_coins = AsyncMock(return_value=[heads])
                    await ctx.ability.effect(ctx)
                    ctx.flip_coins.assert_awaited_once_with(1, title)
                    self.assertEqual(defender in ctx.hand(P2), heads)
                    self.assertEqual(ctx.opponent_active() is defender, not heads)

    async def test_reversing_gust_only_chooses_and_shuffles_on_heads(self):
        for heads in (False, True):
            with self.subTest(heads=heads):
                _, _, ctx = self.ctx('ME1.Shiftry_15', 'Reversing Gust')
                target = ctx.opponent_bench()[0]
                ctx.flip_coins = AsyncMock(return_value=[heads])
                ctx.choose_pokemon = AsyncMock(return_value=target)
                await ctx.ability.effect(ctx)
                ctx.flip_coins.assert_awaited_once_with(1, 'Reversing Gust')
                self.assertEqual(ctx.choose_pokemon.await_count, int(heads))
                self.assertEqual(target in ctx.deck(P2), heads)

    async def test_top_card_picks_select_once_and_shuffle_rest(self):
        cases = (
            ('SM10.Venonat_9', 'Radar Eyes', 7),
            ('XY6.Jirachi_42', 'Diminutive Desire', 7),
            ('Promo_SM.DetectivePikachu_194', 'Brilliant Deduction', 4),
        )
        for path, title, count in cases:
            with self.subTest(path=path):
                _, _, ctx = self.ctx(path, title)
                top = ctx.deck_top(count)
                self.assertEqual(len(top), count)
                selected = top[-1]
                original_hand_size = len(ctx.hand(P1))
                original_deck_size = len(ctx.deck(P1))
                ctx.choose_cards = AsyncMock(return_value=[selected])
                ctx.reveal_cards = AsyncMock()
                shuffle_deck = ctx.shuffle_deck
                ctx.shuffle_deck = AsyncMock(wraps=shuffle_deck)
                await ctx.ability.effect(ctx)
                self.assertEqual(ctx.choose_cards.await_count, 1)
                self.assertEqual(ctx.choose_cards.await_args.args[0], top)
                self.assertEqual(ctx.choose_cards.await_args.kwargs['display_cards'], top)
                ctx.reveal_cards.assert_not_awaited()
                ctx.shuffle_deck.assert_awaited_once_with()
                self.assertIn(selected, ctx.hand(P1))
                self.assertEqual(len(ctx.hand(P1)), original_hand_size + 1)
                self.assertEqual(len(ctx.deck(P1)), original_deck_size - 1)
                self.assertTrue(all(card in ctx.deck(P1) for card in top[:-1]))


if __name__ == '__main__':
    unittest.main()
