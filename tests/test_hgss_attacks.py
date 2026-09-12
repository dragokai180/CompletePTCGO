"""HGSS attack outcome matrix, including negative and partial-result paths."""
import unittest
from unittest.mock import AsyncMock
from tests import test_hgss_rules as fixtures
from tests.test_hgss_rules import definition
from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.session.effects import EffectContext
from spirit.tools.effect_smoke import P1, P2


class AttackTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add
    ctx = fixtures.HgssRulesTests.ctx

    def neutral(self, pokemon):
        pokemon.set_attribute(AttrID.WEAKNESS_TYPES, [])
        pokemon.set_attribute(AttrID.RESISTANCE_TYPES, PokemonTypes.UNSET.value)

    async def test_leaf_guard_is_not_applied_twice_and_switch_clears_it(self):
        rig, e, ctx = self.ctx('HGSS1.Jumpluff_6', 'Leaf Guard')
        self.neutral(ctx.source)
        await ctx.ability.effect(ctx)
        enemy = ctx.defender
        hit = EffectContext(rig.session, P2, enemy, ctx.ability)
        self.assertEqual(await hit.deal_damage(80, target=ctx.source), 50)
        rig.session.clear_pokemon_effects(ctx.source)
        self.assertEqual(await hit.deal_damage(10, target=ctx.source), 10)

    async def test_moonlight_fang_only_blocks_printed_powers_or_bodies(self):
        rig, e, ctx = self.ctx('HGSS3.Umbreon_10', 'Moonlight Fang')
        self.neutral(ctx.source)
        await ctx.ability.effect(ctx)
        power = self.add(rig, definition('HGSS1.Slowking_12'), P2, 'bench')
        body = self.add(rig, definition('HGSS1.Donphan_107'), P2, 'bench')
        plain = self.add(rig, definition('HGSS1.Pikachu_78'), P2, 'bench')
        for attacker, expected in [(power, 0), (body, 0), (plain, 20)]:
            hit = EffectContext(rig.session, P2, attacker, ctx.ability)
            self.assertEqual(await hit.deal_damage(20, target=ctx.source), expected)

    async def test_time_circle_excludes_basic_pokemon(self):
        rig, e, ctx = self.ctx('HGSS4.Celebi_92', 'Time Circle')
        self.neutral(ctx.source)
        await ctx.ability.effect(ctx)
        for path, expected in [('HGSS1.Raichu_10', 0), ('HGSS1.Pikachu_78', 20)]:
            attacker = self.add(rig, definition(path), P2, 'bench')
            hit = EffectContext(rig.session, P2, attacker, ctx.ability)
            self.assertEqual(await hit.deal_damage(20, target=ctx.source), expected)

    async def test_afterimage_flips_only_when_receiving_attack(self):
        rig, e, ctx = self.ctx('HGSS3.Scyther_36', 'Afterimage Strike')
        ctx.flip_coins = AsyncMock()
        await ctx.ability.effect(ctx)
        ctx.flip_coins.assert_not_awaited()
        self.neutral(ctx.source)
        for heads in (False, True):
            hit = EffectContext(rig.session, P2, ctx.defender, ctx.ability)
            hit.flip_coins = AsyncMock(return_value=[heads])
            self.assertEqual(await hit.deal_damage(20, target=ctx.source), 0 if heads else 20)
            self.assertEqual(hit.flip_coins.call_args.kwargs['player_id'], P1)

    async def test_psychic_lock_only_opposing_poke_powers_and_is_player_effect(self):
        from spirit.game.session.passives import ability_locked
        rig, e, ctx = self.ctx('HGSS4.Grumpig_23', 'Psychic Lock')
        power_def = definition('HGSS1.Slowking_12')
        power = self.add(rig, power_def, P2, 'bench')
        body_def = definition('HGSS1.Donphan_107')
        body = self.add(rig, body_def, P2, 'bench')
        await ctx.ability.effect(ctx)
        self.assertTrue(ability_locked(rig.board, power, power_def.abilities[0]))
        self.assertFalse(ability_locked(rig.board, body, body_def.abilities[0]))
        rig.session.clear_pokemon_effects(ctx.source)
        self.assertTrue(ability_locked(rig.board, power, power_def.abilities[0]))

    async def test_headwind_adds_two_colorless(self):
        from spirit.game.session.passives import effective_attack_cost
        rig, e, ctx = self.ctx('HGSS4.Pidgeot_29', 'Headwind')
        before = effective_attack_cost(rig.board, ctx.defender, {'Colorless': 1})
        await ctx.ability.effect(ctx)
        after = effective_attack_cost(rig.board, ctx.defender, {'Colorless': 1})
        self.assertEqual(after['Colorless'] - before['Colorless'], 2)
        rig.session.turn_state.begin_turn(P2, rig.board)
        self.assertEqual(effective_attack_cost(rig.board, ctx.defender, {'Colorless': 1}), {'Colorless': 3})
        rig.session.turn_state.begin_turn(P1, rig.board)
        self.assertEqual(effective_attack_cost(rig.board, ctx.defender, {'Colorless': 1}), {'Colorless': 1})

    async def test_bulk_up_only_boosts_the_next_own_turn(self):
        from spirit.game.session.passives import compute_damage
        rig, e, ctx = self.ctx('HGSS2.Lucario_19', 'Bulk Up')
        self.neutral(ctx.defender)
        await ctx.ability.effect(ctx)
        state = rig.session.turn_state
        state.begin_turn(P2, rig.board)
        state.begin_turn(P1, rig.board)
        self.assertEqual(compute_damage(rig.board, ctx.source, ctx.defender, 50).amount, 80)
        state.begin_turn(P2, rig.board)
        state.begin_turn(P1, rig.board)
        self.assertEqual(compute_damage(rig.board, ctx.source, ctx.defender, 50).amount, 50)

    async def test_mach_wind_and_close_combat_expire(self):
        from spirit.game.session.passives import compute_damage, effective_retreat_cost
        rig, e, ctx = self.ctx('HGSS3.Vespiquen_23', 'Mach Wind')
        ctx.source.set_attribute(AttrID.RETREAT_COST, 3)
        await ctx.ability.effect(ctx)
        state = rig.session.turn_state
        state.begin_turn(P2, rig.board)
        state.begin_turn(P1, rig.board)
        self.assertEqual(effective_retreat_cost(rig.board, ctx.source), 0)
        state.begin_turn(P2, rig.board)
        self.assertEqual(effective_retreat_cost(rig.board, ctx.source), 3)
        rig, e, ctx = self.ctx('HGSS1.Hitmontop_5', 'Close Combat')
        self.neutral(ctx.source)
        await ctx.ability.effect(ctx)
        rig.session.turn_state.begin_turn(P2, rig.board)
        self.assertEqual(compute_damage(rig.board, ctx.defender, ctx.source, 30).amount, 50)
        rig.session.turn_state.begin_turn(P1, rig.board)
        self.assertEqual(compute_damage(rig.board, ctx.defender, ctx.source, 30).amount, 30)

    async def test_solar_suggestion_moves_four_total_from_multiple_sources(self):
        rig, e, ctx = self.ctx('HGSS3.Espeon_2', 'Solar Suggestion')
        donors = ctx.my_bench()[:2]
        for p in donors:
            p.set_attribute(AttrID.HP, ctx.max_hp(p) - 30)
        target = ctx.defender
        ctx.choose_pokemon = AsyncMock(side_effect=donors)
        ctx.choose = AsyncMock(return_value=1)
        rig.session.prompt_damage_counter_placement = AsyncMock(return_value={target.entity_id: 2})
        before = target.get_attribute(AttrID.HP)
        await ctx.ability.effect(ctx)
        self.assertEqual(before - target.get_attribute(AttrID.HP), 40)
        self.assertEqual([ctx.max_hp(p) - p.get_attribute(AttrID.HP) for p in donors], [10, 10])

    async def test_copied_legend_attack_pays_from_its_actual_user(self):
        rig, e = self.rig('HGSS4.Mew_97')
        attack = next(a for a in definition('HGSS1.HoOhLEGEND_111').abilities if a.title == 'Bright Wing')
        ctx = EffectContext(rig.session, P1, e['target'], attack)
        before = len(ctx.attached_energies(ctx.attacker))
        await attack.effect(ctx)
        self.assertEqual(len(ctx.attached_energies(ctx.attacker)), before - 1)

    async def test_moons_invite_can_move_part_of_a_donors_damage(self):
        rig, e, ctx = self.ctx('HGSS4.DarkraiCresseliaLEGEND_99', "Moon's Invite")
        donor = ctx.opponent_bench()[0]
        receiver = ctx.defender
        donor.set_attribute(AttrID.HP, ctx.max_hp(donor) - 40)
        receiver.set_attribute(AttrID.HP, ctx.max_hp(receiver))
        ctx.choose_pokemon = AsyncMock(side_effect=[donor, None])
        ctx.choose = AsyncMock(return_value=1)
        rig.session.prompt_damage_counter_placement = AsyncMock(return_value={receiver.entity_id: 1})
        await ctx.ability.effect(ctx)
        self.assertEqual(ctx.max_hp(donor) - donor.get_attribute(AttrID.HP), 30)
        self.assertEqual(ctx.max_hp(receiver) - receiver.get_attribute(AttrID.HP), 10)

    async def test_coin_gated_energy_discard_and_hydro_launcher_order(self):
        for heads in (False, True):
            rig, e, ctx = self.ctx('HGSS2.Vulpix_68', 'Fireworks')
            for energy in list(ctx.attached_energies(ctx.source)):
                rig.to_area(energy, P1, 'deck')
            energy = rig.pull_guid(P1, self.energies[PokemonTypes.FIRE.value])
            rig.attach(energy, ctx.source)
            ctx.flip_coins = AsyncMock(return_value=[heads])
            await ctx.ability.effect(ctx)
            self.assertEqual(energy.parent is ctx.source, heads)
        rig, e, ctx = self.ctx('HGSS2.Blastoise_13', 'Hydro Launcher')
        for energy in list(ctx.attached_energies(ctx.source)):
            rig.to_area(energy, P1, 'deck')
        from spirit.game.data_utils import def_for
        energies = [self.add(rig, def_for(self.energies[PokemonTypes.WATER.value]), P1, 'hand') for _ in range(2)]
        for energy in energies:
            rig.attach(energy, ctx.source)
        async def damage(*args, **kwargs):
            self.assertTrue(all(e in ctx.hand() for e in energies))
        ctx.deal_damage = AsyncMock(side_effect=damage)
        await ctx.ability.effect(ctx)
        ctx.deal_damage.assert_awaited_once()

    async def test_typed_and_condition_damage_formulas(self):
        rig, e, ctx = self.ctx('HGSS3.Honchkrow_16', 'Vengeance')
        for card in list(ctx.discard_pile()):
            rig.to_area(card, P1, 'deck')
        self.add(rig, definition('HGSS3.Honchkrow_16'), P1, 'discard')
        self.add(rig, definition('HGSS1.Pikachu_78'), P1, 'discard')
        ctx.deal_damage = AsyncMock()
        await ctx.ability.effect(ctx)
        self.assertEqual(ctx.deal_damage.call_args.args[0], 20)
        rig, e, ctx = self.ctx('HGSS3.Umbreon_86', 'Evoblast')
        expected = 50 + 10 * sum(p.get_attribute(AttrID.EVOLUTION_LOGIC_FROM) == 'Eevee'
                                for p in ctx.my_pokemon_in_play())
        ctx.deal_damage = AsyncMock()
        await ctx.ability.effect(ctx)
        self.assertEqual(ctx.deal_damage.call_args.args[0], expected)
        for path in ('HGSS3.Leafeon_17', 'COL.Leafeon_13'):
            for count in (0, 1, 3):
                rig, e, ctx = self.ctx(path, 'Miasma Wind')
                ctx.defender.set_attribute(AttrID.SPECIAL_CONDITIONS, ['Poisoned', 'Burned', 'Confused'][:count])
                ctx.deal_damage = AsyncMock()
                await ctx.ability.effect(ctx)
                self.assertEqual(ctx.deal_damage.call_args.args[0], 50 * count)

    async def test_poltergeist_all_trainer_classes(self):
        rig, e, ctx = self.ctx('HGSS3.Mismagius_19', 'Poltergeist')
        for card in list(ctx.hand(P2)):
            rig.to_area(card, P2, 'deck')
        self.add(rig, definition('HGSS1.Bill_89'), P2, 'hand')
        self.add(rig, definition('HGSS2.GoodRod_76'), P2, 'hand')
        ctx.deal_damage = AsyncMock()
        await ctx.ability.effect(ctx)
        self.assertEqual(ctx.deal_damage.call_args.args[0], 60)

    async def test_thunder_shot_only_hits_energy_bearers(self):
        rig, e, ctx = self.ctx('HGSS4.Electivire_20', 'Thunder Shot')
        targets = ctx.opponent_pokemon_in_play()
        for pokemon in targets:
            for card in list(ctx.attached_energies(pokemon)):
                rig.to_area(card, P2, 'deck')
        rig.attach(rig.pull_guid(P2, self.energies[PokemonTypes.WATER.value]), targets[1])
        ctx.deal_damage = AsyncMock()
        await ctx.ability.effect(ctx)
        self.assertEqual(ctx.deal_damage.await_count, 1)
        self.assertIs(ctx.deal_damage.call_args.kwargs['target'], targets[1])
        self.assertFalse(ctx.deal_damage.call_args.kwargs['apply_modifiers'])

    async def test_snipe_chooses_target_and_uses_printed_exemptions(self):
        for path, title in [('HGSS3.Rotom_20', 'Plasma Arrow'),
                            ('HGSS3.Weavile_25', 'Feint Attack'),
                            ('HGSS2.Primeape_22', 'Bebop Punch')]:
            rig, e, ctx = self.ctx(path, title)
            target = ctx.opponent_bench()[0]
            rig.attach(rig.pull_guid(P2, self.energies[PokemonTypes.WATER.value]), target)
            ctx.choose_pokemon = AsyncMock(return_value=target)
            ctx.flip_coins = AsyncMock(side_effect=[[True], [True], [False]])
            ctx.deal_damage = AsyncMock()
            await ctx.ability.effect(ctx)
            call = ctx.deal_damage.call_args
            self.assertIs(call.kwargs['target'], target)
            self.assertFalse(call.kwargs['apply_modifiers'])
            self.assertEqual(call.kwargs['ignore_target_effects'], title == 'Feint Attack')
            if title == 'Bebop Punch':
                self.assertEqual(call.args[0], 100)

    async def test_eruption_counts_only_cards_actually_discarded(self):
        rig, e, ctx = self.ctx('HGSS4.Magmar_42', 'Eruption')
        for card in list(ctx.deck()):
            rig.to_area(card, P1, 'hand')
        energy = rig.pull_guid(P2, self.energies[PokemonTypes.WATER.value])
        rig.to_area(energy, P2, 'deck')
        ctx.deal_damage = AsyncMock()
        await ctx.ability.effect(ctx)
        self.assertEqual(ctx.deal_damage.call_args.args[0], 20)
        self.assertIn(energy, ctx.discard_pile(P2))

    async def test_poison_effect_requires_own_poison_and_cures_only_it(self):
        for poisoned in (False, True):
            rig, e, ctx = self.ctx('COL.Seviper_51', 'Poison Effect')
            ctx.source.set_attribute(AttrID.SPECIAL_CONDITIONS, ['Poisoned', 'Burned'] if poisoned else ['Burned'])
            ctx.deal_damage = AsyncMock()
            await ctx.ability.effect(ctx)
            self.assertEqual(ctx.deal_damage.call_args.args[0], 80 if poisoned else 20)
            self.assertEqual(ctx.source.get_attribute(AttrID.SPECIAL_CONDITIONS), ['Burned'])

    async def test_strip_bare_both_heads_only(self):
        for coins in ([True, True], [True, False], [False, False]):
            rig, e, ctx = self.ctx('HGSS4.Sharpedo_30', 'Strip Bare')
            hand = list(ctx.hand(P2))
            ctx.flip_coins = AsyncMock(return_value=coins)
            await ctx.ability.effect(ctx)
            self.assertEqual(ctx.hand_size(P2), 0 if all(coins) else len(hand))

    async def test_draw_counts_board_types_and_energy_units(self):
        from spirit.game.card_effects.bw_era import _energy_count
        for path, title in [('HGSS1.Heracross_43', 'Green Draw'), ('HGSS1.Delibird_39', 'Snowy Present')]:
            rig, e, ctx = self.ctx(path, title)
            expected = sum(PokemonTypes.GRASS.value in (p.get_attribute(AttrID.POKEMON_TYPES) or [])
                           for p in ctx.my_pokemon_in_play()) if title == 'Green Draw' else sum(
                _energy_count(ctx, p, 'water') for p in ctx.my_pokemon_in_play())
            ctx.draw_cards = AsyncMock()
            await ctx.ability.effect(ctx)
            self.assertEqual(ctx.draw_cards.call_args.args[0], expected)

    async def test_playground_both_players_in_order_and_only_basics(self):
        rig, e, ctx = self.ctx('HGSS1.Pichu_28', 'Playground')
        mine = self.add(rig, self.filler, P1, 'deck')
        theirs = self.add(rig, self.filler, P2, 'deck')
        ctx.ask_yes_no = AsyncMock(return_value=True)
        ctx.search_deck = AsyncMock(side_effect=[[mine], [theirs]])
        await ctx.ability.effect(ctx)
        self.assertIn(mine, ctx.my_bench())
        self.assertIn(theirs, ctx.opponent_bench())
        self.assertEqual([c.kwargs['player_id'] for c in ctx.search_deck.call_args_list], [P1, P2])
        self.assertIn('Asleep', ctx.source.get_attribute(AttrID.SPECIAL_CONDITIONS))
        predicate = ctx.search_deck.call_args.args[0]
        legend = self.add(rig, definition('HGSS2.EnteiRaikouLEGEND_90'), P1, 'deck')
        self.assertFalse(predicate(legend))

    async def test_illumisile_requires_illumise(self):
        rig, e, ctx = self.ctx('HGSS4.Volbeat_82', 'Illumisile')
        ctx.deal_damage = AsyncMock()
        await ctx.ability.effect(ctx)
        ctx.deal_damage.assert_not_awaited()

    async def test_astonish_and_sharpen_claws_actual_card_count(self):
        for path, title, coins, count in [
                ('HGSS4.Ambipom_13', 'Astonish', [], 2),
                ('HGSS3.Murkrow_58', 'Astonish', [False], 0),
                ('HGSS1.Persian_27', 'Sharpen Claws', [True, False, True], 2)]:
            rig, e, ctx = self.ctx(path, title)
            hand = ctx.hand_size(P2)
            ctx.flip_coins = AsyncMock(return_value=coins)
            await ctx.ability.effect(ctx)
            self.assertEqual(ctx.hand_size(P2), hand - min(hand, count))

    async def test_legacy_coin_damage(self):
        cases = [
            ('HGSS1.Pikachu_78', 'Quick Attack', [True], 30),
            ('HGSS1.Pikachu_78', 'Quick Attack', [False], 20),
            ('HGSS1.Heracross_43', 'Double Headbutt', [True, True], 70),
            ('HGSS1.Corsola_37', 'Hyper Cannon', [True, True], 70),
            ('HGSS1.Corsola_37', 'Hyper Cannon', [True, False], 20),
            ('HGSS3.Doduo_45', 'Double Headstrike', [True, False], 0),
            ('HGSS3.Doduo_45', 'Double Headstrike', [True, True], 50),
        ]
        for path, title, coins, expected in cases:
            with self.subTest(path=path, coins=coins):
                rig, e, ctx = self.ctx(path, title)
                self.neutral(ctx.defender)
                hp = ctx.defender.get_attribute(AttrID.HP)
                ctx.flip_coins = AsyncMock(return_value=coins)
                await ctx.ability.effect(ctx)
                self.assertEqual(hp - ctx.defender.get_attribute(AttrID.HP), expected)

    async def test_flip_until_tails_and_typed_energy_units(self):
        rig, e, ctx = self.ctx('HGSS1.Raichu_10', 'Iron Tail')
        self.neutral(ctx.defender)
        ctx.flip_coins = AsyncMock(side_effect=[[True], [True], [False]])
        hp = ctx.defender.get_attribute(AttrID.HP)
        await ctx.ability.effect(ctx)
        self.assertEqual(ctx.flip_coins.await_count, 3)
        self.assertEqual(hp - ctx.defender.get_attribute(AttrID.HP), 60)
        rig, e, ctx = self.ctx('HGSS4.Dugtrio_19', 'Sand Impact')
        for energy in list(ctx.attached_energies(ctx.attacker)):
            rig.to_area(energy, P1, 'discard')
        for _ in range(3):
            from spirit.game.data_utils import def_for
            energy = self.add(rig, def_for(self.energies[PokemonTypes.FIGHTING.value]), P1, 'hand')
            rig.attach(energy, ctx.attacker)
        ctx.flip_coins = AsyncMock(return_value=[True, False, True])
        self.neutral(ctx.defender)
        hp = ctx.defender.get_attribute(AttrID.HP)
        await ctx.ability.effect(ctx)
        self.assertEqual(ctx.flip_coins.call_args.args[0], 3)
        self.assertEqual(hp - ctx.defender.get_attribute(AttrID.HP), 90)

    async def test_group_heal_does_not_heal_attacker_twice(self):
        rig, e, ctx = self.ctx('HGSS1.Butterfree_16', 'Cure Powder')
        before = {}
        for p in ctx.my_pokemon_in_play():
            p.set_attribute(AttrID.HP, ctx.max_hp(p) - 60)
            before[p.entity_id] = p.get_attribute(AttrID.HP)
        await ctx.ability.effect(ctx)
        for p in ctx.my_pokemon_in_play():
            self.assertEqual(p.get_attribute(AttrID.HP) - before[p.entity_id], 30)

    async def test_energy_bloom_filters_energy_and_fruit_filters_bench(self):
        rig, e, ctx = self.ctx('HGSS2.Shaymin_8', 'Energy Bloom')
        before = {}
        for p in ctx.my_pokemon_in_play():
            p.set_attribute(AttrID.HP, ctx.max_hp(p) - 40)
            before[p.entity_id] = p.get_attribute(AttrID.HP)
        await ctx.ability.effect(ctx)
        for p in ctx.my_pokemon_in_play():
            self.assertEqual(p.get_attribute(AttrID.HP) - before[p.entity_id],
                             30 if ctx.attached_energies(p) else 0)
        rig, e, ctx = self.ctx('HGSS3.Tropius_22', 'Fresh-Picked Fruit')
        target = ctx.my_bench()[0]
        target.set_attribute(AttrID.HP, ctx.max_hp(target) - 70)
        ctx.choose_pokemon = AsyncMock(return_value=target)
        await ctx.ability.effect(ctx)
        self.assertNotIn(ctx.attacker, ctx.choose_pokemon.call_args.args[0])
        self.assertEqual(target.get_attribute(AttrID.HP), ctx.max_hp(target) - 10)

    async def test_recover_requires_correct_energy_and_pays_once(self):
        for water in (False, True):
            with self.subTest(water=water):
                rig, e, ctx = self.ctx('HGSS1.Corsola_37', 'Recover')
                for energy in list(ctx.attached_energies(ctx.attacker)):
                    rig.to_area(energy, P1, 'discard')
                kind = PokemonTypes.WATER if water else PokemonTypes.FIRE
                energy = rig.pull_guid(P1, self.energies[kind.value])
                rig.attach(energy, ctx.attacker)
                ctx.attacker.set_attribute(AttrID.HP, ctx.max_hp(ctx.attacker) - 40)
                await ctx.ability.effect(ctx)
                self.assertEqual(ctx.attacker.get_attribute(AttrID.HP), ctx.max_hp(ctx.attacker) - (0 if water else 40))
                self.assertIs(energy.parent, rig.board.find_player_area(P1, 'discard') if water else ctx.attacker)

    async def test_mountain_eater_requires_actual_mill(self):
        for path, owner in [('HGSS2.Larvitar_50', P2), ('HGSS4.Aron_56', P1)]:
            rig, e, ctx = self.ctx(path, 'Mountain Eater')
            deck = rig.board.find_player_area(owner, 'deck')
            for card in list(deck.children):
                rig.to_area(card, owner, 'hand')
            ctx.attacker.set_attribute(AttrID.HP, ctx.max_hp(ctx.attacker) - 30)
            await ctx.ability.effect(ctx)
            self.assertEqual(ctx.attacker.get_attribute(AttrID.HP), ctx.max_hp(ctx.attacker) - 30)
            self.add(rig, self.filler, owner, 'deck')
            await ctx.ability.effect(ctx)
            self.assertEqual(ctx.attacker.get_attribute(AttrID.HP), ctx.max_hp(ctx.attacker) - 10)

    async def test_poke_power_only_thunder_fall(self):
        rig, e, ctx = self.ctx('HGSS2.EnteiRaikouLEGEND_90', 'Thunder Fall')
        power = self.add(rig, definition('HGSS1.Slowking_12'), P2, 'bench')
        body = self.add(rig, definition('HGSS1.Donphan_107'), P1, 'bench')
        power_hp, body_hp = power.get_attribute(AttrID.HP), body.get_attribute(AttrID.HP)
        await ctx.ability.effect(ctx)
        self.assertEqual(power.get_attribute(AttrID.HP), power_hp - 80)
        self.assertEqual(body.get_attribute(AttrID.HP), body_hp)

    async def test_lost_crisis_energy_and_full_knockout_stack(self):
        rig, e, ctx = self.ctx('HGSS4.DarkraiCresseliaLEGEND_99', 'Lost Crisis')
        self.neutral(ctx.defender)
        ctx.defender.set_attribute(AttrID.HP, 90)
        victim = ctx.defender
        energy = rig.pull_guid(P2, self.energies[PokemonTypes.WATER.value])
        rig.attach(energy, ctx.defender)
        attached = list(ctx.attached_energies(ctx.attacker))
        await ctx.ability.effect(ctx)
        await rig.session.resolve_knockouts(ctx)
        self.assertIs(victim.parent, rig.board.find_player_area(P2, 'lostZone'))
        self.assertIs(energy.parent, rig.board.find_player_area(P2, 'lostZone'))
        self.assertTrue(any(c.parent is rig.board.find_player_area(P1, 'lostZone') for c in attached))

    async def test_plead_opponent_choice_and_selfish_draw(self):
        for yes in (False, True):
            rig, e, ctx = self.ctx('HGSS3.Togepi_70', 'Plead')
            self.neutral(ctx.defender)
            hp, hand = ctx.defender.get_attribute(AttrID.HP), ctx.hand_size()
            ctx.ask_yes_no = AsyncMock(return_value=yes)
            await ctx.ability.effect(ctx)
            self.assertEqual(ctx.ask_yes_no.call_args.kwargs['player_id'], P2)
            self.assertEqual(ctx.hand_size() - hand, 2 if yes else 0)
            self.assertEqual(hp - ctx.defender.get_attribute(AttrID.HP), 0 if yes else 20)
        for yes in (False, True):
            rig, e, ctx = self.ctx('HGSS3.Mawile_56', 'Selfish Draw')
            top, next_card = ctx.deck_top(2)
            hand = ctx.hand_size()
            ctx.ask_yes_no = AsyncMock(return_value=yes)
            await ctx.ability.effect(ctx)
            self.assertEqual(ctx.hand_size() - hand, 1)
            self.assertIn(top if yes else next_card, ctx.hand())
            if not yes:
                self.assertIn(top, ctx.discard_pile())
