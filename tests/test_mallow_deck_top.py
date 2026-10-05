"""Mallow shuffles before putting the chosen cards on top, in chosen order."""

import unittest
from unittest.mock import AsyncMock, patch

from spirit.game.session.effects import EffectContext
from spirit.tools.effect_smoke import P1
from tests import test_hgss_rules as fixtures


class MallowDeckTopTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx

    async def test_both_printings_preserve_order_through_shuffle_and_draw(self):
        for path in ('SM2.Mallow_127', 'SM2.Mallow_145'):
            with self.subTest(path=path):
                rig, entities = self.rig(path, kind='trainer')
                deck = rig.board.find_player_area(P1, 'deck')
                first, second = deck.children[5], deck.children[10]
                ctx = EffectContext(rig.session, P1, entities['target'], None)
                ctx.choose_cards = AsyncMock(return_value=[first, second])

                with patch.object(rig.board, 'shuffle_deck',
                                  side_effect=lambda pid: deck.children.reverse()):
                    await fixtures.definition(path).effect(ctx)

                self.assertTrue(ctx.choose_cards.await_args.kwargs.get('ordered'))
                self.assertEqual(ctx.deck_top(2), [first, second])
                await ctx.draw_cards(2)
                self.assertEqual(ctx.hand()[-2:], [first, second])

    async def test_time_manipulation_uses_same_shuffle_then_stack_order(self):
        rig, _, ctx = self.ctx('SV08.Dialga_135', 'Time Manipulation')
        deck = rig.board.find_player_area(P1, 'deck')
        first, second = deck.children[5], deck.children[10]
        ctx.choose_cards = AsyncMock(return_value=[first, second])

        with patch.object(rig.board, 'shuffle_deck',
                          side_effect=lambda pid: deck.children.reverse()):
            await ctx.ability.effect(ctx)

        self.assertTrue(ctx.choose_cards.await_args.kwargs.get('ordered'))
        self.assertEqual(ctx.deck_top(2), [first, second])
        self.assertNotIn(first, ctx.hand())
        self.assertNotIn(second, ctx.hand())


if __name__ == '__main__':
    unittest.main()
