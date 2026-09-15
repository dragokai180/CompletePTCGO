"""Optional costs and information boundaries of SM/SWSH Trainers."""
import unittest
from unittest.mock import AsyncMock
from tests import test_hgss_rules as fixtures
from spirit.game.session.effects import EffectContext
from spirit.game.session.legal_actions import trainer_condition_met
from spirit.tools.effect_smoke import P1, P2


class SmSwshOptionalRecoveryTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    def setup_card(self, path):
        rig, e = self.rig(path, 'trainer')
        ctx = EffectContext(rig.session, P1, e['target'], None)
        for c in list(ctx.discard_pile()):
            rig.to_area(c, P1, 'deck')
        for c in list(ctx.hand()):
            if c is not ctx.source:
                rig.to_area(c, P1, 'deck')
        return rig, ctx, fixtures.definition(path)

    def legal(self, rig, ctx, definition):
        return trainer_condition_met(definition.condition, rig.board, P1, ctx.source)

    async def test_cynthia_caitlin_recovery_without_optional_cost_does_not_draw(self):
        rig, ctx, definition = self.setup_card('SM12.CynthiaCaitlin_189')
        copy = self.add(rig, definition, P1, 'discard')
        self.assertFalse(self.legal(rig, ctx, definition))
        target = self.add(rig, fixtures.definition('SM4.Lusamine_96'), P1, 'discard')
        self.add(rig, self.filler, P1, 'hand')
        self.assertTrue(self.legal(rig, ctx, definition))
        ctx.ask_yes_no = AsyncMock(return_value=False)
        ctx.draw_cards = AsyncMock()
        await definition.effect(ctx)
        self.assertIn(target, ctx.hand())
        self.assertIn(copy, ctx.discard_pile())
        ctx.draw_cards.assert_not_awaited()

    async def test_cynthia_caitlin_cost_precedes_recovery_and_cannot_be_recovered(self):
        rig, ctx, definition = self.setup_card('SM12.CynthiaCaitlin_189')
        first = self.add(rig, fixtures.definition('SM4.Lusamine_96'), P1, 'discard')
        second = self.add(rig, fixtures.definition('SM9.Dana_137'), P1, 'discard')
        paid = self.add(rig, fixtures.definition('SM9.Evelyn_141'), P1, 'hand')
        copy = self.add(rig, definition, P1, 'discard')
        events = []
        async def choose(pool, count, **kwargs):
            if paid in pool:
                self.assertNotIn(first, ctx.hand())
                events.append('cost')
                return [paid]
            self.assertIn(paid, ctx.discard_pile())
            self.assertEqual(set(c.entity_id for c in pool), {first.entity_id, second.entity_id})
            self.assertNotIn(copy, pool)
            events.append('recovery')
            return [first]
        async def draw(count):
            self.assertIn(first, ctx.hand())
            self.assertEqual(count, 3)
            events.append('draw')
        ctx.ask_yes_no = AsyncMock(return_value=True)
        ctx.choose_cards = choose
        ctx.draw_cards = draw
        await definition.effect(ctx)
        self.assertEqual(events, ['cost', 'recovery', 'draw'])

    async def test_cynthia_caitlin_draw_only_works_but_empty_deck_cannot_pay(self):
        rig, ctx, definition = self.setup_card('SM12.CynthiaCaitlin_189')
        cost = self.add(rig, self.filler, P1, 'hand')
        self.assertTrue(self.legal(rig, ctx, definition))
        ctx.ask_yes_no = AsyncMock(return_value=True)
        ctx.draw_cards = AsyncMock()
        await definition.effect(ctx)
        self.assertIn(cost, ctx.discard_pile())
        ctx.draw_cards.assert_awaited_once_with(3)
        for c in list(ctx.deck()):rig.to_area(c, P1, 'lostZone')
        self.add(rig, self.filler, P1, 'hand')
        self.assertFalse(self.legal(rig, ctx, definition))
        self.add(rig, fixtures.definition('SM4.Lusamine_96'), P1, 'discard')
        self.assertTrue(self.legal(rig, ctx, definition))
        ctx.ask_yes_no.reset_mock()
        ctx.draw_cards.reset_mock()
        await definition.effect(ctx)
        ctx.ask_yes_no.assert_not_awaited()
        ctx.draw_cards.assert_not_awaited()

    async def test_sordward_reveals_selection_before_opponents_choice(self):
        for consent in (False, True):
            rig, ctx, definition = self.setup_card('SWSH5.SordwardShielbert_135')
            target = self.add(rig, self.item, P1, 'discard')
            events = []
            async def reveal(cards, **kwargs):
                self.assertEqual(cards, [target])
                events.append('reveal')
            async def ask(prompt, **kwargs):
                self.assertEqual(events, ['reveal'])
                self.assertEqual(kwargs['player_id'], P2)
                events.append('choice')
                return consent
            ctx.reveal_cards = reveal
            ctx.ask_yes_no = ask
            ctx.draw_cards = AsyncMock()
            await definition.effect(ctx)
            if consent:
                self.assertIn(target, ctx.hand())
                ctx.draw_cards.assert_not_awaited()
            else:
                self.assertIn(target, ctx.discard_pile())
                ctx.draw_cards.assert_awaited_once_with(3)

    async def test_forest_seal_stone_private_search_requires_one_and_nonempty_deck(self):
        rig, e = self.rig('SWSH12.HisuianArcanineV_90')
        ability = fixtures.definition('SWSH12.ForestSealStone_156').granted_abilities[0]
        ctx = EffectContext(rig.session, P1, e['target'], ability)
        self.assertTrue(ability.condition(rig.board, P1, e['target']))
        card = ctx.deck()[0]
        ctx.search_deck = AsyncMock(return_value=[card])
        ctx.reveal_cards = AsyncMock()
        await ability.effect(ctx)
        self.assertEqual(ctx.search_deck.call_args.kwargs['minimum'], 1)
        self.assertIsNone(ctx.search_deck.call_args.args[0])
        self.assertIn(card, ctx.hand())
        ctx.reveal_cards.assert_not_awaited()
        for c in list(ctx.deck()):rig.to_area(c, P1, 'lostZone')
        self.assertFalse(ability.condition(rig.board, P1, e['target']))
