"""Printed Active/Bench clauses control when Pokemon Ability passives exist."""
import unittest

from tests import test_hgss_rules as fixtures
from spirit.game.session.passives import active_passives, trainer_play_blocked
from spirit.tools.effect_smoke import P1, P2


class PassivePositionPrerequisiteTests(unittest.TestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    def test_daunting_gaze_blocks_items_only_while_tyranitar_is_active(self):
        rig, entities = self.rig('SV09.Tyranitar_95')
        item = self.add(rig, self.item, P2, 'hand')
        self.assertTrue(trainer_play_blocked(rig.board, P2, item))

        rig.to_area(entities['target'], P1, 'hand')
        self.assertFalse(trainer_play_blocked(rig.board, P2, item))

    def test_named_bench_clause_excludes_active_dodrio(self):
        rig, entities = self.rig('HGSS3.Dodrio_11')
        ability = fixtures.definition('HGSS3.Dodrio_11').abilities[0]
        carriers = [carrier for passive, carrier in active_passives(rig.board)
                    if passive is ability.passive]
        self.assertEqual(len(carriers), 1)
        self.assertIsNot(carriers[0], entities['target'])

        rig.to_area(carriers[0], P1, 'hand')
        self.assertFalse(any(passive is ability.passive
                             for passive, _ in active_passives(rig.board)))

    def test_active_spot_clause_excludes_benched_arbok(self):
        rig, entities = self.rig('SV10.TeamRocketsArbok_113')
        ability = fixtures.definition('SV10.TeamRocketsArbok_113').abilities[0]
        carriers = [carrier for passive, carrier in active_passives(rig.board)
                    if passive is ability.passive]
        self.assertEqual(carriers, [entities['target']])

        rig.to_area(entities['target'], P1, 'hand')
        self.assertFalse(any(passive is ability.passive
                             for passive, _ in active_passives(rig.board)))

    def test_benched_shell_shield_is_not_active_from_active_spot(self):
        rig, entities = self.rig('BW7.Squirtle_29')
        ability = fixtures.definition('BW7.Squirtle_29').abilities[0]
        carriers = [carrier for passive, carrier in active_passives(rig.board)
                    if passive is ability.passive]
        self.assertEqual(len(carriers), 1)
        self.assertIsNot(carriers[0], entities['target'])

    def test_mention_of_opponents_active_does_not_gate_bench_aura(self):
        rig, entities = self.rig('BW6.Altaria_84')
        ability = fixtures.definition('BW6.Altaria_84').abilities[0]
        carriers = [carrier for passive, carrier in active_passives(rig.board)
                    if passive is ability.passive]
        self.assertIn(entities['target'], carriers)
        self.assertEqual(len(carriers), 2)


if __name__ == '__main__':
    unittest.main()
