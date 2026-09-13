"""Private search failure and effect-driven Stage 1 bench placement."""
import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures
from tests.test_hgss_rules import definition
from spirit.game.session.effects import EffectContext
from spirit.game.card_effects.standard_era import standard_trainer_effect
from spirit.tools.effect_smoke import P1


class DiveBallWaterDuplicatesTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx
    add = fixtures.HgssRulesTests.add

    async def test_water_duplicates_full_bench_does_not_offer_targets(self):
        rig, e, ctx = self.ctx('XY9.Frogadier_39', 'Water Duplicates')
        while len(ctx.my_bench()) < 5:
            self.add(rig, definition('BW1.Snivy_1'), P1, 'bench')
        frog = self.add(rig, definition('XY9.Frogadier_39'), P1, 'deck')
        ctx.search_deck = AsyncMock()
        ctx.shuffle_deck = AsyncMock()
        await ctx.ability.effect(ctx)
        ctx.search_deck.assert_not_awaited()
        ctx.shuffle_deck.assert_awaited_once()
        self.assertIn(frog, ctx.deck())

    async def test_water_duplicates_can_choose_fewer_than_three(self):
        rig, e, ctx = self.ctx('XY9.Frogadier_39', 'Water Duplicates')
        frogs = [self.add(rig, definition('XY9.Frogadier_39'), P1, 'deck')
                 for _ in range(3)]
        ctx.choose_cards = AsyncMock(return_value=[frogs[0]])
        await ctx.ability.effect(ctx)
        self.assertIn(frogs[0], ctx.my_bench())
        self.assertTrue(all(frog in ctx.deck() for frog in frogs[1:]))

    async def test_dive_ball_may_fail_even_with_water_pokemon_in_deck(self):
        rig, e = self.rig('XY5.DiveBall_125', 'trainer')
        ctx = EffectContext(rig.session, P1, e['target'], None)
        water = self.add(rig, definition('XY9.Frogadier_39'), P1, 'deck')
        ctx.choose_cards = AsyncMock(return_value=[])
        ctx.shuffle_deck = AsyncMock()
        before = list(ctx.hand())
        await definition('XY5.DiveBall_125').effect(ctx)
        self.assertEqual(ctx.choose_cards.await_args.kwargs['minimum'], 0)
        self.assertIn(water, ctx.choose_cards.await_args.args[0])
        self.assertEqual(ctx.hand(), before)
        self.assertIn(water, ctx.deck())
        ctx.shuffle_deck.assert_awaited_once()

    async def test_dive_ball_selects_water_evolution_not_other_types(self):
        rig, e = self.rig('XY5.DiveBall_125', 'trainer')
        ctx = EffectContext(rig.session, P1, e['target'], None)
        water = self.add(rig, definition('XY9.Frogadier_39'), P1, 'deck')
        grass = self.add(rig, definition('BW1.Snivy_1'), P1, 'deck')
        ctx.choose_cards = AsyncMock(return_value=[water])
        await definition('XY5.DiveBall_125').effect(ctx)
        offered = ctx.choose_cards.await_args.args[0]
        self.assertIn(water, offered)
        self.assertNotIn(grass, offered)
        self.assertIn(water, ctx.hand())
        self.assertNotIn(water, ctx.deck())

    async def test_unrestricted_private_search_still_requires_full_count(self):
        rig, e = self.rig('XY5.DiveBall_125', 'trainer')
        ctx = EffectContext(rig.session, P1, e['target'], None)
        ctx.choose_cards = AsyncMock(return_value=[])
        await standard_trainer_effect(
            'Search your deck for 2 cards and put them into your hand. '
            'Shuffle your deck afterward.')(ctx)
        self.assertEqual(ctx.choose_cards.await_args.kwargs['minimum'], 2)

    async def test_water_duplicates_benches_three_stage_one_cards(self):
        rig, e, ctx = self.ctx('XY9.Frogadier_39', 'Water Duplicates')
        for p in list(ctx.my_bench()):
            rig.to_area(p, P1, 'discard')
        frogs = [self.add(rig, definition('XY9.Frogadier_39'), P1, 'deck')
                 for _ in range(3)]
        other = self.add(rig, definition('BW1.Snivy_1'), P1, 'deck')
        ctx.choose_cards = AsyncMock(side_effect=lambda pool, count, **kw:
                                     [c for c in pool if c in frogs][:count])
        ctx.shuffle_deck = AsyncMock()
        await ctx.ability.effect(ctx)
        self.assertEqual(ctx.my_bench(), frogs)
        self.assertNotIn(other, ctx.choose_cards.await_args.args[0])
        self.assertEqual(ctx.choose_cards.await_args.args[1], 3)
        self.assertEqual(ctx.choose_cards.await_args.kwargs['minimum'], 0)
        for frog in frogs:
            self.assertEqual(rig.session.turn_state.entered_play_turn[frog.entity_id],
                             rig.session.turn_state.turn_number)
        self.assertTrue(ctx._messages)  # Public intro/move choreography is queued.
        ctx.shuffle_deck.assert_awaited_once()

    async def test_water_duplicates_respects_bench_capacity(self):
        rig, e, ctx = self.ctx('XY9.Frogadier_39', 'Water Duplicates')
        while len(ctx.my_bench()) < 4:
            self.add(rig, definition('BW1.Snivy_1'), P1, 'bench')
        frogs = [self.add(rig, definition('XY9.Frogadier_39'), P1, 'deck')
                 for _ in range(3)]
        ctx.choose_cards = AsyncMock(side_effect=lambda pool, count, **kw:
                                     [c for c in pool if c in frogs][:count])
        await ctx.ability.effect(ctx)
        self.assertEqual(len(ctx.my_bench()), 5)
        self.assertEqual(ctx.choose_cards.await_args.args[1], 1)
        self.assertEqual(sum(f in ctx.deck() for f in frogs), 2)

    async def test_water_duplicates_can_fail_and_still_shuffles(self):
        rig, e, ctx = self.ctx('XY9.Frogadier_39', 'Water Duplicates')
        frog = self.add(rig, definition('XY9.Frogadier_39'), P1, 'deck')
        before = list(ctx.my_bench())
        ctx.choose_cards = AsyncMock(return_value=[])
        ctx.shuffle_deck = AsyncMock()
        await ctx.ability.effect(ctx)
        self.assertEqual(ctx.my_bench(), before)
        self.assertIn(frog, ctx.deck())
        self.assertEqual(ctx.choose_cards.await_args.kwargs['minimum'], 0)
        ctx.shuffle_deck.assert_awaited_once()
