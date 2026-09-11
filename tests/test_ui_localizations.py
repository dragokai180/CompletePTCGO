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
