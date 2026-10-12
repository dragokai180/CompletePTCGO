"""Attached Tool passives change bench damage and attack costs."""

import unittest

from tests import test_hgss_rules as fixtures
from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.session.legal_actions import _attack_entries
from spirit.game.session.passives import compute_damage, effective_attack_cost
from spirit.tools.effect_smoke import P1, P2


class WideLensSparklingCrystalTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx
    add = fixtures.HgssRulesTests.add

    async def test_wide_lens_applies_opponent_bench_weakness_and_resistance(self):
        rig, entities, ctx = self.ctx('SM10.Venonat_9', 'Radar Eyes')
        attacker = entities['target']
        bench = ctx.opponent_bench()[0]
        attack_type = PokemonTypes.GRASS.value
        bench.set_attribute(AttrID.WEAKNESS_TYPES, [attack_type])
        bench.set_attribute(AttrID.RESISTANCE_TYPES, None)

        damage = lambda: compute_damage(
            rig.board, attacker, bench, 30, apply_modifiers=False).amount
        self.assertEqual(damage(), 30)
        tool = self.add(rig, fixtures.definition('XY6.WideLens_95'), P1, 'hand')
        rig.attach(tool, attacker)
        self.assertEqual(damage(), 60)
        bench.set_attribute(AttrID.WEAKNESS_TYPES, [])
        bench.set_attribute(AttrID.RESISTANCE_TYPES, attack_type)
        bench.set_attribute(AttrID.RESISTANCE_AMOUNT, 20)
        self.assertEqual(damage(), 10)

        own_bench = ctx.my_bench()[0]
        own_bench.set_attribute(AttrID.WEAKNESS_TYPES, [attack_type])
        self.assertEqual(compute_damage(
            rig.board, attacker, own_bench, 30,
            apply_modifiers=False).amount, 30)
        rig.to_area(tool, P1, 'hand')
        rig.attach(tool, own_bench)
        self.assertEqual(damage(), 30)

    async def test_sparkling_crystal_discounts_tera_attack_and_enables_it(self):
        for path in ('SV07.SparklingCrystal_142', 'SV085.SparklingCrystal_129'):
            with self.subTest(path=path):
                rig, entities, ctx = self.ctx('SV07.Laprasex_32', 'Larimar Rain')
                attacker = entities['target']
                for energy in list(rig.board.attached_energies(attacker)):
                    rig.to_area(energy, P1, 'hand')
                rig.attach_energy_type(P1, attacker, PokemonTypes.WATER.value)
                rig.attach_energy_type(P1, attacker, PokemonTypes.PSYCHIC.value)
                cost = ctx.ability.to_dict()['cost']
                effective = lambda: effective_attack_cost(
                    rig.board, attacker, cost, ctx.ability)
                legal = lambda: {entry['selectableAction']['actionID'] for entry in
                                 _attack_entries(rig.board, rig.session.turn_state,
                                                 P1, rig.session.game_id)}
                self.assertEqual(effective(), cost)
                self.assertNotIn(ctx.ability.ability_id, legal())
                tool = self.add(rig, fixtures.definition(path), P1, 'hand')
                rig.attach(tool, attacker)
                self.assertEqual(effective(), {'Water': 1, 'Psychic': 1})
                self.assertIn(ctx.ability.ability_id, legal())

    async def test_sparkling_crystal_can_reduce_typed_symbol_instead_of_colorless(self):
        rig, entities, ctx = self.ctx('SV07.Galvantulaex_51', 'Charged Web')
        attacker = entities['target']
        for energy in list(rig.board.attached_energies(attacker)):
            rig.to_area(energy, P1, 'hand')
        rig.attach_energy_type(P1, attacker, PokemonTypes.GRASS.value)
        tool = self.add(
            rig, fixtures.definition('SV07.SparklingCrystal_142'), P1, 'hand')
        rig.attach(tool, attacker)
        cost = ctx.ability.to_dict()['cost']
        self.assertEqual(cost, {'Lightning': 1, 'Colorless': 1})
        self.assertEqual(effective_attack_cost(
            rig.board, attacker, cost, ctx.ability), {'Colorless': 1})
        legal = {entry['selectableAction']['actionID'] for entry in
                 _attack_entries(rig.board, rig.session.turn_state,
                                 P1, rig.session.game_id)}
        self.assertIn(ctx.ability.ability_id, legal)

    async def test_other_tool_cost_and_weakness_modifiers(self):
        rig, entities, ctx = self.ctx('SV07.Laprasex_32', 'Power Splash')
        attacker = entities['target']
        cost = {'Colorless': 1, 'Fighting': 1}
        counter_gain = self.add(
            rig, fixtures.definition('SV08.CounterGain_169'), P1, 'hand')
        rig.attach(counter_gain, attacker)
        self.assertEqual(effective_attack_cost(rig.board, attacker, cost), cost)
        opponent_prizes = rig.board.find_player_area(P2, 'prizePile')
        rig.to_area(opponent_prizes.children[-1], P2, 'discard')
        self.assertEqual(effective_attack_cost(
            rig.board, attacker, cost), {'Fighting': 1})
        rig.to_area(counter_gain, P1, 'hand')

        karate_belt = self.add(
            rig, fixtures.definition('SM11.KarateBelt_201'), P1, 'hand')
        rig.attach(karate_belt, attacker)
        self.assertEqual(effective_attack_cost(
            rig.board, attacker, cost), {'Colorless': 1})
        rig.to_area(karate_belt, P1, 'hand')

        target = ctx.defender
        target.set_attribute(
            AttrID.WEAKNESS_TYPES, [PokemonTypes.WATER.value])
        glasses = self.add(
            rig, fixtures.definition('SWSH10.SupereffectiveGlasses_152'),
            P1, 'hand')
        rig.attach(glasses, attacker)
        self.assertEqual(compute_damage(
            rig.board, attacker, target, 30).amount, 90)

    async def test_hops_choice_band_applies_only_to_its_named_holder(self):
        rig, entities, ctx = self.ctx('SV09.HopsZacianex_111', 'Insta-Strike')
        attacker = entities['target']
        tool = self.add(
            rig, fixtures.definition('SV09.HopsChoiceBand_148'), P1, 'hand')
        rig.attach(tool, attacker)
        ctx.defender.set_attribute(AttrID.WEAKNESS_TYPES, [])
        ctx.defender.set_attribute(AttrID.RESISTANCE_TYPES, None)
        self.assertEqual(effective_attack_cost(
            rig.board, attacker, {'Colorless': 1}), {})
        self.assertEqual(compute_damage(
            rig.board, attacker, ctx.defender, 30).amount, 60)
        self.assertEqual(compute_damage(
            rig.board, attacker, ctx.opponent_bench()[0], 30,
            apply_modifiers=False).amount, 30)

        rig.to_area(tool, P1, 'hand')
        ordinary = self.add(rig, fixtures.definition('SM10.Venonat_9'), P1,
                            'bench')
        rig.attach(tool, ordinary)
        self.assertEqual(effective_attack_cost(
            rig.board, ordinary, {'Colorless': 1}), {'Colorless': 1})
        self.assertEqual(compute_damage(
            rig.board, ordinary, ctx.defender, 30).amount, 30)


if __name__ == '__main__':
    unittest.main()
