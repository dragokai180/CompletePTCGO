"""Eternal Zone forbids the owner's non-Darkness entries, not just extra slots."""
import unittest
from unittest.mock import AsyncMock, patch

from tests import test_chromashift_eternal_zone as helpers
from tests import test_hgss_rules as fixtures
from spirit.game.attributes import PokemonTypes
from spirit.game.session.effects import EffectContext
from spirit.game.session.legal_actions import compute_legal_actions
from spirit.game.session.passives import effective_bench_capacity, pokemon_entry_blocked
from spirit.game.card_effects.standard_era import _generic_search
from spirit.tools.effect_smoke import P1, P2


class EternalZoneEntryTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add
    setup_field = helpers.ChromashiftEternalZoneTests.setup_field
    attach_basic = helpers.ChromashiftEternalZoneTests.attach_basic

    def active_zone(self, path=helpers.PRINTS[0], owner=P1):
        rig, kecleon, ctx = self.setup_field(path, owner)
        self.attach_basic(rig, kecleon)
        rig.session.turn_state.active_player_id = owner
        return rig, kecleon, ctx

    def offered(self, rig, owner, card):
        return any(e['entityID'] == card.entity_id for e in compute_legal_actions(
            rig.board, rig.session.turn_state, owner, rig.session.game_id))

    async def test_non_darkness_hand_play_is_not_offered_for_any_print_or_owner(self):
        for path in helpers.PRINTS:
            for owner in (P1, P2):
                with self.subTest(path=path, owner=owner):
                    rig, _, ctx = self.active_zone(path, owner)
                    blocked = self.add(rig, fixtures.definition('SWSH6.Kecleon_122'), owner, 'hand')
                    allowed = self.add(rig, fixtures.definition('SWSH3.EternatusV_116'), owner, 'hand')
                    self.assertFalse(self.offered(rig, owner, blocked))
                    self.assertTrue(self.offered(rig, owner, allowed))
                    with patch.object(rig.session, 'fire_pokemon_benched_triggers', AsyncMock()) as trigger:
                        await rig.session._execute_play_basic(owner, blocked)
                    self.assertIn(blocked, ctx.hand())
                    trigger.assert_not_awaited()

    async def test_effect_entry_is_blocked_from_hand_deck_and_discard(self):
        for zone in ('hand', 'deck', 'discard'):
            with self.subTest(zone=zone):
                rig, _, ctx = self.active_zone()
                card = self.add(rig, fixtures.definition('SWSH6.Kecleon_122'), P1, zone)
                old_parent = card.parent
                self.assertFalse(ctx.can_bench_pokemon(card))
                self.assertFalse(await ctx.bench_pokemon(card))
                self.assertIs(card.parent, old_parent)
                dark = self.add(rig, fixtures.definition('SWSH3.EternatusV_116'), P1, zone)
                self.assertTrue(await ctx.bench_pokemon(dark))
                self.assertIn(dark, ctx.my_bench())

    async def test_non_darkness_evolution_is_hidden_and_rejected_without_mutation(self):
        rig, _, ctx = self.active_zone()
        basic = self.add(rig, fixtures.definition('SWSH2.Koffing_112'), P1, 'bench')
        evolution = self.add(rig, fixtures.definition('SM10.Weezing_74'), P1, 'hand')
        rig.session.turn_state.turn_number = 5
        self.assertFalse(self.offered(rig, P1, evolution))
        parent = basic.parent
        for zone in ('hand', 'deck', 'discard'):
            rig.to_area(evolution, P1, zone)
            self.assertFalse(await ctx.evolve_pokemon(basic, evolution))
            self.assertIs(basic.parent, parent)
            self.assertIs(evolution.parent, rig.board.find_player_area(P1, zone))

    async def test_identity_swap_cannot_bypass_entry_restriction(self):
        rig, _, ctx = self.active_zone()
        incoming = self.add(rig, fixtures.definition('SWSH6.Kecleon_122'), P1, 'discard')
        outgoing = ctx.my_active()
        self.assertIsNone(await rig.session.perform_identity_swap(outgoing, incoming, ctx=ctx))
        self.assertIs(ctx.my_active(), outgoing)
        self.assertIn(incoming, ctx.discard_pile())

    async def test_suppression_and_existing_non_darkness_disable_restriction(self):
        rig, _, ctx = self.active_zone()
        card = self.add(rig, fixtures.definition('SWSH6.Kecleon_122'), P1, 'hand')
        self.assertTrue(pokemon_entry_blocked(rig.board, P1, card))
        rig.session.turn_state.abilities_disabled_through_turn = rig.session.turn_state.turn_number
        self.assertFalse(pokemon_entry_blocked(rig.board, P1, card))
        self.assertTrue(self.offered(rig, P1, card))
        rig.session.turn_state.abilities_disabled_through_turn = -1
        self.assertTrue(pokemon_entry_blocked(rig.board, P1, card))
        # A pre-existing non-Darkness Pokemon turns the entire condition off.
        rig.to_area(card, P1, 'bench')
        second = self.add(rig, fixtures.definition('SWSH6.Kecleon_122'), P1, 'hand')
        self.assertFalse(pokemon_entry_blocked(rig.board, P1, second))
        self.assertTrue(self.offered(rig, P1, second))
        self.assertEqual(effective_bench_capacity(rig.board, P1), 5)

    async def test_opponents_own_plays_and_in_play_movement_are_not_blocked(self):
        rig, kecleon, ctx = self.active_zone()
        other = self.add(rig, fixtures.definition('SWSH6.Kecleon_122'), P2, 'hand')
        opposing = EffectContext(rig.session, P2, rig.board.active_pokemon(P2), None)
        self.assertFalse(pokemon_entry_blocked(rig.board, P2, other))
        self.assertTrue(await opposing.bench_pokemon(other))
        self.assertFalse(pokemon_entry_blocked(rig.board, P1, kecleon))
        await ctx.switch_active(P1, kecleon)
        self.assertIs(ctx.my_active(), kecleon)
        self.assertEqual(effective_bench_capacity(rig.board, P1), 8)

    async def test_private_bench_search_filters_targets_but_still_allows_failure(self):
        rig, _, ctx = self.active_zone()
        blocked = self.add(rig, fixtures.definition('SWSH6.Kecleon_122'), P1, 'deck')
        allowed = self.add(rig, fixtures.definition('SWSH3.EternatusV_116'), P1, 'deck')
        ctx.choose_cards = AsyncMock(return_value=[])
        await _generic_search(ctx, 'search your deck for a basic pokémon and put it onto your bench. then shuffle your deck.')
        args, kwargs = ctx.choose_cards.call_args
        self.assertNotIn(blocked, args[0])
        self.assertIn(allowed, args[0])
        self.assertIn(blocked, kwargs['display_cards'])
        self.assertEqual(kwargs['minimum'], 0)
        self.assertIn(allowed, ctx.deck())


if __name__ == '__main__':
    unittest.main()
