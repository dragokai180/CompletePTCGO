"""Coin-gated effects must flip before applying their printed outcomes."""
import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures
from spirit.game.session.effects import is_basic_pokemon
from spirit.game.session.passives import effective_bench_capacity
from spirit.tools.effect_smoke import P1, P2


class CoinInteractionTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx
    add = fixtures.HgssRulesTests.add

    async def test_tails_skip_coin_gated_effects(self):
        cases = (
            ('BW2.Krookodile_62', 'Black Eyes', 'discard_cards'),
            ('SM10.Caterpie_2', 'Pupate', 'search_deck'),
            ('SM10.Metapod_3', 'Emerge', 'search_deck'),
            ('SM10.Gloom_7', 'Irresistible Aroma', 'reveal_hand'),
            ('SM11.Wynaut_77', 'Peppy Pick', 'shuffle_into_deck'),
            ('ME3.Talonflame_14', 'Sky Hunt', 'discard_cards'),
        )
        for path, title, outcome in cases:
            with self.subTest(ability=title):
                _, _, ctx = self.ctx(path, title)
                ctx.flip_coins = AsyncMock(return_value=[False])
                skipped = AsyncMock()
                setattr(ctx, outcome, skipped)
                await ctx.ability.effect(ctx)
                ctx.flip_coins.assert_awaited_once_with(1, title)
                skipped.assert_not_awaited()
                if title == 'Peppy Pick':
                    self.assertTrue(ctx.ends_turn)

    async def test_heads_apply_random_hand_effects_once(self):
        for path, title, destination in (
                ('SM11.Wynaut_77', 'Peppy Pick', 'shuffle_into_deck'),
                ('ME3.Talonflame_14', 'Sky Hunt', 'discard_cards')):
            with self.subTest(ability=title):
                _, _, ctx = self.ctx(path, title)
                hand = set(ctx.hand(P2))
                ctx.flip_coins = AsyncMock(return_value=[True])
                ctx.reveal_cards = AsyncMock()
                moved = AsyncMock()
                setattr(ctx, destination, moved)
                await ctx.ability.effect(ctx)
                ctx.flip_coins.assert_awaited_once_with(1, title)
                moved.assert_awaited_once()
                selected = moved.await_args.args[0]
                self.assertEqual(len(selected), 1)
                self.assertIn(selected[0], hand)
                if title == 'Peppy Pick':
                    self.assertEqual(moved.await_args.kwargs['player_id'], P2)
                    ctx.reveal_cards.assert_awaited_once_with(selected)
                    self.assertTrue(ctx.ends_turn)
                else:
                    ctx.reveal_cards.assert_not_awaited()

    async def test_heads_enter_early_search_reveal_and_energy_branches(self):
        for path, title, outcome in (
                ('SM10.Caterpie_2', 'Pupate', 'search_deck'),
                ('SM10.Metapod_3', 'Emerge', 'search_deck'),
                ('SM10.Gloom_7', 'Irresistible Aroma', 'reveal_hand')):
            with self.subTest(ability=title):
                _, _, ctx = self.ctx(path, title)
                ctx.flip_coins = AsyncMock(return_value=[True])
                entered = AsyncMock(return_value=[])
                setattr(ctx, outcome, entered)
                await ctx.ability.effect(ctx)
                ctx.flip_coins.assert_awaited_once_with(1, title)
                entered.assert_awaited_once()

    async def test_black_eyes_heads_discards_opposing_energy(self):
        _, _, ctx = self.ctx('BW2.Krookodile_62', 'Black Eyes')
        energy = ctx.attached_energies(ctx.defender)[0]
        ctx.flip_coins = AsyncMock(return_value=[True])
        ctx.choose_cards = AsyncMock(return_value=[energy])
        ctx.discard_cards = AsyncMock()
        await ctx.ability.effect(ctx)
        ctx.flip_coins.assert_awaited_once_with(1, 'Black Eyes')
        ctx.discard_cards.assert_awaited_once_with([energy])

    async def test_irresistible_aroma_flips_before_offering_only_basics(self):
        rig, _, ctx = self.ctx('SM10.Gloom_7', 'Irresistible Aroma')
        for card in list(ctx.hand(P2)):
            rig.to_area(card, P2, 'deck')
        basic = self.add(rig, self.filler, P2, 'hand')
        evolved = self.add(rig, fixtures.definition('SM10.Gloom_7'), P2, 'hand')
        item = self.add(rig, self.item, P2, 'hand')
        hand = [basic, evolved, item]
        events = []

        async def flip(*args):
            events.append('flip')
            return [True]

        async def flush(*args):
            events.append('coin_shown')

        async def choose(*args):
            events.append('hand_shown')
            self.assertEqual(args[0], P1)
            self.assertEqual(args[2], [basic])
            self.assertEqual(args[7], hand)
            return [basic.entity_id]

        ctx.flip_coins = AsyncMock(side_effect=flip)
        rig.session._flush_effect_runs = AsyncMock(side_effect=flush)
        rig.session.prompt_card_chooser = AsyncMock(side_effect=choose)
        await ctx.ability.effect(ctx)

        self.assertEqual(events[:3], ['flip', 'coin_shown', 'hand_shown'])
        self.assertTrue(is_basic_pokemon(basic))
        self.assertIn(basic, ctx.opponent_bench())
        self.assertNotIn(evolved, ctx.opponent_bench())
        self.assertNotIn(item, ctx.opponent_bench())

    async def test_irresistible_aroma_tails_never_opens_hand(self):
        rig, _, ctx = self.ctx('SM10.Gloom_7', 'Irresistible Aroma')
        rig.session.prompt_card_chooser = AsyncMock()
        rig.session.prompt_view_cards = AsyncMock()
        ctx.flip_coins = AsyncMock(return_value=[False])
        await ctx.ability.effect(ctx)
        rig.session.prompt_card_chooser.assert_not_awaited()
        rig.session.prompt_view_cards.assert_not_awaited()

    async def test_irresistible_aroma_requires_opponent_bench_space(self):
        rig, _, ctx = self.ctx('SM10.Gloom_7', 'Irresistible Aroma')
        while len(ctx.opponent_bench()) < effective_bench_capacity(rig.board, P2):
            self.add(rig, self.filler, P2, 'bench')
        self.assertFalse(ctx.ability.condition(rig.board, P1, ctx.source))
        ctx.flip_coins = AsyncMock()
        await ctx.ability.effect(ctx)
        ctx.flip_coins.assert_not_awaited()

    async def test_pendulum_influence_flips_before_copying(self):
        card = fixtures.definition('SV1.Hypno_83')
        for heads in (False, True):
            with self.subTest(heads=heads):
                rig, _, ctx = self.ctx('SV1.Hypno_83', 'Pendulum Influence')
                target = self.add(rig, card, P2, 'bench')
                copied = card.abilities[1]
                ctx.flip_coins = AsyncMock(return_value=[heads])
                ctx.choose_attack_to_copy = AsyncMock(return_value=(target, copied))
                ctx.use_attack = AsyncMock()
                await ctx.ability.effect(ctx)
                ctx.flip_coins.assert_awaited_once_with(1, 'Pendulum Influence')
                if heads:
                    ctx.choose_attack_to_copy.assert_awaited_once()
                    ctx.use_attack.assert_awaited_once_with(copied)
                else:
                    ctx.choose_attack_to_copy.assert_not_awaited()
                    ctx.use_attack.assert_not_awaited()
