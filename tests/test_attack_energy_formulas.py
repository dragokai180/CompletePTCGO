import unittest
from types import SimpleNamespace
from unittest.mock import patch

from spirit.game.attributes import PokemonTypes
from spirit.game.card_effects.bw_era import _formula_damage


class _Energy:
    def __init__(self, name, *provided):
        self.name = name
        self.provided = list(provided)


class _Pokemon:
    def __init__(self, *energies, name="Pokémon", counters=0, tools=None):
        self.energies = list(energies)
        self.name = name
        self.counters = counters
        self.tools = list(tools or [])


class _FormulaContext:
    def __init__(self, printed, mine, opponent):
        self.ability = SimpleNamespace(damage=printed)
        self.attacker = mine[0]
        self.defender = opponent[0]
        self.board = object()
        self._mine = mine
        self._opponent = opponent

    def attached_energies(self, pokemon):
        return pokemon.energies

    def my_pokemon_in_play(self):
        return self._mine

    def opponent_pokemon_in_play(self):
        return self._opponent

    def my_bench(self):
        return self._mine[1:]


def _options(_board, energy):
    return [energy.provided]


class AttackEnergyFormulaTests(unittest.TestCase):
    def setUp(self):
        self.darkness = PokemonTypes.DARKNESS.value
        self.fire = PokemonTypes.FIRE.value
        self.lightning = PokemonTypes.LIGHTNING.value
        self.colorless = PokemonTypes.COLORLESS.value

    def _ctx(self, printed=20):
        mine = [
            _Pokemon(_Energy("Darkness Energy", self.darkness),
                     _Energy("Fire Energy", self.fire)),
            _Pokemon(_Energy("Darkness Energy", self.darkness)),
        ]
        opponent = [
            _Pokemon(_Energy("Lightning Energy", self.lightning)),
            _Pokemon(_Energy("Double Colorless Energy",
                            self.colorless, self.colorless)),
        ]
        return _FormulaContext(printed, mine, opponent)

    @patch("spirit.game.card_effects.bw_era.energy_provided_options", _options)
    def test_dark_pulse_counts_only_darkness_energy_across_own_field(self):
        text = (
            "this attack does 20 more damage for each darkness energy "
            "attached to all of your pokémon."
        )
        self.assertEqual(_formula_damage(self._ctx(20), text), 60)

    @patch("spirit.game.card_effects.bw_era.energy_provided_options", _options)
    def test_dark_pulse_times_amount_wording_is_supported(self):
        text = (
            "this attack does 30 more damage times the amount of darkness "
            "energy attached to all of your pokémon."
        )
        self.assertEqual(_formula_damage(self._ctx(30), text), 90)

    @patch("spirit.game.card_effects.bw_era.energy_provided_options", _options)
    def test_for_each_wording_counts_full_energy_value(self):
        text = (
            "this attack does 60 damage for each energy attached to all of "
            "your opponent's pokémon."
        )
        self.assertEqual(_formula_damage(self._ctx(0), text), 180)

    @patch("spirit.game.card_effects.bw_era.energy_provided_options", _options)
    def test_times_amount_wording_counts_full_energy_value(self):
        text = (
            "this attack does 20 damage times the amount of energy attached "
            "to all of your opponent's pokémon."
        )
        self.assertEqual(_formula_damage(self._ctx(0), text), 60)

    @patch("spirit.game.card_effects.bw_era._name",
           lambda pokemon: pokemon.name)
    @patch("spirit.game.card_effects.bw_era.energy_provided_options", _options)
    def test_named_pokemon_scope_counts_only_matching_energy(self):
        ctx = self._ctx(20)
        ctx._mine[0].name = "Iono's Voltorb"
        ctx._mine[1].name = "Pikachu"
        ctx._mine[0].energies = [
            _Energy("Lightning Energy", self.lightning),
        ]
        ctx._mine[1].energies = [
            _Energy("Lightning Energy", self.lightning),
        ]
        text = (
            "this attack does 20 more damage for each lightning energy "
            "attached to all of your iono's pokémon."
        )
        self.assertEqual(_formula_damage(ctx, text), 40)

    @patch("spirit.game.card_effects.bw_era._damage_counter_count",
           lambda _ctx, pokemon: pokemon.counters)
    def test_damage_counters_across_opponents_field(self):
        ctx = self._ctx(10)
        ctx._opponent[0].counters = 2
        ctx._opponent[1].counters = 3
        text = (
            "this attack does 10 more damage for each damage counter on all "
            "of your opponent's pokémon."
        )
        self.assertEqual(_formula_damage(ctx, text), 60)

    @patch("spirit.game.card_effects.bw_era.is_pokemon_tool",
           lambda card: card == "tool")
    @patch("spirit.game.card_effects.bw_era.full_stack",
           lambda pokemon: [pokemon] + pokemon.tools)
    def test_tools_across_own_field(self):
        ctx = self._ctx(0)
        ctx._mine[0].tools = ["tool"]
        ctx._mine[1].tools = ["tool", "tool"]
        ctx._opponent[0].tools = ["tool"]
        text = (
            "this attack does 30 damage for each pokémon tool attached to "
            "all of your pokémon."
        )
        self.assertEqual(_formula_damage(ctx, text), 90)


if __name__ == "__main__":
    unittest.main()
