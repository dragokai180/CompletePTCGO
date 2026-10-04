"""Evolution timing exceptions must follow the text of their own card."""
import unittest

from tests import test_hgss_rules as fixtures
from tests.test_hgss_rules import definition

from spirit.game.session.legal_actions import compute_legal_actions
from spirit.tools.effect_smoke import P1, P2


class EvolutionTimingAbilitiesTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    def setup_evolution(self, source_path, evolution_path, *, pid=P1, turn=1):
        rig, entities = self.rig(source_path)
        state = rig.session.turn_state
        state.turn_number = turn
        state.active_player_id = pid
        source = entities['target'] if pid == P1 else self.add(
            rig, definition(source_path), pid, 'bench')
        state.entered_play_turn[source.entity_id] = turn
        evolution = self.add(rig, definition(evolution_path), pid, 'hand')
        return rig, source, evolution

    @staticmethod
    def entry(rig, pid, card):
        return next((entry for entry in compute_legal_actions(
            rig.board, rig.session.turn_state, pid, rig.session.game_id)
            if entry['entityID'] == card.entity_id), None)

    async def test_adaptive_evolution_all_printings_and_second_stage(self):
        cases = (
            ('XY2.Caterpie_1', 'XY2.Metapod_2', 'XY2.Butterfree_3'),
            ('SWSH2.Caterpie_1', 'SWSH2.Metapod_2', 'SWSH2.Butterfree_3'),
            ('SV1.Scatterbug_8', 'SV1.Spewpa_9', 'SV1.Vivillon_10'),
        )
        for basic_path, stage1_path, stage2_path in cases:
            for pid, turn in ((P1, 1), (P2, 2), (P1, 3)):
                with self.subTest(basic=basic_path, pid=pid, turn=turn):
                    rig, basic, stage1 = self.setup_evolution(
                        basic_path, stage1_path, pid=pid, turn=turn)
                    entry = self.entry(rig, pid, stage1)
                    self.assertIsNotNone(entry)
                    await rig.session._execute_evolve(
                        pid, stage1, entry, [basic.entity_id])
                    self.assertIn(stage1, rig.board.pokemon_in_play(pid))
                    stage2 = self.add(rig, definition(stage2_path), pid, 'hand')
                    self.assertIsNotNone(self.entry(rig, pid, stage2))

    async def test_adaptive_evolution_does_not_help_another_pokemon(self):
        rig, _, _ = self.setup_evolution(
            'XY2.Caterpie_1', 'XY2.Metapod_2')
        other = self.add(rig, definition('ME3.Shinx_26'), P1, 'bench')
        rig.session.turn_state.entered_play_turn[other.entity_id] = 1
        luxio = self.add(rig, definition('ME3.Luxio_27'), P1, 'hand')
        self.assertIsNone(self.entry(rig, P1, luxio))

    async def test_go_second_abilities_apply_only_on_second_players_first_turn(self):
        cases = (
            ('SM5.Shinx_45', 'SM5.Luxio_47'),
            ('SM6.Flabb_83', 'SM6.Floette_85'),
            ('SM7.Clamperl_41', 'SM7.Huntail_42'),
            ('SM9.Bronzor_100', 'SM9.Bronzong_101'),
            ('SV035.Spearow_21', 'SV035.Fearow_22'),
        )
        for basic_path, evolution_path in cases:
            with self.subTest(basic=basic_path):
                rig, source, evolution = self.setup_evolution(
                    basic_path, evolution_path, pid=P2, turn=2)
                self.assertIsNotNone(self.entry(rig, P2, evolution))
                state = rig.session.turn_state
                state.turn_number = 3
                state.active_player_id = P2
                state.entered_play_turn[source.entity_id] = 3
                self.assertIsNone(self.entry(rig, P2, evolution))
                rig_first, _, evo_first = self.setup_evolution(
                    basic_path, evolution_path, pid=P1, turn=1)
                self.assertIsNone(self.entry(rig_first, P1, evo_first))

    async def test_partner_and_opponent_conditions(self):
        cases = (
            ('ZSV10PT5.Karrablast_9', 'ZSV10PT5.Escavalier_60',
             'RSV10PT5.Shelmet_8'),
            ('RSV10PT5.Shelmet_8', 'RSV10PT5.Accelgor_9',
             'ZSV10PT5.Karrablast_9'),
        )
        for basic_path, evolution_path, partner_path in cases:
            with self.subTest(basic=basic_path):
                rig, _, evolution = self.setup_evolution(
                    basic_path, evolution_path)
                self.assertIsNone(self.entry(rig, P1, evolution))
                partner = self.add(rig, definition(partner_path), P1, 'bench')
                self.assertIsNotNone(self.entry(rig, P1, evolution))
                rig.to_area(partner, P1, 'discard')
                self.assertIsNone(self.entry(rig, P1, evolution))

        rig, _, luxray = self.setup_evolution(
            'ME3.Luxio_27', 'ME3.Luxray_28')
        self.assertIsNone(self.entry(rig, P1, luxray))
        opposing = rig.board.active_pokemon(P2)
        rig.to_area(opposing, P2, 'discard')
        ex = self.add(rig, definition('SV1.Banetteex_88'), P2,
                      'activePokemonArea')
        self.assertIsNotNone(self.entry(rig, P1, luxray))
        rig.to_area(ex, P2, 'discard')
        self.add(rig, definition('SM12.AlolanPersianGX_129'), P2,
                 'activePokemonArea')
        self.assertIsNone(self.entry(rig, P1, luxray))

    async def test_hakamoo_same_turn_but_not_first_turn(self):
        rig, _, kommoo = self.setup_evolution(
            'SM12.Hakamoo_162', 'SM12.Kommoo_163', turn=3)
        opposing = rig.board.active_pokemon(P2)
        rig.to_area(opposing, P2, 'discard')
        self.add(rig, definition('SM12.AlolanPersianGX_129'), P2,
                 'activePokemonArea')
        self.assertIsNotNone(self.entry(rig, P1, kommoo))
        rig.session.turn_state.turn_number = 1
        self.assertIsNone(self.entry(rig, P1, kommoo))

    async def test_boosted_evolution_still_requires_active_spot(self):
        rig, eevee, evolution = self.setup_evolution(
            'SV08.Eevee_143', 'SV085.Jolteon_29')
        self.assertIsNotNone(self.entry(rig, P1, evolution))
        rig.to_area(eevee, P1, 'bench')
        self.assertIsNone(self.entry(rig, P1, evolution))

    async def test_delta_evolution_applies_only_to_card_in_hand(self):
        rig, _, banette = self.setup_evolution(
            'XY6.Shuppet_30', 'XY6.Banette_32')
        entry = self.entry(rig, P1, banette)
        self.assertIsNotNone(entry)
        shuppet = rig.board.active_pokemon(P1)
        await rig.session._execute_evolve(P1, banette, entry,
                                          [shuppet.entity_id])
        other = self.add(rig, definition('ME3.Shinx_26'), P1, 'bench')
        rig.session.turn_state.entered_play_turn[other.entity_id] = 1
        luxio = self.add(rig, definition('ME3.Luxio_27'), P1, 'hand')
        self.assertIsNone(self.entry(rig, P1, luxio))


if __name__ == '__main__':
    unittest.main()
