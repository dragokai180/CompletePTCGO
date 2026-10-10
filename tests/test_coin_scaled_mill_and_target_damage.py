"""Coin-scaled mill and selected/spread damage keep their printed targets."""
import unittest
from unittest.mock import AsyncMock, Mock

from tests import test_hgss_rules as fixtures
from spirit.tools.effect_smoke import P1, P2


class CoinScaledAttackTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx
    add = fixtures.HgssRulesTests.add

    async def test_undersea_tunnel_mills_three_per_head(self):
        for path in ('SV1.Wugtrio_57', 'SV045.Wugtrio_122'):
            for flips in ([False] * 3, [True, False, False],
                          [True, False, True], [True] * 3):
                with self.subTest(card=path, flips=flips):
                    _, _, ctx = self.ctx(path, 'Undersea Tunnel')
                    ctx.flip_coins = AsyncMock(return_value=flips)
                    ctx.deck_top = Mock(return_value=[])
                    ctx.discard_cards = AsyncMock()
                    await ctx.ability.effect(ctx)
                    ctx.flip_coins.assert_awaited_once_with(3, 'Undersea Tunnel')
                    count = 3 * sum(flips)
                    if count:
                        ctx.deck_top.assert_called_once_with(count, P2)
                        ctx.discard_cards.assert_awaited_once()
                    else:
                        ctx.deck_top.assert_not_called()
                        ctx.discard_cards.assert_not_awaited()

    async def test_undersea_tunnel_moves_six_real_cards_on_two_heads(self):
        _, _, ctx = self.ctx('SV1.Wugtrio_57', 'Undersea Tunnel')
        deck_before = len(ctx.deck(P2))
        discard_before = len(ctx.discard_pile(P2))
        ctx.flip_coins = AsyncMock(return_value=[True, False, True])
        await ctx.ability.effect(ctx)
        self.assertEqual(len(ctx.deck(P2)), deck_before - 6)
        self.assertEqual(len(ctx.discard_pile(P2)), discard_before + 6)

    async def test_other_coin_scaled_mill(self):
        for path, title, flips, per_head in (
                ('SV06.Crawdaunt_48', 'Snip Snip', [True, False], 1),
                ('ME55.Maushold_125', 'Gnaw Together', [True, False], 2)):
            with self.subTest(card=path):
                _, _, ctx = self.ctx(path, title)
                ctx.flip_coins = AsyncMock(return_value=flips)
                ctx.deck_top = Mock(return_value=[])
                ctx.discard_cards = AsyncMock()
                ctx.deal_damage = AsyncMock(return_value=40)
                await ctx.ability.effect(ctx)
                ctx.flip_coins.assert_awaited_once_with(
                    len(flips), *([title] if title == 'Snip Snip' else []))
                ctx.deck_top.assert_called_once_with(per_head, P2)
                if title == 'Snip Snip':
                    ctx.deal_damage.assert_awaited_once()
                    self.assertEqual(ctx.deal_damage.await_args.args[0], 40)

    async def test_flip_until_tails_mill_uses_all_heads(self):
        for results, expected in (([[False]], 0),
                                  ([[True], [True], [False]], 2)):
            with self.subTest(results=results):
                _, _, ctx = self.ctx('ME3.Tyrantrum_45', 'Wreak Havoc')
                ctx.flip_coins = AsyncMock(side_effect=results)
                ctx.deck_top = Mock(return_value=[])
                ctx.discard_cards = AsyncMock()
                ctx.deal_damage = AsyncMock(return_value=160)
                await ctx.ability.effect(ctx)
                self.assertEqual(ctx.flip_coins.await_count, len(results))
                ctx.deal_damage.assert_awaited_once()
                if expected:
                    ctx.deck_top.assert_called_once_with(expected, P2)
                else:
                    ctx.deck_top.assert_not_called()
                    ctx.discard_cards.assert_not_awaited()

    async def test_target_together_chooses_before_flips_and_only_counts_tauros(self):
        for path in ('ME4.Tauros_69', 'ME4.Tauros_96'):
            with self.subTest(card=path):
                _, _, ctx = self.ctx(path, 'Target Together')
                target = ctx.opponent_bench()[0]
                events = []

                async def choose(pool, *_args):
                    events.append('choose')
                    self.assertIn(ctx.defender, pool)
                    self.assertIn(target, pool)
                    return target

                async def flip(count, title):
                    events.append('flip')
                    self.assertEqual((count, title), (2, 'Target Together'))
                    return [True, False]

                ctx.choose_pokemon = AsyncMock(side_effect=choose)
                ctx.flip_coins = AsyncMock(side_effect=flip)
                ctx.deal_damage = AsyncMock(return_value=50)
                await ctx.ability.effect(ctx)
                self.assertEqual(events, ['choose', 'flip'])
                ctx.deal_damage.assert_awaited_once_with(
                    50, target=target, apply_modifiers=False)

    async def test_target_together_tails_does_no_damage(self):
        _, _, ctx = self.ctx('ME4.Tauros_69', 'Target Together')
        ctx.choose_pokemon = AsyncMock(return_value=ctx.defender)
        ctx.flip_coins = AsyncMock(return_value=[False])
        ctx.deal_damage = AsyncMock()
        await ctx.ability.effect(ctx)
        ctx.deal_damage.assert_not_awaited()

    async def test_target_together_can_hit_active_for_each_head(self):
        _, _, ctx = self.ctx('ME4.Tauros_69', 'Target Together')
        ctx.choose_pokemon = AsyncMock(return_value=ctx.defender)
        ctx.flip_coins = AsyncMock(return_value=[True, True])
        ctx.deal_damage = AsyncMock(return_value=100)
        await ctx.ability.effect(ctx)
        ctx.deal_damage.assert_awaited_once_with(
            100, target=ctx.defender, apply_modifiers=True)

    async def test_target_together_damages_chosen_bench_in_board_state(self):
        _, _, ctx = self.ctx('ME4.Tauros_69', 'Target Together')
        target = ctx.opponent_bench()[0]
        active_hp = ctx.defender.get_attribute(fixtures.AttrID.HP)
        bench_hp = target.get_attribute(fixtures.AttrID.HP)
        ctx.choose_pokemon = AsyncMock(return_value=target)
        ctx.flip_coins = AsyncMock(return_value=[True, False])
        await ctx.ability.effect(ctx)
        self.assertEqual(target.get_attribute(fixtures.AttrID.HP), bench_hp - 50)
        self.assertEqual(ctx.defender.get_attribute(fixtures.AttrID.HP), active_hp)

    async def test_miracle_harmony_counts_sing_users_and_hits_every_target(self):
        _, _, ctx = self.ctx('SM8.Meloetta_104', 'Miracle Harmony')
        ctx.flip_coins = AsyncMock(return_value=[True, False])
        ctx.deal_damage = AsyncMock(return_value=10)
        targets = list(ctx.opponent_pokemon_in_play())
        await ctx.ability.effect(ctx)
        ctx.flip_coins.assert_awaited_once_with(2, 'Miracle Harmony')
        self.assertEqual(ctx.deal_damage.await_count, len(targets))
        for call, target in zip(ctx.deal_damage.await_args_list, targets):
            self.assertEqual(call.args[0], 10)
            self.assertIs(call.kwargs['target'], target)
            self.assertEqual(call.kwargs['apply_modifiers'], target is ctx.defender)


if __name__ == '__main__':
    unittest.main()
