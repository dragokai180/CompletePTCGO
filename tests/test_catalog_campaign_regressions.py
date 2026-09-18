"""Outcome regressions found by the all-printings campaign."""
import unittest
from unittest.mock import AsyncMock

import test_hgss_rules as fixtures
from test_hgss_rules import definition
from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.data_utils import Attack
from spirit.game.session.effects import EffectContext, is_energy_card, full_stack
from spirit.tools.effect_smoke import P1, P2
from spirit.game.session.passives import energy_provided_options


class CatalogCampaignTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx
    add = fixtures.HgssRulesTests.add

    async def test_energy_gated_copy_requires_the_chosen_attacks_cost(self):
        for path, title in [('BW9.Kecleon_94', 'Imittack'), ('GUM.Ditto_17', 'Copy Anything')]:
            for paid in (False, True):
                with self.subTest(card=path, paid=paid):
                    rig, e, ctx = self.ctx(path, title)
                    for energy in list(ctx.attached_energies(ctx.attacker)):
                        rig.to_area(energy, P1, 'discard')
                    if paid:
                        rig.attach_energy_type(P1, ctx.attacker, PokemonTypes.GRASS.value)
                    copied = Attack(title='Test copy', cost={PokemonTypes.GRASS: 1}, damage=10)
                    ctx.choose_attack_to_copy = AsyncMock(return_value=(ctx.defender, copied))
                    ctx.use_attack = AsyncMock()
                    await ctx.ability.effect(ctx)
                    self.assertEqual(ctx.use_attack.await_count, int(paid))

    async def test_transfer_junk_one_of_each_plasma_category(self):
        rig, e, ctx = self.ctx('BW9.Raticate_88', 'Transfer Junk')
        wanted = [self.add(rig, definition(path), P1, 'discard') for path in
                  ('BW8.LugiaEX_108', 'BW8.Colress_118', 'BW8.PlasmaEnergy_127')]
        other = list(ctx.discard_pile())
        async def choose(pool, count, **kwargs):
            self.assertEqual(count, 1)
            self.assertEqual(kwargs['minimum'], 1)
            return [next(c for c in wanted if c in pool)]
        ctx.choose_cards = AsyncMock(side_effect=choose)
        await ctx.ability.effect(ctx)
        self.assertTrue(all(c in ctx.hand() for c in wanted))
        self.assertTrue(all(c in ctx.discard_pile() for c in other if c not in wanted))
        self.assertEqual(ctx.choose_cards.await_count, 3)

    async def test_signs_of_evolution_recovers_three_distinct_types(self):
        rig, e, ctx = self.ctx('BW9.Eevee_90', 'Signs of Evolution')
        wanted = [self.add(rig, definition(path), P1, 'deck') for path in
                  ('BW9.Vaporeon_20', 'BW9.Jolteon_34', 'BW9.Flareon_12')]
        duplicate = self.add(rig, definition('BW9.Vaporeon_20'), P1, 'deck')
        seen = []
        async def choose(pool, count, **kwargs):
            if seen:
                self.assertNotIn(duplicate, pool)
            card = wanted[len(seen)]
            self.assertIn(card, pool)
            seen.append(card)
            return [card]
        ctx.choose_cards = AsyncMock(side_effect=choose)
        ctx.put_in_hand = AsyncMock(wraps=ctx.put_in_hand)
        await ctx.ability.effect(ctx)
        self.assertTrue(all(c in ctx.hand() for c in wanted))
        self.assertIn(duplicate, ctx.deck())
        self.assertEqual(len(seen), 3)
        ctx.put_in_hand.assert_awaited_once_with(wanted, reveal=True)

    async def test_improvisational_performance_all_hand_size_branches(self):
        for size in (0, 1, 2, 3, 6):
            with self.subTest(size=size):
                rig, e, ctx = self.ctx('SM12.Kricketune_14', 'Improvisational Performance')
                while len(ctx.hand()) > size:
                    rig.to_area(ctx.hand()[0], P1, 'deck')
                while len(ctx.hand()) < size:
                    rig.to_area(ctx.deck()[0], P1, 'hand')
                ctx.deal_damage = AsyncMock(return_value=0)
                ctx.apply_special_condition = AsyncMock()
                await ctx.ability.effect(ctx)
                self.assertEqual(ctx.deal_damage.call_args_list[0].args[0], 130 if size == 1 else 30)
                self.assertEqual(ctx.apply_special_condition.await_count, int(size == 3))
                self.assertEqual(ctx.deal_damage.await_count, 1 + (len(ctx.opponent_bench()) if size == 6 else 0))

    async def test_puzzle_of_time_single_and_double_modes(self):
        for double in (False, True):
            with self.subTest(double=double):
                rig, e = self.rig('XY9.PuzzleofTime_109', 'trainer')
                card = definition('XY9.PuzzleofTime_109')
                ctx = EffectContext(rig.session, P1, e['target'], None)
                second = self.add(rig, card, P1, 'hand') if double else None
                ctx.ask_yes_no = AsyncMock(return_value=True)
                ctx.reorder_deck_top = AsyncMock()
                before = len(ctx.hand())
                await card.effect(ctx)
                if double:
                    self.assertIn(second, ctx.discard_pile())
                    self.assertEqual(len(ctx.hand()), before + 1)
                    ctx.reorder_deck_top.assert_not_awaited()
                else:
                    ctx.reorder_deck_top.assert_awaited_once()

    async def test_energy_doublers_do_not_recurse_stack_or_affect_opponent(self):
        for path, kind in [('ME1.Meganium_10', PokemonTypes.GRASS),
                           ('PGO.Charizard_10', PokemonTypes.FIRE),
                           ('SWSH6.GalarianWeezing_96', PokemonTypes.DARKNESS)]:
            with self.subTest(card=path):
                rig, e = self.rig(path)
                self.add(rig, definition(path), P1, 'bench')
                for pid, holder, expected in [(P1, e['p1_active'], 2), (P2, e['p2_active'], 1)]:
                    rig.attach_energy_type(pid, holder, kind.value)
                    energy = next(c for c in rig.board.attached_energies(holder)
                                  if c.archetype_id.lower() == self.energies[kind.value].lower())
                    self.assertEqual(energy_provided_options(rig.board, energy), [[kind.value] * expected])

    async def test_growth_and_tailwind_attach_exactly_one_from_hand(self):
        for path, title, own_only in [('BW11.Snivy_RC1', 'Growth', True),
                                     ('BW2.Unfezant_82', 'Tailwind', False)]:
            with self.subTest(title=title):
                rig, e, ctx = self.ctx(path, title)
                energy = next(c for c in ctx.hand() if c.archetype_id.lower() ==
                              self.energies[PokemonTypes.GRASS.value].lower())
                target = ctx.source if own_only else ctx.my_bench()[0]
                ctx.choose_cards = AsyncMock(return_value=[energy])
                ctx.choose_pokemon = AsyncMock(return_value=target)
                before = len(ctx.attached_energies(target))
                await ctx.ability.effect(ctx)
                self.assertNotIn(energy, ctx.hand())
                self.assertIn(energy, ctx.attached_energies(target))
                self.assertEqual(len(ctx.attached_energies(target)), before + 1)
                if own_only:
                    ctx.choose_pokemon.assert_not_awaited()

    async def test_dragon_vortex_counts_both_types_then_shuffles_only_them(self):
        rig, e, ctx = self.ctx('BW9.Kingdra_84', 'Dragon Vortex')
        chosen_guids = {self.energies[t.value].lower() for t in
                        (PokemonTypes.WATER, PokemonTypes.LIGHTNING)}
        energies = [c for c in ctx.discard_pile() if c.archetype_id.lower() in chosen_guids]
        others = [c for c in ctx.discard_pile() if c not in energies]
        ctx.deal_damage = AsyncMock(return_value=0)
        await ctx.ability.effect(ctx)
        ctx.deal_damage.assert_awaited_once_with(20 * len(energies))
        self.assertTrue(all(c in ctx.deck() for c in energies))
        self.assertTrue(all(c in ctx.discard_pile() for c in others))

    async def test_spit_squall_returns_entire_defending_stack(self):
        rig, e, ctx = self.ctx('BW5.Carnivine_5', 'Spit Squall')
        cards = list(full_stack(ctx.defender))
        await ctx.ability.effect(ctx)
        self.assertTrue(all(c in ctx.hand(P2) for c in cards))
        self.assertIsNone(rig.board.active_pokemon(P2))

    async def test_whirlwind_opponent_selects_replacement(self):
        rig, e, ctx = self.ctx('BW6.Honchkrow_73', 'Whirlwind')
        target = ctx.opponent_bench()[-1]
        ctx.ask_yes_no = AsyncMock(return_value=True)
        ctx.choose_pokemon = AsyncMock(return_value=target)
        await ctx.ability.effect(ctx)
        self.assertIs(rig.board.active_pokemon(P2), target)
        self.assertEqual(ctx.choose_pokemon.call_args.kwargs.get('player_id'), P2)

    async def test_astonish_random_card_only_on_heads(self):
        for heads in (True, False):
            with self.subTest(heads=heads):
                rig, e, ctx = self.ctx('BW5.Yamask_51', 'Astonish')
                before = list(ctx.hand(P2))
                ctx.flip_coins = AsyncMock(return_value=[heads])
                ctx.reveal_cards = AsyncMock()
                await ctx.ability.effect(ctx)
                self.assertEqual(len(ctx.hand(P2)), len(before) - int(heads))
                self.assertEqual(ctx.reveal_cards.await_count, int(heads))

    async def test_doom_decree_requires_two_heads(self):
        for flips in ([True, True], [True, False], [False, True], [False, False]):
            with self.subTest(flips=flips):
                rig, e, ctx = self.ctx('BW6.Gothitelle_57', 'Doom Decree')
                ctx.flip_coins = AsyncMock(return_value=flips)
                ctx.knock_out = AsyncMock()
                await ctx.ability.effect(ctx)
                self.assertEqual(ctx.knock_out.await_count, int(all(flips)))

    async def test_wreck_adds_bonus_and_discards_stadium(self):
        rig, e, ctx = self.ctx('BW8.Donphan_72', 'Wreck')
        stadium = self.add(rig, definition('BW4.SkyarrowBridge_91'), P2, 'hand')
        rig.board.move_card(stadium.entity_id, rig.board.find_global_area('activeStadium').entity_id)
        stadium.owning_player_id = P2
        ctx.deal_damage = AsyncMock(return_value=0)
        await ctx.ability.effect(ctx)
        self.assertEqual(ctx.deal_damage.call_args.args[0], 140)
        self.assertIn(stadium, ctx.discard_pile(P2))

    async def test_reboot_pod_permission_and_energy_destination(self):
        rig, e = self.rig('SV05.RebootPod_158', 'trainer')
        card = definition('SV05.RebootPod_158')
        self.assertFalse(card.condition(rig.board, P1, e['target']))

        future = self.add(rig, definition('SV05.IronLeavesex_25'), P1, 'bench')
        self.assertTrue(card.condition(rig.board, P1, e['target']))
        from spirit.game.session.effects import EffectContext
        ctx = EffectContext(rig.session, P1, e['target'], None)
        energy = next(c for c in ctx.discard_pile() if is_energy_card(c))
        ctx.choose_cards = AsyncMock(return_value=[energy])
        await card.effect(ctx)
        self.assertIn(energy, ctx.attached_energies(future))
        for other in list(ctx.discard_pile()): rig.to_area(other, P1, 'deck')
        self.assertFalse(card.condition(rig.board, P1, e['target']))

    async def test_surfer_accepts_nonwater_and_draws_after_switch(self):
        from spirit.game.session.effects import EffectContext
        card = definition('SV08.Surfer_187')
        rig, e = self.rig('SV08.Surfer_187', 'trainer')
        ctx = EffectContext(rig.session, P1, e['target'], None)
        target = ctx.my_bench()[0]
        self.assertTrue(card.condition(rig.board, P1))
        ctx.choose_pokemon = AsyncMock(return_value=target)
        for entry in list(ctx.hand()): rig.to_area(entry, P1, 'deck')
        await card.effect(ctx)
        self.assertIs(rig.board.active_pokemon(P1), target)
        self.assertEqual(len(ctx.hand()), 5)


if __name__ == '__main__':
    unittest.main()
