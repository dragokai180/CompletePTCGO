"""Activated self-counter costs gate every following benefit."""
import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures
from spirit.game.attributes import AttrID


class SelfCounterAbilityCostTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx

    async def test_zooming_draw_places_counter_before_drawing(self):
        _, entries, ctx = self.ctx('SV035.Dodrio_85', 'Zooming Draw')
        before_hp = entries['target'].get_attribute(AttrID.HP)
        before_hand = len(ctx.hand())

        await ctx.ability.effect(ctx)

        self.assertEqual(entries['target'].get_attribute(AttrID.HP),
                         before_hp - 10)
        self.assertEqual(len(ctx.hand()), before_hand + 1)

    async def test_zooming_draw_cannot_draw_if_counters_are_blocked(self):
        _, _, ctx = self.ctx('SV035.Dodrio_85', 'Zooming Draw')
        ctx.deal_damage = AsyncMock(return_value=0)
        ctx.draw_cards = AsyncMock()

        await ctx.ability.effect(ctx)

        ctx.draw_cards.assert_not_awaited()

    async def test_energy_search_requires_counter_payment(self):
        cases = (
            ('SM9.IncineroarGX_97', 'Scar Charge'),
            ('Promo_SM.Charizard_158', 'Roaring Resolve'),
        )
        for path, title in cases:
            with self.subTest(ability=title):
                _, _, ctx = self.ctx(path, title)
                ctx.deal_damage = AsyncMock(return_value=0)
                ctx.search_deck = AsyncMock(return_value=[])
                ctx.shuffle_deck = AsyncMock()

                await ctx.ability.effect(ctx)

                ctx.search_deck.assert_not_awaited()
                ctx.shuffle_deck.assert_not_awaited()

    async def test_energy_search_follows_successful_counter_payment(self):
        cases = (
            ('SM9.IncineroarGX_97', 'Scar Charge', 30),
            ('Promo_SM.Charizard_158', 'Roaring Resolve', 20),
        )
        for path, title, cost in cases:
            with self.subTest(ability=title):
                _, entries, ctx = self.ctx(path, title)
                before_hp = entries['target'].get_attribute(AttrID.HP)
                ctx.search_deck = AsyncMock(return_value=[])
                ctx.shuffle_deck = AsyncMock()

                await ctx.ability.effect(ctx)

                self.assertEqual(entries['target'].get_attribute(AttrID.HP),
                                 before_hp - cost)
                ctx.search_deck.assert_awaited_once()
                ctx.shuffle_deck.assert_awaited_once()


if __name__ == '__main__':
    unittest.main()
