"""Draw-only Trainers must change the hand, using public information only."""
import unittest
from types import SimpleNamespace
from unittest.mock import Mock, patch

from tests.test_hgss_rules import definition
from spirit.game.session.legal_actions import trainer_condition_met
from spirit.game.card_effects.support_common import draw_until_condition


class TrainerDrawPermissionTests(unittest.TestCase):
    def board(self, count, deck=1):
        source = object()
        hand = SimpleNamespace(children=[source] + [object() for _ in range(count - 1)])
        areas = {"hand": hand, "deck": SimpleNamespace(children=[object()] * deck)}
        board = SimpleNamespace(
            find_player_area=lambda pid, zone: areas.get(zone),
            player_ids=["me", "them"],
            turn_state=SimpleNamespace(pokemon_lost_last_turn=Mock(return_value=[])),
            pokemon_in_play=Mock(return_value=[]),
        )
        return board, source, areas

    def test_bicycle_bianca_and_existing_korrina_boundaries(self):
        for path, limit in (
            ("BW8.Bicycle_117", 4), ("BW2.Bianca_90", 6),
            ("BW7.Bianca_147", 6), ("BW11.Bianca_109", 6),
            ("SWSH5.KorrinasFocus_128", 6),
        ):
            condition = definition(path).condition
            self.assertIsNotNone(condition, path)
            for count in (1, limit, limit + 1, limit + 4):
                with self.subTest(path=path, count=count):
                    board, source, areas = self.board(count)
                    self.assertEqual(trainer_condition_met(condition, board, "me", source), count <= limit)
                    areas["deck"].children.clear()
                    self.assertFalse(trainer_condition_met(condition, board, "me", source))

    def test_source_already_out_of_hand_is_not_subtracted_twice(self):
        board, source, areas = self.board(5)
        areas["hand"].children.remove(source)
        self.assertFalse(draw_until_condition(4)(board, "me", source))

    def test_cynthia_uses_last_turn_history(self):
        for number in (138, 169, 178):
            condition = definition(f"SWSH9.CynthiasAmbition_{number}").condition
            for count in (5, 6, 8, 9):
                board, source, areas = self.board(count)
                self.assertEqual(trainer_condition_met(condition, board, "me", source), count <= 5)
                board.turn_state.pokemon_lost_last_turn.return_value = ["knocked-out"]
                self.assertEqual(trainer_condition_met(condition, board, "me", source), count <= 8)
                areas["deck"].children.clear()
                self.assertFalse(trainer_condition_met(condition, board, "me", source))

    def test_ariana_requires_all_pokemon_for_higher_limit(self):
        condition = definition("SV10.TeamRocketsAriana_171").condition
        board, source, areas = self.board(8)
        board.pokemon_in_play.return_value = [SimpleNamespace(archetype_id="rocket")]
        with patch("spirit.game.card_effects.trainer_draw_permissions.def_for",
                   return_value=SimpleNamespace(display_name="Team Rocket's Mewtwo ex")) as lookup:
            self.assertTrue(trainer_condition_met(condition, board, "me", source))
            lookup.return_value.display_name = "Mewtwo ex"
            self.assertFalse(trainer_condition_met(condition, board, "me", source))
        board.pokemon_in_play.return_value = []
        self.assertFalse(trainer_condition_met(condition, board, "me", source))

    def test_honey_requires_opposing_benched_v_and_drawable_card(self):
        for number in (142, 192):
            condition = definition(f"SWSH6.Honey_{number}").condition
            board, source, areas = self.board(1)
            with patch("spirit.game.card_effects.trainer_draw_permissions._bench_pokemon",
                       return_value=[]) as bench, \
                 patch("spirit.game.card_effects.trainer_draw_permissions.is_pokemon_v",
                       return_value=True) as is_v:
                self.assertFalse(trainer_condition_met(condition, board, "me", source))
                bench.return_value = [SimpleNamespace(archetype_id="v")]
                self.assertTrue(trainer_condition_met(condition, board, "me", source))
                bench.assert_called_with(board, "them")
                is_v.return_value = False
                self.assertFalse(trainer_condition_met(condition, board, "me", source))
                is_v.return_value = True
                areas["deck"].children.clear()
                self.assertFalse(trainer_condition_met(condition, board, "me", source))

    def test_cheren_requires_nonempty_deck(self):
        for path in ("BW2.Cheren_91", "BW5.Cheren_91", "BW7.Cheren_148"):
            condition = definition(path).condition
            self.assertIsNotNone(condition)
            board, source, areas = self.board(8)
            self.assertTrue(trainer_condition_met(condition, board, "me", source))
            areas["deck"].children.clear()
            self.assertFalse(trainer_condition_met(condition, board, "me", source))


if __name__ == "__main__":
    unittest.main()
