"""Coin attacks preserve the printed number of flips and damage targets."""
import unittest
from unittest.mock import AsyncMock, call

from tests import test_hgss_rules as fixtures
from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.data_utils import def_for
from spirit.tools.effect_smoke import P1


class CoinAttackAuditTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx
    add = fixtures.HgssRulesTests.add

    async def test_trample_flips_for_both_benches_and_keeps_active_hit(self):
        _, _, ctx = self.ctx('SM7.Tyranitar_87', 'Trample')
        bench = list(ctx.my_bench()) + list(ctx.opponent_bench())
        results = [index % 2 == 0 for index in range(len(bench))]
        ctx.flip_coins = AsyncMock(return_value=results)
        ctx.deal_damage = AsyncMock(return_value=60)

        await ctx.ability.effect(ctx)

        ctx.flip_coins.assert_awaited_once_with(len(bench), 'Trample')
        ctx.deal_damage.assert_has_awaits([
            call(120, ignore_weakness=True, ignore_resistance=True),
            *(call(60, target=target, apply_modifiers=False)
              for target, heads in zip(bench, results) if heads),
        ])
        self.assertEqual(ctx.deal_damage.await_count, 1 + sum(results))

    async def test_heads_scaled_spread_hits_every_opposing_pokemon(self):
        for path, title, per_head in (
            ('BW2.Swoobat_37', 'Phat Sound', 10),
            ('Promo_XY.Meloetta_120', 'Soprano Wave', 10),
            ('XY5.Rhyperior_76', 'Rock Shower', 20),
            ('SM8.Forretress_124', 'Thorny Eruption', 10),
        ):
            with self.subTest(card=path):
                _, _, ctx = self.ctx(path, title)
                ctx.flip_coins = AsyncMock(return_value=[True, False, True])
                ctx.deal_damage = AsyncMock(return_value=20)
                await ctx.ability.effect(ctx)
                ctx.flip_coins.assert_awaited_once_with(3, title)
                targets = list(ctx.opponent_pokemon_in_play())
                ctx.deal_damage.assert_has_awaits([
                    call(2 * per_head, target=target,
                         apply_modifiers=(target is ctx.defender))
                    for target in targets
                ])
                self.assertEqual(ctx.deal_damage.await_count, len(targets))

    async def test_base_plus_each_head_keeps_the_base_damage(self):
        for path, title, base, bonus in (
            ('HGSS2.Onix_57', 'Swing Around', 20, 20),
            ('HGSS3.Makuhita_55', 'Slap Down', 20, 10),
        ):
            with self.subTest(card=path):
                _, _, ctx = self.ctx(path, title)
                ctx.flip_coins = AsyncMock(return_value=[True, False])
                ctx.deal_damage = AsyncMock(return_value=base + bonus)
                await ctx.ability.effect(ctx)
                self.assertEqual(ctx.deal_damage.await_args.args[0], base + bonus)

    async def test_flips_once_per_damage_counter(self):
        _, _, ctx = self.ctx('XY1.Tauros_100', 'Seething Anger')
        ctx.attacker.set_attribute(AttrID.HP, ctx.max_hp(ctx.attacker) - 20)
        ctx.flip_coins = AsyncMock(return_value=[True, False])
        ctx.deal_damage = AsyncMock(return_value=30)

        await ctx.ability.effect(ctx)

        ctx.flip_coins.assert_awaited_once_with(2, 'Seething Anger')
        self.assertEqual(ctx.deal_damage.await_args.args[0], 30)

    async def test_team_aqua_coin_count_uses_team_name(self):
        rig, _, ctx = self.ctx('TATM.TeamAquasMightyena_18', 'Teampact')
        self.add(rig, fixtures.definition('TATM.TeamAquasPoochyena_16'),
                 P1, 'bench')
        self.add(rig, fixtures.definition('TATM.TeamMagmasPoochyena_17'),
                 P1, 'bench')
        expected = sum(def_for(pokemon.archetype_id).display_name.startswith(
            "Team Aqua's ") for pokemon in ctx.my_pokemon_in_play())
        ctx.flip_coins = AsyncMock(return_value=[True] + [False] * (expected - 1))
        ctx.deal_damage = AsyncMock(return_value=30)

        await ctx.ability.effect(ctx)

        ctx.flip_coins.assert_awaited_once_with(expected, 'Teampact')
        self.assertEqual(ctx.deal_damage.await_args.args[0], 30)

    async def test_primeape_chooses_target_before_repeated_coins(self):
        _, _, ctx = self.ctx('HGSS2.Primeape_22', 'Bebop Punch')
        target = ctx.opponent_bench()[0]
        events = []

        async def choose(*_args, **_kwargs):
            events.append('choose')
            return target

        async def flip(*_args, **_kwargs):
            events.append('flip')
            return [len(events) < 3]

        ctx.choose_pokemon = AsyncMock(side_effect=choose)
        ctx.flip_coins = AsyncMock(side_effect=flip)
        ctx.deal_damage = AsyncMock(return_value=50)

        await ctx.ability.effect(ctx)

        self.assertEqual(events, ['choose', 'flip', 'flip'])
        ctx.deal_damage.assert_awaited_once_with(
            50, target=target, apply_modifiers=False)

    async def test_ash_greninja_flips_before_choosing_target(self):
        _, _, ctx = self.ctx('Promo_XY.AshGreninjaEX_133',
                             'Dancing Shuriken')
        target = ctx.opponent_bench()[0]
        events = []

        async def flip(*_args, **_kwargs):
            events.append('flip')
            return [True, False, True]

        async def choose(*_args, **_kwargs):
            events.append('choose')
            return target

        ctx.flip_coins = AsyncMock(side_effect=flip)
        ctx.choose_pokemon = AsyncMock(side_effect=choose)
        ctx.deal_damage = AsyncMock(return_value=40)

        await ctx.ability.effect(ctx)

        self.assertEqual(events, ['flip', 'choose'])
        ctx.deal_damage.assert_awaited_once_with(
            40, target=target, apply_modifiers=False)

    async def test_conditional_spread_respects_heads_and_tails(self):
        for path, title, damage in (
            ('BW8.Cubchoo_40', 'Hail', 10),
            ('COL.Kyogre_12', 'Destructive Tsunami', 40),
            ('COL.Kyogre_101', 'Destructive Tsunami', 40),
        ):
            for heads in (True, False):
                with self.subTest(card=path, heads=heads):
                    _, _, ctx = self.ctx(path, title)
                    ctx.flip_coins = AsyncMock(return_value=[heads])
                    ctx.deal_damage = AsyncMock(return_value=damage)
                    await ctx.ability.effect(ctx)
                    targets = (ctx.opponent_pokemon_in_play() if heads else
                               ctx.my_pokemon_in_play()
                               if path.startswith('COL.') else [])
                    ctx.deal_damage.assert_has_awaits([
                        call(damage, target=target,
                             apply_modifiers=(target is ctx.defender))
                        for target in targets
                    ])
                    self.assertEqual(ctx.deal_damage.await_count,
                                     len(targets))

    async def test_psyduck_coin_chooses_from_correct_side(self):
        for heads in (True, False):
            with self.subTest(heads=heads):
                _, _, ctx = self.ctx('HGSS4.Psyduck_74',
                                     'Tripping Headbutt')
                target = (ctx.opponent_bench()[0] if heads else
                          ctx.my_bench()[0])
                ctx.flip_coins = AsyncMock(return_value=[heads])
                ctx.choose_pokemon = AsyncMock(return_value=target)
                ctx.deal_damage = AsyncMock(return_value=30)
                await ctx.ability.effect(ctx)
                offered = ctx.choose_pokemon.await_args.args[0]
                self.assertIn(target, offered)
                self.assertEqual(set(offered), set(
                    ctx.opponent_pokemon_in_play() if heads else
                    ctx.my_pokemon_in_play()))
                ctx.deal_damage.assert_awaited_once_with(
                    30, target=target, apply_modifiers=False)

    async def test_sacred_fire_tails_does_not_select_or_damage(self):
        for heads in (True, False):
            with self.subTest(heads=heads):
                _, _, ctx = self.ctx('Promo_HGSS.HoOh_1', 'Sacred Fire')
                ctx.flip_coins = AsyncMock(return_value=[heads])
                ctx.choose_pokemon = AsyncMock(return_value=ctx.defender)
                ctx.deal_damage = AsyncMock(return_value=80)
                await ctx.ability.effect(ctx)
                if heads:
                    ctx.deal_damage.assert_awaited_once_with(
                        80, target=ctx.defender, apply_modifiers=True,
                        ignore_weakness=True, ignore_resistance=True)
                else:
                    ctx.choose_pokemon.assert_not_awaited()
                    ctx.deal_damage.assert_not_awaited()

    async def test_discrete_head_outcomes_use_correct_damage(self):
        for path, title, expected in (
            ('BW1.Maractus_12', 'Constant Rattle', (0, 10, 30, 60)),
            ('HGSS4.Kricketune_24', 'Fury Cutter', (20, 40, 60, 120)),
            ('SM8.Scyther_3', 'Fury Cutter', (10, 30, 60, 80)),
            ('SM1.Parasect_5', 'Fury Cutter', (10, 30, 70, 120)),
        ):
            for heads, damage in enumerate(expected):
                with self.subTest(card=path, heads=heads):
                    _, _, ctx = self.ctx(path, title)
                    ctx.flip_coins = AsyncMock(
                        return_value=[True] * heads + [False] * (3 - heads))
                    ctx.deal_damage = AsyncMock(return_value=damage)
                    await ctx.ability.effect(ctx)
                    if damage:
                        self.assertEqual(ctx.deal_damage.await_args.args[0],
                                         damage)
                    else:
                        ctx.deal_damage.assert_not_awaited()

    async def test_both_heads_adds_printed_plus_damage(self):
        for heads, expected in ((0, 20), (1, 20), (2, 70)):
            with self.subTest(heads=heads):
                _, _, ctx = self.ctx('HGSS1.Corsola_37', 'Hyper Cannon')
                ctx.flip_coins = AsyncMock(
                    return_value=[True] * heads + [False] * (2 - heads))
                ctx.deal_damage = AsyncMock(return_value=expected)
                await ctx.ability.effect(ctx)
                self.assertEqual(ctx.deal_damage.await_args.args[0], expected)

    async def test_kyogre_tails_damages_own_side_on_board(self):
        _, _, ctx = self.ctx('COL.Kyogre_12', 'Destructive Tsunami')
        own = list(ctx.my_pokemon_in_play())
        opposing = list(ctx.opponent_pokemon_in_play())
        for pokemon in own + opposing:
            pokemon.set_attribute(AttrID.HP, 400)
        ctx.flip_coins = AsyncMock(return_value=[False])

        await ctx.ability.effect(ctx)

        self.assertTrue(all(pokemon.get_attribute(AttrID.HP) == 360
                            for pokemon in own))
        self.assertTrue(all(pokemon.get_attribute(AttrID.HP) == 400
                            for pokemon in opposing))

    async def test_heads_bonus_above_base_damage(self):
        for path, title, base, bonus in (
            ('HGSS4.Pidgeot_29', 'Quick Attack', 40, 30),
            ('HGSS3.Umbreon_10', 'Quick Blow', 30, 30),
        ):
            for heads in (True, False):
                with self.subTest(card=path, heads=heads):
                    _, _, ctx = self.ctx(path, title)
                    ctx.flip_coins = AsyncMock(return_value=[heads])
                    ctx.deal_damage = AsyncMock(return_value=base)
                    await ctx.ability.effect(ctx)
                    self.assertEqual(ctx.deal_damage.await_args.args[0],
                                     base + (bonus if heads else 0))

    async def test_meowth_tails_damages_only_itself(self):
        for heads in (True, False):
            with self.subTest(heads=heads):
                _, _, ctx = self.ctx('XY8.Meowth_114',
                                     'Exhausted Tackle')
                ctx.flip_coins = AsyncMock(return_value=[heads])
                ctx.deal_damage = AsyncMock(return_value=30)
                await ctx.ability.effect(ctx)
                if heads:
                    ctx.deal_damage.assert_awaited_once_with(30)
                else:
                    ctx.deal_damage.assert_awaited_once_with(
                        30, target=ctx.attacker, apply_modifiers=False)

    async def test_named_voltorb_recoil_on_tails(self):
        for heads in (True, False):
            with self.subTest(heads=heads):
                _, _, ctx = self.ctx('HGSS4.Voltorb_83', 'Magnetic Bomb')
                ctx.flip_coins = AsyncMock(return_value=[heads])
                ctx.deal_damage = AsyncMock(return_value=20)
                await ctx.ability.effect(ctx)
                self.assertEqual(ctx.deal_damage.call_args_list[0].args[0],
                                 30 if heads else 20)
                recoil = [entry for entry in ctx.deal_damage.call_args_list
                          if entry.kwargs.get('target') is ctx.attacker]
                self.assertEqual(len(recoil), 0 if heads else 1)

    async def test_conditional_formula_uses_zero_on_tails(self):
        for path, title, count, per_counter in (
            ('BW6.Wailord_26', 'Water Cannon', 2, 30),
            ('HGSS1.Wobbuffet_13', 'Double Return', 3, 20),
            ('XY4.Blissey_81', 'Tender Vengeance', 2, 10),
        ):
            for heads in (True, False):
                with self.subTest(card=path, heads=heads):
                    rig, _, ctx = self.ctx(path, title)
                    if 'Wailord' in path:
                        for _ in range(count):
                            energy = self.add(
                                rig, def_for(self.energies[PokemonTypes.WATER.value]),
                                P1, 'hand')
                            rig.attach(energy, ctx.attacker)
                        expected = per_counter * len(
                            ctx.attached_energies(ctx.attacker))
                    elif 'Blissey' in path:
                        bench = ctx.my_bench()[0]
                        bench.set_attribute(AttrID.HP,
                                            ctx.max_hp(bench) - count * 10)
                        expected = count * per_counter
                    else:
                        ctx.attacker.set_attribute(
                            AttrID.HP, ctx.max_hp(ctx.attacker) - count * 10)
                        expected = count * per_counter
                    ctx.flip_coins = AsyncMock(return_value=[heads])
                    ctx.deal_damage = AsyncMock(return_value=expected)
                    await ctx.ability.effect(ctx)
                    if heads:
                        self.assertEqual(ctx.deal_damage.await_args.args[0],
                                         expected)
                    else:
                        ctx.deal_damage.assert_not_awaited()
