"""Recover both printed card categories from a single discard selection."""
import unittest

from tests import test_hgss_rules as fixtures
from spirit.game.attributes import PokemonTypes
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.session.effects import EffectContext, is_basic_energy
from spirit.tools.effect_smoke import P1


class TypedDiscardRecoveryTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    async def test_tulip_and_tarragon_recover_pokemon_and_matching_basic_energy(self):
        cases = (
            ('SV4.Tulip_181', 'SV4.Flittle_79', 'SV4.Nacli_101',
             PokemonTypes.PSYCHIC.value, PokemonTypes.FIGHTING.value),
            ('ME3.Tarragon_85', 'SV4.Nacli_101', 'SV4.Flittle_79',
             PokemonTypes.FIGHTING.value, PokemonTypes.PSYCHIC.value),
        )
        for path, pokemon_path, other_path, energy_type, other_energy_type in cases:
            with self.subTest(card=path):
                rig, entities = self.rig(path, 'trainer')
                card = fixtures.definition(path)
                ctx = EffectContext(rig.session, P1, entities['target'], None)
                energies = list(ctx.discard_pile())
                energy = next(entry for entry in energies if is_basic_energy(entry)
                              and energy_provides_type(entry, energy_type))
                other_energy = next(entry for entry in energies
                                    if is_basic_energy(entry)
                                    and energy_provides_type(entry, other_energy_type))
                for entry in energies:
                    if entry not in (energy, other_energy):
                        rig.to_area(entry, P1, 'deck')
                pokemon = self.add(rig, fixtures.definition(pokemon_path), P1, 'discard')
                other_pokemon = self.add(rig, fixtures.definition(other_path), P1, 'discard')

                if card.condition is not None:
                    rig.to_area(energy, P1, 'deck')
                    self.assertTrue(card.condition(rig.board, P1))
                    rig.to_area(energy, P1, 'discard')
                    rig.to_area(pokemon, P1, 'deck')
                    self.assertTrue(card.condition(rig.board, P1))
                    rig.to_area(energy, P1, 'deck')
                    self.assertFalse(card.condition(rig.board, P1))
                    rig.to_area(pokemon, P1, 'discard')
                    rig.to_area(energy, P1, 'discard')

                async def choose(pool, maximum, **kwargs):
                    self.assertEqual(set(pool), {pokemon, energy})
                    self.assertEqual(maximum, 2)
                    self.assertEqual(kwargs['minimum'], 0)
                    self.assertNotIn(other_pokemon, pool)
                    self.assertNotIn(other_energy, pool)
                    return [pokemon, energy]

                ctx.choose_cards = choose
                await card.effect(ctx)
                self.assertIn(pokemon, ctx.hand())
                self.assertIn(energy, ctx.hand())
