"""Printed 'choose 1' effects execute exactly the selected branch."""

import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures
from spirit.game.session.effects import EffectContext
from spirit.game.session.legal_actions import trainer_condition_met
from spirit.tools.effect_smoke import P1


class ModalEffectChoiceTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    def trainer(self, path):
        rig, entities = self.rig(path, 'trainer')
        ctx = EffectContext(rig.session, P1, entities['target'], None)
        ctx.is_trainer_effect = True
        rig.to_area(ctx.source, P1, 'discard')
        return rig, ctx, fixtures.definition(path)

    async def test_tate_and_liza_draw_and_switch_are_exclusive(self):
        for printing in ('SM7.TateLiza_148', 'SM7.TateLiza_166',
                         'SM7.TateLiza_186'):
            for choice in (0, 1):
                with self.subTest(printing=printing, choice=choice):
                    rig, ctx, definition = self.trainer(printing)
                    active = ctx.my_active()
                    bench = ctx.my_bench()[0]
                    hand_before = list(ctx.hand())
                    deck_before = list(ctx.deck())
                    ctx.choose = AsyncMock(return_value=choice)
                    ctx.choose_pokemon = AsyncMock(return_value=bench)
                    await definition.effect(ctx)
                    ctx.choose.assert_awaited_once()
                    if choice == 0:
                        self.assertIs(ctx.my_active(), active)
                        self.assertEqual(len(ctx.hand()), 5)
                        ctx.choose_pokemon.assert_not_awaited()
                    else:
                        self.assertIs(ctx.my_active(), bench)
                        self.assertEqual(ctx.hand(), hand_before)
                        self.assertEqual(ctx.deck(), deck_before)
                        ctx.choose_pokemon.assert_awaited_once()

    async def test_giovanni_scheme_draw_or_damage_boost(self):
        for printing in ('XY8.GiovannisScheme_138',
                         'XY8.GiovannisScheme_162'):
            for choice in (0, 1):
                with self.subTest(printing=printing, choice=choice):
                    rig, ctx, definition = self.trainer(printing)
                    hand_before = list(ctx.hand())
                    deck_before = list(ctx.deck())
                    modifiers_before = len(rig.session.turn_state.damage_modifiers)
                    ctx.choose = AsyncMock(return_value=choice)
                    await definition.effect(ctx)
                    if choice == 0:
                        self.assertEqual(len(ctx.hand()), max(5, len(hand_before)))
                        self.assertEqual(len(rig.session.turn_state.damage_modifiers),
                                         modifiers_before)
                    else:
                        self.assertEqual(ctx.hand(), hand_before)
                        self.assertEqual(ctx.deck(), deck_before)
                        added = rig.session.turn_state.damage_modifiers[modifiers_before:]
                        self.assertEqual(len(added), 1)
                        self.assertEqual(added[0].amount, 20)

    async def test_ingo_emmet_draws_from_selected_end_after_private_look(self):
        for printing in ('SM9.IngoEmmet_144', 'SM9.IngoEmmet_176'):
            for choice in (0, 1):
                with self.subTest(printing=printing, choice=choice):
                    rig, ctx, definition = self.trainer(printing)
                    for card in list(ctx.deck()):
                        rig.to_area(card, P1, 'discard')
                    deck = [self.add(rig, fixtures.definition('BW1.Snivy_1'),
                                     P1, 'deck') for _ in range(6)]
                    old_hand = list(ctx.hand())
                    ctx.choose = AsyncMock(return_value=choice)
                    ctx.reveal_cards = AsyncMock()
                    await definition.effect(ctx)
                    ctx.reveal_cards.assert_awaited_once_with([deck[-1]],
                                                             to_player=P1)
                    self.assertTrue(all(card in ctx.discard_pile()
                                        for card in old_hand))
                    expected_remaining = deck[0] if choice == 0 else deck[-1]
                    self.assertEqual(ctx.deck(), [expected_remaining])
                    self.assertEqual(len(ctx.hand()), 5)

    async def test_ingo_emmet_requires_a_card_to_inspect(self):
        rig, ctx, definition = self.trainer('SM9.IngoEmmet_144')
        for card in list(ctx.deck()):
            rig.to_area(card, P1, 'discard')
        self.assertFalse(trainer_condition_met(
            definition.condition, rig.board, P1, ctx.source))

    async def test_pelipper_hearsay_recovers_or_searches_not_both(self):
        for choice in (0, 1):
            with self.subTest(choice=choice):
                rig, _, ctx = fixtures.HgssRulesTests.ctx(
                    self, 'SV2.Pelipper_159', 'Hearsay')
                from_discard = self.add(
                    rig, fixtures.definition('SM7.TateLiza_148'), P1, 'discard')
                from_deck = self.add(
                    rig, fixtures.definition('XY8.GiovannisScheme_138'), P1, 'deck')
                ctx.ask_yes_no = AsyncMock(return_value=True)
                ctx.choose = AsyncMock(return_value=choice)
                ctx.choose_cards = AsyncMock(return_value=[from_discard])
                ctx.search_deck = AsyncMock(return_value=[from_deck])
                await ctx.ability.effect(ctx)
                if choice == 0:
                    self.assertIn(from_discard, ctx.hand())
                    self.assertIn(from_deck, ctx.deck())
                    ctx.search_deck.assert_not_awaited()
                else:
                    self.assertIn(from_deck, ctx.hand())
                    self.assertIn(from_discard, ctx.discard_pile())
                    ctx.choose_cards.assert_not_awaited()
