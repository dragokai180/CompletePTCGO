import unittest
from pathlib import Path

from spirit.tools.install_recent_card_art import (
    RECENT_SETS,
    collector_number_from_script,
    image_url,
    mega_promo_url,
    selected_sets,
)


class InstallRecentCardArtTests(unittest.TestCase):
    def test_mega_era_contains_main_sets_and_promos(self):
        selected = selected_sets(["mega"])
        self.assertEqual(
            [card_set.set_code for card_set in selected],
            ["ME1", "ME2", "ME2PT5", "ME3", "ME4", "ME5", "MEP"],
        )

    def test_script_filename_preserves_collector_number(self):
        self.assertEqual(
            collector_number_from_script(Path("AcerolasMischief_183.py")),
            "183",
        )

    def test_mega_promo_uses_english_limitless_archive(self):
        self.assertEqual(
            mega_promo_url("3"),
            "https://limitlesstcg.nyc3.cdn.digitaloceanspaces.com/"
            "tpci/MEP/MEP_003_R_EN.png",
        )

    def test_bundled_metadata_url_wins(self):
        card_set = RECENT_SETS["me2pt5"]
        self.assertEqual(
            image_url(card_set, "1", {"1": "https://example.test/card.png"}),
            "https://example.test/card.png",
        )

    def test_unknown_selection_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "Unknown era or set"):
            selected_sets(["not-a-set"])


if __name__ == "__main__":
    unittest.main()
