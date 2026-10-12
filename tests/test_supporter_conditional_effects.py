"""Conditional Supporters resolve their printed cost, choice, and draw."""

import unittest
from unittest.mock import AsyncMock, patch

from tests import test_hgss_rules as fixtures
from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.session.effects import EffectContext
from spirit.game.session.legal_actions import trainer_condition_met
from spirit.tools.effect_smoke import P1, P2


class SupporterConditionalEffectsTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    def trainer(self, path):
        rig, entities = self.rig(path, 'trainer')
        source = entities['target']
        ctx = EffectContext(rig.session, P1, source, None)
        ctx.is_trainer_effect = True
        return rig, ctx, fixtures.definition(path)

    def play(self, rig, ctx):
        rig.to_area(ctx.source, P1, 'discard')

    def fewer_opponent_prizes(self, rig):
        prizes = rig.board.find_player_area(P2, 'prizePile')
        for card in list(prizes.children)[3:]:
            rig.to_area(card, P2, 'discard')

    async def test_mars_draws_before_random_opponent_discard(self):
        for path in ('SM5.Mars_128', 'SM5.Mars_154'):
            with self.subTest(path=path):
                rig, ctx, definition = self.trainer(path)
                self.play(rig, ctx)
                opponent_hand = list(ctx.hand(P2))
                selected = opponent_hand[0]
                hand_before = len(ctx.hand())
                with patch('spirit.game.card_effects.standard_era.random.choice',
                           return_value=selected):
                    await definition.effect(ctx)
                self.assertEqual(len(ctx.hand()), hand_before + 2)
                self.assertIn(selected, ctx.discard_pile(P2))
                self.assertNotIn(selected, ctx.hand(P2))
                self.assertEqual(len(ctx.hand(P2)), len(opponent_hand) - 1)

        rig, ctx, definition = self.trainer('SM5.Mars_128')
        self.play(rig, ctx)
        ctx.draw_cards = AsyncMock(return_value=0)
        ctx.discard_cards = AsyncMock()
        await definition.effect(ctx)
        ctx.discard_cards.assert_not_awaited()

    async def test_team_rockets_trickery_opponent_chooses_discard(self):
        rig, ctx, definition = self.trainer('HGSS3.TeamRocketsTrickery_78')
        self.play(rig, ctx)
        opponent_hand = list(ctx.hand(P2))
        selected = opponent_hand[-1]
        ctx.choose_cards = AsyncMock(return_value=[selected])
        hand_before = len(ctx.hand())
        await definition.effect(ctx)
        self.assertEqual(len(ctx.hand()), hand_before + 2)
        args = ctx.choose_cards.await_args
        self.assertEqual(args.args[:2], (opponent_hand, 1))
        self.assertEqual(args.kwargs['player_id'], P2)
        self.assertIn(selected, ctx.discard_pile(P2))

    async def test_morty_requires_psychic_ko_and_selects_two_cards(self):
        for path in ('SM8.Morty_186', 'SM8.Morty_212'):
            with self.subTest(path=path):
                rig, ctx, definition = self.trainer(path)
                legal = lambda: trainer_condition_met(
                    definition.condition, rig.board, P1, ctx.source)
                self.assertFalse(legal())
                state = rig.session.turn_state
                state.kos_suffered_last_turn[P1] = [{
                    'archetype_id': fixtures.definition('SV1.Miraidonex_81').guid,
                    'pokemon_types': [PokemonTypes.LIGHTNING.value],
                }]
                self.assertFalse(legal())
                state.kos_suffered_last_turn[P1] = [{
                    'archetype_id': fixtures.definition('SV1.Klefki_96').guid,
                    'pokemon_types': [PokemonTypes.PSYCHIC.value],
                }]
                self.assertTrue(legal())
                self.play(rig, ctx)
                original_hand = list(ctx.hand(P2))
                chosen = original_hand[:2]
                ctx.choose_from_revealed_hand = AsyncMock(return_value=chosen)
                await definition.effect(ctx)
                args = ctx.choose_from_revealed_hand.await_args
                self.assertEqual(args.args[:2], (original_hand, 2))
                self.assertEqual(args.kwargs['minimum'], 2)
                self.assertEqual(args.kwargs['of_player'], P2)
                self.assertTrue(all(card in ctx.deck(P2) for card in chosen))
                self.assertTrue(all(card not in ctx.hand(P2) for card in chosen))
                self.assertEqual(len(ctx.hand(P2)), len(original_hand) - 2)

    async def test_diantha_keeps_its_fairy_ko_requirement(self):
        rig, ctx, definition = self.trainer('SM6.Diantha_105')
        legal = lambda: trainer_condition_met(
            definition.condition, rig.board, P1, ctx.source)
        self.assertFalse(legal())
        rig.session.turn_state.kos_suffered_last_turn[P1] = [{
            'archetype_id': fixtures.definition('SM4.Xerneas_73').guid,
            'pokemon_types': [PokemonTypes.FAIRY.value],
        }]
        self.assertTrue(legal())

    async def test_lacey_draws_four_or_eight_on_every_printing(self):
        printings = (
            'SV07.Lacey_139', 'SV07.Lacey_166', 'SV07.Lacey_172',
            'SV085.Lacey_114', 'SV085.Lacey_175',
        )
        for path in printings:
            for qualifying in (False, True):
                with self.subTest(path=path, qualifying=qualifying):
                    rig, ctx, definition = self.trainer(path)
                    if qualifying:
                        self.fewer_opponent_prizes(rig)
                    self.play(rig, ctx)
                    await definition.effect(ctx)
                    self.assertEqual(len(ctx.hand()), 8 if qualifying else 4)

    async def test_other_conditional_draw_supporters(self):
        cases = (
            ('SV4.Norman_168', 'opponent_ex'),
            ('SV2.Falkner_180', 'stadium'),
            ('SM11.CoachTrainer_192', 'tag_team'),
            ('SM10.SamsonOak_185', 'same_type'),
            ('SV10.EmceesHype_163', 'opponent_prizes'),
        )
        for path, qualifier in cases:
            with self.subTest(path=path):
                rig, ctx, definition = self.trainer(path)
                self.play(rig, ctx)
                if qualifier == 'same_type':
                    ctx.my_active().set_attribute(
                        AttrID.POKEMON_TYPES, [PokemonTypes.FIRE.value])
                    ctx.opponent_active().set_attribute(
                        AttrID.POKEMON_TYPES, [PokemonTypes.WATER.value])
                ctx.draw_cards = AsyncMock(return_value=2)
                await definition.effect(ctx)
                ctx.draw_cards.assert_awaited_once_with(2)
                ctx.draw_cards.reset_mock()

                if qualifier == 'opponent_ex':
                    rig.to_area(ctx.opponent_active(), P2, 'bench')
                    self.add(rig, fixtures.definition('SV1.Miraidonex_81'),
                             P2, 'activePokemonArea')
                elif qualifier == 'stadium':
                    stadium = self.add(rig, fixtures.definition('XY5.SilentLab_140'),
                                       P1, 'hand')
                    rig.board.move_card(
                        stadium.entity_id,
                        rig.board.find_global_area('activeStadium').entity_id,
                    )
                    stadium.owning_player_id = P1
                elif qualifier == 'tag_team':
                    rig.to_area(ctx.my_active(), P1, 'bench')
                    self.add(rig, fixtures.definition('SM12.ArceusDialgaPalkiaGX_156'),
                             P1, 'activePokemonArea')
                elif qualifier == 'same_type':
                    ctx.my_active().set_attribute(
                        AttrID.POKEMON_TYPES, [PokemonTypes.WATER.value])
                else:
                    self.fewer_opponent_prizes(rig)
                await definition.effect(ctx)
                ctx.draw_cards.assert_awaited_once_with(4)

    async def test_billy_bonus_uses_hand_size_after_initial_draw(self):
        for starting_hand, expected in ((7, 9), (8, 12)):
            with self.subTest(starting_hand=starting_hand):
                rig, ctx, definition = self.trainer('SV09.BillyONare_142')
                self.play(rig, ctx)
                for card in list(ctx.hand())[starting_hand:]:
                    rig.to_area(card, P1, 'discard')
                self.assertEqual(len(ctx.hand()), starting_hand)
                await definition.effect(ctx)
                self.assertEqual(len(ctx.hand()), expected)


if __name__ == '__main__':
    unittest.main()
