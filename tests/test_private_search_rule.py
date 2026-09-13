"""Fail-to-find is shared by private searches, not by public-zone costs."""
import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures
from tests.test_hgss_rules import definition
from spirit.game.card_effects.standard_era import standard_trainer_effect
from spirit.game.card_effects.support_common import search_to_hand
from spirit.tools.effect_smoke import P1


class PrivateSearchRuleTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx
    add = fixtures.HgssRulesTests.add

    async def test_common_search_overrides_required_minimum_for_typed_or_revealed_search(self):
        for predicate, reveal in ((lambda card: True, False), (None, True)):
            for minimum in (None, 1, 2):
                rig, e, ctx = self.ctx('BW1.Snivy_1', 'Tackle')
                ctx.choose_cards = AsyncMock(return_value=[])
                picks = await ctx.search_deck(predicate, 2, minimum=minimum,
                                              reveal_result=reveal)
                self.assertEqual(picks, [])
                self.assertEqual(ctx.choose_cards.await_args.kwargs['minimum'], 0)
                self.assertTrue(ctx.choose_cards.await_args.kwargs['display_cards'])

    async def test_unrestricted_unrevealed_search_keeps_minimum(self):
        rig, e, ctx = self.ctx('BW1.Snivy_1', 'Tackle')
        ctx.choose_cards = AsyncMock(return_value=[])
        await ctx.search_deck(None, 2, minimum=2)
        self.assertEqual(ctx.choose_cards.await_args.kwargs['minimum'], 2)

    async def test_generated_searches_can_fail_for_all_revealed_card_kinds(self):
        for descriptor in ('a Water Pokémon', 'a Pokémon', 'a basic Energy card',
                           'a Supporter card', '2 cards'):
            rig, e, ctx = self.ctx('BW1.Snivy_1', 'Tackle')
            ctx.choose_cards = AsyncMock(return_value=[])
            ctx.put_in_hand = AsyncMock()
            ctx.shuffle_deck = AsyncMock()
            await standard_trainer_effect(
                f'Search your deck for {descriptor}, reveal them, and put them '
                'into your hand. Shuffle your deck afterward.')(ctx)
            self.assertEqual(ctx.choose_cards.await_args.kwargs['minimum'], 0, descriptor)
            ctx.put_in_hand.assert_awaited_once_with([], reveal=True)
            ctx.shuffle_deck.assert_awaited_once()

    async def test_shared_attack_search_template_propagates_reveal(self):
        rig, e, ctx = self.ctx('BW1.Snivy_1', 'Tackle')
        ctx.choose_cards = AsyncMock(return_value=[])
        ctx.deal_damage = AsyncMock()
        ctx.shuffle_deck = AsyncMock()
        await search_to_hand(None, count=2, minimum=2, reveal=True)(ctx)
        self.assertEqual(ctx.choose_cards.await_args.kwargs['minimum'], 0)
        ctx.shuffle_deck.assert_awaited_once()

    async def test_private_top_and_bottom_consultations_can_fail(self):
        for position in ('top', 'bottom'):
            rig, e, ctx = self.ctx('BW1.Snivy_1', 'Tackle')
            for _ in range(8):
                self.add(rig, definition('XY9.Frogadier_39'), P1, 'deck')
            ctx.choose_cards = AsyncMock(return_value=[])
            await standard_trainer_effect(
                f'Look at the {position} 7 cards of your deck. Choose 1 Water Pokémon '
                'you find there, reveal it, and put it into your hand. '
                'Shuffle the other cards back into your deck.')(ctx)
            self.assertEqual(ctx.choose_cards.await_args.kwargs['minimum'], 0)

    async def test_revealed_top_is_not_a_private_search(self):
        rig, e, ctx = self.ctx('BW1.Snivy_1', 'Tackle')
        for _ in range(8):
            self.add(rig, definition('XY9.Frogadier_39'), P1, 'deck')
        ctx.choose_cards = AsyncMock(return_value=[])
        await standard_trainer_effect(
            'Reveal the top 7 cards of your deck. Choose 1 Water Pokémon '
            'you find there and put it into your hand. '
            'Shuffle the other cards back into your deck.')(ctx)
        self.assertEqual(ctx.choose_cards.await_args.kwargs['minimum'], 1)

    async def test_hand_discard_cost_is_not_relaxed(self):
        rig, e, ctx = self.ctx('BW1.Snivy_1', 'Tackle')
        ctx.choose_cards = AsyncMock(return_value=[])
        await ctx.discard_from_hand(2, minimum=2)
        self.assertEqual(ctx.choose_cards.await_args.kwargs['minimum'], 2)
