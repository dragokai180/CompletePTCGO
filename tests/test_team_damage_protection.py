"""Damage protection applies only to the printed targets and attackers."""
import unittest

from tests import test_hgss_rules as fixtures
from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.session.passives import compute_damage
from spirit.tools.effect_smoke import P1, P2


class TeamDamageProtectionTests(unittest.TestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    @staticmethod
    def clear_energy(rig, pokemon):
        for energy in list(rig.board.attached_energies(pokemon)):
            rig.to_area(energy, pokemon.owning_player_id, "discard")

    @staticmethod
    def damage(rig, attacker, target):
        return compute_damage(rig.board, attacker, target, 100,
                              apply_modifiers=False).amount

    def test_tundra_wall_requires_water_on_each_protected_pokemon(self):
        rig, entities = self.rig("ME3.Aurorus_24")
        aurorus = entities["target"]
        teammate = next(p for p in rig.board.pokemon_in_play(P1) if p is not aurorus)
        attacker = rig.board.active_pokemon(P2)
        self.clear_energy(rig, aurorus)
        self.clear_energy(rig, teammate)

        self.assertEqual(self.damage(rig, attacker, aurorus), 100)
        self.assertEqual(self.damage(rig, attacker, teammate), 100)
        rig.attach_energy_type(P1, teammate, PokemonTypes.WATER.value)
        self.assertEqual(self.damage(rig, attacker, teammate), 50)
        rig.attach_energy_type(P1, aurorus, PokemonTypes.WATER.value)
        self.assertEqual(self.damage(rig, attacker, aurorus), 50)

    def test_earthen_shield_requires_metal_target_and_special_attacker_energy(self):
        rig, entities = self.rig("SM5.Bastiodon_85")
        bastiodon = entities["target"]
        teammate = next(p for p in rig.board.pokemon_in_play(P1) if p is not bastiodon)
        attacker = rig.board.active_pokemon(P2)
        self.clear_energy(rig, attacker)
        teammate.set_attribute(AttrID.POKEMON_TYPES, [PokemonTypes.METAL.value])

        self.assertEqual(self.damage(rig, attacker, bastiodon), 100)
        self.assertEqual(self.damage(rig, attacker, teammate), 100)
        special = self.add(rig, fixtures.definition("XY1.DoubleColorlessEnergy_130"), P2, "hand")
        rig.attach(special, attacker)
        self.assertEqual(self.damage(rig, attacker, bastiodon), 0)
        self.assertEqual(self.damage(rig, attacker, teammate), 0)
        teammate.set_attribute(AttrID.POKEMON_TYPES, [PokemonTypes.GRASS.value])
        self.assertEqual(self.damage(rig, attacker, teammate), 100)

    def test_power_of_nature_requires_grass_and_ultra_beast_attacker(self):
        rig, entities = self.rig("SM7.Sceptile_10")
        sceptile = entities["target"]
        teammate = next(p for p in rig.board.pokemon_in_play(P1) if p is not sceptile)
        self.clear_energy(rig, sceptile)
        self.clear_energy(rig, teammate)
        ordinary = rig.board.active_pokemon(P2)
        rig.to_area(ordinary, P2, "discard")
        ultra_beast = self.add(rig, fixtures.definition("SM4.BuzzwoleGX_57"), P2, "activePokemonArea")

        self.assertEqual(self.damage(rig, ultra_beast, sceptile), 100)
        self.assertEqual(self.damage(rig, ultra_beast, teammate), 100)
        rig.attach_energy_type(P1, teammate, PokemonTypes.GRASS.value)
        self.assertEqual(self.damage(rig, ultra_beast, teammate), 0)
        rig.attach_energy_type(P1, sceptile, PokemonTypes.GRASS.value)
        self.assertEqual(self.damage(rig, ultra_beast, sceptile), 0)
        rig.to_area(ultra_beast, P2, "discard")
        rig.to_area(ordinary, P2, "activePokemonArea")
        self.assertEqual(self.damage(rig, ordinary, teammate), 100)
