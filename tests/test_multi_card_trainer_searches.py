"""Trainer searches keep their printed quantities and type restrictions."""
import unittest
from unittest.mock import AsyncMock

from spirit.game.attributes import PokemonTypes
from spirit.game.card_effects.standard_era import _basic_energy_types
from spirit.game.session.effects import EffectContext, is_basic_energy
from spirit.tools.effect_smoke import P1
from tests import test_hgss_rules as fixtures


class MultiCardTrainerSearchTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    def setup_trainer(self, path):
        rig, entities = self.rig(path, 'trainer')
        definition = fixtures.definition(path)
        return rig, EffectContext(rig.session, P1, entities['target'], None), definition

    async def test_energy_search_pro_takes_multiple_distinct_basic_types(self):
        rig, ctx, definition = self.setup_trainer('SV08.EnergySearchPro_176')
        groups_seen = []
        chosen_energies = []

        async def select_groups(groups, **kwargs):
            groups_seen.extend(groups)
            self.assertTrue(all(count == 1 for _, count, _ in groups))
            self.assertGreaterEqual(len(groups), 3)
            selected = []
            for predicate, _, _ in groups:
                candidates = [card for card in ctx.deck() if predicate(card)]
                picked = candidates[:1] if len(selected) < 3 else []
                selected.append(picked)
                chosen_energies.extend(picked)
            return selected

        ctx.search_deck_groups = AsyncMock(side_effect=select_groups)
        await definition.effect(ctx)
        self.assertEqual(len(chosen_energies), 3)
        self.assertTrue(all(card in ctx.hand() for card in chosen_energies))
        self.assertEqual(len({next(iter(_basic_energy_types(card)))
                              for card in chosen_energies}), 3)
        self.assertGreaterEqual(len(groups_seen), 3)

    async def test_professor_oaks_setup_benches_three_distinct_types(self):
        rig, ctx, definition = self.setup_trainer('SM12.ProfessorOaksSetup_201')
        grass = self.add(rig, fixtures.definition('SV1.Smoliv_20'), P1, 'deck')
        another_grass = self.add(rig, fixtures.definition('SV1.Capsakid_28'), P1, 'deck')
        psychic = self.add(rig, fixtures.definition('SV4.Flittle_79'), P1, 'deck')
        fire = self.add(rig, fixtures.definition('SV4.Fuecoco_23'), P1, 'deck')
        choices = [grass, psychic, fire]

        async def search(predicate, **kwargs):
            choice = choices.pop(0)
            self.assertTrue(predicate(choice))
            if choice is not grass:
                self.assertFalse(predicate(another_grass))
            return [choice]

        ctx.search_deck = AsyncMock(side_effect=search)
        await definition.effect(ctx)
        self.assertEqual(ctx.search_deck.await_count, 3)
        self.assertTrue(all(card in ctx.my_bench() for card in
                            (grass, psychic, fire)))
        self.assertIn(another_grass, ctx.deck())

    async def test_sabrina_brycen_additional_search_requires_five_card_payment(self):
        rig, ctx, definition = self.setup_trainer('Promo_SM.SabrinaBrycen_246')
        grass = self.add(rig, fixtures.definition('SV1.Smoliv_20'), P1, 'deck')
        psychic = self.add(rig, fixtures.definition('SV4.Flittle_79'), P1, 'deck')
        fire = self.add(rig, fixtures.definition('SV4.Fuecoco_23'), P1, 'deck')
        energies = [card for card in ctx.deck() if is_basic_energy(card)][:2]
        payment = [card for card in ctx.hand() if card is not ctx.source][:5]
        ctx.ask_yes_no = AsyncMock(return_value=True)
        ctx.choose_cards = AsyncMock(return_value=payment)
        choices = [grass, psychic, fire]

        async def search(predicate, **kwargs):
            self.assertTrue(all(card in ctx.discard_pile() for card in payment))
            if kwargs.get('count') == 2:
                self.assertTrue(all(predicate(card) for card in energies))
                return energies
            choice = choices.pop(0)
            self.assertTrue(predicate(choice))
            return [choice]

        ctx.search_deck = AsyncMock(side_effect=search)
        await definition.effect(ctx)
        self.assertEqual(ctx.search_deck.await_count, 4)
        self.assertTrue(all(card in ctx.hand() for card in
                            (*energies, grass, psychic, fire)))

    async def test_sabrina_brycen_without_payment_only_searches_energy(self):
        rig, ctx, definition = self.setup_trainer('Promo_SM.SabrinaBrycen_246')
        energies = [card for card in ctx.deck() if is_basic_energy(card)][:2]
        before_discard = list(ctx.discard_pile())
        ctx.ask_yes_no = AsyncMock(return_value=False)

        async def search(predicate, **kwargs):
            self.assertEqual(kwargs['count'], 2)
            self.assertTrue(all(predicate(card) for card in energies))
            return energies

        ctx.search_deck = AsyncMock(side_effect=search)
        await definition.effect(ctx)
        ctx.search_deck.assert_awaited_once()
        self.assertTrue(all(card in ctx.hand() for card in energies))
        self.assertEqual(list(ctx.discard_pile()), before_discard)

    async def test_misty_lorelei_extra_gx_permission_is_water_only_this_turn(self):
        rig, ctx, definition = self.setup_trainer('SM12.MistyLorelei_199')
        water = self.add(rig, fixtures.definition('SV1.Buizel_46'), P1, 'bench')
        fire = self.add(rig, fixtures.definition('SV4.Fuecoco_23'), P1, 'bench')
        payment = [card for card in ctx.hand() if card is not ctx.source][:5]
        ctx.ask_yes_no = AsyncMock(return_value=True)
        ctx.choose_cards = AsyncMock(return_value=payment)
        water_guid = self.energies[PokemonTypes.WATER.value]
        water_energies = [card for card in ctx.deck()
                          if card.archetype_id.lower() == water_guid.lower()][:3]

        async def search(predicate, **kwargs):
            self.assertEqual(kwargs['count'], 3)
            self.assertTrue(all(predicate(card) for card in water_energies))
            return water_energies

        ctx.search_deck = AsyncMock(side_effect=search)
        await definition.effect(ctx)
        state = rig.session.turn_state
        self.assertTrue(all(card in ctx.discard_pile() for card in payment))
        self.assertTrue(all(card in ctx.hand() for card in water_energies))
        self.assertTrue(state.can_repeat_gx(P1, water, rig.board))
        self.assertFalse(state.can_repeat_gx(P1, fire, rig.board))
        state.begin_turn(ctx.opponent_id, rig.board)
        self.assertFalse(state.can_repeat_gx(P1, water, rig.board))

    async def test_musharna_dream_calling_searches_all_fennel_copies(self):
        path = 'ZSV10PT5.Musharna_36'
        rig, entities = self.rig(path)
        ability = next(a for a in fixtures.definition(path).abilities
                       if a.title == 'Dream Calling')
        ctx = EffectContext(rig.session, P1, entities['target'], ability)
        fennel = fixtures.definition('ZSV10PT5.Fennel_82')
        cards = [self.add(rig, fennel, P1, 'deck') for _ in range(3)]
        unrelated = self.add(rig, fixtures.definition('SV1.Buizel_46'), P1, 'deck')

        async def search(predicate, count, **kwargs):
            self.assertEqual(count, 60)
            self.assertTrue(all(predicate(card) for card in cards))
            self.assertFalse(predicate(unrelated))
            return cards

        ctx.search_deck = AsyncMock(side_effect=search)
        await ability.effect(ctx)
        self.assertTrue(all(card in ctx.hand() for card in cards))


if __name__ == '__main__':
    unittest.main()
