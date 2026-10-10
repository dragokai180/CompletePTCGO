"""Optional draw-to-hand abilities only ask when a card can be drawn."""
import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures
from spirit.game.session.legal_actions import ability_condition_met
from spirit.tools.effect_smoke import P1


class DrawUntilAbilityPromptsTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx
    add = fixtures.HgssRulesTests.add

    def set_hand_size(self, rig, size):
        hand = rig.board.find_player_area(P1, 'hand')
        for card in list(hand.children)[size:]:
            rig.to_area(card, P1, 'discard')
        while len(hand.children) < size:
            self.add(rig, fixtures.definition('BW1.Snivy_1'), P1, 'hand')

    async def test_generic_trigger_skips_confirmation_at_target(self):
        for path, title, target in (
            ('XY6.ShayminEX_77', 'Set Up', 6),
            ('SV3.Togekiss_85', 'Precious Gift', 8),
        ):
            with self.subTest(card=path):
                rig, _, ctx = self.ctx(path, title)
                self.set_hand_size(rig, target)
                ctx.ask_yes_no = AsyncMock(return_value=True)
                ctx.draw_until = AsyncMock()
                await ctx.ability.effect(ctx)
                ctx.ask_yes_no.assert_not_awaited()
                ctx.draw_until.assert_not_awaited()
                self.assertTrue(ctx.suppress_announce)

                self.set_hand_size(rig, target - 1)
                ctx.suppress_announce = False
                await ctx.ability.effect(ctx)
                ctx.ask_yes_no.assert_awaited_once()
                ctx.draw_until.assert_awaited_once_with(target)

    async def test_dark_asset_skips_confirmation_at_target(self):
        rig, _, ctx = self.ctx('SWSH3.CrobatV_104', 'Dark Asset')
        self.set_hand_size(rig, 6)
        ctx.ask_yes_no = AsyncMock(return_value=True)
        ctx.draw_until = AsyncMock()
        await ctx.ability.effect(ctx)
        ctx.ask_yes_no.assert_not_awaited()
        ctx.draw_until.assert_not_awaited()

        self.set_hand_size(rig, 5)
        await ctx.ability.effect(ctx)
        ctx.ask_yes_no.assert_awaited_once()
        ctx.draw_until.assert_awaited_once_with(6)

    async def test_activated_draw_ability_is_unavailable_at_target(self):
        rig, _, ctx = self.ctx('SV035.Mewex_151', 'Restart')
        self.set_hand_size(rig, 3)
        self.assertFalse(ability_condition_met(
            ctx.ability, rig.board, P1, ctx.source))
        self.set_hand_size(rig, 2)
        self.assertTrue(ability_condition_met(
            ctx.ability, rig.board, P1, ctx.source))
