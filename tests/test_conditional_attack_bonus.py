"""Conditional attack bonuses require their printed condition and payment."""
import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures
from spirit.game.session.effects import EffectContext
from spirit.tools.effect_smoke import P1, P2


class ConditionalAttackBonusTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    async def attack(self, path, title, stadium_owner=None, accept=True):
        rig, entities = self.rig(path)
        attack = next(a for a in fixtures.definition(path).abilities
                      if a.title == title)
        stadium = None
        if stadium_owner:
            stadium = self.add(rig, fixtures.definition('SV1.Mesagoza_178'),
                               stadium_owner, 'hand')
            rig.board.move_card(stadium.entity_id,
                                rig.board.find_global_area('activeStadium').entity_id)
            stadium.owning_player_id = stadium_owner
        ctx = EffectContext(rig.session, P1, entities['target'], attack)
        ctx.deal_damage = AsyncMock(return_value=0)
        ctx.ask_yes_no = AsyncMock(return_value=accept)
        await attack.effect(ctx)
        self.assertTrue(ctx.deal_damage.await_count)
        return ctx.deal_damage.await_args_list[0].args[0], stadium, rig, ctx

    async def test_optional_stadium_discard_pays_for_extra_damage(self):
        for path, title, base, bonus in (
            ('SV085.RoaringMoonex_162', 'Calamity Storm', 100, 120),
            ('SV10.Cetitanex_65', 'Crushing Press', 140, 140),
            ('BW7.Swanna_43', 'Defog', 60, 40),
        ):
            with self.subTest(path=path):
                amount, stadium, rig, ctx = await self.attack(path, title, P2)
                self.assertEqual(amount, base + bonus)
                self.assertIs(stadium.parent,
                              rig.board.find_player_area(P2, 'discard'))
                ctx.ask_yes_no.assert_awaited_once()

                amount, stadium, rig, ctx = await self.attack(
                    path, title, P2, accept=False)
                self.assertEqual(amount, base)
                self.assertIs(stadium.parent,
                              rig.board.find_global_area('activeStadium'))

                amount, _, _, ctx = await self.attack(path, title)
                self.assertEqual(amount, base)
                ctx.ask_yes_no.assert_not_awaited()

    async def test_own_stadium_bonus_requires_ownership(self):
        for path, title, base, bonus in (
            ('SWSH11.PidgeotV_137', 'Flight Surf', 80, 80),
            ('SWSH11.PidgeotV_188', 'Flight Surf', 80, 80),
            ('SWSH4.Terrakion_92', 'Earthen Power', 80, 80),
            ('SWSH10.HeatranV_25', 'Magma Fall', 90, 90),
            ('SWSH10.HeatranV_165', 'Magma Fall', 90, 90),
            ('SWSH6.Sawsbuck_12', 'Winter Horn', 80, 80),
            ('SV2.Palossand_96', 'Earthen Power', 80, 80),
        ):
            for owner in (None, P2, P1):
                with self.subTest(path=path, owner=owner):
                    amount, _, _, _ = await self.attack(path, title, owner)
                    self.assertEqual(amount, base + (bonus if owner == P1 else 0))

    async def test_any_stadium_bonus_accepts_opponents_stadium(self):
        for owner in (None, P2, P1):
            amount, _, _, _ = await self.attack(
                'SWSH5.Stonjourner_84', "Land's Pulse", owner)
            self.assertEqual(amount, 30 + (30 if owner else 0))

    async def test_optional_attached_card_bonuses_require_discard(self):
        for path, title, attachment_path, base, bonus in (
            ('SM4.Octillery_23', 'Special Artillery',
             'SWSH1.AuroraEnergy_186', 40, 80),
            ('SM12.Kommoo_163', 'Scaly Uppercut',
             'SWSH12.ForestSealStone_156', 90, 90),
        ):
            for chosen in (True, False):
                with self.subTest(path=path, chosen=chosen):
                    rig, entities = self.rig(path)
                    attack = next(a for a in fixtures.definition(path).abilities
                                  if a.title == title)
                    attached = self.add(rig, fixtures.definition(attachment_path),
                                        P1, 'hand')
                    rig.attach(attached, entities['target'])
                    self.assertIs(attached.parent, entities['target'])
                    ctx = EffectContext(rig.session, P1, entities['target'], attack)
                    ctx.deal_damage = AsyncMock(return_value=0)
                    ctx.choose_cards = AsyncMock(
                        return_value=[attached] if chosen else [])
                    await attack.effect(ctx)
                    self.assertEqual(ctx.deal_damage.await_args_list[0].args[0],
                                     base + (bonus if chosen else 0))
                    self.assertIs(attached.parent,
                                  rig.board.find_player_area(P1, 'discard')
                                  if chosen else entities['target'])


if __name__ == '__main__':
    unittest.main()
