"""First-turn Supporter exceptions must survive alternate-art reprints."""
import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures
from tests.test_hgss_rules import definition

from spirit.game.data_utils import Attack, CARD_DEFS_BY_GUID
from spirit.game.session.effects import EffectContext
from spirit.game.session.legal_actions import ACTION_USE_ATTACK, compute_legal_actions
from spirit.game.session.passives import effective_retreat_cost
from spirit.tools.effect_smoke import P1, P2


FIRST_TURN_SUPPORTERS = (
    'SWSH4.Beauty_148', 'SWSH4.Beauty_181', 'SWSH4.Beauty_194',
    'SV06.Carmine_145', 'SV06.Carmine_204', 'SV06.Carmine_217',
    'SV085.Carmine_103',
    'SV10.TeamRocketsProton_177', 'SV10.TeamRocketsProton_227',
    'ME2PT5.TeamRocketsProton_208',
)


class FirstTurnSupporterTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    async def test_each_printing_can_be_played_on_first_turn(self):
        rig, _ = self.rig('BW1.Snivy_1')
        cards = {
            path: self.add(rig, definition(path), P1, 'hand')
            for path in FIRST_TURN_SUPPORTERS
        }
        ordinary = self.add(rig, definition('SM1.Hau_120'), P1, 'hand')
        # Wally's older evolution-timing text does not waive the later
        # no-Supporter rule for the player who goes first.
        wally = self.add(rig, definition('XY6.Wally_94'), P1, 'hand')
        state = rig.session.turn_state
        state.turn_number = 1
        state.active_player_id = P1

        def offered():
            return {entry['entityID'] for entry in compute_legal_actions(
                rig.board, state, P1, rig.session.game_id)}

        first_turn = offered()
        for path, card in cards.items():
            with self.subTest(path=path):
                self.assertIn(card.entity_id, first_turn)
        self.assertNotIn(ordinary.entity_id, first_turn)
        self.assertNotIn(wally.entity_id, first_turn)

        state.supporter_played = True
        self.assertTrue(all(card.entity_id not in offered()
                            for card in cards.values()))
        state.supporter_played = False
        state.turn_number = 3
        later_turn = offered()
        self.assertTrue(all(card.entity_id in later_turn for card in cards.values()))
        self.assertIn(ordinary.entity_id, later_turn)
        self.assertIn(wally.entity_id, later_turn)

    async def test_carmine_reprint_resolves_on_first_turn(self):
        rig, _ = self.rig('BW1.Snivy_1')
        carmine = self.add(rig, definition('SV06.Carmine_204'), P1, 'hand')
        state = rig.session.turn_state
        state.turn_number = 1
        state.active_player_id = P1
        offered = compute_legal_actions(rig.board, state, P1, rig.session.game_id)
        self.assertTrue(any(entry['entityID'] == carmine.entity_id
                            for entry in offered))
        deck = rig.board.find_player_area(P1, 'deck')
        before = len(deck.children)
        await rig.session._execute_play_trainer(P1, carmine)
        self.assertEqual(len(deck.children), before - 5)
        self.assertEqual(len(rig.board.find_player_area(P1, 'hand').children), 5)
        self.assertIn(carmine, rig.board.find_player_area(P1, 'discard').children)
        self.assertTrue(state.supporter_played)

    async def test_beauty_draws_two_on_first_turn(self):
        rig, _ = self.rig('BW1.Snivy_1')
        beauty = self.add(rig, definition('SWSH4.Beauty_194'), P1, 'hand')
        state = rig.session.turn_state
        state.turn_number = 1
        state.active_player_id = P1
        deck = rig.board.find_player_area(P1, 'deck')
        hand = rig.board.find_player_area(P1, 'hand')
        before_deck = len(deck.children)
        before_hand = len(hand.children)

        await rig.session._execute_play_trainer(P1, beauty)

        self.assertEqual(len(deck.children), before_deck - 2)
        self.assertEqual(len(hand.children), before_hand + 1)
        self.assertIn(beauty, rig.board.find_player_area(P1, 'discard').children)
        self.assertTrue(state.supporter_played)

    async def test_printed_first_turn_attacks_are_marked_playable(self):
        checked = 0
        for card in CARD_DEFS_BY_GUID.values():
            for attack in getattr(card, 'abilities', ()) or ():
                if not isinstance(attack, Attack):
                    continue
                text = attack.game_text.strip().casefold()
                if not text.startswith((
                    'if you go first, you can use this attack during your first turn',
                    'if you go first, you can use this attack on your first turn',
                )):
                    continue
                with self.subTest(card=card.display_name, attack=attack.title):
                    self.assertTrue(attack.usable_first_turn)
                checked += 1
        self.assertGreaterEqual(checked, 10)

    async def test_first_turn_attacks_reach_action_menu(self):
        for path, title in (
            ('SV4.Bombirdierex_156', 'Fast Carrier'),
            ('ME1.Delibird_105', 'Quick Gift'),
            ('XY6.LatiosEX_58', 'Fast Raid'),
        ):
            with self.subTest(path=path):
                rig, entities = self.rig(path)
                state = rig.session.turn_state
                state.turn_number = 1
                state.active_player_id = P1
                offered = {
                    entry['selectableAction']['actionID']
                    for entry in compute_legal_actions(
                        rig.board, state, P1, rig.session.game_id)
                    if entry['entityID'] == entities['target'].entity_id
                    and entry['selectableAction']['description'] == ACTION_USE_ATTACK
                }
                attack = next(a for a in definition(path).abilities if a.title == title)
                self.assertIn(attack.ability_id, offered)

    async def test_second_player_first_turn_items_are_time_limited(self):
        for path in (
            'SM8.WaitandSeeHammer_192',
            'SV08.CallBell_165',
            'SV08.ChillTeaserToy_166',
        ):
            with self.subTest(path=path):
                rig, _ = self.rig('BW1.Snivy_1')
                item = self.add(rig, definition(path), P1, 'hand')
                state = rig.session.turn_state

                def offered():
                    return any(entry['entityID'] == item.entity_id
                               for entry in compute_legal_actions(
                                   rig.board, state, P1, rig.session.game_id))

                state.turn_number = 1
                self.assertFalse(offered())
                state.turn_number = 2
                self.assertTrue(offered())
                state.turn_number = 3
                self.assertFalse(offered())

    async def test_cards_forbidden_on_either_first_turn(self):
        for path in ('ME2.GrimsleysMove_90', 'SM12.RedBlue_202'):
            with self.subTest(path=path):
                rig, _ = self.rig('BW1.Snivy_1')
                item = self.add(rig, definition(path), P1, 'hand')
                state = rig.session.turn_state
                state.active_player_id = P1
                for turn in (1, 2):
                    state.turn_number = turn
                    offered = compute_legal_actions(
                        rig.board, state, P1, rig.session.game_id)
                    self.assertFalse(any(entry['entityID'] == item.entity_id
                                         for entry in offered))

    async def test_second_player_first_turn_search_bonus(self):
        rig, _ = self.rig('BW1.Snivy_1')
        jasmine = self.add(rig, definition('SM9.Jasmine_145'), P1, 'hand')
        rig.session.first_player_id = P2
        state = rig.session.turn_state
        state.active_player_id = P1
        for turn, expected in ((2, 5), (3, 1)):
            with self.subTest(turn=turn):
                state.turn_number = turn
                ctx = EffectContext(rig.session, P1, jasmine, None)
                ctx.search_deck = AsyncMock(return_value=[])
                ctx.shuffle_deck = AsyncMock()
                await definition('SM9.Jasmine_145').effect(ctx)
                self.assertEqual(ctx.search_deck.await_args.kwargs['count'], expected)

    async def test_second_player_first_turn_draw_bonus(self):
        rig, _ = self.rig('BW1.Snivy_1')
        parasol = self.add(rig, definition('SV4.ParasolLady_169'), P1, 'hand')
        rig.session.first_player_id = P2
        state = rig.session.turn_state
        state.active_player_id = P1
        for turn, expected in ((2, 8), (3, 4)):
            with self.subTest(turn=turn):
                state.turn_number = turn
                ctx = EffectContext(rig.session, P1, parasol, None)
                ctx.shuffle_into_deck = AsyncMock()
                ctx.draw_cards = AsyncMock()
                await definition('SV4.ParasolLady_169').effect(ctx)
                ctx.draw_cards.assert_awaited_once_with(expected)

    async def test_first_turn_retreat_discount_applies_to_either_player(self):
        rig, entities = self.rig('SM3.Wimpod_16')
        wimpod = entities['target']
        state = rig.session.turn_state
        state.active_player_id = P1
        state.turn_number = 1
        self.assertEqual(effective_retreat_cost(rig.board, wimpod), 0)
        state.turn_number = 2
        self.assertEqual(effective_retreat_cost(rig.board, wimpod), 0)
        state.turn_number = 3
        self.assertEqual(effective_retreat_cost(rig.board, wimpod), 3)
