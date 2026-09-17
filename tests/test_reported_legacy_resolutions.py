"""Regression tests for duplicate legacy effects and printed search counts."""
import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures
from tests.test_hgss_rules import definition
from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.data_utils import def_for
from spirit.game.session.effects import EffectContext
from spirit.tools.effect_smoke import P1, P2


class LegacyResolutionTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx
    add = fixtures.HgssRulesTests.add

    async def test_cleffa_shuffles_before_drawing_six_exactly_once(self):
        rig, entries, ctx = self.ctx('Promo_HGSS.Cleffa_12', 'Eeeeeeek')
        events = []
        shuffle, draw = ctx.shuffle_into_deck, ctx.draw_cards

        async def record_shuffle(cards, **kwargs):
            events.append('shuffle')
            return await shuffle(cards, **kwargs)

        async def record_draw(count, **kwargs):
            events.append(('draw', count))
            return await draw(count, **kwargs)

        ctx.shuffle_into_deck = record_shuffle
        ctx.draw_cards = record_draw
        status = ctx.apply_special_condition

        async def record_status(*args, **kwargs):
            events.append('status')
            return await status(*args, **kwargs)

        ctx.apply_special_condition = record_status
        await ctx.ability.effect(ctx)
        self.assertEqual(events, ['shuffle', ('draw', 6), 'status'])
        self.assertEqual(ctx.hand_size(), 6)
        self.assertIn('Asleep', entries['target'].get_attribute(AttrID.SPECIAL_CONDITIONS))

    async def test_twins_requests_two_private_cards(self):
        for remaining in (1, 4):
            with self.subTest(remaining=remaining):
                rig, entries = self.rig('HGSS4.Twins_89', 'trainer')
                rig.to_area(entries['target'], P1, 'discard')
                ctx = EffectContext(rig.session, P1, entries['target'], None)
                prize = rig.board.find_player_area(P2, 'prizePile').children[0]
                rig.to_area(prize, P2, 'hand')
                for card in list(ctx.deck())[remaining:]:
                    rig.to_area(card, P1, 'discard')
                ctx.choose_cards = AsyncMock(wraps=ctx.choose_cards)
                ctx.put_in_hand = AsyncMock(wraps=ctx.put_in_hand)
                before = ctx.hand_size()
                await definition('HGSS4.Twins_89').effect(ctx)
                ctx.choose_cards.assert_awaited_once()
                call = ctx.choose_cards.call_args
                self.assertEqual(call.args[1], 2)
                self.assertEqual(call.kwargs['minimum'], 2)
                self.assertEqual(ctx.hand_size() - before, min(2, remaining))
                self.assertFalse(ctx.put_in_hand.call_args.kwargs['reveal'])

    async def test_junk_hunt_recovers_at_most_two_items_once(self):
        for available in (0, 1, 2, 4):
            with self.subTest(available=available):
                rig, entries, ctx = self.ctx('BW5.Sableye_62', 'Junk Hunt')
                for card in list(ctx.discard_pile()):
                    rig.to_area(card, P1, 'deck')
                items = [self.add(rig, self.item, P1, 'discard') for _ in range(available)]
                supporter = self.add(rig, definition('HGSS4.Twins_89'), P1, 'discard')
                ctx.choose_cards = AsyncMock(wraps=ctx.choose_cards)
                before = ctx.hand_size()
                await ctx.ability.effect(ctx)
                self.assertEqual(ctx.hand_size() - before, min(2, available))
                self.assertEqual(ctx.choose_cards.await_count, int(available > 0))
                self.assertIn(supporter, ctx.discard_pile())
                self.assertEqual(sum(card in ctx.hand() for card in items), min(2, available))

    async def test_other_hand_resets_use_the_printed_count_once(self):
        cases = (
            ('XY8.Starmie_30', 'Deep Sea Swirl', 7),
            ('BW4.Darmanitan_60', 'Synchrodraw', 'opponent'),
            ('Promo_SM.Mimikyu_163', 'Mimic', 'opponent'),
            ('XY6.Altaria_53', 'Song of Echoes', 'bench'),
        )
        for path, title, expected in cases:
            with self.subTest(path=path):
                rig, entries, ctx = self.ctx(path, title)
                if expected == 'opponent':
                    expected = ctx.hand_size(P2)
                elif expected == 'bench':
                    expected = len(ctx.my_bench()) + len(ctx.opponent_bench())
                ctx.draw_cards = AsyncMock(wraps=ctx.draw_cards)
                ctx.shuffle_into_deck = AsyncMock(wraps=ctx.shuffle_into_deck)
                await ctx.ability.effect(ctx)
                ctx.draw_cards.assert_awaited_once()
                ctx.shuffle_into_deck.assert_awaited_once()
                self.assertEqual(ctx.draw_cards.call_args.args[0], expected)
                self.assertEqual(ctx.hand_size(), expected)

    async def test_tag_draw_preserves_minun_bonus_without_an_extra_draw(self):
        for has_minun in (False, True):
            with self.subTest(has_minun=has_minun):
                rig, entries, ctx = self.ctx('BW5.Plusle_39', 'Tag Draw')
                if has_minun:
                    self.add(rig, definition('BW5.Minun_40'), P1, 'bench')
                ctx.draw_cards = AsyncMock(wraps=ctx.draw_cards)
                await ctx.ability.effect(ctx)
                ctx.draw_cards.assert_awaited_once()
                self.assertEqual(ctx.hand_size(), 8 if has_minun else 4)

    async def test_other_public_recovery_templates_do_not_repeat(self):
        cases = (
            ('SV2.Tinkatink_101', self.item, 1),
            ('SM5.Spiritomb_53', definition('HGSS4.Twins_89'), 2),
            ('XY3.Minun_32', def_for(self.energies[PokemonTypes.WATER.value]), 2),
        )
        for path, recovered_card, count in cases:
            with self.subTest(path=path):
                title = next(a.title for a in definition(path).abilities
                             if 'discard pile into your hand' in a.game_text)
                rig, entries, ctx = self.ctx(path, title)
                for card in list(ctx.discard_pile()):
                    rig.to_area(card, P1, 'deck')
                for _ in range(4):
                    self.add(rig, recovered_card, P1, 'discard')
                ctx.choose_cards = AsyncMock(wraps=ctx.choose_cards)
                before = ctx.hand_size()
                await ctx.ability.effect(ctx)
                self.assertEqual(ctx.hand_size() - before, count)
                ctx.choose_cards.assert_awaited_once()


if __name__ == '__main__':
    unittest.main()
