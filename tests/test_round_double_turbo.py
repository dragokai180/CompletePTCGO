"""Round counts only allied Pokémon with Round before Double Turbo reduces damage."""

import unittest

from tests import test_hgss_rules as fixtures
from spirit.game.attributes import AttrID
from spirit.game.session.legal_actions import compute_legal_actions
from spirit.tools.effect_smoke import P1, P2


class RoundDoubleTurboTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx
    add = fixtures.HgssRulesTests.add

    async def test_tympole_round_counts_allies_then_applies_one_reduction(self):
        for path, per in (
            ('ZSV10PT5.Tympole_19', 20),
            ('XY9.Tympole_33', 10),
        ):
            for allies in (0, 1, 2):
                with self.subTest(path=path, allies=allies):
                    rig, _, ctx = self.ctx(path, 'Round')
                    attacker = ctx.attacker
                    for energy in list(rig.board.attached_energies(attacker)):
                        rig.to_area(energy, P1, 'discard')
                    for pokemon in list(ctx.my_bench()):
                        if pokemon.archetype_id == attacker.archetype_id:
                            rig.to_area(pokemon, P1, 'hand')
                    for _ in range(allies):
                        self.add(rig, fixtures.definition('BW3.Palpitoad_23'),
                                 P1, 'bench')
                    # Opposing Round must not enter the multiplier.
                    self.add(rig, fixtures.definition('XY10.Whismur_80'),
                             P2, 'bench')
                    turbo = self.add(rig, fixtures.definition(
                        'SWSH9.DoubleTurboEnergy_151'), P1, 'hand')
                    rig.attach(turbo, attacker)
                    defender = ctx.defender
                    defender.set_attribute(AttrID.HP, 500)
                    defender.set_attribute(AttrID.WEAKNESS_TYPES, [])
                    defender.set_attribute(AttrID.RESISTANCE_TYPES, [])

                    await ctx.ability.effect(ctx)

                    expected = max(0, per * (1 + allies) - 20)
                    self.assertEqual(500 - defender.get_attribute(AttrID.HP),
                                     expected)

    async def test_round_without_double_turbo_keeps_full_multiplier(self):
        rig, _, ctx = self.ctx('ZSV10PT5.Tympole_19', 'Round')
        defender = ctx.defender
        defender.set_attribute(AttrID.HP, 500)
        defender.set_attribute(AttrID.WEAKNESS_TYPES, [])
        defender.set_attribute(AttrID.RESISTANCE_TYPES, [])

        await ctx.ability.effect(ctx)

        # The attacker and its second copy on the Bench both have Round.
        self.assertEqual(500 - defender.get_attribute(AttrID.HP), 40)

    def test_one_double_turbo_pays_tympoles_two_colorless_cost(self):
        rig, _, ctx = self.ctx('ZSV10PT5.Tympole_19', 'Round')
        attacker = ctx.attacker
        for energy in list(rig.board.attached_energies(attacker)):
            rig.to_area(energy, P1, 'discard')

        def offered():
            return any(entry['entityID'] == attacker.entity_id
                       and entry['selectableAction']['actionID'] ==
                       ctx.ability.ability_id
                       for entry in compute_legal_actions(
                           rig.board, rig.session.turn_state, P1,
                           rig.session.game_id))

        self.assertFalse(offered())
        turbo = self.add(rig, fixtures.definition(
            'SWSH9.DoubleTurboEnergy_151'), P1, 'hand')
        rig.attach(turbo, attacker)
        self.assertTrue(offered())


if __name__ == '__main__':
    unittest.main()
