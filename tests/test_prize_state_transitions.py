"""Prize visibility and progress survive zone changes and added Prizes."""
import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures
from spirit.game.attributes import GameSequence, PokemonTypes
from spirit.game.data_utils import def_for
from spirit.game.session.effects import EffectContext, is_energy_card
from spirit.network.message_names import OutboundMsg
from spirit.tools.effect_smoke import P1, P2


class PrizeStateTransitionTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx
    add = fixtures.HgssRulesTests.add

    async def test_face_up_prize_redealt_from_deck_is_face_down(self):
        rig, _ = self.rig('BW7.TownMap_136', 'trainer')
        board = rig.board
        pile = board.find_player_area(P1, 'prizePile')
        deck = board.find_player_area(P1, 'deck')
        prize = pile.children[0]
        prize.publicly_revealed = True

        self.assertTrue(board.move_card(prize.entity_id, deck.entity_id))
        self.assertFalse(prize.publicly_revealed)
        self.assertTrue(board.move_card(prize.entity_id, pile.entity_id))
        self.assertFalse(prize.publicly_revealed)
        self.assertTrue(prize.is_hidden_from(P2))

    async def test_revealing_prize_after_gap_keeps_its_board_slot(self):
        rig, entities = self.rig('BW7.TownMap_136', 'trainer')
        pile = rig.board.find_player_area(P1, 'prizePile')
        hand = rig.board.find_player_area(P1, 'hand')
        for slot, prize in enumerate(pile.children):
            prize.board_slot = slot
        chosen = pile.children[2]
        rig.board.move_card(pile.children[1].entity_id, hand.entity_id)
        self.assertEqual(pile.children.index(chosen), 1)
        ctx = EffectContext(rig.session, P1, entities['target'], None)

        await ctx.reveal_cards([chosen], to_player=P1)

        self.assertEqual(chosen.board_slot, 2)

    async def test_added_prize_does_not_erase_taken_prize_progress(self):
        rig, entities = self.rig('SM4.NihilegoGX_49')
        board = rig.board
        opponent_prizes = board.find_player_area(P2, 'prizePile')
        opponent_hand = board.find_player_area(P2, 'hand')
        for slot, prize in enumerate(opponent_prizes.children):
            prize.board_slot = slot
        taken = opponent_prizes.children[0]
        board.move_card(taken.entity_id, opponent_hand.entity_id)
        self.assertEqual(board.prizes_taken(P2), 1)

        ctx = EffectContext(rig.session, P1, entities['target'], None)
        added = list(ctx.deck_top(2, P2))
        self.assertEqual(await ctx.put_in_prizes(added, player_id=P2,
                                                   additional=True), 2)
        self.assertEqual(board.prizes_taken(P2), 1)
        self.assertEqual(len(opponent_prizes.children), 7)

        more = list(ctx.deck_top(1, P2))
        self.assertEqual(await ctx.put_in_prizes(more, player_id=P2,
                                                   additional=True), 1)
        self.assertEqual(board.prizes_taken(P2), 1)
        slots = [card.board_slot for card in opponent_prizes.children]
        self.assertEqual(len(slots), len(set(slots)))

        # Replacing a Prize after Peonia is not a new Prize to be taken.
        replacement = next(card for card in ctx.hand(P2) if card is not taken)
        removed = opponent_prizes.children[0]
        board.move_card(removed.entity_id, opponent_hand.entity_id)
        before = board.prizes_taken(P2)
        await ctx.put_in_prizes([replacement], player_id=P2)
        self.assertEqual(board.prizes_taken(P2), before - 1)

    async def test_attacks_that_add_prizes_preserve_taken_count(self):
        cases = (
            ('SM4.NihilegoGX_49', 'Symbiont-GX', 2),
            ('SM11.NaganadelGX_160', 'Injection-GX', 1),
        )
        for path, title, added in cases:
            with self.subTest(attack=title):
                rig, _, ctx = self.ctx(path, title)
                board = rig.board
                prizes = board.find_player_area(P2, 'prizePile')
                hand = board.find_player_area(P2, 'hand')
                board.move_card(prizes.children[0].entity_id, hand.entity_id)
                if title == 'Injection-GX':
                    chosen = ctx.discard_pile(P2)[0]
                    ctx.choose_cards = AsyncMock(return_value=[chosen])

                await ctx.ability.effect(ctx)

                self.assertEqual(len(prizes.children), 5 + added)
                self.assertEqual(board.prizes_taken(P2), 1)

    async def test_burst_gx_discards_through_prize_picker_without_taking(self):
        rig, entities, ctx = self.ctx('SM8.BlacephalonGX_52', 'Burst-GX')
        board = rig.board
        pile = board.find_player_area(P1, 'prizePile')
        selected = next(card for card in pile.children
                        if not is_energy_card(card))
        rig.session._prompt_prize_pick = AsyncMock(
            return_value=[selected.entity_id])
        rig.session.send_game_sequence = AsyncMock()

        await ctx.ability.effect(ctx)

        self.assertEqual(selected._containing_area_name(), 'discard')
        self.assertEqual(board.prizes_taken(P1), 0)
        self.assertEqual(rig.session.turn_state.prizes_taken.get(P1, 0), 0)
        self.assertTrue(any(
            call.args[1] == GameSequence.WITH_OPEN_PRIZE_CARDS
            for call in rig.session.send_game_sequence.await_args_list
        ))

    async def test_burst_gx_attaches_energy_after_closing_prize_picker(self):
        rig, entities, ctx = self.ctx('SM8.BlacephalonGX_52', 'Burst-GX')
        energy = self.add(rig,
            def_for(self.energies[PokemonTypes.FIRE.value]),
            P1, 'prizePile')
        rig.session._prompt_prize_pick = AsyncMock(
            return_value=[energy.entity_id])
        rig.session.send_game_sequence = AsyncMock()
        ctx.choose_pokemon = AsyncMock(return_value=entities['target'])

        await ctx.ability.effect(ctx)

        self.assertIn(energy, rig.board.attached_energies(entities['target']))
        self.assertEqual(rig.session.turn_state.prizes_taken.get(P1, 0), 0)
        self.assertTrue(any(
            call.args[1] == GameSequence.WITH_OPEN_PRIZE_CARDS
            for call in rig.session.send_game_sequence.await_args_list
        ))

    async def test_burst_gx_routes_prism_star_energy_to_lost_zone(self):
        rig, _, ctx = self.ctx('SM8.BlacephalonGX_52', 'Burst-GX')
        energy = self.add(rig, fixtures.definition('SM6.BeastEnergy_117'),
                          P1, 'prizePile')
        rig.session._prompt_prize_pick = AsyncMock(
            return_value=[energy.entity_id])
        rig.session.send_game_sequence = AsyncMock()
        ctx.choose_pokemon = AsyncMock()

        await ctx.ability.effect(ctx)

        self.assertEqual(energy._containing_area_name(), 'lostZone')
        ctx.choose_pokemon.assert_not_awaited()

    async def test_stinger_gx_replaces_prizes_without_counting_them_as_taken(self):
        rig, _, ctx = self.ctx('Promo_SM.NaganadelGX_125', 'Stinger-GX')
        board = rig.board
        own_prizes = board.find_player_area(P1, 'prizePile')
        opponent_prizes = board.find_player_area(P2, 'prizePile')
        rig.session.send_game_sequence = AsyncMock()

        await ctx.ability.effect(ctx)

        self.assertEqual(len(own_prizes.children), 3)
        self.assertEqual(len(opponent_prizes.children), 3)
        self.assertEqual(board.prizes_taken(P1), 0)
        self.assertEqual(board.prizes_taken(P2), 0)

    async def test_peonia_puts_prizes_into_hand_without_take_triggers(self):
        rig, entities = self.rig('SWSH6.Peonia_149', 'trainer')
        board = rig.board
        prize_area = board.find_player_area(P1, 'prizePile')
        original_prizes = list(prize_area.children)
        ctx = EffectContext(rig.session, P1, entities['target'], None)
        replacements = [card for card in ctx.hand()
                        if card is not entities['target']][:3]
        ctx.choose_cards = AsyncMock(return_value=replacements)
        rig.session.send_game_sequence = AsyncMock()
        rig.session._fire_triggered_abilities = AsyncMock()

        await fixtures.definition('SWSH6.Peonia_149').effect(ctx)

        self.assertEqual(len(prize_area.children), 6)
        self.assertEqual(board.prizes_taken(P1), 0)
        self.assertEqual(rig.session.turn_state.prizes_taken.get(P1, 0), 0)
        rig.session._fire_triggered_abilities.assert_not_awaited()
        for prize in original_prizes[:3]:
            self.assertIn(prize, ctx.hand())

    async def test_empty_prize_pile_wins_only_after_a_prize_is_taken(self):
        rig, _ = self.rig('SM8.BlacephalonGX_52')
        board = rig.board
        pile = board.find_player_area(P1, 'prizePile')
        discard = board.find_player_area(P1, 'discard')
        rig.session.send_game_sequence = AsyncMock()
        rig.session.end_game = AsyncMock()

        for prize in list(pile.children):
            board.move_card(prize.entity_id, discard.entity_id)
        board.prize_count_adjustment[P1] = 6
        await rig.session._resolve_simultaneous_win_conditions()
        rig.session.end_game.assert_not_awaited()

        last = discard.children[-1]
        board.move_card(last.entity_id, pile.entity_id)
        board.prize_count_adjustment[P1] = 5
        await rig.session._take_prizes(P1, 1)
        await rig.session._resolve_simultaneous_win_conditions()
        rig.session.end_game.assert_awaited_once()

    async def test_one_prize_peeks_reveal_only_the_selected_card(self):
        cases = (
            ('XY3.Patrat_84', 'Safety Check', P1),
            ('SM3.Porygon_103', 'Code Check', P2),
        )
        for path, title, owner in cases:
            with self.subTest(attack=title):
                rig, _, ctx = self.ctx(path, title)
                pile = rig.board.find_player_area(owner, 'prizePile')
                chosen = pile.children[1]
                rig.session._prompt_prize_pick = AsyncMock(
                    return_value=[chosen.entity_id])
                rig.session.send_game_sequence = AsyncMock()
                ctx.choose_cards = AsyncMock(
                    side_effect=AssertionError('used ordinary card browser'))

                await ctx.ability.effect(ctx)

                offered = rig.session._prompt_prize_pick.await_args.args[1]
                self.assertEqual(len(offered), len(pile.children))
                self.assertIs(
                    rig.session._prompt_prize_pick.await_args.kwargs['prize_area'],
                    pile,
                )
                intros = [
                    (call.args[0], message['value']['entityID'])
                    for call in rig.session.send_game_sequence.await_args_list
                    for message in call.args[2]
                    if message['name'] == OutboundMsg.ENTITY_INTRODUCED.value
                ]
                self.assertEqual(intros, [([rig.session.players[P1]],
                                           chosen.entity_id)])
                self.assertFalse(chosen.publicly_revealed)
                self.assertTrue(any(
                    call.args[1] == GameSequence.WITH_OPEN_PRIZE_CARDS
                    for call in rig.session.send_game_sequence.await_args_list
                ))


if __name__ == '__main__':
    unittest.main()
