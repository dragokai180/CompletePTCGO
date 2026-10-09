"""Hand evolution restrictions must also gate Rare Candy's legal targets."""
import unittest

from tests import test_hgss_rules as fixtures
from spirit.game.session.effects import EffectContext
from spirit.game.session.legal_actions import compute_legal_actions
from spirit.game.session.passives import pokemon_play_blocked
from spirit.tools.effect_smoke import P1, P2


class BellOfSilenceRareCandyTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    async def test_rare_candy_only_offered_for_stage_two_without_ability(self):
        for print_path in ('CZ.RareCandy_141', 'PGO.RareCandy_69',
                           'SWSH1.RareCandy_180'):
            with self.subTest(card=print_path):
                rig, entities = self.rig('SM4.Chimecho_43')
                basic = self.add(rig, fixtures.definition('SWSH4.Charmander_23'),
                                 P2, 'bench')
                with_ability = self.add(
                    rig, fixtures.definition('SWSH4.Charizard_25'), P2, 'hand')
                candy_def = fixtures.definition(print_path)
                candy = self.add(rig, candy_def, P2, 'hand')
                self.assertTrue(candy_def.condition(rig.board, P2))

                bell = fixtures.definition('SM4.Chimecho_43').abilities[0]
                await bell.effect(EffectContext(
                    rig.session, P1, entities['target'], bell))
                rig.session.turn_state.begin_turn(P2, rig.board)

                self.assertTrue(rig.session.turn_state.play_locked(
                    P2, with_ability))
                self.assertFalse(candy_def.condition(rig.board, P2))
                offered = compute_legal_actions(
                    rig.board, rig.session.turn_state, P2, rig.session.game_id)
                self.assertFalse(any(entry['entityID'] == candy.entity_id
                                     for entry in offered))
                self.assertFalse(await rig.session.perform_evolution(
                    P2, with_ability, basic))
                self.assertIn(with_ability,
                              rig.board.find_player_area(P2, 'hand').children)

                without_ability = self.add(
                    rig, fixtures.definition('BW7.Charizard_20'), P2, 'hand')
                self.assertFalse(rig.session.turn_state.play_locked(
                    P2, without_ability))
                self.assertTrue(candy_def.condition(rig.board, P2))
                offered = compute_legal_actions(
                    rig.board, rig.session.turn_state, P2, rig.session.game_id)
                self.assertTrue(any(entry['entityID'] == candy.entity_id
                                    for entry in offered))

    def test_continuous_ability_pokemon_lock_also_filters_rare_candy(self):
        rig, _ = self.rig('SV10.TeamRocketsArbok_113')
        self.add(rig, fixtures.definition('SWSH4.Charmander_23'), P2, 'bench')
        with_ability = self.add(
            rig, fixtures.definition('SWSH4.Charizard_25'), P2, 'hand')
        candy = fixtures.definition('SV1.RareCandy_191')

        self.assertTrue(pokemon_play_blocked(rig.board, P2, with_ability))
        self.assertFalse(candy.condition(rig.board, P2))

        self.add(rig, fixtures.definition('BW7.Charizard_20'), P2, 'hand')
        self.assertTrue(candy.condition(rig.board, P2))


if __name__ == '__main__':
    unittest.main()
