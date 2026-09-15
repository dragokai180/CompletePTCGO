"""Resolve the SM Stadium review flags with both-player outcome scenarios."""
import unittest
from unittest.mock import AsyncMock
from tests import test_hgss_rules as fixtures
from tests import test_sm_swsh_final_trainers as helpers
from spirit.game.attributes import PokemonTypes
from spirit.game.session.effects import EffectContext
from spirit.tools.effect_smoke import P1, P2


class StadiumClosureTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add
    energy = helpers.RemainingTrainerTests.energy

    def stadium_context(self, path, pid):
        rig, e = self.rig(path, 'trainer')
        stadium = e['target']
        rig.board.move_card(stadium.entity_id, rig.board.find_global_area('activeStadium').entity_id)
        stadium.owning_player_id = P1
        rig.session.turn_state.active_player_id = pid
        return rig, EffectContext(rig.session, pid, stadium, fixtures.definition(path).ability)

    async def test_viridian_forest_and_giant_hearth_pay_before_typed_private_search(self):
        for pid in (P1, P2):
            for path, count in (('SM9.ViridianForest_156', 1), ('SM11.GiantHearth_197', 2)):
                rig, ctx = self.stadium_context(path, pid)
                cost = self.energy(rig, PokemonTypes.METAL, pid=pid)
                fire = self.energy(rig, PokemonTypes.FIRE, zone='deck', pid=pid)
                water = self.energy(rig, PokemonTypes.WATER, zone='deck', pid=pid)
                special = self.add(rig, fixtures.definition('SM1.DoubleColorlessEnergy_136'), pid, 'deck')
                ctx.choose_cards = AsyncMock(return_value=[cost])
                ctx.ask_yes_no = AsyncMock(return_value=True)
                async def search(predicate, *args, **kwargs):
                    self.assertIn(cost, ctx.discard_pile())
                    self.assertTrue(predicate(fire))
                    self.assertEqual(predicate(water), count == 1)
                    self.assertFalse(predicate(special))
                    self.assertEqual(kwargs.get('count', args[0] if args else 1), count)
                    self.assertEqual(kwargs['minimum'], 0)
                    return [fire]
                ctx.search_deck = AsyncMock(side_effect=search)
                await ctx.ability.effect(ctx)
                ctx.search_deck.assert_awaited_once()
                self.assertIn(fire, ctx.hand())
                self.assertIn(water, ctx.deck())

    async def test_stadium_once_per_turn_resets_for_the_other_player(self):
        from spirit.game.session.legal_actions import _stadium_ability_entries
        rig, ctx = self.stadium_context('SM9.ViridianForest_156', P1)
        ts = rig.session.turn_state
        self.assertTrue(_stadium_ability_entries(rig.board, ts, P1, 'test'))
        ts.used_abilities.add((ctx.source.entity_id, ctx.ability.ability_id))
        self.assertFalse(_stadium_ability_entries(rig.board, ts, P1, 'test'))
        ts.begin_turn(P2, rig.board)
        self.assertTrue(_stadium_ability_entries(rig.board, ts, P2, 'test'))

    async def test_failed_private_stadium_search_still_pays_and_shuffles(self):
        for path in ('SM9.ViridianForest_156', 'SM11.GiantHearth_197'):
            rig, ctx = self.stadium_context(path, P1)
            cost = self.energy(rig, PokemonTypes.METAL)
            ctx.choose_cards = AsyncMock(return_value=[cost])
            ctx.search_deck = AsyncMock(return_value=[])
            ctx.shuffle_deck = AsyncMock()
            await ctx.ability.effect(ctx)
            self.assertIn(cost, ctx.discard_pile())
            self.assertEqual(ctx.search_deck.call_args.kwargs['minimum'], 0)
            ctx.shuffle_deck.assert_awaited_once()

    async def test_heat_factory_discards_one_fire_before_drawing_three(self):
        for pid in (P1, P2):
            rig, ctx = self.stadium_context('SM8.HeatFactory_178', pid)
            fire = self.energy(rig, PokemonTypes.FIRE, pid=pid)
            wrong = self.energy(rig, PokemonTypes.WATER, pid=pid)
            async def choose(pool, count, **kwargs):
                self.assertIn(fire, pool); self.assertNotIn(wrong, pool)
                self.assertEqual(count, 1)
                return [fire]
            async def draw(count, **kwargs):
                self.assertIn(fire, ctx.discard_pile())
                self.assertEqual(count, 3)
            ctx.choose_cards = AsyncMock(side_effect=choose)
            ctx.ask_yes_no = AsyncMock(return_value=True)
            ctx.draw_cards = AsyncMock(side_effect=draw)
            await ctx.ability.effect(ctx)
            ctx.draw_cards.assert_awaited_once()
            self.assertIn(wrong, ctx.hand())

    async def test_mt_coronet_recovers_only_two_metal_and_resolves_with_one(self):
        for pid in (P1, P2):
            for available in (1, 3):
                rig, ctx = self.stadium_context('SM5.MtCoronet_130', pid)
                for c in list(ctx.discard_pile()): rig.to_area(c, pid, 'deck')
                metal = [self.energy(rig, PokemonTypes.METAL, zone='discard', pid=pid) for _ in range(available)]
                wrong = self.energy(rig, PokemonTypes.WATER, zone='discard', pid=pid)
                async def choose(pool, count, **kwargs):
                    self.assertNotIn(wrong, pool)
                    self.assertEqual(set(pool), set(metal))
                    self.assertLessEqual(count, 2)
                    return metal[:2]
                ctx.choose_cards = AsyncMock(side_effect=choose)
                ctx.ask_yes_no = AsyncMock(return_value=True)
                await ctx.ability.effect(ctx)
                self.assertTrue(all(c in ctx.hand() for c in metal[:2]))
                self.assertIn(wrong, ctx.discard_pile())
                if available == 3: self.assertIn(metal[2], ctx.discard_pile())

    async def test_brooklet_hill_benches_only_water_or_fighting_basics(self):
        for pid in (P1, P2):
            rig, ctx = self.stadium_context('SM2.BrookletHill_120', pid)
            water = self.add(rig, fixtures.definition('SWSH6.IceRiderCalyrexV_45'), pid, 'deck')
            evolution = self.add(rig, fixtures.definition('SWSH6.Walrein_39'), pid, 'deck')
            wrong = self.add(rig, fixtures.definition('SM12.Flareon_25'), pid, 'deck')
            ctx.search_deck = AsyncMock(return_value=[water])
            ctx.ask_yes_no = AsyncMock(return_value=True)
            await ctx.ability.effect(ctx)
            pred = ctx.search_deck.call_args.args[0]
            self.assertTrue(pred(water)); self.assertFalse(pred(evolution)); self.assertFalse(pred(wrong))
            self.assertIn(water, ctx.my_bench())
            self.assertNotIn(water, ctx.hand())

    async def test_ultra_space_puts_ultra_beast_in_hand_not_on_bench(self):
        for pid in (P1, P2):
            rig, ctx = self.stadium_context('SM6.UltraSpace_115', pid)
            beast = self.add(rig, fixtures.definition('SM10.PheromosaBuzzwoleGX_1'), pid, 'deck')
            wrong = self.add(rig, fixtures.definition('SM12.ArceusDialgaPalkiaGX_156'), pid, 'deck')
            ctx.search_deck = AsyncMock(return_value=[beast])
            ctx.ask_yes_no = AsyncMock(return_value=True)
            await ctx.ability.effect(ctx)
            pred = ctx.search_deck.call_args.args[0]
            self.assertTrue(pred(beast)); self.assertFalse(pred(wrong))
            self.assertIn(beast, ctx.hand()); self.assertNotIn(beast, ctx.my_bench())
