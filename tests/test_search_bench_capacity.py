"""Deck-to-Bench searches honor live space and keep private failure legal."""
import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures
from tests import test_restoration_bench_capacity as bench_fixtures
from spirit.game.card_effects.support_common import search_to_bench
from spirit.game.session.effects import EffectContext
from spirit.game.session.passives import effective_bench_capacity
from spirit.tools.effect_smoke import P1, P2


class SearchBenchCapacityTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add
    setup_field = bench_fixtures.RestorationBenchCapacityTests.setup_field

    def setup_search(self, occupied, owner=P1, sky=True, path="SV05.BuddyBuddyPoffin_144"):
        rig, _, _ = self.setup_field(occupied, owner, eternal=not sky)
        if sky:
            stadium = self.add(rig, fixtures.definition("XY6.SkyField_89"), owner, "hand")
            rig.board.move_card(stadium.entity_id, rig.board.find_global_area("activeStadium").entity_id)
        source = self.add(rig, fixtures.definition(path), owner, "hand")
        ctx = EffectContext(rig.session, owner, source, None)
        # Only cards inserted by this test remain in the private deck.
        for card in list(ctx.deck()):
            rig.to_area(card, owner, "hand")
        return rig, ctx, fixtures.definition(path).effect

    def add_targets(self, rig, ctx, count=3, path="SWSH9.Impidimp_92"):
        return [self.add(rig, fixtures.definition(path), ctx.player_id, "deck")
                for _ in range(count)]

    def select_first(self, ctx):
        async def search(predicate, *, count, minimum, **kwargs):
            self.assertEqual(minimum, 0)
            return [c for c in ctx.deck() if predicate is None or predicate(c)][:count]
        ctx.search_deck = AsyncMock(side_effect=search)

    async def test_poffin_and_gloria_use_expanded_slots_for_both_players(self):
        for path, requested in (("SV05.BuddyBuddyPoffin_144", 2), ("SWSH9.Gloria_141", 3)):
            for sky in (True, False):
                for owner in (P1, P2):
                    for occupied in (5, 6, 7):
                        with self.subTest(path=path, sky=sky, owner=owner, occupied=occupied):
                            rig, ctx, effect = self.setup_search(occupied, owner, sky, path)
                            targets = self.add_targets(rig, ctx)
                            self.select_first(ctx)
                            ctx.shuffle_deck = AsyncMock()
                            self.assertEqual(effective_bench_capacity(rig.board, owner), 8)
                            self.assertTrue(effect.play_condition(rig.board, owner, ctx.source))
                            await effect(ctx)
                            take = min(requested, 8 - occupied)
                            self.assertEqual(ctx.search_deck.await_args.kwargs["count"], take)
                            self.assertEqual(len(ctx.my_bench()), occupied + take)
                            self.assertTrue(all(c in ctx.my_bench() for c in targets[:take]))
                            ctx.shuffle_deck.assert_awaited_once()

    async def test_call_for_family_uses_last_sky_field_slot(self):
        rig, ctx, _ = self.setup_search(7)
        target = self.add_targets(rig, ctx, 1)[0]
        ability = next(a for a in fixtures.definition("BW4.Lapras_25").abilities
                       if a.title == "Call for Family")
        attacker = self.add(rig, fixtures.definition("BW4.Lapras_25"), P1, "hand")
        rig.to_area(ctx.my_active(), P1, "hand")
        rig.to_area(attacker, P1, "activePokemonArea")
        attack_ctx = EffectContext(rig.session, P1, attacker, ability)
        self.select_first(attack_ctx)
        await ability.effect(attack_ctx)
        self.assertEqual(attack_ctx.search_deck.await_args.kwargs["count"], 1)
        self.assertIn(target, attack_ctx.my_bench())

    async def test_full_and_reduced_bench_do_not_offer_or_select_cards(self):
        for occupied, collapsed in ((8, False), (4, True)):
            with self.subTest(occupied=occupied, collapsed=collapsed):
                rig, ctx, effect = self.setup_search(occupied)
                targets = self.add_targets(rig, ctx)
                if collapsed:
                    old = rig.board.find_global_area("activeStadium").children[0]
                    rig.to_area(old, P1, "discard")
                    stadium = self.add(rig, fixtures.definition("SWSH9.CollapsedStadium_137"), P1, "hand")
                    rig.board.move_card(stadium.entity_id, rig.board.find_global_area("activeStadium").entity_id)
                self.assertFalse(effect.play_condition(rig.board, P1, ctx.source))
                ctx.search_deck = AsyncMock(return_value=targets)
                await effect(ctx)
                ctx.search_deck.assert_not_awaited()
                self.assertTrue(all(c in ctx.deck() for c in targets))

    async def test_eternal_zone_filters_forbidden_types_without_forbidding_private_failure(self):
        rig, ctx, effect = self.setup_search(5, sky=False)
        effect = search_to_bench(count=2)
        forbidden = self.add_targets(rig, ctx, 1, "SWSH6.Kecleon_122")[0]
        # A nonempty private deck may be searched even without a legal match.
        self.assertTrue(effect.play_condition(rig.board, P1, ctx.source))
        ctx.search_deck = AsyncMock(return_value=[])
        ctx.shuffle_deck = AsyncMock()
        await effect(ctx)
        predicate = ctx.search_deck.await_args.args[0]
        self.assertFalse(predicate(forbidden))
        self.assertEqual(ctx.search_deck.await_args.kwargs["minimum"], 0)
        self.assertIn(forbidden, ctx.deck())
        self.assertEqual(len(ctx.my_bench()), 5)
        ctx.shuffle_deck.assert_awaited_once()

    async def test_empty_deck_is_not_playable_and_callback_only_gets_successful_entries(self):
        rig, ctx, _ = self.setup_search(7)
        callback = AsyncMock()
        effect = search_to_bench(count=3, then=callback)
        self.assertFalse(effect.play_condition(rig.board, P1, ctx.source))
        targets = self.add_targets(rig, ctx)
        self.select_first(ctx)
        await effect(ctx)
        callback.assert_awaited_once_with(ctx, targets[:1])
