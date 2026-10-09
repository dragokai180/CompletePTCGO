"""Frenzied Gouging KOs the defender and conditionally damages its user."""
import unittest

from tests import test_hgss_rules as fixtures
from spirit.game.attributes import AttrID
from spirit.game.session.effects import EffectContext
from spirit.tools.effect_smoke import P1, P2


class FrenziedGougingTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    async def test_knocks_out_defender_and_recoil_can_knock_out_attacker(self):
        for attacker_hp, expected_hp in ((230, 30), (200, 0)):
            with self.subTest(attacker_hp=attacker_hp):
                path = 'SV085.RoaringMoonex_162'
                rig, entities = self.rig(path)
                attacker = entities['target']
                defender = rig.board.active_pokemon(P2)
                attacker.set_attribute(AttrID.HP, attacker_hp)
                attack = next(a for a in fixtures.definition(path).abilities
                              if a.title == 'Frenzied Gouging')
                ctx = EffectContext(rig.session, P1, attacker, attack)

                await attack.effect(ctx)

                self.assertEqual(defender.get_attribute(AttrID.HP), 0)
                self.assertIn(defender, ctx.knockouts)
                self.assertEqual(attacker.get_attribute(AttrID.HP), expected_hp)
                self.assertEqual(attacker in ctx.knockouts, expected_hp == 0)

    async def test_prevented_knockout_does_not_trigger_recoil(self):
        path = 'SV085.RoaringMoonex_162'
        rig, entities = self.rig(path)
        attacker = entities['target']
        defender = rig.board.active_pokemon(P2)
        mist = self.add(rig, fixtures.definition('SV05.MistEnergy_161'),
                        P2, 'hand')
        rig.attach(mist, defender)
        attack = next(a for a in fixtures.definition(path).abilities
                      if a.title == 'Frenzied Gouging')
        ctx = EffectContext(rig.session, P1, attacker, attack)
        attacker_hp = attacker.get_attribute(AttrID.HP)
        defender_hp = defender.get_attribute(AttrID.HP)

        await attack.effect(ctx)

        self.assertEqual(defender.get_attribute(AttrID.HP), defender_hp)
        self.assertEqual(attacker.get_attribute(AttrID.HP), attacker_hp)
        self.assertFalse(ctx.knockouts)


if __name__ == '__main__':
    unittest.main()
