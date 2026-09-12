"""Semantic BW regressions: outcomes, choices and conditional clauses."""
import unittest
from unittest.mock import AsyncMock, Mock
from tests import test_hgss_rules as fixtures
from spirit.game.attributes import AttrID, PokemonTypes, SpecialConditions
from spirit.tools.effect_smoke import P1, P2
from tests.test_hgss_rules import definition
from spirit.game.session.effects import EffectContext, is_basic_energy


class BwRulesAuditTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx
    add = fixtures.HgssRulesTests.add

    async def test_black_eyes_requires_active_position_and_opposing_energy(self):
        rig, e, ctx = self.ctx('BW2.Krookodile_62', 'Black Eyes')
        for energy in list(ctx.attached_energies(ctx.defender)):
            rig.to_area(energy, P2, 'deck')
        self.assertFalse(ctx.ability.condition(rig.board, P1, ctx.source))
        energy = rig.pull_guid(P2, self.energies[PokemonTypes.FIRE.value])
        rig.attach(energy, ctx.defender)
        self.assertTrue(ctx.ability.condition(rig.board, P1, ctx.source))
        rig.to_area(ctx.source, P1, 'bench')
        self.assertFalse(ctx.ability.condition(rig.board, P1, ctx.source))

    async def test_old_amber_requires_space_but_not_a_private_deck_target(self):
        from spirit.game.card_effects.bw_era import bw_trainer_playable
        from spirit.game.session.passives import effective_bench_capacity
        rig, e = self.rig('BW5.OldAmberAerodactyl_97', 'trainer')
        self.assertTrue(bw_trainer_playable(rig.board, P1, e['target']))
        bench = rig.board.find_player_area(P1, 'bench')
        while len(bench.children) < effective_bench_capacity(rig.board, P1):
            self.add(rig, self.filler, P1, 'bench')
        self.assertFalse(bw_trainer_playable(rig.board, P1, e['target']))

    async def test_quick_tail_smash_can_decline_the_coin(self):
        rig, e, ctx = self.ctx('BW2.Watchog_79', 'Quick Tail Smash')
        ctx.ask_yes_no = AsyncMock(return_value=False)
        ctx.flip_coins = AsyncMock(return_value=[False])
        ctx.deal_damage = AsyncMock(return_value=20)
        await ctx.ability.effect(ctx)
        ctx.ask_yes_no.assert_awaited_once()
        ctx.flip_coins.assert_not_awaited()
        self.assertEqual(ctx.deal_damage.call_args_list[0].args[0], 20)

    async def test_tornadus_moves_energy_in_both_directions(self):
        for title in ('Energy Wheel', 'Hurricane'):
            rig, e, ctx = self.ctx('BW2.Tornadus_89', title)
            energy = rig.pull_guid(P1, self.energies[PokemonTypes.FIRE.value])
            rig.attach(energy, ctx.my_bench()[0] if title == 'Energy Wheel' else ctx.attacker)
            ctx.move_energy = AsyncMock()
            await ctx.ability.effect(ctx)
            ctx.move_energy.assert_awaited_once()
            energy, target = ctx.move_energy.call_args.args
            if title == 'Energy Wheel':
                self.assertIs(target, ctx.attacker)
            else:
                self.assertIn(target, ctx.my_bench())
                self.assertTrue(is_basic_energy(energy))

    async def test_ether_can_attach_to_bench(self):
        path = 'BW8.Ether_121'
        rig, e = self.rig(path, 'trainer')
        ctx = EffectContext(rig.session, P1, e['target'], None)
        energy = rig.pull_guid(P1, self.energies[PokemonTypes.FIRE.value])
        ctx.deck_top = Mock(return_value=[energy])
        target = ctx.my_bench()[0]
        ctx.choose_pokemon = AsyncMock(return_value=target)
        ctx.attach_energy = AsyncMock()
        await definition(path).effect(ctx)
        ctx.attach_energy.assert_awaited_once_with(energy, target)

    async def test_computer_search_requires_a_card_without_revealing(self):
        path = 'BW7.ComputerSearch_137'
        rig, e = self.rig(path, 'trainer')
        ctx = EffectContext(rig.session, P1, e['target'], None)
        ctx.search_deck = AsyncMock(return_value=[ctx.deck()[0]])
        ctx.put_in_hand = AsyncMock()
        await definition(path).effect(ctx)
        self.assertEqual(ctx.search_deck.call_args.kwargs['minimum'], 1)
        self.assertFalse(ctx.put_in_hand.call_args.kwargs['reveal'])

    async def test_old_amber_shows_all_seven_even_without_target(self):
        path = 'BW5.OldAmberAerodactyl_97'
        rig, e = self.rig(path, 'trainer')
        ctx = EffectContext(rig.session, P1, e['target'], None)
        viewed = list(ctx.deck())[:7]
        ctx.choose_cards = AsyncMock(return_value=[])
        await definition(path).effect(ctx)
        ctx.choose_cards.assert_awaited_once()
        self.assertEqual(ctx.choose_cards.call_args.kwargs['display_cards'], viewed)

    async def test_magical_leaf_heals_only_on_heads(self):
        for heads in (False, True):
            rig, e, ctx = self.ctx('BW1.Petilil_9', 'Magical Leaf')
            ctx.flip_coins = AsyncMock(return_value=[heads])
            ctx.heal = AsyncMock()
            await ctx.ability.effect(ctx)
            self.assertEqual(ctx.heal.await_count, int(heads))

    async def test_monkey_secondary_effect_requires_matching_energy(self):
        for path, attack, ptype, method in [
            ('BW2.Simisage_2', "Fire's Power", PokemonTypes.FIRE, 'apply_special_condition'),
            ('BW2.Simisear_19', "Water's Power", PokemonTypes.WATER, 'apply_special_condition'),
            ('BW2.Simipour_23', "Grass' Power", PokemonTypes.GRASS, 'heal'),
        ]:
            for attached in (False, True):
                with self.subTest(attack=attack, attached=attached):
                    rig, e, ctx = self.ctx(path, attack)
                    for energy in list(ctx.attached_energies(ctx.source)):
                        rig.to_area(energy, P1, 'deck')
                    if attached:
                        energy = rig.pull_guid(P1, self.energies[ptype.value])
                        rig.attach(energy, ctx.source)
                    callback = AsyncMock()
                    setattr(ctx, method, callback)
                    await ctx.ability.effect(ctx)
                    self.assertEqual(callback.await_count, int(attached))

    async def test_spit_acid_always_burns_and_also_paralyzes_on_heads(self):
        for heads in (False, True):
            rig, e, ctx = self.ctx('BW1.Scrafty_69', 'Spit Acid')
            ctx.flip_coins = AsyncMock(return_value=[heads])
            ctx.apply_special_condition = AsyncMock()
            await ctx.ability.effect(ctx)
            actual = {c.args[1] for c in ctx.apply_special_condition.call_args_list}
            self.assertEqual(actual, {SpecialConditions.BURNED, SpecialConditions.PARALYZED} if heads else {SpecialConditions.BURNED})

    async def test_zap_cannon_locks_only_on_tails(self):
        for heads in (False, True):
            rig, e, ctx = self.ctx('BW2.Klinklang_76', 'Zap Cannon')
            ctx.flip_coins = AsyncMock(return_value=[heads])
            rig.session.turn_state.lock_attack = Mock()
            await ctx.ability.effect(ctx)
            self.assertEqual(rig.session.turn_state.lock_attack.call_count, int(not heads))

    async def test_gyro_ball_switches_self_first_and_opponent_chooses(self):
        rig, e, ctx = self.ctx('BW2.Ferrothorn_72', 'Gyro Ball')
        calls = []
        async def choose(pool, *args, **kwargs):
            calls.append(('choose', kwargs.get('player_id', P1)))
            return pool[0]
        async def switch(pid, target):
            calls.append(('switch', pid))
        ctx.choose_pokemon = AsyncMock(side_effect=choose)
        ctx.switch_active = AsyncMock(side_effect=switch)
        await ctx.ability.effect(ctx)
        self.assertEqual(calls, [('choose', P1), ('switch', P1), ('choose', P2), ('switch', P2)])

    async def test_final_gambit_recoil_only_when_both_tails(self):
        for coins in ([False, False], [True, False], [True, True]):
            rig, e, ctx = self.ctx('BW2.Basculin_24', 'Final Gambit')
            ctx.flip_coins = AsyncMock(return_value=coins)
            ctx.deal_damage = AsyncMock(return_value=0)
            await ctx.ability.effect(ctx)
            recoil = [c for c in ctx.deal_damage.call_args_list if c.kwargs.get('target') is ctx.attacker]
            self.assertEqual(len(recoil), int(not any(coins)))
