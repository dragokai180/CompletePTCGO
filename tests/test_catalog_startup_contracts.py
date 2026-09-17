"""Startup, artwork identity and printed source-zone regression contracts."""
import unittest
from contextlib import ExitStack
from pathlib import Path
from unittest.mock import patch

from spirit.game.attributes import AttrID
from spirit.game.card_effects.standard_era import standard_ability_source_zone
from spirit.game.data_utils import ABILITIES_BY_ID, CARD_DEFS_BY_GUID, def_for, prize_value
from spirit.game.scripts.cards import loader
from spirit.game.session.legal_actions import _ability_entries, _out_of_zone_ability_entries
from spirit.tools.effect_smoke import P1
from tests import test_hgss_rules as fixtures
from tests.test_hgss_rules import definition


class CatalogStartupTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx

    def test_entire_catalog_has_unique_art_and_collector_slots(self):
        for attr in (AttrID.IMAGE_URL, AttrID.COLLECTOR_NUMBER):
            seen = {}
            for model in loader.cards:
                key = (model.key, model.get_attribute_value(attr))
                self.assertNotIn(key, seen, (key, seen.get(key), loader.script_by_guid[model.guid]))
                seen[key] = loader.script_by_guid[model.guid]

    def test_tepig_and_radiant_meloetta_are_not_the_same_print(self):
        tepig = definition("BW11.Tepig_25")
        meloetta = definition("BW11.MeloettaEX_RC25")
        self.assertEqual(tepig.extra_attributes[str(AttrID.HP.value)]["value"], 70)
        self.assertEqual(prize_value(tepig.guid), 1)
        self.assertEqual(prize_value(meloetta.guid), 2)
        self.assertEqual(meloetta.collector_number, 140)
        self.assertEqual(loader.cards_by_guid[meloetta.guid].get_attribute_value(AttrID.CARD_NUMBER_TEXT), "RC25")
        for card, image in ((tepig, "025"), (meloetta, "140")):
            model = loader.cards_by_guid[card.guid]
            self.assertEqual(model.get_attribute_value(AttrID.IMAGE_URL), image)
            self.assertEqual(model.to_archetype_attributes("BW11")[str(AttrID.IMAGE_URL.value)]["value"], image)

    def test_bundling_does_not_reregister_any_rules(self):
        from spirit.server import auto_bundle
        before_defs = dict(CARD_DEFS_BY_GUID)
        before_abilities = dict(ABILITIES_BY_ID)
        captured = {}
        def capture(code, mapping):
            captured[code] = mapping
            return 0
        with ExitStack() as stack:
            for target in ("compile_all_cosmetics", "dynamic_pages.compile_custom_landing_bundle",
                           "generate_energy_pip_png", "generate_tool_pip_png",
                           "prune_obsolete_foil_bundles"):
                stack.enter_context(patch("spirit.server.auto_bundle." + target, return_value=None))
            stack.enter_context(patch.object(auto_bundle, "generate_foil_bundles", return_value=0))
            stack.enter_context(patch.object(auto_bundle, "self_generate_set_bundle", side_effect=capture))
            self.assertEqual(auto_bundle.check_and_generate_bundles(), 0)
        self.assertEqual(before_defs, CARD_DEFS_BY_GUID)
        self.assertEqual(before_abilities, ABILITIES_BY_ID)
        self.assertTrue(captured["BW11"]["025"].endswith("Tepig_25.png"))
        self.assertTrue(captured["BW11"]["140"].endswith("MeloettaEX_RC25.png"))
        for number in range(1, 26):
            self.assertTrue(captured["BW11"][str(115 + number)].endswith("_RC" + str(number) + ".png"))

    async def test_mystical_fire_only_from_play_and_draws_to_six(self):
        rig, entities, ctx = self.ctx("XY1.Delphox_26", "Mystical Fire")
        source = entities["target"]
        for card in list(ctx.hand())[3:]:
            rig.to_area(card, P1, "deck")
        for zone in ("hand", "discard", "deck"):
            rig.to_area(source, P1, zone)
            offers = _out_of_zone_ability_entries(rig.board, rig.session.turn_state, P1, rig.session.game_id)
            self.assertNotIn(ctx.ability.ability_id, str(offers), zone)
        rig.to_area(source, P1, "bench")
        offers = _ability_entries(rig.board, rig.session.turn_state, P1, rig.session.game_id, [source])
        self.assertIn(ctx.ability.ability_id, str(offers))
        before = len(ctx.deck())
        hand_before = len(ctx.hand())
        await ctx.ability.effect(ctx)
        self.assertEqual(len(ctx.hand()), 6)
        self.assertEqual(len(ctx.deck()), before - (6 - hand_before))
        self.assertNotIn(ctx.ability.ability_id, str(_ability_entries(
            rig.board, rig.session.turn_state, P1, rig.session.game_id, [source])))

    def test_explicit_hand_and_discard_powers_keep_their_zones(self):
        for path, zone in (
            ("Promo_SM.GreninjaGX_197", "hand"), ("SWSH4.Beedrill_3", "hand"),
            ("SWSH8.Pyukumuku_77", "hand"), ("SM8.Trumbeak_165", "hand"),
            ("SV07.Klinklang_101", "hand"), ("SM3.DarkraiGX_88", "discard"),
            ("BW9.Exeggcute_4", "discard"), ("SWSH9.Empoleon_37", "discard"),
        ):
            with self.subTest(path=path):
                ability = definition(path).abilities[0]
                self.assertEqual(ability.usable_from, zone)

    def test_importer_does_not_infer_source_from_cost_or_destination(self):
        from spirit.tools.import_standard_sets import trigger_expr
        for text in (
            "Once during your turn, you may draw cards until you have 6 cards in your hand.",
            "This Pokémon can use the attacks of Basic Pokémon in your discard pile.",
            "Once during your turn, discard an Energy card from your hand. Draw 2 cards.",
        ):
            self.assertIsNone(trigger_expr(text)[2])
        self.assertEqual(trigger_expr("Once during your turn, if this Pokémon is the last card in your hand, you may play it onto your Bench.")[2], "hand")

    def test_importer_preserves_rule_boxes_and_multiple_weaknesses(self):
        import ast
        from spirit.tools.import_standard_sets import render_pokemon
        for rule, required in (("Mega Evolution ex Rule", {"ex", "SV_Mega"}),
                               ("Pokémon ex rule", {"ex"}),
                               ("Pokémon-GX rule", {"GX"})):
            raw = dict(name="Example", number="1", hp="100", rules=[rule],
                       subtypes=["Basic"], weaknesses=[dict(type="Water", value="x2"),
                                                       dict(type="Fighting", value="x2")])
            tree = ast.parse(render_pokemon(raw, "AUDIT", {}))
            call = tree.body[-1].value
            keywords = {entry.arg: entry.value for entry in call.keywords}
            self.assertTrue(required.issubset(ast.literal_eval(keywords["subtypes"])))
            self.assertEqual(len(keywords["weakness_types"].elts), 2)
