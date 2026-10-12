"""Prism Star Pokemon have a Rule Box but still yield one Prize."""
import unittest

from tests import test_hgss_rules as fixtures
from spirit.game.data_utils import has_rule_box, prize_value
from spirit.game.scripts.cards.ME2PT5.PokPad_198 import _no_rule_box_pokemon
from spirit.game.session.passives import ability_locked
from spirit.tools.effect_smoke import P1, P2


class PrismStarRuleBoxTests(unittest.TestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    def test_poke_pad_excludes_prism_star_pokemon(self):
        rig, _ = self.rig('ME2PT5.PokPad_198', 'trainer')
        ditto = self.add(rig, fixtures.definition('SM8.Ditto_154'), P1, 'deck')
        normal = self.add(rig, fixtures.definition('BW1.Snivy_1'), P1, 'deck')

        self.assertTrue(has_rule_box(ditto.archetype_id))
        self.assertEqual(prize_value(ditto.archetype_id), 1)
        self.assertFalse(_no_rule_box_pokemon(ditto))
        self.assertTrue(_no_rule_box_pokemon(normal))

    def test_initialization_blocks_prism_star_ability(self):
        rig, entities = self.rig('SV06.IronThornsex_77')
        koko_def = fixtures.definition('SM9.TapuKoko_51')
        koko = self.add(rig, koko_def, P2, 'bench')
        ability = koko_def.abilities[0]

        self.assertTrue(ability_locked(rig.board, koko, ability))
        rig.to_area(entities['target'], P1, 'bench')
        self.assertFalse(ability_locked(rig.board, koko, ability))


if __name__ == '__main__':
    unittest.main()
