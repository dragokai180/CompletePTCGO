"""Attack costs and effects conditioned on an attached Pokémon Tool."""
import unittest
from unittest.mock import AsyncMock

from spirit.game.attributes import AttrID
from spirit.game.session.legal_actions import _attack_entries
from spirit.game.session.passives import effective_attack_cost
from spirit.tools.effect_smoke import P1, P2
from tests import test_hgss_rules as fixtures


class ToolConditionalEffectsTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx
    add = fixtures.HgssRulesTests.add

    async def test_baryon_beam_requires_the_named_capsule_for_alternate_cost(self):
        rig, entities, ctx = self.ctx('SV4.IronJugulis_158', 'Baryon Beam')
        attacker = entities['target']
        cost = ctx.ability.to_dict()['cost']
        self.assertEqual(effective_attack_cost(rig.board, attacker, cost, ctx.ability),
                         {'Colorless': 5})
        unrelated = self.add(rig, fixtures.definition('BW9.FloatStone_99'), P1, 'hand')
        rig.attach(unrelated, attacker)
        self.assertEqual(effective_attack_cost(rig.board, attacker, cost, ctx.ability),
                         {'Colorless': 5})
        rig.to_area(unrelated, P1, 'hand')
        capsule = self.add(rig, fixtures.definition('SV4.FutureBoosterEnergyCapsule_164'), P1, 'hand')
        rig.attach(capsule, attacker)
        self.assertEqual(effective_attack_cost(rig.board, attacker, cost, ctx.ability),
                         {'Colorless': 3})
        self.assertEqual(effective_attack_cost(rig.board, attacker, cost,
                                               next(a for a in fixtures.definition(
                                                   'SV4.IronJugulis_158').abilities
                                                    if a.title == 'Homing Headbutt')),
                         {'Colorless': 5})

    async def test_baryon_beam_is_offered_with_three_energy_and_capsule(self):
        rig, entities, ctx = self.ctx('SV4.IronJugulis_158', 'Baryon Beam')
        attacker = entities['target']
        for energy in list(rig.board.attached_energies(attacker))[3:]:
            rig.to_area(energy, P1, 'hand')
        actions = lambda: {a['selectableAction']['actionID'] for a in
                           _attack_entries(rig.board, rig.session.turn_state,
                                           P1, rig.session.game_id)}
        self.assertNotIn(ctx.ability.ability_id, actions())
        capsule = self.add(rig, fixtures.definition('SV05.FutureBoosterEnergyCapsule_149'), P1, 'hand')
        rig.attach(capsule, attacker)
        self.assertIn(ctx.ability.ability_id, actions())

    async def test_toxic_powder_needs_ancient_capsule(self):
        rig, entities, ctx = self.ctx('SV4.BruteBonnet_123', 'Toxic Powder')
        self.assertFalse(ctx.ability.condition(rig.board, P1, entities['target']))
        wrong = self.add(rig, fixtures.definition('SV05.FutureBoosterEnergyCapsule_149'), P1, 'hand')
        rig.attach(wrong, entities['target'])
        self.assertFalse(ctx.ability.condition(rig.board, P1, entities['target']))
        rig.to_area(wrong, P1, 'hand')
        capsule = self.add(rig, fixtures.definition('SV4.AncientBoosterEnergyCapsule_159'), P1, 'hand')
        rig.attach(capsule, entities['target'])
        self.assertTrue(ctx.ability.condition(rig.board, P1, entities['target']))

    async def test_tool_damage_bonuses_cover_both_sides_and_named_tools(self):
        cases = (
            ('SV4.Absol_113', 'tool', 'SV05.FutureBoosterEnergyCapsule_149', 60),
            ('SV06.Probopass_102', 'opponent', 'BW9.FloatStone_99', 80),
            ('SM8.Wigglytuff_134', 'tool', 'SM8.FairyCharmPsychic_175', 70),
        )
        for path, side, tool_path, bonus in cases:
            with self.subTest(path=path):
                card = fixtures.definition(path)
                attack = next(a for a in card.abilities if
                              'more damage' in a.game_text)
                rig, entities, ctx = self.ctx(path, attack.title)
                ctx.deal_damage = AsyncMock()
                await attack.effect(ctx)
                self.assertEqual(ctx.deal_damage.call_args.args[0], attack.damage)
                tool = self.add(rig, fixtures.definition(tool_path), P1 if side == 'tool' else P2, 'hand')
                rig.attach(tool, entities['target'] if side == 'tool' else ctx.defender)
                ctx.deal_damage.reset_mock()
                await attack.effect(ctx)
                self.assertEqual(ctx.deal_damage.call_args.args[0], attack.damage + bonus)

    async def test_custom_trap_requires_tool_to_retaliate(self):
        rig, entities, ctx = self.ctx('SV3.Stunfisk_112', 'Custom Trap')
        ctx.damaged_by = rig.board.active_pokemon(P2)
        ctx.deal_damage = AsyncMock()
        await ctx.ability.effect(ctx)
        ctx.deal_damage.assert_not_awaited()
        tool = self.add(rig, fixtures.definition('BW9.FloatStone_99'), P1, 'hand')
        rig.attach(tool, entities['target'])
        await ctx.ability.effect(ctx)
        ctx.deal_damage.assert_awaited_once()
        self.assertEqual(ctx.deal_damage.call_args.args[0], 50)


if __name__ == '__main__':
    unittest.main()
