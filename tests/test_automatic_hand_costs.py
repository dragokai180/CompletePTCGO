"""Forced hand payments skip selection, not their movement or follow-up choice."""
import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures
from spirit.game.session.effects import EffectContext
from spirit.tools.effect_smoke import P1, P2


class AutomaticHandCostTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    def context(self, path='BW5.UltraBall_102', owner=P1):
        rig, e = self.rig(path, 'trainer')
        source = e['target']
        rig.to_area(source, P1, 'discard')  # The played Trainer is not a cost.
        for card in list(rig.board.find_player_area(owner, 'hand').children):
            rig.to_area(card, owner, 'deck')
        ctx = EffectContext(rig.session, owner, source, None)
        rig.session.prompt_entity_picker = AsyncMock(return_value=[])
        rig.session.prompt_card_chooser = AsyncMock(return_value=[])
        return rig, ctx

    def card(self, rig, path='BW1.Snivy_1', owner=P1, zone='hand'):
        return self.add(rig, fixtures.definition(path), owner, zone)

    async def test_ultra_ball_exact_cost_is_discarded_before_manual_search(self):
        rig, ctx = self.context()
        cards = [self.card(rig), self.card(rig, 'BW1.FireEnergy_106')]
        async def search(*args, **kwargs):
            self.assertTrue(all(c in ctx.discard_pile() for c in cards))
            return []  # The private search can still fail.
        ctx.search_deck = AsyncMock(side_effect=search)
        await fixtures.definition('BW5.UltraBall_102').effect(ctx)
        rig.session.prompt_entity_picker.assert_not_awaited()
        rig.session.prompt_card_chooser.assert_not_awaited()
        ctx.search_deck.assert_awaited_once()

    async def test_communication_one_valid_pokemon_returns_before_search(self):
        for path in ('HGSS1.PokmonCommunication_98', 'BW1.PokmonCommunication_99',
                     'SM9.PokmonCommunication_152'):
            with self.subTest(path=path):
                rig, ctx = self.context(path)
                pokemon = self.card(rig)
                other = self.card(rig, 'BW1.FireEnergy_106')
                async def search(*args, **kwargs):
                    self.assertIn(pokemon, ctx.deck())
                    self.assertIn(other, ctx.hand())
                    return []
                ctx.search_deck = AsyncMock(side_effect=search)
                ctx.shuffle_deck = AsyncMock()
                await fixtures.definition(path).effect(ctx)
                rig.session.prompt_entity_picker.assert_not_awaited()
                rig.session.prompt_card_chooser.assert_not_awaited()
                ctx.search_deck.assert_awaited_once()
                ctx.shuffle_deck.assert_awaited_once()

    async def test_filtered_payment_counts_valid_cards_not_entire_hand(self):
        for owner in (P1, P2):
            rig, ctx = self.context(owner=owner)
            energy = self.card(rig, 'BW1.FireEnergy_106', owner)
            other = self.card(rig, owner=owner)
            paid = await ctx.discard_from_hand(1, predicate=lambda c: c is energy)
            self.assertEqual(paid, [energy])
            self.assertIn(energy, ctx.discard_pile())
            self.assertIn(other, ctx.hand())
            rig.session.prompt_entity_picker.assert_not_awaited()

    async def test_choice_surplus_optional_short_ordered_or_browser_is_not_automatic(self):
        for scenario in ('surplus', 'optional', 'short', 'ordered', 'browser', 'opponent'):
            with self.subTest(scenario=scenario):
                rig, ctx = self.context()
                owner = P2 if scenario == 'opponent' else P1
                cards = [self.card(rig, owner=owner), self.card(rig, owner=owner)]
                kwargs = {}
                count = 2
                if scenario == 'surplus': count = 1
                if scenario == 'short': count = 3
                if scenario == 'optional': kwargs['minimum'] = 0
                if scenario == 'ordered': kwargs['ordered'] = True
                if scenario == 'browser': kwargs['display_cards'] = cards
                if scenario == 'opponent': kwargs['player_id'] = P2
                await ctx.choose_cards(cards, count, **kwargs)
                self.assertEqual(rig.session.prompt_entity_picker.await_count
                                 + rig.session.prompt_card_chooser.await_count, 1)

    async def test_deck_discard_and_played_source_do_not_auto_select(self):
        for zone in ('deck', 'discard', 'hand'):
            rig, ctx = self.context()
            card = ctx.source if zone == 'hand' else self.card(rig, zone=zone)
            if zone == 'hand': rig.to_area(card, P1, 'hand')
            await ctx.choose_cards([card], 1)
            self.assertEqual(rig.session.prompt_entity_picker.await_count
                             + rig.session.prompt_card_chooser.await_count, 1)


if __name__ == '__main__':
    unittest.main()
