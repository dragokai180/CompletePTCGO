import unittest
from types import SimpleNamespace
from unittest.mock import patch

from spirit.game.session import legal_actions


class _Card:
    def __init__(self, archetype_id, name=""):
        self.archetype_id = archetype_id
        self._name = name

    def get_attribute(self, _attribute):
        return self._name


class StadiumNameLegalityTests(unittest.TestCase):
    def _board(self, *cards):
        area = SimpleNamespace(children=list(cards))
        return SimpleNamespace(find_global_area=lambda _name: area)

    def test_same_name_reprint_cannot_replace_stadium(self):
        current = _Card("stadium-print-a")
        incoming = _Card("stadium-print-b")
        definitions = {
            "stadium-print-a": SimpleNamespace(display_name="Training Court"),
            "stadium-print-b": SimpleNamespace(display_name=" training  court "),
        }

        with patch.object(
            legal_actions, "def_for", side_effect=lambda key: definitions.get(key)
        ):
            self.assertTrue(
                legal_actions.same_stadium_in_play(self._board(current), incoming)
            )

    def test_different_stadium_name_can_replace_current_stadium(self):
        current = _Card("stadium-print-a")
        incoming = _Card("stadium-print-b")
        definitions = {
            "stadium-print-a": SimpleNamespace(display_name="Training Court"),
            "stadium-print-b": SimpleNamespace(display_name="Skyarrow Bridge"),
        }

        with patch.object(
            legal_actions, "def_for", side_effect=lambda key: definitions.get(key)
        ):
            self.assertFalse(
                legal_actions.same_stadium_in_play(self._board(current), incoming)
            )

    def test_directional_stadium_can_replace_same_name_to_change_orientation(self):
        current = _Card("parallel-city-a")
        incoming = _Card("parallel-city-b")
        definitions = {
            "parallel-city-a": SimpleNamespace(display_name="Parallel City"),
            "parallel-city-b": SimpleNamespace(
                display_name="Parallel City",
                allows_same_name_replacement=True,
            ),
        }

        with patch.object(
            legal_actions, "def_for", side_effect=lambda key: definitions.get(key)
        ):
            self.assertFalse(
                legal_actions.same_stadium_in_play(self._board(current), incoming)
            )


if __name__ == "__main__":
    unittest.main()
