"""Mixed searches must offer every printed category, not just the first one."""
import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures
from spirit.game.card_effects.bw_era import _ability_search_predicate
from spirit.game.card_effects.standard_era import _search_predicate
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.attributes import PokemonTypes
from spirit.game.session.effects import EffectContext, is_basic_energy
from spirit.tools.effect_smoke import P1


class MixedSearchCategoryTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    async def test_ethans_adventure_finds_evolution_pokemon_and_basic_fire_energy(self):
        rig, entities = self.rig('SV10.EthansAdventure_165', 'trainer')
        card = fixtures.definition('SV10.EthansAdventure_165')
        ctx = EffectContext(rig.session, P1, entities['target'], None)
        pokemon = self.add(rig, fixtures.definition('SV10.EthansQuilava_33'), P1, 'deck')
        other = self.add(rig, fixtures.definition('SV10.Growlithe_27'), P1, 'deck')
        energy = next(c for c in ctx.discard_pile() if is_basic_energy(c)
                      and energy_provides_type(c, PokemonTypes.FIRE.value))
        rig.to_area(energy, P1, 'deck')

        async def search(predicate, **kwargs):
            self.assertTrue(predicate(pokemon))
            self.assertTrue(predicate(energy))
            self.assertFalse(predicate(other))
            self.assertEqual(kwargs['count'], 3)
            return [pokemon, energy]

        ctx.search_deck = AsyncMock(side_effect=search)
        await card.effect(ctx)
        self.assertIn(pokemon, ctx.hand())
        self.assertIn(energy, ctx.hand())

    async def test_heatmor_search_offers_fire_pokemon_and_basic_fire_energy(self):
        rig, entities = self.rig('RSV10PT5.Heatmor_19')
        ability = fixtures.definition('RSV10PT5.Heatmor_19').abilities[0]
        ctx = EffectContext(rig.session, P1, entities['target'], ability)
        pokemon = self.add(rig, fixtures.definition('SV4.Volcanion_22'), P1, 'deck')
        other = self.add(rig, fixtures.definition('SV4.Flittle_79'), P1, 'deck')
        energy = next(c for c in ctx.discard_pile() if is_basic_energy(c)
                      and energy_provides_type(c, PokemonTypes.FIRE.value))
        rig.to_area(energy, P1, 'deck')

        async def search(predicate, _count, **kwargs):
            self.assertTrue(predicate(pokemon))
            self.assertTrue(predicate(energy))
            self.assertFalse(predicate(other))
            return [pokemon, energy]

        ctx.search_deck = AsyncMock(side_effect=search)
        await ability.effect(ctx)
        self.assertIn(pokemon, ctx.hand())
        self.assertIn(energy, ctx.hand())

    async def test_related_mixed_descriptors(self):
        rig, _ = self.rig('SV4.Tulip_181', 'trainer')
        pokemon = self.add(rig, fixtures.definition('SV4.Flittle_79'), P1, 'deck')
        energy = next(c for c in rig.board.find_player_area(P1, 'discard').children
                      if is_basic_energy(c) and energy_provides_type(c, PokemonTypes.PSYCHIC.value))
        tulip = _search_predicate(
            'put up to 4 in any combination of psychic pokémon and basic psychic energy cards '
            'from your discard pile into your hand.')
        self.assertTrue(tulip(pokemon))
        self.assertTrue(tulip(energy))

        lilligant = _ability_search_predicate(
            'search your deck for up to 5 in any combination of grass pokémon '
            'and grass energy cards, reveal them, and put them into your hand.')
        grass = self.add(rig, fixtures.definition('SV1.Smoliv_20'), P1, 'deck')
        grass_energy = next(c for c in rig.board.find_player_area(P1, 'discard').children
                            if is_basic_energy(c)
                            and energy_provides_type(c, PokemonTypes.GRASS.value))
        self.assertTrue(lilligant(grass))
        self.assertTrue(lilligant(grass_energy))
        self.assertFalse(lilligant(pokemon))

        starmie = _ability_search_predicate(
            'search your deck for up to 3 in any combination of water and psychic energy cards '
            'and attach them to 1 of your benched pokémon.')
        water_energy = next(c for c in rig.board.find_player_area(P1, 'discard').children
                            if is_basic_energy(c)
                            and energy_provides_type(c, PokemonTypes.WATER.value))
        self.assertTrue(starmie(water_energy))
        self.assertTrue(starmie(energy))
        self.assertFalse(starmie(grass_energy))

    async def test_flabebe_shuffles_pokemon_and_basic_energy(self):
        rig, entities = self.rig('SM6.Flabb_84')
        ability = fixtures.definition('SM6.Flabb_84').abilities[0]
        ctx = EffectContext(rig.session, P1, entities['target'], ability)
        pokemon = self.add(rig, fixtures.definition('SV4.Flittle_79'), P1, 'discard')
        energy = next(c for c in ctx.discard_pile() if is_basic_energy(c))

        async def choose(pool, maximum, **kwargs):
            self.assertIn(pokemon, pool)
            self.assertIn(energy, pool)
            self.assertEqual(maximum, 3)
            return [pokemon, energy]

        ctx.choose_cards = AsyncMock(side_effect=choose)
        await ability.effect(ctx)
        self.assertIn(pokemon, ctx.deck())
        self.assertIn(energy, ctx.deck())

    async def test_fossil_excavation_kit_only_offers_named_fossils(self):
        path = 'XY10.FossilExcavationKit_101'
        rig, entities = self.rig(path, 'trainer')
        card = fixtures.definition(path)
        ctx = EffectContext(rig.session, P1, entities['target'], None)
        for entry in list(ctx.discard_pile()):
            rig.to_area(entry, P1, 'deck')
        unrelated = self.add(rig, self.item, P1, 'discard')
        self.assertFalse(card.condition(rig.board, P1))
        fossil = self.add(rig, fixtures.definition('XY10.HelixFossilOmanyte_102'), P1, 'discard')
        self.assertTrue(card.condition(rig.board, P1))

        async def choose(pool, maximum, **kwargs):
            self.assertEqual(pool, [fossil])
            self.assertEqual(maximum, 1)
            self.assertNotIn(unrelated, pool)
            return [fossil]

        ctx.choose_cards = AsyncMock(side_effect=choose)
        await card.effect(ctx)
        self.assertIn(fossil, ctx.hand())

    async def test_starmie_attaches_both_printed_energy_types(self):
        rig, entities = self.rig('SM9.Starmie_65')
        ability = fixtures.definition('SM9.Starmie_65').abilities[0]
        ctx = EffectContext(rig.session, P1, entities['target'], ability)
        bench = rig.board.pokemon_in_play(P1)[1]
        energies = []
        for kind in (PokemonTypes.WATER.value, PokemonTypes.PSYCHIC.value):
            energy = next(c for c in ctx.discard_pile() if is_basic_energy(c)
                          and energy_provides_type(c, kind))
            rig.to_area(energy, P1, 'deck')
            energies.append(energy)

        async def search(predicate, _count, **kwargs):
            self.assertTrue(all(predicate(energy) for energy in energies))
            return energies

        ctx.search_deck = AsyncMock(side_effect=search)
        ctx.choose_pokemon = AsyncMock(return_value=bench)
        await ability.effect(ctx)
        self.assertTrue(all(energy in rig.board.attached_energies(bench)
                            for energy in energies))
