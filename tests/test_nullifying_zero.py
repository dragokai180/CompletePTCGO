"""Nullifying Zero flips separately for every opposing Pokémon."""
import unittest
from unittest.mock import AsyncMock, call

from tests import test_hgss_rules as fixtures
from spirit.game.attributes import AttrID


class NullifyingZeroTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx

    async def test_each_print_pairs_a_flip_with_each_target(self):
        for path in ('ME3.MegaZygardeex_47', 'MEP.MegaZygardeex_71'):
            with self.subTest(card=path):
                _, _, ctx = self.ctx(path, 'Nullifying Zero')
                targets = list(ctx.opponent_pokemon_in_play())
                self.assertGreaterEqual(len(targets), 2)
                self.assertIs(targets[0], ctx.defender)
                results = [True, False] + [True] * (len(targets) - 2)
                ctx.flip_coins = AsyncMock(return_value=results)
                ctx.deal_damage = AsyncMock(return_value=150)

                await ctx.ability.effect(ctx)

                ctx.flip_coins.assert_awaited_once_with(
                    len(targets), 'Nullifying Zero')
                ctx.deal_damage.assert_has_awaits([
                    call(150, target=target,
                         apply_modifiers=(target is ctx.defender))
                    for target, heads in zip(targets, results) if heads
                ])
                self.assertEqual(ctx.deal_damage.await_count, sum(results))

    async def test_all_tails_do_no_damage(self):
        _, _, ctx = self.ctx('ME3.MegaZygardeex_47', 'Nullifying Zero')
        ctx.flip_coins = AsyncMock(
            return_value=[False] * len(ctx.opponent_pokemon_in_play()))
        ctx.deal_damage = AsyncMock()

        await ctx.ability.effect(ctx)

        ctx.deal_damage.assert_not_awaited()

    async def test_benched_target_takes_damage_on_board(self):
        _, _, ctx = self.ctx('ME3.MegaZygardeex_47', 'Nullifying Zero')
        targets = list(ctx.opponent_pokemon_in_play())
        for target in targets:
            target.set_attribute(AttrID.HP, 400)
        ctx.flip_coins = AsyncMock(return_value=[False, True] +
                                   [False] * (len(targets) - 2))

        await ctx.ability.effect(ctx)

        self.assertEqual(ctx.defender.get_attribute(AttrID.HP), 400)
        self.assertEqual(targets[1].get_attribute(AttrID.HP), 250)
