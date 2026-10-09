"""Festival Grounds removes existing conditions and prevents new ones."""
import unittest

from tests import test_hgss_rules as fixtures

from spirit.game.attributes import AttrID, SpecialConditions
from spirit.game.session.effects import EffectContext
from spirit.game.session.legal_actions import compute_legal_actions
from spirit.tools.effect_smoke import P1, P2


class FestivalGroundsTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    def clear_energy(self, rig, pokemon):
        for energy in list(rig.board.attached_energies(pokemon)):
            rig.to_area(energy, energy.owning_player_id, 'discard')

    def stadium_in_play(self, rig, path='SV06.FestivalGrounds_149'):
        stadium = self.add(rig, fixtures.definition(path), P1, 'hand')
        rig.board.move_card(stadium.entity_id,
                            rig.board.find_global_area('activeStadium').entity_id)
        return stadium

    async def test_playing_either_printing_cures_both_sides_with_energy(self):
        for path in ('SV06.FestivalGrounds_149', 'SV085.FestivalGrounds_108'):
            with self.subTest(path=path):
                rig, entities = self.rig(path, 'trainer')
                own, other = entities['p1_active'], entities['p2_active']
                self.clear_energy(rig, other)
                own_ctx = EffectContext(rig.session, P1, own, None)
                other_ctx = EffectContext(rig.session, P2, other, None)
                self.assertTrue(await own_ctx.apply_special_condition(
                    own, SpecialConditions.ASLEEP))
                self.assertTrue(await other_ctx.apply_special_condition(
                    other, SpecialConditions.POISONED))
                self.assertIn(own.entity_id, rig.session.sleep_checkup_coins)
                self.assertIn(other.entity_id, rig.session.poison_counters)

                await rig.session._execute_play_stadium(P1, entities['target'])

                self.assertEqual(own.get_attribute(AttrID.SPECIAL_CONDITIONS), [])
                self.assertNotIn(own.entity_id, rig.session.sleep_checkup_coins)
                self.assertIn('Poisoned', other.get_attribute(AttrID.SPECIAL_CONDITIONS))
                self.assertIn(other.entity_id, rig.session.poison_counters)
                self.assertFalse(await own_ctx.apply_special_condition(
                    own, SpecialConditions.BURNED))
                self.assertTrue(await other_ctx.apply_special_condition(
                    other, SpecialConditions.BURNED))

    async def test_effect_attachment_cures_after_stadium_is_active(self):
        rig, entities = self.rig('SV06.FestivalGrounds_149', 'trainer')
        self.stadium_in_play(rig)
        target = entities['p1_active']
        self.clear_energy(rig, target)
        ctx = EffectContext(rig.session, P1, target, None)
        self.assertTrue(await ctx.apply_special_condition(
            target, SpecialConditions.CONFUSED))
        energy = self.add(rig, fixtures.definition('BW1.WaterEnergy_107'), P1, 'hand')

        self.assertTrue(await ctx.attach_energy(energy, target))
        self.assertEqual(target.get_attribute(AttrID.SPECIAL_CONDITIONS), [])
        self.assertNotIn(target.entity_id, rig.session.confusion_damage)

    async def test_manual_attachment_cures_after_stadium_is_active(self):
        rig, entities = self.rig('SV06.FestivalGrounds_149', 'trainer')
        self.stadium_in_play(rig)
        target = entities['p1_active']
        self.clear_energy(rig, target)
        ctx = EffectContext(rig.session, P1, target, None)
        self.assertTrue(await ctx.apply_special_condition(
            target, SpecialConditions.PARALYZED))
        energy = self.add(rig, fixtures.definition('BW1.WaterEnergy_107'), P1, 'hand')
        actions = compute_legal_actions(rig.board, rig.session.turn_state,
                                        P1, rig.session.game_id)
        entry = next(action for action in actions if action['entityID'] == energy.entity_id)

        await rig.session._execute_attach_energy(
            P1, energy, entry, [target.entity_id])
        self.assertEqual(target.get_attribute(AttrID.SPECIAL_CONDITIONS), [])
        self.assertNotIn(target.entity_id, rig.session.paralyzed_since)

    async def test_moving_energy_cures_destination(self):
        rig, entities = self.rig('SV06.FestivalGrounds_149', 'trainer')
        self.stadium_in_play(rig)
        target = entities['p1_active']
        self.clear_energy(rig, target)
        ctx = EffectContext(rig.session, P1, target, None)
        self.assertTrue(await ctx.apply_special_condition(
            target, SpecialConditions.POISONED))
        donor = rig.board.pokemon_in_play(P1)[1]
        energy = self.add(rig, fixtures.definition('BW1.WaterEnergy_107'), P1, 'hand')
        rig.attach(energy, donor)

        self.assertTrue(await ctx.move_energy(energy, target))
        self.assertEqual(target.get_attribute(AttrID.SPECIAL_CONDITIONS), [])
        self.assertNotIn(target.entity_id, rig.session.poison_counters)


if __name__ == '__main__':
    unittest.main()
