"""Inspected cards stay visible while only legal cards can be selected."""
import unittest
from unittest.mock import AsyncMock, Mock

from tests import test_hgss_rules as fixtures
from spirit.game.session.effects import EffectContext, is_item_card, is_trainer_card
from spirit.tools.effect_smoke import P1, P2


class RevealedSelectionVisibilityTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx
    add = fixtures.HgssRulesTests.add

    async def test_stellar_wish_shows_all_five_with_only_trainers_selectable(self):
        for has_trainer in (False, True):
            with self.subTest(has_trainer=has_trainer):
                rig, e, ctx = self.ctx('Promo_SM.Jirachi_161', 'Stellar Wish')
                viewed = [card for card in ctx.deck() if not is_trainer_card(card)][:5]
                if has_trainer:
                    trainer = self.add(rig, self.item, P1, 'deck')
                    viewed[2] = trainer
                ctx.deck_top = Mock(return_value=viewed)
                ctx.choose_cards = AsyncMock(return_value=[trainer] if has_trainer else [])
                ctx.put_in_hand = AsyncMock()
                ctx.shuffle_deck = AsyncMock()
                ctx.apply_special_condition = AsyncMock()
                await ctx.ability.effect(ctx)
                self.assertEqual(ctx.choose_cards.await_args.args[:2],
                                 ([trainer] if has_trainer else [], 1))
                self.assertEqual(ctx.choose_cards.await_args.kwargs['display_cards'],
                                 viewed)
                ctx.shuffle_deck.assert_awaited_once()
                ctx.apply_special_condition.assert_awaited_once()

    async def test_adventurous_appetite_shows_non_items_too(self):
        rig, e, ctx = self.ctx('SM9.AlolanMuk_84', 'Adventurous Appetite')
        viewed = [card for card in ctx.deck(P2) if not is_item_card(card)][:6]
        ctx.deck_top = Mock(return_value=viewed)
        ctx.choose_cards = AsyncMock(return_value=[])
        ctx.reveal_cards = AsyncMock()
        ctx.shuffle_deck = AsyncMock()
        await ctx.ability.effect(ctx)
        self.assertEqual(ctx.choose_cards.await_args.args[:2], ([], 1))
        self.assertEqual(ctx.choose_cards.await_args.kwargs['display_cards'], viewed)

    async def test_accompanying_flute_shows_all_revealed_cards(self):
        path = 'SV06.AccompanyingFlute_142'
        rig, e = self.rig(path, 'trainer')
        ctx = EffectContext(rig.session, P1, e['target'], None)
        viewed = list(ctx.deck_top(5, P2))
        ctx.deck_top = Mock(return_value=viewed)
        ctx.choose_cards = AsyncMock(return_value=[])
        ctx.reveal_cards = AsyncMock()
        ctx.shuffle_deck = AsyncMock()
        await fixtures.definition(path).effect(ctx)
        self.assertEqual(ctx.choose_cards.await_args.kwargs['display_cards'], viewed)
