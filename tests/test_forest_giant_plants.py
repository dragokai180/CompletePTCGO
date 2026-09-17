"""Forest of Giant Plants waives both evolution timing restrictions."""
import unittest

from tests import test_hgss_rules as fixtures
from tests.test_hgss_rules import definition
from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.session.legal_actions import compute_legal_actions
from spirit.tools.effect_smoke import P1, P2


class ForestGiantPlantsTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    def setup_forest(self, pid=P1, turn=1, path='XY7.ForestofGiantPlants_74'):
        rig, e = self.rig(path, 'trainer')
        stadium = e['target']
        rig.board.move_card(stadium.entity_id,
                            rig.board.find_global_area('activeStadium').entity_id)
        state = rig.session.turn_state
        state.turn_number = turn
        state.active_player_id = pid
        basic = self.add(rig, definition('BW1.Snivy_1'), pid, 'bench')
        state.entered_play_turn[basic.entity_id] = turn
        evolution = self.add(rig, definition('BW1.Servine_3'), pid, 'hand')
        return rig, stadium, basic, evolution

    def evolution_entry(self, rig, pid, card):
        return next((entry for entry in compute_legal_actions(
            rig.board, rig.session.turn_state, pid, rig.session.game_id)
            if entry['entityID'] == card.entity_id), None)

    async def test_first_turn_and_newly_played_for_both_players(self):
        for pid, turn in ((P1, 1), (P2, 2), (P1, 3), (P2, 4)):
            with self.subTest(pid=pid, turn=turn):
                rig, stadium, basic, evolution = self.setup_forest(pid, turn)
                entry = self.evolution_entry(rig, pid, evolution)
                self.assertIsNotNone(entry)
                await rig.session._execute_evolve(pid, evolution, entry, [basic.entity_id])
                self.assertIn(evolution, rig.board.pokemon_in_play(pid))
                # A second evolution is also legal during the same turn.
                stage2 = self.add(rig, definition('BW1.Serperior_5'), pid, 'hand')
                self.assertIsNotNone(self.evolution_entry(rig, pid, stage2))

    async def test_stadium_must_remain_in_play(self):
        rig, stadium, basic, evolution = self.setup_forest()
        self.assertIsNotNone(self.evolution_entry(rig, P1, evolution))
        rig.to_area(stadium, P1, 'discard')
        self.assertIsNone(self.evolution_entry(rig, P1, evolution))

    async def test_checks_pre_evolution_type(self):
        rig, stadium, basic, evolution = self.setup_forest()
        evolution.set_attribute(AttrID.POKEMON_TYPES, [PokemonTypes.FIRE.value])
        self.assertIsNotNone(self.evolution_entry(rig, P1, evolution))
        basic.set_attribute(AttrID.POKEMON_TYPES, [PokemonTypes.FIRE.value])
        evolution.set_attribute(AttrID.POKEMON_TYPES, [PokemonTypes.GRASS.value])
        self.assertIsNone(self.evolution_entry(rig, P1, evolution))

    async def test_does_not_override_evolution_lock(self):
        rig, stadium, basic, evolution = self.setup_forest()
        self.add(rig, definition('BW3.Archeops_67'), P2, 'bench')
        self.assertIsNone(self.evolution_entry(rig, P1, evolution))

    async def test_vitality_still_blocks_first_turn(self):
        for pid, turn in ((P1, 1), (P2, 2)):
            with self.subTest(pid=pid):
                rig, stadium, basic, evolution = self.setup_forest(
                    pid, turn, 'ME1.ForestofVitality_117')
                self.assertIsNone(self.evolution_entry(rig, pid, evolution))
                rig.session.turn_state.turn_number = turn + 2
                rig.session.turn_state.entered_play_turn[basic.entity_id] = turn + 2
                self.assertIsNotNone(self.evolution_entry(rig, pid, evolution))
