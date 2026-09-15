"""Iono's state changes and per-hand native animation boundaries."""
import unittest

from tests import test_hgss_rules as fixtures
from spirit.game.attributes import GameSequence
from spirit.game.data_utils import CARD_DEFS_BY_GUID
from spirit.game.game_sequence_packets import NestedSequence
from spirit.game.scripts.cards import loader
from spirit.game.session.effects import EffectContext
from spirit.network.message_names import OutboundMsg
from spirit.tools.effect_smoke import P1, P2


class IonoRedrawTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig

    def setup_iono(self):
        rig, entities = self.rig('SV2.Iono_185', 'trainer')
        source = entities['target']
        rig.to_area(source, P1, 'discard')
        ctx = EffectContext(rig.session, P1, source, None)
        for pid, count in ((P1, 2), (P2, 4)):
            prizes = rig.board.find_player_area(pid, 'prizePile')
            for card in list(prizes.children)[count:]:
                rig.to_area(card, pid, 'discard')
        return rig, ctx

    def empty_hand(self, rig, ctx, pid):
        for card in list(ctx.hand(pid)):
            rig.to_area(card, pid, 'discard')

    async def test_every_print_draws_own_prize_count_and_separates_hand_animations(self):
        prints = [d for guid, d in list(CARD_DEFS_BY_GUID.items())
                  if d.display_name == 'Iono' and guid in loader.cards_by_guid]
        self.assertGreaterEqual(len(prints), 6)
        for card in prints:
            with self.subTest(set=card.set_code, number=card.collector_number):
                rig, ctx = self.setup_iono()
                old_hands = {pid: set(ctx.hand(pid)) for pid in (P1, P2)}
                tops = {pid: set(ctx.deck_top(n, pid)) for pid, n in ((P1, 2), (P2, 4))}
                await card.effect(ctx)
                for pid, n in ((P1, 2), (P2, 4)):
                    self.assertEqual(set(ctx.hand(pid)), tops[pid])
                    self.assertEqual(set(ctx.deck(pid)[:len(old_hands[pid])]), old_hands[pid])
                    self.assertEqual(len(ctx.hand(pid)), n)
                for viewer in (P1, P2):
                    runs = ctx.bracket_runs_for(viewer)
                    shuffles = [(i, msgs) for i, (name, msgs) in enumerate(runs)
                                if name == GameSequence.HAND_SHUFFLED_AND_MOVED_TO_DECK.value]
                    self.assertEqual(len(shuffles), 2)
                    for _, msgs in shuffles:
                        self.assertEqual(sum(m['name'] == OutboundMsg.SHUFFLED.value for m in msgs), 1)
                        self.assertEqual(sum(m['name'] == OutboundMsg.PLACE_ON_BOTTOM.value for m in msgs), 1)
                    first_draw = next(i for i, (name, _) in enumerate(runs) if name == GameSequence.DRAW.value)
                    self.assertLess(shuffles[-1][0], first_draw)

    async def test_no_cards_bottomed_means_no_draw_for_either_player(self):
        rig, ctx = self.setup_iono()
        for pid in (P1, P2):
            self.empty_hand(rig, ctx, pid)
        decks = {pid: list(ctx.deck(pid)) for pid in (P1, P2)}
        await fixtures.definition('SV2.Iono_185').effect(ctx)
        for pid in (P1, P2):
            self.assertEqual(ctx.hand(pid), [])
            self.assertEqual(ctx.deck(pid), decks[pid])
        self.assertEqual(ctx._messages, [])

    async def test_only_one_nonempty_hand_still_draws_for_both_players(self):
        for empty_pid in (P1, P2):
            with self.subTest(empty_pid=empty_pid):
                rig, ctx = self.setup_iono()
                self.empty_hand(rig, ctx, empty_pid)
                await fixtures.definition('SV2.Iono_185').effect(ctx)
                self.assertEqual(ctx.hand_size(P1), 2)
                self.assertEqual(ctx.hand_size(P2), 4)

    async def test_consecutive_bottom_moves_preserve_each_players_sequence(self):
        rig, ctx = self.setup_iono()
        await ctx.hand_to_bottom_of_deck(P1)
        await ctx.hand_to_bottom_of_deck(P2)
        for viewer in (P1, P2):
            runs = ctx.bracket_runs_for(viewer)
            self.assertEqual(len(runs), 2)
            for (name, messages), pid in zip(runs, (P1, P2)):
                self.assertEqual(name, GameSequence.HAND_SHUFFLED_AND_MOVED_TO_DECK.value)
                self.assertEqual(messages[0]['value']['entityID'], rig.board.find_player_area(pid, 'hand').entity_id)
                self.assertEqual(messages[-1]['value']['target'], rig.board.find_player_area(pid, 'deck').entity_id)

    async def test_draw_batches_are_not_split_into_one_sequence_per_card(self):
        rig, ctx = self.setup_iono()
        await ctx.draw_cards(4)
        for viewer in (P1, P2):
            runs = ctx.bracket_runs_for(viewer)
            self.assertEqual(len(runs), 1)
            self.assertEqual(runs[0][0], GameSequence.DRAW.value)
            moves = [m for m in runs[0][1] if isinstance(m, NestedSequence)]
            self.assertEqual(len(moves), 1)
            self.assertEqual(len(moves[0].messages), 4)
