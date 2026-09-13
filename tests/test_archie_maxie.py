"""Archie/Maxie permissions and ordered resolution, including full arts."""
import unittest
from unittest.mock import AsyncMock
from tests import test_hgss_rules as fixtures
from tests.test_hgss_rules import definition
from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.session.effects import EffectContext
from spirit.tools.effect_smoke import P1


class ArchieMaxieTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add
    prints = [('XY5.ArchiesAceintheHole_124', PokemonTypes.WATER),
              ('XY5.ArchiesAceintheHole_157', PokemonTypes.WATER),
              ('XY5.MaxiesHiddenBallTrick_133', PokemonTypes.FIGHTING),
              ('XY5.MaxiesHiddenBallTrick_158', PokemonTypes.FIGHTING)]

    def scenario(self, path, kind):
        rig, e = self.rig('BW1.Snivy_1')
        for zone in ('hand', 'discard'):
            for card in list(rig.board.find_player_area(P1, zone).children):
                rig.to_area(card, P1, 'deck')
        trainer = self.add(rig, definition(path), P1, 'hand')
        # An evolved Pokemon, not a Basic: both cards allow this.
        target = self.add(rig, definition('BW1.Serperior_5'), P1, 'discard')
        target.set_attribute(AttrID.POKEMON_TYPES, [kind.value])
        return rig, trainer, target

    async def test_permissions_all_prints(self):
        for path, kind in self.prints:
            with self.subTest(path=path):
                rig, trainer, target = self.scenario(path, kind)
                check = lambda: definition(path).condition(rig.board, P1, trainer)
                self.assertTrue(check())
                extra = self.add(rig, definition('BW1.Snivy_1'), P1, 'hand')
                self.assertFalse(check())
                rig.to_area(extra, P1, 'deck')
                target.set_attribute(AttrID.POKEMON_TYPES, [PokemonTypes.GRASS.value])
                self.assertFalse(check())
                target.set_attribute(AttrID.POKEMON_TYPES, [kind.value])
                bench = rig.board.find_player_area(P1, 'bench')
                while len(bench.children) < 5:
                    self.add(rig, definition('BW1.Snivy_1'), P1, 'bench')
                self.assertFalse(check())

    async def test_bench_evolved_pokemon_before_drawing(self):
        for path, kind in self.prints:
            with self.subTest(path=path):
                rig, trainer, target = self.scenario(path, kind)
                rig.to_area(trainer, P1, 'discard')  # Played card has left hand.
                ctx = EffectContext(rig.session, P1, trainer, None)
                ctx.choose_cards = AsyncMock(return_value=[target])
                async def drawn(count):
                    self.assertIn(target, rig.board.find_player_area(P1, 'bench').children)
                    self.assertEqual(count, 5)
                ctx.draw_cards = AsyncMock(side_effect=drawn)
                await definition(path).effect(ctx)
                ctx.draw_cards.assert_awaited_once_with(5)
                self.assertEqual(ctx.choose_cards.call_args.kwargs['minimum'], 1)
                self.assertEqual(rig.session.turn_state.entered_play_turn[target.entity_id],
                                 rig.session.turn_state.turn_number)

    async def test_no_draw_if_bench_move_fails(self):
        rig, trainer, target = self.scenario(*self.prints[0])
        rig.to_area(trainer, P1, 'discard')
        ctx = EffectContext(rig.session, P1, trainer, None)
        ctx.choose_cards = AsyncMock(return_value=[target])
        ctx.bench_pokemon = AsyncMock(return_value=False)
        ctx.draw_cards = AsyncMock()
        await definition(self.prints[0][0]).effect(ctx)
        ctx.draw_cards.assert_not_awaited()

    async def test_empty_deck_does_not_prevent_recovery(self):
        for path, kind in self.prints:
            rig, trainer, target = self.scenario(path, kind)
            for card in list(rig.board.find_player_area(P1, 'deck').children):
                rig.to_area(card, P1, 'discard')
            self.assertTrue(definition(path).condition(rig.board, P1, trainer))
