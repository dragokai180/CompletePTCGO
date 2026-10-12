"""Future and Ancient card effects use the printed subtype and tool scope."""
import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures
from spirit.game.attributes import AttrID, SpecialConditions
from spirit.game.data_utils import def_for
from spirit.game.session.effects import EffectContext
from spirit.game.session.passives import (
    compute_damage, conditions_blocked, effective_max_hp, effective_retreat_cost,
)
from spirit.tools.effect_smoke import P1, P2


class FutureAncientEffectsTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx
    add = fixtures.HgssRulesTests.add

    def test_future_capsule_grants_only_future_holder_damage_and_free_retreat(self):
        for capsule in ('SV05.FutureBoosterEnergyCapsule_149',
                        'SV4.FutureBoosterEnergyCapsule_164'):
            for pokemon, future in (('SV05.IronTreads_118', True),
                                    ('SV4.BruteBonnet_123', False)):
                with self.subTest(capsule=capsule, pokemon=pokemon):
                    rig, entities = self.rig(pokemon)
                    holder = entities['target']
                    tool = self.add(rig, fixtures.definition(capsule), P1, 'hand')
                    original_retreat = effective_retreat_cost(rig.board, holder)
                    rig.attach(tool, holder)
                    self.assertEqual(effective_retreat_cost(rig.board, holder),
                                     0 if future else original_retreat)
                    damage = compute_damage(
                        rig.board, holder, entities['p2_active'], 40,
                        ignore_weakness=True, ignore_resistance=True).amount
                    self.assertEqual(damage, 60 if future else 40)
                    bench = rig.board.find_player_area(P2, 'bench').children[0]
                    bench_damage = compute_damage(
                        rig.board, holder, bench, 40,
                        ignore_weakness=True, ignore_resistance=True).amount
                    self.assertEqual(bench_damage, 40)
                    rig.to_area(tool, P1, 'hand')
                    self.assertEqual(effective_retreat_cost(rig.board, holder),
                                     original_retreat)

    async def test_ancient_capsule_hp_cure_and_condition_immunity_require_ancient(self):
        for capsule in ('SV05.AncientBoosterEnergyCapsule_140',
                        'SV4.AncientBoosterEnergyCapsule_159'):
            for pokemon, ancient in (('SV4.BruteBonnet_123', True),
                                     ('SV05.IronTreads_118', False)):
                with self.subTest(capsule=capsule, pokemon=pokemon):
                    rig, entities = self.rig(pokemon)
                    holder = entities['target']
                    holder.set_attribute(AttrID.SPECIAL_CONDITIONS, ['Confused'])
                    hp_before = effective_max_hp(rig.board, holder)
                    tool = self.add(rig, fixtures.definition(capsule), P1, 'hand')
                    rig.attach(tool, holder)
                    await rig.session.fire_tool_attached_triggers(P1, tool, holder)
                    self.assertEqual(effective_max_hp(rig.board, holder),
                                     hp_before + (60 if ancient else 0))
                    self.assertEqual(holder.get_attribute(AttrID.SPECIAL_CONDITIONS),
                                     [] if ancient else ['Confused'])
                    self.assertEqual(conditions_blocked(
                        rig.board, holder, SpecialConditions.POISONED), ancient)

    async def test_awakening_drum_counts_only_ancient_pokemon(self):
        rig, entities = self.rig('SV4.BruteBonnet_123')
        card = self.add(rig, fixtures.definition('SV05.AwakeningDrum_141'), P1, 'hand')
        ctx = EffectContext(rig.session, P1, card, None)
        count = sum('Ancient' in def_for(p.archetype_id).subtypes
                    for p in ctx.my_pokemon_in_play())
        self.assertLess(count, len(ctx.my_pokemon_in_play()))
        ctx.draw_cards = AsyncMock()
        await fixtures.definition('SV05.AwakeningDrum_141').effect(ctx)
        ctx.draw_cards.assert_awaited_once_with(count)

    async def test_iron_smasher_checks_future_subtype_not_elemental_type(self):
        rig, entities, ctx = self.ctx('SV065.SlitherWing_26', 'Iron Smasher')
        ctx.deal_damage = AsyncMock()
        await ctx.ability.effect(ctx)
        self.assertEqual(ctx.deal_damage.call_args.args[0], 20)
        self.add(rig, fixtures.definition('SV05.IronTreads_118'), P2, 'bench')
        ctx.deal_damage.reset_mock()
        await ctx.ability.effect(ctx)
        self.assertEqual(ctx.deal_damage.call_args.args[0], 140)

    async def test_supportive_singing_heals_only_benched_ancient_pokemon(self):
        rig, entities, ctx = self.ctx('SV05.ScreamTail_77', 'Supportive Singing')
        ancient = self.add(rig, fixtures.definition('SV4.BruteBonnet_123'),
                           P1, 'bench')
        ordinary = self.add(rig, fixtures.definition('SV05.IronTreads_118'),
                            P1, 'bench')
        for pokemon in (ancient, ordinary):
            pokemon.set_attribute(AttrID.HP, 20)
        ctx.choose_pokemon = AsyncMock(return_value=ancient)
        ctx.heal = AsyncMock()
        await ctx.ability.effect(ctx)
        candidates = ctx.choose_pokemon.await_args.args[0]
        self.assertIn(ancient, candidates)
        self.assertNotIn(ordinary, candidates)
        ctx.heal.assert_awaited_once_with(100, ancient)

    async def test_anachronism_repulsor_shields_only_from_ancient_attackers(self):
        rig, entities, ctx = self.ctx('SV065.IronMoth_9',
                                      'Anachronism Repulsor')
        ctx.deal_damage = AsyncMock()
        await ctx.ability.effect(ctx)
        ordinary = entities['p2_active']
        ancient = self.add(rig, fixtures.definition('SV4.BruteBonnet_123'),
                           P2, 'bench')
        target = entities['target']
        def hit(attacker):
            return compute_damage(rig.board, attacker, target, 40,
                                  ignore_weakness=True,
                                  ignore_resistance=True).amount
        self.assertEqual(hit(ordinary), 40)
        self.assertEqual(hit(ancient), 0)

    async def test_code_protect_shields_future_team_only_from_modern_ex(self):
        rig, entities, ctx = self.ctx('SV08.Miraidon_69', 'C.O.D.E.: Protect')
        ctx.deal_damage = AsyncMock()
        await ctx.ability.effect(ctx)
        ordinary = entities['p2_active']
        modern_ex = self.add(rig, fixtures.definition('SV05.WalkingWakeex_50'),
                             P2, 'bench')
        target = entities['target']
        def hit(attacker):
            return compute_damage(rig.board, attacker, target, 40,
                                  ignore_weakness=True,
                                  ignore_resistance=True).amount
        self.assertEqual(hit(ordinary), 40)
        self.assertEqual(hit(modern_ex), 0)


if __name__ == '__main__':
    unittest.main()
