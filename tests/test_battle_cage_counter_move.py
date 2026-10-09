"""Battle Cage blocks placement, not removal, during counter movement."""
import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures
from spirit.game.attributes import AttrID
from spirit.game.session.effects import EffectContext
from spirit.tools.effect_smoke import P1, P2


class BattleCageCounterMoveTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    def setup_move(self):
        rig, entities = self.rig('SV06.Munkidori_95')
        stadium = self.add(rig, fixtures.definition('ME2.BattleCage_85'),
                           P2, 'hand')
        rig.board.move_card(
            stadium.entity_id,
            rig.board.find_global_area('activeStadium').entity_id,
        )
        stadium.owning_player_id = P2
        ability = next(a for a in fixtures.definition('SV06.Munkidori_95').abilities
                       if a.title == 'Adrena-Brain')
        ctx = EffectContext(rig.session, P1, entities['target'], ability)
        for pokemon in (entities['target'], ctx.opponent_bench()[0]):
            pokemon.set_attribute(AttrID.HP, ctx.max_hp(pokemon) - 30)
        return rig, entities, ctx

    async def test_blocked_benched_destination_removes_source_counters(self):
        rig, entities, ctx = self.setup_move()
        source = entities['target']
        bench = ctx.opponent_bench()[0]
        source_hp = source.get_attribute(AttrID.HP)
        bench_hp = bench.get_attribute(AttrID.HP)

        self.assertEqual(await ctx.move_damage_counters(source, bench, 2), 2)
        self.assertEqual(source.get_attribute(AttrID.HP), source_hp + 20)
        self.assertEqual(bench.get_attribute(AttrID.HP), bench_hp)

        active = entities['p2_active']
        active_hp = active.get_attribute(AttrID.HP)
        self.assertEqual(await ctx.move_damage_counters(source, active, 1), 1)
        self.assertEqual(source.get_attribute(AttrID.HP), source_hp + 30)
        self.assertEqual(active.get_attribute(AttrID.HP), active_hp - 10)

    async def test_mixed_distribution_places_only_on_unprotected_target(self):
        rig, entities, ctx = self.setup_move()
        source = entities['target']
        bench = ctx.opponent_bench()[0]
        active = entities['p2_active']
        hp = {p.entity_id: p.get_attribute(AttrID.HP)
              for p in (source, bench, active)}
        rig.session.prompt_damage_counter_placement = AsyncMock(return_value={
            bench.entity_id: 1, active.entity_id: 1,
        })

        self.assertEqual(await ctx.move_damage_counters(
            source, [bench, active], 2), 2)
        self.assertEqual(source.get_attribute(AttrID.HP), hp[source.entity_id] + 20)
        self.assertEqual(bench.get_attribute(AttrID.HP), hp[bench.entity_id])
        self.assertEqual(active.get_attribute(AttrID.HP), hp[active.entity_id] - 10)

    async def test_adrena_brain_can_choose_protected_bench(self):
        rig, entities, ctx = self.setup_move()
        source = entities['target']
        active = entities['p2_active']
        bench = ctx.opponent_bench()[0]
        source_hp = source.get_attribute(AttrID.HP)
        bench_hp = bench.get_attribute(AttrID.HP)
        ctx.choose_pokemon = AsyncMock(side_effect=[source, bench])
        ctx.choose = AsyncMock(return_value=0)

        await ctx.ability.effect(ctx)

        offered = ctx.choose_pokemon.await_args_list[1].args[0]
        self.assertEqual(offered, [active, *ctx.opponent_bench()])
        self.assertEqual(source.get_attribute(AttrID.HP), source_hp + 10)
        self.assertEqual(bench.get_attribute(AttrID.HP), bench_hp)

    async def test_sinister_hand_can_move_from_bench_to_active(self):
        rig, entities, _ = self.setup_move()
        ability = next(a for a in fixtures.definition('BW7.Dusknoir_63').abilities
                       if a.title == 'Sinister Hand')
        dusknoir = self.add(rig, fixtures.definition('BW7.Dusknoir_63'),
                            P1, 'bench')
        ctx = EffectContext(rig.session, P1, dusknoir, ability)
        source = ctx.opponent_bench()[0]
        dest = ctx.opponent_active()
        source_hp = source.get_attribute(AttrID.HP)
        dest_hp = dest.get_attribute(AttrID.HP)
        ctx.choose_pokemon = AsyncMock(side_effect=[source, dest])
        rig.session.prompt_damage_counter_placement = AsyncMock(
            return_value={source.entity_id: 1})

        await ctx.ability.effect(ctx)
        self.assertEqual(ctx.choose_pokemon.await_count, 2)
        self.assertEqual(source.get_attribute(AttrID.HP), source_hp + 10)
        self.assertEqual(dest.get_attribute(AttrID.HP), dest_hp - 10)

    async def test_sinister_hand_to_bench_removes_without_placing(self):
        rig, entities, _ = self.setup_move()
        ability = next(a for a in fixtures.definition('BW7.Dusknoir_63').abilities
                       if a.title == 'Sinister Hand')
        dusknoir = self.add(rig, fixtures.definition('BW7.Dusknoir_63'),
                            P1, 'bench')
        ctx = EffectContext(rig.session, P1, dusknoir, ability)
        source = ctx.opponent_active()
        dest = ctx.opponent_bench()[0]
        source.set_attribute(AttrID.HP, ctx.max_hp(source) - 30)
        source_hp = source.get_attribute(AttrID.HP)
        dest_hp = dest.get_attribute(AttrID.HP)

        self.assertEqual(await ctx.move_damage_counters(source, dest, 1), 1)
        self.assertEqual(source.get_attribute(AttrID.HP), source_hp + 10)
        self.assertEqual(dest.get_attribute(AttrID.HP), dest_hp)


if __name__ == '__main__':
    unittest.main()
