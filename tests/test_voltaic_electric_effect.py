"""Voltaic Lightning Energy uses the attacking Pokémon's live types."""

import unittest

from tests import test_hgss_rules as fixtures
from spirit.game.attributes import PokemonTypes
from spirit.game.session.passives import compute_damage, effective_pokemon_types
from spirit.tools.effect_smoke import P1, P2


class VoltaicElectricEffectTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    def test_electric_effect_enables_voltaic_bonus_for_other_stage_one(self):
        rig, _ = self.rig('BW1.Snivy_1')
        attacker = self.add(rig, fixtures.definition('BW1.Servine_3'),
                            P1, 'activePokemonArea')
        defender = rig.board.active_pokemon(P2)
        energy = self.add(rig, fixtures.definition('ME5.VoltaicLightningEnergy_84'),
                          P1, 'hand')
        rig.attach(energy, attacker)

        def damage():
            return compute_damage(rig.board, attacker, defender, 30,
                                  apply_modifiers=False).amount

        self.assertNotIn(PokemonTypes.LIGHTNING.value,
                         effective_pokemon_types(rig.board, attacker))
        self.assertEqual(damage(), 30)

        jolteon = self.add(rig, fixtures.definition('XY7.Jolteon_26'), P1, 'bench')
        self.assertIn(PokemonTypes.LIGHTNING.value,
                      effective_pokemon_types(rig.board, attacker))
        self.assertEqual(damage(), 50)

        rig.to_area(jolteon, P1, 'discard')
        self.assertEqual(damage(), 30)

    def test_voltaic_still_requires_lightning_and_opposing_active(self):
        rig, _ = self.rig('BW1.Snivy_1')
        attacker = self.add(rig, fixtures.definition('BW1.Snivy_1'),
                            P1, 'activePokemonArea')
        jolteon = self.add(rig, fixtures.definition('XY7.Jolteon_26'), P1, 'bench')
        energy = self.add(rig, fixtures.definition('ME5.VoltaicLightningEnergy_84'),
                          P1, 'hand')
        rig.attach(energy, attacker)
        defender = rig.board.active_pokemon(P2)

        self.assertNotIn(PokemonTypes.LIGHTNING.value,
                         effective_pokemon_types(rig.board, attacker))
        self.assertEqual(compute_damage(rig.board, attacker, defender, 30,
                                        apply_modifiers=False).amount, 30)

        rig.to_area(attacker, P1, 'discard')
        attacker = self.add(rig, fixtures.definition('XY7.Jolteon_26'),
                            P1, 'activePokemonArea')
        rig.attach(energy, attacker)
        self.assertEqual(compute_damage(rig.board, attacker, defender, 30,
                                        apply_modifiers=False).amount, 50)
        bench_target = rig.board.find_player_area(P2, 'bench').children[0]
        self.assertEqual(compute_damage(rig.board, attacker, bench_target, 30,
                                        apply_modifiers=False).amount, 30)


if __name__ == '__main__':
    unittest.main()
