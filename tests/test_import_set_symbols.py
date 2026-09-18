import json
import unittest
from pathlib import Path

from PIL import Image

from spirit.tools.import_set_symbols import OUTPUT_DIR, SYMBOL_SLUGS, SYMBOL_URLS, symbol_url


PROJECT_DIR = Path(__file__).resolve().parents[1]


class ImportSetSymbolsTests(unittest.TestCase):
    def test_every_symbol_target_matches_set_data(self):
        sets = json.loads(
            (PROJECT_DIR / "spirit" / "database" / "json_data" / "sets.json")
            .read_text(encoding="utf-8")
        )
        set_names = {item["name"].lower() for item in sets}
        self.assertEqual(set(), set(SYMBOL_URLS) - set_names)

    def test_mee_uses_its_own_symbol(self):
        self.assertEqual(SYMBOL_URLS["mee"],
                         "https://images.scrydex.com/pokemon/mee-symbol/symbol")

    def test_source_urls_are_png_urls(self):
        for slug in SYMBOL_SLUGS.values():
            self.assertEqual(
                symbol_url(slug),
                f"https://pokesymbols.com/images/tcg/sets/symbols/{slug}.png",
            )

    def test_imported_symbols_are_valid_rgba_pngs(self):
        missing = []
        for texture_name in SYMBOL_URLS:
            path = OUTPUT_DIR / f"{texture_name}.png"
            if not path.is_file():
                missing.append(texture_name)
                continue
            with Image.open(path) as image:
                self.assertEqual(image.format, "PNG", texture_name)
                self.assertEqual(image.mode, "RGBA", texture_name)
                self.assertEqual(image.width, image.height, texture_name)
        self.assertEqual(missing, [])


if __name__ == "__main__":
    unittest.main()
