"""Trainer choices, paid discards and conditional draws resolve together."""
import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures
from spirit.game.attributes import PokemonTypes
from spirit.game.data_utils import def_for
from spirit.game.session.effects import EffectContext
from spirit.game.session.legal_actions import compute_legal_actions
from spirit.game.card_effects.bw_era import _pokemon_ex
from spirit.game.session.passives import effective_bench_capacity
from spirit.tools.effect_smoke import P1, P2


class TrainerChoiceAndDiscardTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    def trainer(self, path):
        rig, entities = self.rig(path, 'trainer')
        ctx = EffectContext(rig.session, P1, entities['target'], None)
        return rig, entities['target'], ctx

    async def test_scorched_earth_pays_energy_and_draws_for_either_player(self):
        card = fixtures.definition('XY5.ScorchedEarth_138')
        for pid, kind in ((P1, PokemonTypes.FIRE),
                          (P2, PokemonTypes.FIGHTING)):
            with self.subTest(player=pid, energy=kind):
                rig, source, _ = self.trainer('XY5.ScorchedEarth_138')
                stadium = rig.board.find_global_area('activeStadium')
                rig.board.move_card(source.entity_id, stadium.entity_id)
                ctx = EffectContext(rig.session, pid, source, card.ability)
                energy = self.add(rig, def_for(self.energies[kind.value]),
                                  pid, 'hand')
                actions = compute_legal_actions(
                    rig.board, rig.session.turn_state, pid, rig.session.game_id)
                self.assertTrue(any(
                    entry['entityID'] == source.entity_id
                    and entry['selectableAction']['actionID'] == card.ability.ability_id
                    for entry in actions))
                deck_before = len(ctx.deck(pid))
                ctx.choose_cards = AsyncMock(return_value=[energy])
                await card.ability.effect(ctx)
                self.assertIn(energy, ctx.discard_pile(pid))
                self.assertEqual(len(ctx.deck(pid)), deck_before - 2)

    async def test_cycling_road_discards_basic_energy_before_drawing(self):
        card = fixtures.definition('SV035.CyclingRoad_157')
        rig, source, _ = self.trainer('SV035.CyclingRoad_157')
        rig.board.move_card(
            source.entity_id,
            rig.board.find_global_area('activeStadium').entity_id,
        )
        ctx = EffectContext(rig.session, P1, source, card.ability)
        energy = self.add(rig, def_for(self.energies[PokemonTypes.WATER.value]),
                          P1, 'hand')
        before = len(ctx.deck())
        ctx.choose_cards = AsyncMock(return_value=[energy])
        await card.ability.effect(ctx)
        self.assertIn(energy, ctx.discard_pile())
        self.assertEqual(len(ctx.deck()), before - 1)

    async def test_heat_factory_still_draws_three(self):
        card = fixtures.definition('SM8.HeatFactory_178')
        rig, source, _ = self.trainer('SM8.HeatFactory_178')
        rig.board.move_card(
            source.entity_id,
            rig.board.find_global_area('activeStadium').entity_id,
        )
        ctx = EffectContext(rig.session, P1, source, card.ability)
        energy = self.add(rig, def_for(self.energies[PokemonTypes.FIRE.value]),
                          P1, 'hand')
        before = len(ctx.deck())
        ctx.choose_cards = AsyncMock(return_value=[energy])
        await card.ability.effect(ctx)
        self.assertIn(energy, ctx.discard_pile())
        self.assertEqual(len(ctx.deck()), before - 3)

    async def test_brigette_filters_each_branch_and_benches_the_selection(self):
        for branch in (0, 1):
            with self.subTest(branch=branch):
                rig, _, ctx = self.trainer('XY8.Brigette_134')
                old_ex = self.add(rig, fixtures.definition('XY8.MewtwoEX_61'),
                                  P1, 'deck')
                modern_ex = self.add(rig, fixtures.definition('SV1.Miraidonex_81'),
                                     P1, 'deck')
                plain = self.add(rig, self.filler, P1, 'deck')
                ctx.choose = AsyncMock(return_value=branch)
                chosen = [old_ex] if branch == 0 else [modern_ex, plain]
                ctx.search_deck = AsyncMock(return_value=chosen)
                await fixtures.definition('XY8.Brigette_134').effect(ctx)
                ctx.choose.assert_awaited_once()
                predicate = ctx.search_deck.await_args.args[0]
                self.assertEqual(predicate(old_ex), branch == 0)
                self.assertEqual(predicate(modern_ex), branch == 1)
                self.assertEqual(predicate(plain), branch == 1)
                self.assertEqual(ctx.search_deck.await_args.kwargs['count'],
                                 1 if branch == 0 else 3)
                for pokemon in chosen:
                    self.assertIn(pokemon, ctx.my_bench())
                self.assertEqual(_pokemon_ex(old_ex), True)
                self.assertEqual(_pokemon_ex(modern_ex), False)

    async def test_brigette_unavailable_with_full_bench(self):
        rig, source, _ = self.trainer('XY8.Brigette_134')
        bench = rig.board.find_player_area(P1, 'bench')
        while len(bench.children) < effective_bench_capacity(rig.board, P1):
            self.add(rig, self.filler, P1, 'bench')
        self.assertFalse(fixtures.definition('XY8.Brigette_134').condition(
            rig.board, P1, source))

    async def test_brigette_caps_the_three_basic_branch_to_free_slots(self):
        rig, _, ctx = self.trainer('XY8.Brigette_161')
        bench = rig.board.find_player_area(P1, 'bench')
        while len(bench.children) < effective_bench_capacity(rig.board, P1) - 1:
            self.add(rig, self.filler, P1, 'bench')
        chosen = self.add(rig, self.filler, P1, 'deck')
        ctx.choose = AsyncMock(return_value=1)
        ctx.search_deck = AsyncMock(return_value=[chosen])
        await fixtures.definition('XY8.Brigette_161').effect(ctx)
        self.assertEqual(ctx.search_deck.await_args.kwargs['count'], 1)
        self.assertIn(chosen, ctx.my_bench())

    async def test_roller_skater_draws_two_or_four_for_paid_card(self):
        for kind, expected in (('item', 2), ('energy', 4)):
            with self.subTest(discarded=kind):
                rig, _, ctx = self.trainer('SM12.RollerSkater_203')
                card = self.add(
                    rig,
                    def_for(self.energies[PokemonTypes.FIRE.value])
                    if kind == 'energy' else self.item,
                    P1, 'hand',
                )
                ctx.choose_cards = AsyncMock(return_value=[card])
                before = len(ctx.deck())
                await fixtures.definition('SM12.RollerSkater_203').effect(ctx)
                self.assertIn(card, ctx.discard_pile())
                self.assertEqual(len(ctx.deck()), before - expected)

    async def test_team_grunts_draw_bonus_only_for_their_team(self):
        for path, pokemon_path in (
                ('TATM.TeamAquaGrunt_26', 'TATM.TeamAquasCarvanha_20'),
                ('TATM.TeamMagmaGrunt_30', 'TATM.TeamMagmasNumel_1')):
            for matching in (True, False):
                with self.subTest(trainer=path, matching=matching):
                    rig, _, ctx = self.trainer(path)
                    chosen = self.add(rig, fixtures.definition(pokemon_path)
                                      if matching else self.filler, P1, 'hand')
                    ctx.choose_cards = AsyncMock(return_value=[chosen])
                    before = len(ctx.deck())
                    await fixtures.definition(path).effect(ctx)
                    self.assertIn(chosen, ctx.discard_pile())
                    self.assertEqual(len(ctx.deck()), before - (4 if matching else 3))

    async def test_psychics_third_eye_draws_exactly_cards_discarded(self):
        rig, _, ctx = self.trainer('XY9.PsychicsThirdEye_108')
        cards = list(ctx.hand())[:2]
        ctx.reveal_hand = AsyncMock(return_value=list(ctx.hand(P2)))
        ctx.choose_cards = AsyncMock(return_value=cards)
        before = len(ctx.deck())
        await fixtures.definition('XY9.PsychicsThirdEye_108').effect(ctx)
        ctx.reveal_hand.assert_awaited_once_with(P2, P1)
        self.assertTrue(all(card in ctx.discard_pile() for card in cards))
        self.assertEqual(len(ctx.deck()), before - 2)


if __name__ == '__main__':
    unittest.main()
