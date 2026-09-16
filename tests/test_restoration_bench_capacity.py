"""Restoration uses the live Bench capacity, not the standard five slots."""
import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures
from spirit.game.attributes import PokemonTypes
from spirit.game.data_utils import CARD_DEFS_BY_GUID
from spirit.game.card_effects.support_common import requires_bench_space
from spirit.game.session.effects import EffectContext
from spirit.game.session.legal_actions import _out_of_zone_ability_entries
from spirit.game.session.passives import effective_bench_capacity
from spirit.tools.effect_smoke import P1, P2

PRINTS = ("SM3.DarkraiGX_88", "SM3.DarkraiGX_139", "SM3.DarkraiGX_158",
          "SM3.DarkraiGX_172", "HF.DarkraiGX_170")


class RestorationBenchCapacityTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    def setup_field(self, count, owner=P1, path=PRINTS[0], eternal=True):
        rig, _ = self.rig(path)
        for pid in (P1, P2):
            for pokemon in list(rig.board.pokemon_in_play(pid)):
                rig.to_area(pokemon, pid, "hand")
            # The smoke fixture seeds several discard Energies. This case
            # supplies its own single eligible Energy to make the pick exact.
            for card in list(rig.board.find_player_area(pid, "discard").children):
                rig.to_area(card, pid, "hand")
        self.add(rig, fixtures.definition(
            "SWSH3.EternatusVMAX_117" if eternal else PRINTS[0]),
            owner, "activePokemonArea")
        opponent = P2 if owner == P1 else P1
        self.add(rig, self.filler, opponent, "activePokemonArea")
        for _ in range(count):
            existing = self.add(rig, fixtures.definition(path), owner, "bench")
            power = next(a for a in fixtures.definition(path).abilities if a.title == "Restoration")
            rig.session.turn_state.used_abilities.add((existing.entity_id, power.ability_id))
        source = self.add(rig, fixtures.definition(path), owner, "discard")
        power = next(a for a in fixtures.definition(path).abilities if a.title == "Restoration")
        rig.session.turn_state.active_player_id = owner
        rig.session.turn_state.turn_number = 4
        return rig, source, power

    def offered(self, rig, owner, source):
        return any(e["entityID"] == source.entity_id for e in
                   _out_of_zone_ability_entries(rig.board, rig.session.turn_state,
                                               owner, rig.session.game_id))

    def test_all_prints_and_owners_can_restore_with_five_to_seven_benched(self):
        for path in PRINTS:
            for owner in (P1, P2):
                for count in (5, 6, 7):
                    with self.subTest(path=path, owner=owner, count=count):
                        rig, source, power = self.setup_field(count, owner, path)
                        self.assertEqual(effective_bench_capacity(rig.board, owner), 8)
                        self.assertTrue(power.condition(rig.board, owner, source))
                        self.assertTrue(self.offered(rig, owner, source))
                        self.assertEqual(requires_bench_space(2)(rig.board, owner), count <= 6)

    async def test_restoration_enters_eighth_slot_and_attaches_to_the_new_copy(self):
        for owner in (P1, P2):
            with self.subTest(owner=owner):
                rig, source, power = self.setup_field(7, owner)
                energy = self.add(rig, CARD_DEFS_BY_GUID[
                    self.energies[PokemonTypes.DARKNESS.value].lower()], owner, "discard")
                ctx = EffectContext(rig.session, owner, source, power)
                ctx.ask_yes_no = AsyncMock(return_value=True)
                self.assertTrue(self.offered(rig, owner, source))
                await power.effect(ctx)
                self.assertIn(source, ctx.my_bench())
                self.assertEqual(len(ctx.my_bench()), 8)
                self.assertIs(energy.parent, source)
                self.assertNotIn(source, ctx.discard_pile())
                self.assertFalse(ctx.ends_turn)

    async def test_eight_slots_full_blocks_menu_and_stale_entry(self):
        rig, source, power = self.setup_field(8)
        self.assertFalse(self.offered(rig, P1, source))
        ctx = EffectContext(rig.session, P1, source, power)
        self.assertFalse(await ctx.bench_pokemon(source))
        self.assertIn(source, ctx.discard_pile())

    def test_normal_bench_and_other_copy_usage_remain_independent(self):
        for count, expected in ((1, True), (4, True), (5, False)):
            with self.subTest(count=count):
                rig, source, _ = self.setup_field(count, eternal=False)
                self.assertEqual(effective_bench_capacity(rig.board, P1), 5)
                self.assertEqual(self.offered(rig, P1, source), expected)

    def test_capacity_rechecks_ability_suppression_and_reduced_bench(self):
        rig, source, _ = self.setup_field(5)
        self.assertTrue(self.offered(rig, P1, source))
        state = rig.session.turn_state
        state.abilities_disabled_through_turn = state.turn_number
        self.assertFalse(requires_bench_space()(rig.board, P1))
        state.abilities_disabled_through_turn = -1
        self.assertTrue(self.offered(rig, P1, source))
        rig, source, _ = self.setup_field(4)
        stadium = self.add(rig, fixtures.definition("SWSH9.CollapsedStadium_137"), P1, "hand")
        rig.board.move_card(stadium.entity_id, rig.board.find_global_area("activeStadium").entity_id)
        self.assertEqual(effective_bench_capacity(rig.board, P1), 4)
        self.assertFalse(self.offered(rig, P1, source))
        rig.to_area(stadium, P1, "discard")
        self.assertTrue(self.offered(rig, P1, source))
