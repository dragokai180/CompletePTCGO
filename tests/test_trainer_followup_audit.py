"""Outcome and public-information permission checks for Trainer cards."""
import unittest
from unittest.mock import AsyncMock
from tests import test_hgss_rules as fixtures
from tests.test_hgss_rules import definition
from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.session.effects import EffectContext
from spirit.game.session.passives import effective_max_hp
from spirit.tools.effect_smoke import P1, P2


class TrainerFollowupTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    def stadium(self, path):
        rig, e = self.rig('BW1.Snivy_1')
        card = self.add(rig, definition(path), P1, 'hand')
        return rig, e, EffectContext(rig.session, P1, card, definition(path).ability)

    async def test_rough_seas_requires_own_damaged_water_or_lightning(self):
        rig, e, ctx = self.stadium('XY5.RoughSeas_137')
        self.assertIsNotNone(ctx.ability.condition)
        check = lambda: ctx.ability.condition(rig.board, P1, ctx.source)
        self.assertFalse(check())
        target = rig.board.active_pokemon(P1)
        hp = effective_max_hp(rig.board, target)
        target.set_attribute(AttrID.HP, hp - 40)
        self.assertFalse(check())  # Grass damage is not a valid target.
        target.set_attribute(AttrID.POKEMON_TYPES, [PokemonTypes.WATER.value])
        self.assertTrue(check())
        other = rig.board.active_pokemon(P2)
        other.set_attribute(AttrID.POKEMON_TYPES, [PokemonTypes.WATER.value])
        other.set_attribute(AttrID.HP, effective_max_hp(rig.board, other) - 40)
        other_hp = other.get_attribute(AttrID.HP)
        lightning = rig.board.pokemon_in_play(P1)[1]
        lightning.set_attribute(AttrID.POKEMON_TYPES, [PokemonTypes.LIGHTNING.value])
        lightning.set_attribute(AttrID.HP, effective_max_hp(rig.board, lightning) - 20)
        await ctx.ability.effect(ctx)
        self.assertEqual(target.get_attribute(AttrID.HP), hp - 10)
        self.assertEqual(lightning.get_attribute(AttrID.HP), effective_max_hp(rig.board, lightning))
        self.assertEqual(other.get_attribute(AttrID.HP), other_hp)

    async def test_life_forest_can_cure_without_damage(self):
        rig, e, ctx = self.stadium('SM8.LifeForest_180')
        self.assertIsNotNone(ctx.ability.condition)
        target = rig.board.active_pokemon(P1)
        self.assertFalse(ctx.ability.condition(rig.board, P1, ctx.source))
        target.set_attribute(AttrID.SPECIAL_CONDITIONS, ['Poisoned'])
        self.assertTrue(ctx.ability.condition(rig.board, P1, ctx.source))
        ctx.choose_pokemon = AsyncMock(return_value=target)
        await ctx.ability.effect(ctx)
        self.assertFalse(target.get_attribute(AttrID.SPECIAL_CONDITIONS))

    async def test_all_night_party_requires_sleep_not_only_damage(self):
        rig, e, ctx = self.stadium('XY9.AllNightParty_96')
        self.assertIsNotNone(ctx.ability.condition)
        target = rig.board.active_pokemon(P1)
        target.set_attribute(AttrID.HP, 20)
        self.assertFalse(ctx.ability.condition(rig.board, P1, ctx.source))
        target.set_attribute(AttrID.SPECIAL_CONDITIONS, ['Asleep'])
        self.assertTrue(ctx.ability.condition(rig.board, P1, ctx.source))
        await ctx.ability.effect(ctx)
        self.assertFalse(target.get_attribute(AttrID.SPECIAL_CONDITIONS))
        self.assertEqual(target.get_attribute(AttrID.HP), 50)

    async def test_evosoda_timing_and_private_deck(self):
        rig, e = self.rig('BW1.Snivy_1')
        d = definition('XY1.Evosoda_116')
        state = rig.session.turn_state
        for turn in (1, 2):
            state.turn_number = turn
            self.assertFalse(d.condition(rig.board, P1))
        state.turn_number = 3
        self.assertTrue(d.condition(rig.board, P1))
        for pokemon in rig.board.pokemon_in_play(P1):
            state.mark_entered_play(pokemon.entity_id)
        self.assertFalse(d.condition(rig.board, P1))
        state.turn_number = 5
        for card in list(rig.board.find_player_area(P1, 'deck').children):
            rig.to_area(card, P1, 'discard')
        self.assertFalse(d.condition(rig.board, P1))
        self.add(rig, definition('XY1.Evosoda_116'), P1, 'deck')
        self.assertTrue(d.condition(rig.board, P1))  # No matching evolution is private.

    async def test_evosoda_evolves_directly_from_deck(self):
        for path in ('XY1.Evosoda_116', 'TwentiethAnn.Evosoda_62'):
            with self.subTest(path=path):
                rig, e = self.rig('BW1.Snivy_1')
                rig.session.turn_state.turn_number = 3
                source = self.add(rig, definition(path), P1, 'hand')
                target = rig.board.active_pokemon(P1)
                evolution = self.add(rig, definition('BW1.Servine_3'), P1, 'deck')
                stage2 = self.add(rig, definition('BW1.Serperior_5'), P1, 'deck')
                ctx = EffectContext(rig.session, P1, source, None)
                ctx.choose_pokemon = AsyncMock(return_value=target)
                ctx.search_deck = AsyncMock(return_value=[evolution])
                ctx.evolve_pokemon = AsyncMock(return_value=True)
                ctx.shuffle_deck = AsyncMock()
                await definition(path).effect(ctx)
                ctx.evolve_pokemon.assert_awaited_once_with(target, evolution)
                predicate = ctx.search_deck.call_args.args[0]
                self.assertTrue(predicate(evolution))
                self.assertFalse(predicate(stage2))
                self.assertEqual(ctx.search_deck.call_args.kwargs['minimum'], 0)
                ctx.shuffle_deck.assert_awaited_once()

    async def test_wally_requires_nonempty_deck(self):
        rig, e = self.rig('BW1.Snivy_1')
        for card in list(rig.board.find_player_area(P1, 'deck').children):
            rig.to_area(card, P1, 'discard')
        self.assertFalse(definition('XY6.Wally_94').condition(rig.board, P1))

    async def test_breeders_nurturing_requires_deck_and_old_target(self):
        for number in (166, 188, 195):
            rig, e = self.rig('BW1.Snivy_1')
            d = definition(f'SWSH3.PokemonBreedersNurturing_{number}')
            state = rig.session.turn_state
            state.turn_number = 3
            self.assertTrue(d.condition(rig.board, P1))
            for pokemon in rig.board.pokemon_in_play(P1):
                state.mark_entered_play(pokemon.entity_id)
            self.assertFalse(d.condition(rig.board, P1))
            state.turn_number = 5
            for card in list(rig.board.find_player_area(P1, 'deck').children):
                rig.to_area(card, P1, 'discard')
            self.assertFalse(d.condition(rig.board, P1))

    async def test_celebratory_fanfare_ends_turn_only_if_healing_succeeds(self):
        rig, e, ctx = self.stadium('MEP.CelebratoryFanfare_28')
        self.assertIsNotNone(ctx.ability.condition)
        self.assertFalse(ctx.ability.condition(rig.board, P1, ctx.source))
        target = rig.board.active_pokemon(P1)
        target.set_attribute(AttrID.HP, 20)
        self.assertTrue(ctx.ability.condition(rig.board, P1, ctx.source))
        ctx.heal = AsyncMock(return_value=0)
        await ctx.ability.effect(ctx)
        self.assertFalse(ctx.ends_turn)
        ctx.heal = AsyncMock(return_value=10)
        await ctx.ability.effect(ctx)
        self.assertTrue(ctx.ends_turn)
