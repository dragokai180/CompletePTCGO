"""Pantomime's optional, private Prize/deck-top exchange."""
import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures
from spirit.game.attributes import GameSequence
from spirit.tools.effect_smoke import P1


class PantomimeTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx

    async def test_swaps_only_a_face_down_prize_with_deck_top(self):
        rig, entities, ctx = self.ctx('GUM.MrMime_11', 'Pantomime')
        rig.to_area(entities['target'], P1, 'bench')
        prizes = rig.board.find_player_area(P1, 'prizePile')
        for slot, prize in enumerate(prizes.children):
            prize.board_slot = slot
        shown = prizes.children[0]
        shown.publicly_revealed = True
        chosen = prizes.children[1]
        top = ctx.deck_top(1)[0]
        original_slot = chosen.board_slot
        rig.session.prompt_player_choice = AsyncMock(return_value=0)
        rig.session._prompt_prize_pick = AsyncMock(return_value=[chosen.entity_id])
        rig.session.send_game_sequence = AsyncMock()

        await ctx.ability.effect(ctx)

        offered = rig.session._prompt_prize_pick.await_args.args[1]
        self.assertNotIn(shown.entity_id, offered)
        self.assertIn(chosen.entity_id, offered)
        self.assertIs(ctx.deck_top(1)[0], chosen)
        self.assertIs(top.parent, prizes)
        self.assertEqual(top.board_slot, original_slot)
        self.assertIs(shown.parent, prizes)
        self.assertFalse(top.publicly_revealed)
        sequences = [call.args[1] for call in
                     rig.session.send_game_sequence.await_args_list]
        self.assertEqual(sequences.count(GameSequence.WITH_OPEN_PRIZE_CARDS), 2)
        self.assertIn(GameSequence.GROUPED_MOVE, sequences)
        self.assertIs(entities['target'].parent,
                      rig.board.find_player_area(P1, 'bench'))

    async def test_declining_pantomime_keeps_both_piles(self):
        rig, entities, ctx = self.ctx('GUM.MrMime_11', 'Pantomime')
        rig.to_area(entities['target'], P1, 'bench')
        prizes = rig.board.find_player_area(P1, 'prizePile')
        original_prizes = list(prizes.children)
        top = ctx.deck_top(1)[0]
        rig.session.prompt_player_choice = AsyncMock(return_value=1)
        rig.session._prompt_prize_pick = AsyncMock()

        await ctx.ability.effect(ctx)

        self.assertEqual(prizes.children, original_prizes)
        self.assertIs(ctx.deck_top(1)[0], top)
        rig.session._prompt_prize_pick.assert_not_awaited()

    async def test_playing_mr_mime_from_hand_activates_pantomime(self):
        rig, entities, ctx = self.ctx('GUM.MrMime_11', 'Pantomime')
        mr_mime = entities['target']
        rig.to_area(mr_mime, P1, 'hand')
        replacement = rig.board.find_player_area(P1, 'bench').children[0]
        rig.to_area(replacement, P1, 'activePokemonArea')
        prize = rig.board.find_player_area(P1, 'prizePile').children[0]
        top = ctx.deck_top(1)[0]
        rig.session.prompt_player_choice = AsyncMock(return_value=0)
        rig.session._prompt_prize_pick = AsyncMock(return_value=[prize.entity_id])

        await rig.session._execute_play_basic(P1, mr_mime)

        self.assertIn(mr_mime, rig.board.find_player_area(P1, 'bench').children)
        rig.session._prompt_prize_pick.assert_awaited_once()
        self.assertIs(ctx.deck_top(1)[0], prize)
        self.assertIs(top.parent, rig.board.find_player_area(P1, 'prizePile'))

    async def test_rotom_uses_the_same_prize_picker_cleanup(self):
        rig, _, ctx = self.ctx('HGSS3.Rotom_20', 'Mischievous Trick')
        prize = rig.board.find_player_area(P1, 'prizePile').children[0]
        top = ctx.deck_top(1)[0]
        rig.session._prompt_prize_pick = AsyncMock(return_value=[prize.entity_id])
        rig.session.send_game_sequence = AsyncMock()

        await ctx.ability.effect(ctx)

        self.assertIs(ctx.deck_top(1)[0], prize)
        self.assertIs(top.parent, rig.board.find_player_area(P1, 'prizePile'))
        self.assertEqual(sum(
            call.args[1] == GameSequence.WITH_OPEN_PRIZE_CARDS
            for call in rig.session.send_game_sequence.await_args_list), 2)


if __name__ == '__main__':
    unittest.main()
