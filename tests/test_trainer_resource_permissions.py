"""Bespoke Trainer effects must participate in the action-menu gates."""
import unittest
from unittest.mock import AsyncMock, patch

from tests import test_hgss_rules as fixtures
from tests.test_hgss_rules import definition
from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.data_utils import CARD_DEFS_BY_GUID, ItemCardDef, SupporterCardDef
from spirit.game.session.legal_actions import compute_legal_actions, trainer_condition_met
from spirit.game.session.trainer_resource_permissions import DECK_SEARCH_NAMES, DRAW_ONLY_NAMES
from spirit.tools.effect_smoke import P1, P2


class TrainerResourcePermissionTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    def clear(self, rig, pid, zone):
        for c in list(rig.board.find_player_area(pid, zone).children):
            rig.to_area(c, pid, 'lostZone')

    def offered(self, rig, source):
        return any(e['entityID'] == source.entity_id for e in compute_legal_actions(
            rig.board, rig.session.turn_state, P1, rig.session.game_id))

    async def test_deck_prerequisite_all_bespoke_trainer_printings(self):
        checked = 0
        for d in list(CARD_DEFS_BY_GUID.values()):
            if not isinstance(d, (ItemCardDef, SupporterCardDef)) or d.display_name not in DECK_SEARCH_NAMES | DRAW_ONLY_NAMES:
                continue
            rig, _ = self.rig('BW1.Snivy_1')
            source = self.add(rig, d, P1, 'hand')
            self.clear(rig, P1, 'deck')
            with self.subTest(card=d.display_name, guid=d.guid):
                self.assertFalse(self.offered(rig, source))
            checked += 1
        self.assertGreater(checked, 100)

    async def test_search_does_not_check_the_hidden_match(self):
        for path in ('BW1.PokBall_97', 'SWSH1.EvolutionIncense_163', 'SWSH1.Pokgear30_174'):
            rig, _ = self.rig('BW1.Snivy_1')
            source = self.add(rig, definition(path), P1, 'hand')
            self.clear(rig, P1, 'deck')
            self.add(rig, definition('HGSS1.Switch_102'), P1, 'deck')
            self.assertTrue(self.offered(rig, source))

    async def test_nest_ball_requires_bench_space(self):
        rig, _ = self.rig('BW1.Snivy_1')
        source = self.add(rig, definition('SM1.NestBall_123'), P1, 'hand')
        self.assertTrue(self.offered(rig, source))
        while len(rig.board.find_player_area(P1, 'bench').children) < 5:
            self.add(rig, self.filler, P1, 'bench')
        self.assertFalse(self.offered(rig, source))

    async def test_kabu_can_refill_empty_deck_before_drawing(self):
        rig, _ = self.rig('BW1.Snivy_1')
        self.clear(rig, P1, 'hand')
        self.clear(rig, P1, 'deck')
        source = self.add(rig, definition('SWSH3.Kabu_163'), P1, 'hand')
        self.assertFalse(self.offered(rig, source))
        self.add(rig, self.filler, P1, 'hand')
        self.assertTrue(self.offered(rig, source))

    async def test_milo_requires_another_card(self):
        rig, _ = self.rig('BW1.Snivy_1')
        self.clear(rig, P1, 'hand')
        source = self.add(rig, definition('SWSH2.Milo_161'), P1, 'hand')
        self.assertFalse(self.offered(rig, source))
        self.add(rig, self.filler, P1, 'hand')
        self.assertTrue(self.offered(rig, source))

    async def test_gardenia_independent_energy_attachment(self):
        rig, _ = self.rig('BW1.Snivy_1')
        self.clear(rig, P1, 'deck')
        self.clear(rig, P1, 'hand')
        source = self.add(rig, definition('SWSH10.GardeniasVigor_143'), P1, 'hand')
        self.assertFalse(self.offered(rig, source))
        self.add(rig, CARD_DEFS_BY_GUID[self.energies[PokemonTypes.GRASS.value].lower()], P1, 'hand')
        self.assertTrue(self.offered(rig, source))

    async def test_stale_empty_deck_request_never_moves_trainer(self):
        rig, _ = self.rig('BW1.Snivy_1')
        source = self.add(rig, definition('SWSH1.EvolutionIncense_163'), P1, 'hand')
        self.clear(rig, P1, 'deck')
        with patch.object(rig.session, '_broadcast_attack_sources', new_callable=AsyncMock) as animation:
            self.assertFalse(await rig.session._execute_play_trainer(P1, source))
            animation.assert_not_awaited()
        self.assertIn(source, rig.board.find_player_area(P1, 'hand').children)
