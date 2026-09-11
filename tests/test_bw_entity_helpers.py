import unittest

from spirit.game.attributes import AttrID
from spirit.game.card_effects.bw_era import _BWTextPassive, _pokemon_in_play_from
from spirit.game.models.board import BoardEntity, BoardState, PokemonEntity


def _bare_pokemon(player_id: str) -> PokemonEntity:
    pokemon = object.__new__(PokemonEntity)
    BoardEntity.__init__(pokemon, owning_player_id=player_id)
    return pokemon


class BwEntityHelperTests(unittest.TestCase):
    def test_in_play_lookup_ignores_attached_evolution_name_objects(self):
        board = BoardState("test-game", ["p1", "p2"])
        active_area = board.find_player_area("p1", "activePokemonArea")

        active = _bare_pokemon("p1")
        previous_stage = _bare_pokemon("p1")
        # Card names arrive as localized JSON objects.  The old raw-tree scan
        # reached ``previous_stage``, then tried to hash its parent's value.
        active.set_attribute(AttrID.NAME, {"id": "Servine"})
        active.add_child(previous_stage)
        active_area.add_child(active)

        self.assertEqual(_pokemon_in_play_from(previous_stage, "p1"), [active])

        # Legal-action calculation calls every in-play text passive after a
        # promotion.  This is the exact path that formerly ended the match.
        passive = _BWTextPassive("This Pokémon has no additional effect.")
        self.assertFalse(passive.blocks_attacks(active, active))


if __name__ == "__main__":
    unittest.main()
