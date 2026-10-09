"""Shady Dealings is an optional on-evolution trigger."""
import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures


class ShadyDealingsConfirmationTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx

    async def test_declining_skips_search_reveal_and_shuffle(self):
        for path in ('SWSH1.Drizzile_56', 'SWSH1.Inteleon_58'):
            with self.subTest(card=path):
                _, _, ctx = self.ctx(path, 'Shady Dealings')
                ctx.ask_yes_no = AsyncMock(return_value=False)
                ctx.search_deck = AsyncMock()
                ctx.put_in_hand = AsyncMock()
                ctx.shuffle_deck = AsyncMock()

                await ctx.ability.effect(ctx)

                ctx.ask_yes_no.assert_awaited_once_with('Use Shady Dealings?')
                ctx.search_deck.assert_not_awaited()
                ctx.put_in_hand.assert_not_awaited()
                ctx.shuffle_deck.assert_not_awaited()
                self.assertTrue(ctx.suppress_announce)

    async def test_accepting_confirms_before_search_and_shuffles(self):
        for path, count in (('SWSH1.Drizzile_56', 1),
                            ('SWSH1.Inteleon_58', 2)):
            with self.subTest(card=path):
                _, _, ctx = self.ctx(path, 'Shady Dealings')
                events = []

                async def confirm(*args):
                    events.append('confirm')
                    return True

                async def search(*args, **kwargs):
                    events.append('search')
                    self.assertEqual(kwargs['count'], count)
                    self.assertEqual(kwargs['minimum'], 0)
                    return []

                ctx.ask_yes_no = AsyncMock(side_effect=confirm)
                ctx.search_deck = AsyncMock(side_effect=search)
                ctx.put_in_hand = AsyncMock()
                ctx.shuffle_deck = AsyncMock()

                await ctx.ability.effect(ctx)

                self.assertEqual(events, ['confirm', 'search'])
                ctx.put_in_hand.assert_awaited_once_with([], reveal=True)
                ctx.shuffle_deck.assert_awaited_once()
