"""Type-gated Special Energy effects follow the Pokémon's live type."""

import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures
from spirit.game.attributes import PokemonTypes, SpecialConditions
from spirit.game.session.effects import EffectContext
from spirit.game.session.passives import (
    Passive, TempPassive, compute_damage, conditions_blocked,
    effective_pokemon_types, effective_retreat_cost, energy_provided_options,
)
from spirit.tools.effect_smoke import P1, P2


class GrantType(Passive):
    def __init__(self, pokemon_type):
        self.pokemon_type = pokemon_type.value

    def modify_pokemon_types(self, types, pokemon, carrier):
        return list(dict.fromkeys(types + [self.pokemon_type])) \
            if pokemon is carrier else types


class EnergyLivePokemonTypesTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    def grant_type(self, rig, pokemon, pokemon_type):
        effect = TempPassive(GrantType(pokemon_type), pokemon.entity_id)
        rig.board.temporary_passives.append(effect)
        self.assertIn(pokemon_type.value,
                      effective_pokemon_types(rig.board, pokemon))
        return effect

    async def test_bubbly_water_uses_water_from_aqua_effect(self):
        rig, _ = self.rig('BW1.Snivy_1')
        target = self.add(rig, fixtures.definition('BW1.Servine_3'), P1, 'bench')
        energy_def = fixtures.definition('ME4.BubblyWaterEnergy_84')
        energy = self.add(rig, energy_def, P1, 'hand')
        rig.attach(energy, target)
        ctx = EffectContext(rig.session, P1, energy, None, attached_to=target)
        ctx.cure_all_conditions = AsyncMock()

        await energy_def.on_attach(ctx)
        ctx.cure_all_conditions.assert_not_awaited()
        self.assertFalse(conditions_blocked(rig.board, target,
                                            SpecialConditions.POISONED))

        vaporeon = self.add(rig, fixtures.definition('XY7.Vaporeon_22'), P1, 'bench')
        await energy_def.on_attach(ctx)
        ctx.cure_all_conditions.assert_awaited_once_with(target)
        self.assertTrue(conditions_blocked(rig.board, target,
                                           SpecialConditions.POISONED))

        splash = fixtures.definition('XY9.SplashEnergy_113')
        self.assertTrue(splash.attach_to(target))
        rig.to_area(vaporeon, P1, 'discard')
        self.assertFalse(splash.attach_to(target))

    def test_magnetic_metal_free_retreat_uses_granted_type(self):
        rig, _ = self.rig('BW1.Snivy_1')
        target = self.add(rig, fixtures.definition('BW1.Servine_3'),
                          P1, 'activePokemonArea')
        energy = self.add(rig, fixtures.definition('ME4.MagneticMetalEnergy_85'),
                          P1, 'hand')
        rig.attach(energy, target)
        printed_cost = effective_retreat_cost(rig.board, target)
        self.assertGreater(printed_cost, 0)
        effect = self.grant_type(rig, target, PokemonTypes.METAL)
        self.assertEqual(effective_retreat_cost(rig.board, target), 0)
        rig.board.temporary_passives.remove(effect)
        self.assertEqual(effective_retreat_cost(rig.board, target), printed_cost)

    def test_shadowy_darkness_protects_granted_darkness_bench(self):
        rig, _ = self.rig('BW1.Snivy_1')
        target = self.add(rig, fixtures.definition('BW1.Snivy_1'), P1, 'bench')
        energy = self.add(rig, fixtures.definition('ME5.ShadowyDarknessEnergy_83'),
                          P1, 'hand')
        rig.attach(energy, target)
        attacker = rig.board.active_pokemon(P2)

        def damage():
            return compute_damage(rig.board, attacker, target, 30,
                                  apply_modifiers=False).amount

        self.assertEqual(damage(), 30)
        effect = self.grant_type(rig, target, PokemonTypes.DARKNESS)
        self.assertEqual(damage(), 0)
        rig.board.temporary_passives.remove(effect)
        self.assertEqual(damage(), 30)

    def test_double_dragon_accepts_granted_dragon_type(self):
        rig, _ = self.rig('BW1.Snivy_1')
        target = self.add(rig, fixtures.definition('BW1.Servine_3'), P1, 'bench')
        energy_def = fixtures.definition('XY6.DoubleDragonEnergy_97')
        self.assertFalse(energy_def.attach_to(target))
        effect = self.grant_type(rig, target, PokemonTypes.DRAGON)
        self.assertTrue(energy_def.attach_to(target))
        energy = self.add(rig, energy_def, P1, 'hand')
        rig.attach(energy, target)
        self.assertTrue(energy_provided_options(rig.board, energy))
        rig.board.temporary_passives.remove(effect)
        self.assertFalse(energy_def.attach_to(target))


if __name__ == '__main__':
    unittest.main()
