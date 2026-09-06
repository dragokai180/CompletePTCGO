import ast
import re
import unittest
from pathlib import Path

from spirit.game.text_encoding import (
    ascii_fold,
    client_localization_value,
    fix_mojibake,
    with_ascii_aliases,
)


CARDS_ROOT = Path(__file__).resolve().parents[1] / "spirit" / "game" / "scripts" / "cards"
_DISPLAY_NAME = re.compile(r"display_name\s*=\s*(\".*?\"|'.*?')")

# Every scripted card whose printed name includes Poké / Pokémon.
POKE_NAMED_CARDS = {
    "CZ/PokBall_137.py": "Poké Ball",
    "CZ/PokemonCatcher_138.py": "Pokémon Catcher",
    "ME2PT5/PokPad_198.py": "Poké Pad",
    "ME3/PokemonCatcher_82.py": "Pokémon Catcher",
    "PGO/PokStop_68.py": "PokéStop",
    "SV1/Pokgear30_186.py": "Pokégear 3.0",
    "SWSH1/PokKid_173.py": "Poké Kid",
    "SWSH1/PokemonCatcher_175.py": "Pokémon Catcher",
    "SWSH1/PokemonCenterLady_176.py": "Pokémon Center Lady",
    "SWSH1/Pokgear30_174.py": "Pokégear 3.0",
    "SWSH2/PokBall_164.py": "Poké Ball",
    "SWSH3/PokemonBreedersNurturing_166.py": "Pokémon Breeder's Nurturing",
    "SWSH3/PokemonBreedersNurturing_188.py": "Pokémon Breeder's Nurturing",
    "SWSH3/PokemonBreedersNurturing_195.py": "Pokémon Breeder's Nurturing",
    "SWSH35/PokBall_59.py": "Poké Ball",
    "SWSH35/PokemonCenterLady_60.py": "Pokémon Center Lady",
    "SWSH4/PokemonCenterLady_185.py": "Pokémon Center Lady",
    "SWSH45/PokKid_70.py": "Poké Kid",
}


def _display_name(path: Path) -> str:
    match = _DISPLAY_NAME.search(path.read_text(encoding="utf-8"))
    if not match:
        raise AssertionError(f"no display_name in {path}")
    return ast.literal_eval(match.group(1))


class FixMojibakeTests(unittest.TestCase):
    def test_repairs_cp1252_pokemon(self):
        mojibake = "Pok\u00c3\u00a9mon Catcher"
        self.assertEqual(fix_mojibake(mojibake), "Pokémon Catcher")

    def test_leaves_correct_utf8_alone(self):
        self.assertEqual(fix_mojibake("Pokémon Catcher"), "Pokémon Catcher")
        self.assertEqual(fix_mojibake("Poké Ball"), "Poké Ball")

    def test_client_keeps_accent(self):
        self.assertEqual(client_localization_value("Pokémon Catcher"), "Pokémon Catcher")
        self.assertEqual(client_localization_value("Poké Ball"), "Poké Ball")
        self.assertEqual(client_localization_value("Pok\u00c3\u00a9mon Catcher"), "Pokémon Catcher")
        self.assertEqual(client_localization_value("Flabébé"), "Flabébé")
        self.assertEqual(client_localization_value("Café Master"), "Café Master")
        self.assertIn("é", client_localization_value("Pokémon Catcher"))

    def test_ascii_fold_is_import_alias_only(self):
        self.assertEqual(ascii_fold("Pokémon Catcher"), "Pokemon Catcher")
        self.assertEqual(ascii_fold("Poké Ball"), "Poke Ball")
        self.assertEqual(
            with_ascii_aliases(["Pokémon Catcher", "Item"]),
            ["Pokémon Catcher", "Pokemon Catcher", "Item"],
        )


class PokeNamedCardScriptsTests(unittest.TestCase):
    def test_every_poke_named_card_uses_real_accent(self):
        for rel, expected in POKE_NAMED_CARDS.items():
            path = CARDS_ROOT / rel
            name = _display_name(path)
            self.assertEqual(name, expected, rel)
            self.assertNotIn("\u00c3", name, rel)
            self.assertIn("é", name, rel)

    def test_no_card_script_contains_mojibake_accent(self):
        offenders = []
        for path in CARDS_ROOT.rglob("*.py"):
            text = path.read_text(encoding="utf-8")
            if "\u00c3\u00a9" in text or "\\u00c3\\u00a9" in text:
                offenders.append(str(path.relative_to(CARDS_ROOT)))
        self.assertEqual(offenders, [])


if __name__ == "__main__":
    unittest.main()
