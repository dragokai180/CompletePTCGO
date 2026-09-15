"""Restricted SM searches, public prerequisites, and card destinations."""
import unittest
from unittest.mock import AsyncMock
from tests import test_hgss_rules as fixtures
from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.card_effects.standard_era import _search_predicate
from spirit.game.card_effects.bw_era import _ability_search_predicate
from spirit.game.card_effects.sm_searches import resolve_sm_search
from spirit.game.session.effects import EffectContext
from spirit.game.session.legal_actions import trainer_condition_met
from spirit.tools.effect_smoke import P1, P2


class SmSearchTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    def setup_card(self, path):
        rig, e = self.rig(path, 'trainer')
        return rig, e, EffectContext(rig.session, P1, e['target'], None)

    async def test_narrow_searches_reject_wrong_subtypes_names_and_types(self):
        rig, e, ctx = self.setup_card('SM12.TagCall_206')
        paths = [
            'SM12.ArceusDialgaPalkiaGX_156', 'SM11.RaichuAlolanRaichuGX_54',
            'SM10.PheromosaBuzzwoleGX_1', 'SM5.Looker_126',
            'SM6.UnidentifiedFossil_116', 'SM6.UltraSpace_115',
        ]
        cards = [self.add(rig, fixtures.definition(p), P1, 'deck') for p in paths]
        cases = [
            ('a pokémon-gx', {0, 1, 2}),
            ('an ultra beast card', {2}),
            ('up to 2 cards named looker', {3}),
            ('an unidentified fossil card', {4}),
            ('a stadium card', {5}),
            ('up to 2 in any combination of lightning pokémon-gx and lightning pokémon-ex', {1}),
        ]
        for descriptor, allowed in cases:
            text = 'search your deck for ' + descriptor + ', reveal it, and put it into your hand.'
            for builder in (_search_predicate, _ability_search_predicate):
                predicate = builder(text)
                self.assertEqual({i for i, card in enumerate(cards) if predicate(card)}, allowed)
                self.assertFalse(predicate(e['target']))

    async def test_net_ball_allows_grass_basic_or_grass_energy(self):
        rig, e, ctx = self.setup_card('SM8.NetBall_187')
        pokemon = self.add(rig, fixtures.definition('SM10.PheromosaBuzzwoleGX_1'), P1, 'deck')
        grass = rig.pull_guid(P1, self.energies[PokemonTypes.GRASS.value])
        water = rig.pull_guid(P1, self.energies[PokemonTypes.WATER.value])
        pred = _search_predicate('search your deck for a basic grass pokémon or a grass energy card, reveal it')
        self.assertTrue(pred(pokemon))
        self.assertTrue(pred(grass))
        self.assertFalse(pred(water))

    async def test_beast_ring_window_and_single_ultra_beast_target(self):
        rig, e, ctx = self.setup_card('SM6.BeastRing_102')
        target = self.add(rig, fixtures.definition('SM10.PheromosaBuzzwoleGX_1'), P1, 'bench')
        prizes = rig.board.find_player_area(P2, 'prizePile')
        self.assertFalse(trainer_condition_met(fixtures.definition('SM6.BeastRing_102').condition, rig.board, P1, e['target']))
        for card in list(prizes.children)[4:]:rig.to_area(card, P2, 'discard')
        self.assertTrue(trainer_condition_met(fixtures.definition('SM6.BeastRing_102').condition, rig.board, P1, e['target']))
        energies = [rig.pull_guid(P1, self.energies[t.value]) for t in (PokemonTypes.GRASS, PokemonTypes.WATER)]
        ctx.choose_pokemon = AsyncMock(return_value=target)
        ctx.search_deck = AsyncMock(return_value=energies)
        await fixtures.definition('SM6.BeastRing_102').effect(ctx)
        ctx.choose_pokemon.assert_awaited_once()
        self.assertTrue(set(energies).issubset(set(ctx.attached_energies(target))))
        self.assertNotIn(ctx.my_active(), ctx.choose_pokemon.call_args.args[0])

    async def test_energy_spinner_three_only_on_second_players_first_turn(self):
        for turn, first, count in ((1,P1,1),(2,P1,1),(2,P2,3),(4,P1,1)):
            rig, e, ctx = self.setup_card('SM10.EnergySpinner_170')
            rig.session.first_player_id = first
            rig.session.turn_state.turn_number = turn
            ctx.search_deck = AsyncMock(return_value=[])
            await fixtures.definition('SM10.EnergySpinner_170').effect(ctx)
            self.assertEqual(ctx.search_deck.call_args.args[1], count)
            self.assertEqual(ctx.search_deck.call_args.kwargs['minimum'], 0)

    async def test_dusk_stone_evolves_compatible_target_not_hand(self):
        rig, e, ctx = self.setup_card('SM10.DuskStone_167')
        basic = self.add(rig, fixtures.definition('SM10.Murkrow_108'), P1, 'bench')
        evolution = self.add(rig, fixtures.definition('SM10.HonchkrowGX_109'), P1, 'deck')
        ctx.search_deck = AsyncMock(return_value=[evolution])
        ctx.choose_pokemon = AsyncMock(return_value=basic)
        await fixtures.definition('SM10.DuskStone_167').effect(ctx)
        pred = ctx.search_deck.call_args.args[0]
        self.assertTrue(pred(evolution))
        self.assertFalse(pred(ctx.my_active()))
        self.assertIn(evolution, ctx.my_bench())
        self.assertNotIn(evolution, ctx.hand())

    async def test_research_lab_ends_turn_even_on_failed_private_search(self):
        rig, e, ctx = self.setup_card('SM11.PokmonResearchLab_205')
        fossil_pokemon = self.add(rig, fixtures.definition('SM6.Tyrunt_68'), P1, 'deck')
        ctx.search_deck = AsyncMock(return_value=[])
        await resolve_sm_search(ctx)
        self.assertTrue(ctx.search_deck.call_args.args[0](fossil_pokemon))
        self.assertFalse(ctx.search_deck.call_args.args[0](ctx.my_active()))
        self.assertTrue(ctx.ends_turn)


    async def test_red_blue_pays_optional_cost_then_evolves_and_attaches(self):
        for accepts in (False, True):
            rig, e, ctx = self.setup_card('SM12.RedBlue_202')
            rig.session.turn_state.turn_number = 3
            basic = self.add(rig, fixtures.definition('SM1.Eevee_101'), P1, 'bench')
            evolution = self.add(rig, fixtures.definition('SM1.EspeonGX_61'), P1, 'deck')
            energies = [rig.pull_guid(P1, self.energies[t.value]) for t in (PokemonTypes.WATER, PokemonTypes.FIRE)]
            before = len(ctx.discard_pile())
            calls = []
            async def search(predicate, count, **kwargs):
                self.assertEqual(len(ctx.discard_pile()) - before, 2 if accepts else 0)
                self.assertEqual(kwargs['minimum'], 0)
                calls.append(count)
                if len(calls) == 1:
                    self.assertTrue(predicate(evolution))
                    self.assertFalse(predicate(ctx.my_active()))
                    return [evolution]
                return energies
            ctx.ask_yes_no = AsyncMock(return_value=accepts)
            ctx.search_deck = AsyncMock(side_effect=search)
            ctx.choose_pokemon = AsyncMock(return_value=basic)
            await fixtures.definition('SM12.RedBlue_202').effect(ctx)
            self.assertIn(evolution, ctx.my_bench())
            self.assertEqual(calls, [1, 2] if accepts else [1])
            self.assertEqual(len(ctx.attached_energies(evolution)), 2 if accepts else 0)
            rig.session.turn_state.turn_number = 1
            self.assertFalse(trainer_condition_met(fixtures.definition('SM12.RedBlue_202').condition,
                                                  rig.board, P1, e['target']))

    async def test_fossil_map_recovery_works_with_empty_deck(self):
        rig, e, ctx = self.setup_card('SM6.FossilExcavationMap_107')
        for card in list(ctx.deck()):rig.to_area(card, P1, 'discard')
        fossil = self.add(rig, fixtures.definition('SM6.UnidentifiedFossil_116'), P1, 'discard')
        self.assertTrue(trainer_condition_met(fixtures.definition('SM6.FossilExcavationMap_107').condition, rig.board, P1, e['target']))
        await fixtures.definition('SM6.FossilExcavationMap_107').effect(ctx)
        self.assertIn(fossil, ctx.hand())
