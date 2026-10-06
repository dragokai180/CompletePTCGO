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

    @patch("spirit.game.card_effects.bw_era.energy_provided_options", _options)
    def test_energy_blow_counts_energy_units_on_attacker(self):
        ctx = self._ctx(10)
        ctx.attacker.energies = [
            _Energy("Fairy Energy", self.fire),
            _Energy("Double Colorless Energy", self.colorless, self.colorless),
        ]
        text = "this attack does 30 more damage times the amount of energy attached to this pokémon."
        self.assertEqual(_formula_damage(ctx, text), 100)

    @patch("spirit.game.card_effects.bw_era.energy_provided_options", _options)
    def test_more_damage_for_each_energy_on_attacker(self):
        ctx = self._ctx(10)
        ctx.attacker.energies = [_Energy("Double Colorless Energy", self.colorless, self.colorless)]
        text = "this attack does 50 more damage for each energy attached to this pokémon."
        self.assertEqual(_formula_damage(ctx, text), 110)

    @patch("spirit.game.card_effects.bw_era.energy_provided_options", _options)
    def test_energy_on_both_active_pokemon(self):
        ctx = self._ctx(20)
        ctx.attacker.energies = [_Energy("Double Colorless Energy", self.colorless, self.colorless)]
        ctx.defender.energies = [_Energy("Lightning Energy", self.lightning)]
        more = "this attack does 20 more damage times the amount of energy attached to both active pokémon."
        multiplier = "this attack does 30 damage for each energy attached to both active pokémon."
        self.assertEqual(_formula_damage(ctx, more), 80)
        self.assertEqual(_formula_damage(ctx, multiplier), 90)

    @patch("spirit.game.card_effects.bw_era.is_basic_energy",
           lambda energy: energy.name.endswith("Energy") and not energy.name.startswith("Double"))
    @patch("spirit.game.card_effects.bw_era.energy_provided_options", _options)
    def test_different_basic_energy_types_and_basic_only(self):
        ctx = self._ctx(20)
        ctx.attacker.energies = [
            _Energy("Fire Energy", self.fire),
            _Energy("Fire Energy", self.fire),
            _Energy("Darkness Energy", self.darkness),
            _Energy("Double Colorless Energy", self.colorless, self.colorless),
        ]
        distinct = "does 20 more damage for each different type of basic energy attached to this pokémon."
        basic = "this attack does 40 more damage times the amount of basic energy attached to this pokémon."
        self.assertEqual(_formula_damage(ctx, distinct), 60)
        self.assertEqual(_formula_damage(ctx, basic), 140)

    @patch("spirit.game.card_effects.bw_era.is_special_energy",
           lambda energy: energy.name.startswith("Double"))
    @patch("spirit.game.card_effects.bw_era.energy_provided_options", _options)
    def test_special_energy_cards_count_cards_not_energy_units(self):
        ctx = self._ctx(0)
        ctx.attacker.energies = [
            _Energy("Double Colorless Energy", self.colorless, self.colorless),
            _Energy("Fire Energy", self.fire),
        ]
        text = "this attack does 70 damage for each special energy card attached to this pokémon."
        self.assertEqual(_formula_damage(ctx, text), 70)

    @patch("spirit.game.card_effects.bw_era.is_basic_energy",
           lambda energy: not energy.name.startswith("Double"))
    @patch("spirit.game.card_effects.bw_era.energy_provided_options", _options)
    def test_distinct_basic_energy_types_across_field(self):
        ctx = self._ctx(10)
        ctx._mine[0].energies = [_Energy("Fire Energy", self.fire)]
        ctx._mine[1].energies = [
            _Energy("Fire Energy", self.fire),
            _Energy("Darkness Energy", self.darkness),
            _Energy("Double Colorless Energy", self.colorless, self.colorless),
        ]
        text = "this attack does 50 damage for each type of basic energy attached to all of your pokémon."
        self.assertEqual(_formula_damage(ctx, text), 100)

    @patch("spirit.game.card_effects.bw_era.is_basic_energy",
           lambda energy: not energy.name.startswith("Double"))
    @patch("spirit.game.card_effects.bw_era.energy_provided_options", _options)
    def test_two_basic_energy_types_across_field(self):
        ctx = self._ctx(0)
        ctx._mine[0].energies = [
            _Energy("Fire Energy", self.fire),
            _Energy("Darkness Energy", self.darkness),
            _Energy("Double Colorless Energy", self.colorless, self.colorless),
        ]
        ctx._mine[1].energies = [_Energy("Fire Energy", self.fire)]
        text = "this attack does 30 damage times the amount of basic fire and basic darkness energy attached to your pokémon."
        self.assertEqual(_formula_damage(ctx, text), 90)

    @patch("spirit.game.card_effects.bw_era.energy_provided_options", _options)
    def test_less_damage_for_opponents_energy_has_zero_floor(self):
        ctx = self._ctx(90)
        ctx.defender.energies = [_Energy("Double Colorless Energy", self.colorless, self.colorless)]
        text = "this attack does 30 less damage times the amount of energy attached to your opponent's active pokémon."
        self.assertEqual(_formula_damage(ctx, text), 30)
        ctx.defender.energies.append(_Energy("Fire Energy", self.fire))
        self.assertEqual(_formula_damage(ctx, text), 0)

    @patch("spirit.game.card_effects.bw_era._damage_counter_count",
           lambda _ctx, pokemon: pokemon.counters)
    def test_less_damage_for_own_counters(self):
        ctx = self._ctx(150)
        ctx.attacker.counters = 4
        text = "this attack does 10 less damage for each damage counter on this pokémon."
        self.assertEqual(_formula_damage(ctx, text), 110)

    @patch("spirit.game.card_effects.bw_era._damage_counter_count",
           lambda _ctx, pokemon: pokemon.counters)
    def test_more_damage_for_counters_on_each_benched_pokemon(self):
        ctx = self._ctx(10)
        ctx.attacker.counters = 3
        ctx._mine[1].counters = 2
        text = "does 10 more damage for each damage counter on each of your benched pokémon."
        self.assertEqual(_formula_damage(ctx, text), 30)

    @patch("spirit.game.card_effects.bw_era.effective_retreat_cost",
           lambda _board, _pokemon: 3)
    def test_damage_from_defenders_retreat_cost(self):
        ctx = self._ctx(100)
        subject = "colorless in your opponent's active pokémon's retreat cost."
        self.assertEqual(_formula_damage(
            ctx, "this attack does 20 more damage for each " + subject), 160)
        self.assertEqual(_formula_damage(
            ctx, "this attack does 30 damage for each " + subject), 90)
        self.assertEqual(_formula_damage(
            ctx, "this attack does 40 less damage for each " + subject), 0)
        self.assertEqual(_formula_damage(
            ctx, "does 80 damage minus 20 damage for each " + subject), 20)


if __name__ == "__main__":
    unittest.main()
