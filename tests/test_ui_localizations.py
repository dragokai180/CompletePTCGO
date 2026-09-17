import sqlite3
import unittest
from pathlib import Path

from spirit.game.localization_overrides import (
    SET_NAME_LOCALIZATION_OVERRIDES,
    UI_LOCALIZATION_OVERRIDES,
)


ROOT = Path(__file__).resolve().parents[1]
LOCALIZATION_DB = ROOT / "spirit" / "database" / "game_data" / "LocalizationDB-UTF8.db"


class UiLocalizationTests(unittest.TestCase):
    def test_every_native_attribute_filter_has_a_label(self):
        # All 32 entries in the GX-support client's FilterAttributes enum.
        names = ('pokemon_ex legend ace full_art league foil team_plasma megaevolution '
                 'nonfoil parallelfoil specialfoil team_aqua team_magma prime hasability '
                 'haspokepower haspokebody secret hasancienttrait pokemon_gx shinypokemon '
                 'ultrabeast yellow_a prism basic_energy special_energy team tag_team '
                 'pokemon_v single_strike rapid_strike fusion_strike').split()
        with sqlite3.connect(LOCALIZATION_DB) as connection:
            known = {k.lower() for (k,) in connection.execute('SELECT key FROM Lookup')}
        known.update(UI_LOCALIZATION_OVERRIDES)
        self.assertEqual([n for n in names if 'deckbuilder.cardfilters.attributes.' + n not in known], [])

    def test_classic_collection_hidden_without_hiding_celebrations(self):
        import json
        sets = json.loads((ROOT / 'spirit/database/json_data/sets.json').read_text(encoding='utf8'))
        by_name = {s['name']: s for s in sets}
        self.assertFalse(by_name['Ann25thR']['filter'])
        self.assertFalse(by_name['Ann25thR']['visibleUnfilterable'])
        self.assertTrue(by_name['CEL25']['filter'])

    def test_custom_filter_keys_are_localized(self):
        expected = {
            "collection.filter.series.swsh": "<i>Sword & Shield</i> Series",
            "collection.filter.series.sv": "<i>Scarlet & Violet</i> Series",
            "collection.filter.series.none": "<i>Mega Evolution</i> Series",
            "deckbuilder.cardfilters.attributes.single_strike": "Single Strike",
            "deckbuilder.cardfilters.attributes.rapid_strike": "Rapid Strike",
            "deckbuilder.cardfilters.attributes.fusion_strike": "Fusion Strike",
        }
        self.assertEqual(
            {key: UI_LOCALIZATION_OVERRIDES.get(key) for key in expected},
            expected,
        )

    def test_every_visible_set_series_has_a_label(self):
        # RSP uses its dedicated set-name label instead of the series template.
        client_special_series = {"rsp"}
        with sqlite3.connect(LOCALIZATION_DB) as connection:
            database_keys = {
                key.lower()
                for (key,) in connection.execute("SELECT key FROM Lookup")
            }

        import json

        sets = json.loads(
            (ROOT / "spirit" / "database" / "json_data" / "sets.json")
            .read_text(encoding="utf-8")
        )
        blocks = {str(item.get("block", "")).lower() for item in sets if item.get("filter")}
        missing = {
            block
            for block in blocks - client_special_series
            if f"collection.filter.series.{block}" not in database_keys
            and f"collection.filter.series.{block}" not in UI_LOCALIZATION_OVERRIDES
        }
        self.assertEqual(missing, set())

    def test_every_visible_set_has_a_name(self):
        with sqlite3.connect(LOCALIZATION_DB) as connection:
            database_keys = {
                key.lower()
                for (key,) in connection.execute("SELECT key FROM Lookup")
            }

        import json

        sets = json.loads(
            (ROOT / "spirit" / "database" / "json_data" / "sets.json")
            .read_text(encoding="utf-8")
        )
        missing = {
            item["name"]
            for item in sets
            if item.get("filter")
            and f"set.name.{item['name'].lower()}" not in database_keys
            and f"set.name.{item['name'].lower()}"
            not in SET_NAME_LOCALIZATION_OVERRIDES
        }
        self.assertEqual(missing, set())


if __name__ == "__main__":
    unittest.main()
