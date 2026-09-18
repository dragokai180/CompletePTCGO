"""Restored rules and Hero's Spirit apply before selection and zone changes."""
import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures
from tests.test_hgss_rules import definition
from spirit.game.attributes import AttrID, PokemonStage
from spirit.game.data_utils import def_for
from spirit.game.scripts.cards import loader
from spirit.game.session.effects import EffectContext
from spirit.game.session.passives import (
    out_of_play_ability_locked, pokemon_entry_blocked, pokemon_play_blocked,
)
from spirit.tools.effect_smoke import P1, P2


class RestrictedEntryTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add
    palafins = ('SV06.Palafinex_61', 'SV06.Palafinex_193',
                'SVP.Palafinex_126', 'SV085.Palafinex_151')
    garbodors = ('XY9.Garbodor_57', 'BW6.Garbodor_54')

    def clean(self, path='BW1.Snivy_1'):
        rig, entities = self.rig(path)
        for zone in ('hand', 'discard'):
            for card in list(rig.board.find_player_area(P1, zone).children):
                rig.to_area(card, P1, 'deck')
        return rig, entities

    def garbotoxin(self, rig, enabled, path='XY9.Garbodor_57'):
        garbodor = self.add(rig, definition(path), P2, 'bench')
        if enabled:
            tool = self.add(rig, definition('BW9.FloatStone_99'), P2, 'hand')
            rig.attach(tool, garbodor)
        return garbodor

    async def test_maxie_cannot_play_anorith_even_under_garbotoxin(self):
        for enabled in (False, True):
            rig, _ = self.clean()
            self.garbotoxin(rig, enabled)
            anorith = self.add(rig, definition('XY11.Anorith_56'), P1, 'discard')
            trainer_def = definition('XY5.MaxiesHiddenBallTrick_133')
            trainer = self.add(rig, trainer_def, P1, 'hand')
            self.assertFalse(trainer_def.condition(rig.board, P1, trainer))
            ctx = EffectContext(rig.session, P1, trainer, None)
            ctx.choose_cards = AsyncMock(return_value=[anorith])
            ctx.draw_cards = AsyncMock()
            await trainer_def.effect(ctx)
            ctx.choose_cards.assert_not_awaited()
            ctx.draw_cards.assert_not_awaited()
            self.assertEqual(anorith._containing_area_name(), 'discard')

    async def test_archie_palafin_all_prints_with_and_without_garbotoxin(self):
        for printing in self.palafins:
            for garbo in self.garbodors:
                for enabled in (False, True):
                    with self.subTest(printing=printing, garbo=garbo, enabled=enabled):
                        rig, _ = self.clean()
                        self.garbotoxin(rig, enabled, garbo)
                        target = self.add(rig, definition(printing), P1, 'discard')
                        trainer_def = definition('XY5.ArchiesAceintheHole_124')
                        trainer = self.add(rig, trainer_def, P1, 'hand')
                        self.assertEqual(trainer_def.condition(rig.board, P1, trainer), enabled)
                        rig.to_area(trainer, P1, 'discard')
                        ctx = EffectContext(rig.session, P1, trainer, None)
                        ctx.choose_cards = AsyncMock(return_value=[target])
                        await trainer_def.effect(ctx)
                        self.assertEqual(target._containing_area_name(), 'bench' if enabled else 'discard')
                        self.assertEqual(len(ctx.hand()), 5 if enabled else 0)
                        if not enabled:
                            ctx.choose_cards.assert_not_awaited()

    async def test_cinnabar_lure_never_selects_palafin_or_restored(self):
        for garbo in self.garbodors:
            for enabled in (False, True):
                rig, entities = self.clean('SV08.Tatsugiriex_142')
                self.garbotoxin(rig, enabled, garbo)
                targets = [self.add(rig, definition(p), P1, 'deck') for p in
                           (*self.palafins, 'XY11.Anorith_56')]
                ability = next(a for a in definition('SV08.Tatsugiriex_142').abilities
                               if a.title == 'Cinnabar Lure')
                ctx = EffectContext(rig.session, P1, entities['target'], ability)
                ctx.choose_cards = AsyncMock(return_value=[])
                await ability.effect(ctx)
                pool = ctx.choose_cards.await_args.args[0]
                shown = ctx.choose_cards.await_args.kwargs['display_cards']
                for card in targets:
                    self.assertIn(card, shown)
                    self.assertNotIn(card, pool)
                    self.assertFalse(out_of_play_ability_locked(rig.board, card))
                    self.assertEqual(card._containing_area_name(), 'deck')

    async def test_archie_mixed_discard_only_offers_legal_targets(self):
        rig, _ = self.clean()
        palafin = self.add(rig, definition(self.palafins[0]), P1, 'discard')
        ordinary = self.add(rig, definition('BW1.Oshawott_27'), P1, 'discard')
        trainer_def = definition('XY5.ArchiesAceintheHole_124')
        trainer = self.add(rig, trainer_def, P1, 'hand')
        self.assertTrue(trainer_def.condition(rig.board, P1, trainer))
        rig.to_area(trainer, P1, 'discard')
        ctx = EffectContext(rig.session, P1, trainer, None)
        ctx.choose_cards = AsyncMock(return_value=[ordinary])
        await trainer_def.effect(ctx)
        self.assertEqual(ctx.choose_cards.await_args.args[0], [ordinary])
        self.assertEqual(palafin._containing_area_name(), 'discard')

    async def test_claw_fossil_still_benches_anorith_from_bottom_seven(self):
        rig, _ = self.clean()
        anorith = self.add(rig, definition('XY11.Anorith_56'), P1, 'deck')
        deck = rig.board.find_player_area(P1, 'deck')
        deck.children.remove(anorith)
        deck.children.insert(0, anorith)
        fossil_def = definition('XY11.ClawFossilAnorith_100')
        fossil = self.add(rig, fossil_def, P1, 'hand')
        ctx = EffectContext(rig.session, P1, fossil, None)
        ctx.choose_cards = AsyncMock(return_value=[anorith])
        await fossil_def.effect(ctx)
        self.assertEqual(ctx.choose_cards.await_args.args[0], [anorith])
        self.assertEqual(anorith._containing_area_name(), 'bench')

    async def test_specific_restored_support_and_wrong_fossil(self):
        for path, title, zone, allowed in (
            ('BW5.TwistMountain_101', None, 'hand', True),
            ('XY10.Omastar_18', 'Restoring Beam', 'deck', True),
            ('XY3.FossilResearcher_92', None, 'deck', False),
            ('XY10.OldAmberAerodactyl_106', None, 'deck', False),
        ):
            rig, _ = self.clean()
            source_def = definition(path)
            source = self.add(rig, source_def, P1, 'hand')
            ability = next((a for a in source_def.abilities if a.title == title), None)
            target = self.add(rig, definition('XY11.Anorith_56'), P1, zone)
            ctx = EffectContext(rig.session, P1, source, ability)
            self.assertEqual(ctx.can_bench_pokemon(target), allowed)
            self.assertEqual(await ctx.bench_pokemon(target), allowed)

    async def test_zero_to_hero_still_swaps_from_deck(self):
        rig, entities = self.clean('SV06.Palafin_60')
        outgoing = entities['target']
        rig.to_area(outgoing, P1, 'bench')
        target = self.add(rig, definition(self.palafins[0]), P1, 'deck')
        ability = next(a for a in definition('SV06.Palafin_60').abilities if a.title == 'Zero to Hero')
        ctx = EffectContext(rig.session, P1, outgoing, ability)
        ctx.search_deck = AsyncMock(return_value=[target])
        await ability.effect(ctx)
        self.assertEqual(target._containing_area_name(), 'bench')
        self.assertEqual(outgoing._containing_area_name(), 'deck')

    async def test_hand_entry_and_stale_selection_recheck(self):
        rig, _ = self.clean()
        garbodor = self.garbotoxin(rig, True)
        target = self.add(rig, definition(self.palafins[0]), P1, 'hand')
        self.assertFalse(pokemon_play_blocked(rig.board, P1, target))
        rig.to_area(garbodor.children[0], P2, 'discard')
        self.assertTrue(pokemon_play_blocked(rig.board, P1, target))
        ctx = EffectContext(rig.session, P1, rig.board.active_pokemon(P1), None)
        self.assertFalse(await ctx.bench_pokemon(target))
        rig.to_area(target, P1, 'bench')
        self.assertFalse(pokemon_entry_blocked(rig.board, P1, target))

    async def test_generic_identity_swap_cannot_bypass_hero_spirit(self):
        rig, entities = self.clean()
        target = self.add(rig, definition(self.palafins[0]), P1, 'hand')
        ctx = EffectContext(rig.session, P1, entities['target'], None)
        self.assertFalse(await ctx.identity_swap(entities['target'], target))
        self.assertEqual(target._containing_area_name(), 'hand')

    async def test_all_restored_prints_require_matching_fossil(self):
        restored = [model for model in loader.cards
                    if 'restored' in {s.casefold() for s in
                       (getattr(def_for(model.guid), 'subtypes', []) or [])}]
        self.assertGreaterEqual(len(restored), 13)
        for model in restored:
            with self.subTest(card=model.guid):
                rig, _ = self.clean()
                target = self.add(rig, def_for(model.guid), P1, 'deck')
                self.assertEqual(target.get_attribute(AttrID.STAGE), PokemonStage.RESTORED)
                self.assertTrue(pokemon_entry_blocked(rig.board, P1, target))
                fossil_key = target.get_attribute(AttrID.EVOLUTION_LOGIC_FROM)
                fossil_model = next(c for c in loader.cards
                    if getattr(def_for(c.guid), 'name', '').endswith('.' + fossil_key + '.Name')
                    and '.trainer.' in getattr(def_for(c.guid), 'name', ''))
                fossil = self.add(rig, def_for(fossil_model.guid), P1, 'hand')
                ctx = EffectContext(rig.session, P1, fossil, None)
                self.assertTrue(ctx.can_bench_pokemon(target))

    async def test_fossil_researcher_allows_amaura_and_tyrunt(self):
        rig, _ = self.clean()
        source = self.add(rig, definition('XY3.FossilResearcher_92'), P1, 'hand')
        ctx = EffectContext(rig.session, P1, source, None)
        for path in ('XY3.Amaura_25', 'XY3.Tyrunt_61'):
            target = self.add(rig, definition(path), P1, 'deck')
            self.assertTrue(await ctx.bench_pokemon(target))

    async def test_twist_mountain_and_restoring_beam_still_resolve(self):
        for path, title, zone in (
            ('BW5.TwistMountain_101', None, 'hand'),
            ('XY10.Omastar_18', 'Restoring Beam', 'deck'),
        ):
            rig, _ = self.clean()
            source_def = definition(path)
            source = self.add(rig, source_def, P1, 'hand')
            ability = (next(a for a in source_def.abilities if a.title == title)
                       if title else source_def.ability)
            target = self.add(rig, definition('XY11.Anorith_56'), P1, zone)
            ctx = EffectContext(rig.session, P1, source, ability)
            ctx.flip_coins = AsyncMock(return_value=[True])
            ctx.choose_cards = AsyncMock(return_value=[target])
            ctx.search_deck = AsyncMock(return_value=[target])
            await ability.effect(ctx)
            self.assertEqual(target._containing_area_name(), 'bench')

    async def test_maxie_still_allows_evolutions_of_restored_pokemon(self):
        rig, _ = self.clean()
        target = self.add(rig, definition('BW3.Archeops_67'), P1, 'discard')
        trainer_def = definition('XY5.MaxiesHiddenBallTrick_133')
        source = self.add(rig, trainer_def, P1, 'hand')
        self.assertTrue(trainer_def.condition(rig.board, P1, source))
        rig.to_area(source, P1, 'discard')
        ctx = EffectContext(rig.session, P1, source, None)
        ctx.choose_cards = AsyncMock(return_value=[target])
        await trainer_def.effect(ctx)
        self.assertEqual(target._containing_area_name(), 'bench')
        self.assertEqual(len(ctx.hand()), 5)


if __name__ == '__main__':
    unittest.main()
