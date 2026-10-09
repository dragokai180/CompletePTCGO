"""Both Bide Barricade printings lock every non-Psychic Ability path."""
import unittest

from tests import test_hgss_rules as fixtures
from spirit.game.session.effects import resolve_triggered_ability
from spirit.game.session.legal_actions import _ability_entries
from spirit.game.session.passives import (
    ability_locked, out_of_play_ability_locked,
)
from spirit.tools.effect_smoke import P1, P2


WOBBUFFET_PRINTINGS = ('XY4.Wobbuffet_36', 'TwentiethAnn.Wobbuffet_111')


class BideBarricadeTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    def test_both_printings_lock_non_psychic_gx_vstar_and_regular_abilities(self):
        for printing in WOBBUFFET_PRINTINGS:
            with self.subTest(printing=printing):
                rig, entries = self.rig(printing)
                for path in (
                    'SWSH1.Oranguru_148',       # activated: Primate Wisdom
                    'SWSH9.ArceusVSTAR_123',   # VSTAR Power: Starbirth
                    'SWSH3.CrobatV_104',       # on-play: Dark Asset
                    'SM10.DedenneGX_57',       # on-play GX: Dedechange
                ):
                    with self.subTest(card=path):
                        definition = fixtures.definition(path)
                        pokemon = self.add(rig, definition, P2, 'bench')
                        self.assertTrue(ability_locked(
                            rig.board, pokemon, definition.abilities[0]))

                psychic = fixtures.definition('SM2.TapuLeleGX_60')
                tapu_lele = self.add(rig, psychic, P2, 'bench')
                self.assertFalse(ability_locked(
                    rig.board, tapu_lele, psychic.abilities[0]))

                hand_oranguru = self.add(
                    rig, fixtures.definition('SWSH1.Oranguru_148'), P2, 'hand')
                self.assertTrue(out_of_play_ability_locked(
                    rig.board, hand_oranguru))
                rig.to_area(entries['target'], P1, 'hand')
                self.assertFalse(out_of_play_ability_locked(
                    rig.board, hand_oranguru))

    async def test_on_play_v_and_gx_abilities_do_not_run_under_barricade(self):
        for printing in WOBBUFFET_PRINTINGS:
            with self.subTest(printing=printing):
                rig, _ = self.rig(printing)
                for path in ('SWSH3.CrobatV_104', 'SM10.DedenneGX_57'):
                    definition = fixtures.definition(path)
                    pokemon = self.add(rig, definition, P2, 'bench')
                    result = await resolve_triggered_ability(
                        rig.session, P2, pokemon, definition.abilities[0])
                    self.assertIsNone(result)

    async def test_stale_activated_action_cannot_spend_primate_wisdom(self):
        rig, entries = self.rig('TwentiethAnn.Wobbuffet_111')
        oranguru = self.add(
            rig, fixtures.definition('SWSH1.Oranguru_148'), P2, 'bench')
        arceus = self.add(
            rig, fixtures.definition('SWSH9.ArceusVSTAR_123'), P2, 'bench')
        rig.to_area(entries['target'], P1, 'hand')
        available = _ability_entries(
            rig.board, rig.session.turn_state, P2, rig.session.game_id,
            rig.board.pokemon_in_play(P2),
        )
        actions = {entry['entityID']: entry for entry in available}
        self.assertIn(oranguru.entity_id, actions)
        self.assertIn(arceus.entity_id, actions)
        rig.to_area(entries['target'], P1, 'activePokemonArea')

        self.assertFalse(await rig.session._execute_use_ability(
            P2, oranguru, actions[oranguru.entity_id]))
        self.assertFalse(await rig.session._execute_use_ability(
            P2, arceus, actions[arceus.entity_id]))
        self.assertFalse(rig.session.turn_state.used_abilities)
        self.assertNotIn(P2, rig.session.turn_state.vstar_used)
        self.assertFalse(any(entry['entityID'] in actions
                             for entry in _ability_entries(
                                 rig.board, rig.session.turn_state, P2,
                                 rig.session.game_id, rig.board.pokemon_in_play(P2))))


if __name__ == '__main__':
    unittest.main()
