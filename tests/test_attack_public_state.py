"""Conditional damage must agree with the printed state, not just hit once."""
import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures
from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes
from spirit.game.data_utils import def_for
from spirit.game.session.effects import full_stack
from spirit.game.card_effects.attack_state_clauses import public_attack_condition
from spirit.tools.effect_smoke import P1, P2


class AttackPublicState(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx
    add = fixtures.HgssRulesTests.add

    def count_zone(self, rig, pid, zone, count):
        area = rig.board.find_player_area(pid, zone)
        for card in list(area.children)[count:]:
            rig.to_area(card, pid, 'deck')
        while len(area.children) < count:
            self.add(rig, def_for(self.energies[PokemonTypes.GRASS.value]), pid, zone)

    async def test_hand_and_prize_thresholds_both_sides_of_boundary(self):
        cases = [
            ('SM8.Granbull_138', 'All Out', P1, 'hand', 0, 1, 130),
            ('SV3.Absolex_135', 'Cursed Slug', P2, 'hand', 3, 4, 120),
            ('SV07.Mienshao_84', 'Gale Roundhouse', P2, 'hand', 5, 6, 60),
            ('SM9.Pupitar_80', 'Payback', P2, 'prizePile', 1, 2, 90),
            ('SM6.Buzzwole_77', 'Sledgehammer', P2, 'prizePile', 4, 3, 90),
            ('SM10.Kartana_19', 'Big Cut', P1, 'prizePile', 4, 3, 120),
            ('SM8.Naganadel_108', 'Turning Point', P1, 'prizePile', 3, 2, 80),
            ('SV08.GougingFire_38', 'Blazing Charge', P2, 'prizePile', 4, 5, 70),
            ('SV3.Houndstone_101', 'Two Four-ocious', P2, 'prizePile', 2, 3, 120),
            ('ME1.Steelix_93', 'Welcoming Tail', P1, 'prizePile', 6, 5, 200),
        ]
        for path, title, pid, zone, yes, no, bonus in cases:
            for count in (yes, no):
                with self.subTest(path=path, count=count):
                    rig, e, ctx = self.ctx(path, title)
                    self.count_zone(rig, pid, zone, count)
                    ctx.deal_damage = AsyncMock(return_value=0)
                    await ctx.ability.effect(ctx)
                    self.assertEqual(ctx.deal_damage.call_args.args[0], ctx.ability.damage + (bonus if count == yes else 0))
                    self.assertEqual(ctx.deal_damage.await_count, 1)

    async def test_status_bonuses_and_cleanup(self):
        cases = [('SV065.Okidogiex_36', 'Chain-Crazed', 130, False),
                 ('SV4.Klawf_105', 'Unhinged Scissors', 160, False),
                 ('Promo_XY.MachampEX_108', 'Crazy Hammer', 80, True),
                 ('SM3.Toxicroak_55', 'Poison Boost', 80, True)]
        for path, title, bonus, cure in cases:
            for poisoned in (False, True):
                rig, e, ctx = self.ctx(path, title)
                ctx.source.set_attribute(AttrID.SPECIAL_CONDITIONS, ['Poisoned'] if poisoned else [])
                ctx.deal_damage = AsyncMock(return_value=0)
                await ctx.ability.effect(ctx)
                self.assertEqual(ctx.deal_damage.call_args.args[0], ctx.ability.damage + (bonus if poisoned else 0))
                self.assertEqual('Poisoned' in (ctx.source.get_attribute(AttrID.SPECIAL_CONDITIONS) or []), poisoned and not cure)

    async def test_empty_hand_bonus_gates_both_secondary_conditions(self):
        for empty in (False, True):
            rig, e, ctx = self.ctx('SV035.Beedrill_15', 'Nadir Needle')
            self.count_zone(rig, P1, 'hand', 0 if empty else 1)
            ctx.deal_damage = AsyncMock(return_value=0)
            await ctx.ability.effect(ctx)
            self.assertEqual(ctx.deal_damage.call_args.args[0], ctx.ability.damage + (120 if empty else 0))
            self.assertEqual(set(ctx.defender.get_attribute(AttrID.SPECIAL_CONDITIONS) or []),
                             {'Paralyzed', 'Poisoned'} if empty else set())

    async def test_modern_ex_and_v_are_not_legacy_ex(self):
        for target_path, eligible in (('BW4.MewtwoEX_54', False), ('SV035.Charizardex_6', True),
                                      ('SWSH1.ZacianV_138', True),
                                      ('BW1.Snivy_1', False)):
            rig, e, ctx = self.ctx('SV07.Galvantulaex_51', 'Charged Web')
            rig.to_area(ctx.defender, P2, 'discard')
            self.add(rig, fixtures.definition(target_path), P2, 'activePokemonArea')
            ctx.deal_damage = AsyncMock(return_value=0)
            await ctx.ability.effect(ctx)
            self.assertEqual(ctx.deal_damage.call_args.args[0], ctx.ability.damage + (110 if eligible else 0))

    async def test_stage_and_type_qualifiers_on_bench(self):
        for stage, kind, eligible in ((1, PokemonTypes.DARKNESS, False),
                                      (2, PokemonTypes.GRASS, False), (2, PokemonTypes.DARKNESS, True)):
            rig, e, ctx = self.ctx('ME2.Sableye_59', 'Cocky Claw')
            for pokemon in ctx.my_bench():
                rig.to_area(pokemon, P1, 'discard')
            target = self.add(rig, fixtures.definition('BW1.Snivy_1'), P1, 'bench')
            target.set_attribute(AttrID.STAGE, stage)
            target.set_attribute(AttrID.POKEMON_TYPES, [kind.value])
            ctx.deal_damage = AsyncMock(return_value=0)
            await ctx.ability.effect(ctx)
            self.assertEqual(ctx.deal_damage.call_args.args[0], ctx.ability.damage + (70 if eligible else 0))

    async def test_named_bench_bonuses_add_independently(self):
        for paths, bonus in (([], 0), (['XY10.Solosis_33'], 30),
                             (['XY10.Duosion_34', 'XY10.Reuniclus_35'], 150)):
            rig, e, ctx = self.ctx('XY10.Reuniclus_35', 'Link Fusion')
            for pokemon in ctx.my_bench():
                rig.to_area(pokemon, P1, 'discard')
            for path in paths:
                self.add(rig, fixtures.definition(path), P1, 'bench')
            ctx.deal_damage = AsyncMock(return_value=0)
            await ctx.ability.effect(ctx)
            self.assertEqual(ctx.deal_damage.call_args.args[0], ctx.ability.damage + bonus)
            self.assertEqual(ctx.deal_damage.await_count, 1)

    async def test_love_impact_matches_nidoking_in_bench_name(self):
        rig, e, ctx = self.ctx('SV10.TeamRocketsNidoqueen_116', 'Love Impact')
        ctx.deal_damage = AsyncMock(return_value=0)
        await ctx.ability.effect(ctx)
        self.assertEqual(ctx.deal_damage.call_args.args[0], 60)

        self.add(rig, fixtures.definition('SV10.TeamRocketsNidokingex_119'), P1, 'bench')
        ctx.deal_damage.reset_mock()
        await ctx.ability.effect(ctx)
        ctx.deal_damage.assert_awaited_once_with(180, ignore_weakness=False)

    async def test_hot_lick_checks_defending_pokemon_name(self):
        rig, e, ctx = self.ctx('BW5.Heatmor_19', 'Hot Lick')
        ctx.deal_damage = AsyncMock(return_value=0)
        await ctx.ability.effect(ctx)
        self.assertEqual(ctx.deal_damage.call_args.args[0], 10)

        rig.to_area(ctx.defender, P2, 'discard')
        self.add(rig, fixtures.definition('BW3.Durant_83'), P2, 'activePokemonArea')
        ctx.deal_damage.reset_mock()
        await ctx.ability.effect(ctx)
        self.assertEqual(ctx.deal_damage.call_args.args[0], 60)
        self.assertEqual(ctx.deal_damage.await_count, 1)

    async def test_color_coordination_requires_matching_basic_energy(self):
        rig, e, ctx = self.ctx('BW11.Ninetales_21', 'Color Coordination')
        for energy in list(ctx.attached_energies(ctx.source)):
            rig.to_area(energy, P1, 'discard')
        basic_fire = self.add(rig, def_for(self.energies[PokemonTypes.FIRE.value]), P1, 'hand')
        rig.attach(basic_fire, ctx.source)
        ctx.deal_damage = AsyncMock(return_value=0)

        ctx.defender.set_attribute(AttrID.POKEMON_TYPES, [PokemonTypes.WATER.value])
        await ctx.ability.effect(ctx)
        self.assertEqual(ctx.deal_damage.call_args.args[0], 50)

        ctx.defender.set_attribute(AttrID.POKEMON_TYPES, [PokemonTypes.FIRE.value])
        ctx.deal_damage.reset_mock()
        await ctx.ability.effect(ctx)
        self.assertEqual(ctx.deal_damage.call_args.args[0], 90)
        self.assertEqual(ctx.deal_damage.await_count, 1)

    async def test_chlorowhip_heals_only_with_two_grass_energy(self):
        rig, e, ctx = self.ctx('SM10.Tangrowth_17', 'Chlorowhip')
        for energy in list(ctx.attached_energies(ctx.source)):
            rig.to_area(energy, P1, 'discard')
        ctx.source.set_attribute(AttrID.HP, ctx.max_hp(ctx.source) - 80)
        ctx.deal_damage = AsyncMock(return_value=0)
        ctx.heal = AsyncMock(return_value=60)

        for count in (1, 2):
            energy = self.add(rig, def_for(self.energies[PokemonTypes.GRASS.value]), P1, 'hand')
            rig.attach(energy, ctx.source)
            await ctx.ability.effect(ctx)
            self.assertEqual(ctx.deal_damage.call_args.args[0], 90)
            self.assertEqual(ctx.heal.await_count, 1 if count == 2 else 0)

    async def test_first_freeze_paralyzes_only_on_second_players_first_turn(self):
        rig, e, ctx = self.ctx('SV3.Cryogonal_55', 'First Freeze')
        rig.session.first_player_id = P2
        ctx.deal_damage = AsyncMock(return_value=0)
        ctx.apply_special_condition = AsyncMock()

        for turn in (2, 3):
            rig.session.turn_state.turn_number = turn
            ctx.apply_special_condition.reset_mock()
            await ctx.ability.effect(ctx)
            self.assertEqual(ctx.apply_special_condition.await_count, 1 if turn == 2 else 0)

    async def test_balance_bind_requires_equal_bench_sizes(self):
        rig, e, ctx = self.ctx('XY8.Starmie_30', 'Balance Bind')
        ctx.deal_damage = AsyncMock(return_value=0)
        ctx.apply_special_condition = AsyncMock()

        await ctx.ability.effect(ctx)
        ctx.apply_special_condition.assert_not_awaited()
        rig.to_area(ctx.my_bench()[0], P1, 'discard')
        await ctx.ability.effect(ctx)
        ctx.apply_special_condition.assert_awaited_once()

    async def test_bared_fangs_does_nothing_without_prior_damage(self):
        rig, e, ctx = self.ctx('RSV10PT5.Basculin_24', 'Bared Fangs')
        ctx.deal_damage = AsyncMock(return_value=0)
        await ctx.ability.effect(ctx)
        ctx.deal_damage.assert_not_awaited()

        ctx.defender.set_attribute(AttrID.HP, ctx.max_hp(ctx.defender) - 10)
        await ctx.ability.effect(ctx)
        self.assertEqual(ctx.deal_damage.call_args.args[0], 50)

    async def test_seventh_kick_needs_exactly_seven_cards(self):
        for count in (6, 7):
            rig, e, ctx = self.ctx('ME2PT5.Medicham_104', 'Seventh Kick')
            self.count_zone(rig, P1, 'hand', count)
            ctx.deal_damage = AsyncMock(return_value=0)
            await ctx.ability.effect(ctx)
            self.assertEqual(ctx.deal_damage.await_count, 1 if count == 7 else 0)

    async def test_brain_crush_requires_confused_defender(self):
        rig, e, ctx = self.ctx('ME5.Malamar_52', 'Brain Crush')
        ctx.deal_damage = AsyncMock(return_value=0)
        await ctx.ability.effect(ctx)
        ctx.deal_damage.assert_not_awaited()

        ctx.defender.set_attribute(AttrID.SPECIAL_CONDITIONS, ['Confused'])
        await ctx.ability.effect(ctx)
        self.assertEqual(ctx.deal_damage.call_args.args[0], 130)

    async def test_v_create_needs_five_benched_pokemon(self):
        rig, e, ctx = self.ctx('BW3.Victini_15', 'V-create')
        ctx.deal_damage = AsyncMock(return_value=0)
        await ctx.ability.effect(ctx)
        ctx.deal_damage.assert_not_awaited()

        for _ in range(2):
            self.add(rig, fixtures.definition('BW1.Snivy_1'), P1, 'bench')
        await ctx.ability.effect(ctx)
        self.assertEqual(ctx.deal_damage.call_args.args[0], 100)

    async def test_dark_penalty_needs_tool_on_defender(self):
        rig, e, ctx = self.ctx('BW4.Weavile_70', 'Dark Penalty')
        ctx.deal_damage = AsyncMock(return_value=0)
        await ctx.ability.effect(ctx)
        ctx.deal_damage.assert_not_awaited()

        tool = self.add(rig, fixtures.definition('XY3.FocusSash_91'), P2, 'hand')
        rig.attach(tool, ctx.defender)
        await ctx.ability.effect(ctx)
        self.assertEqual(ctx.deal_damage.call_args.args[0], 90)

    async def test_giga_railgun_needs_named_special_energy(self):
        rig, e, ctx = self.ctx('ME5.Vikavolt_26', 'Giga Railgun')
        ctx.deal_damage = AsyncMock(return_value=0)
        await ctx.ability.effect(ctx)
        ctx.deal_damage.assert_not_awaited()

        energy = self.add(rig, fixtures.definition('ME5.VoltaicLightningEnergy_84'), P1, 'hand')
        rig.attach(energy, ctx.source)
        await ctx.ability.effect(ctx)
        self.assertEqual(ctx.deal_damage.call_args.args[0], 260)

    async def test_revelation_dance_needs_stadium(self):
        rig, e, ctx = self.ctx('Promo_SM.Oricorio_19', 'Revelation Dance')
        ctx.deal_damage = AsyncMock(return_value=0)
        await ctx.ability.effect(ctx)
        ctx.deal_damage.assert_not_awaited()

        stadium = self.add(rig, fixtures.definition('BW4.SkyarrowBridge_91'), P1, 'hand')
        rig.board.move_card(stadium.entity_id,
                            rig.board.find_global_area('activeStadium').entity_id)
        await ctx.ability.effect(ctx)
        self.assertEqual(ctx.deal_damage.call_args.args[0], 30)

    async def test_rising_chop_requires_modern_pokemon_ex(self):
        rig, e, ctx = self.ctx('RSV10PT5.Sawk_49', 'Rising Chop')
        ctx.deal_damage = AsyncMock(return_value=0)
        await ctx.ability.effect(ctx)
        ctx.deal_damage.assert_not_awaited()

        rig.to_area(ctx.defender, P2, 'discard')
        self.add(rig, fixtures.definition('SV035.Charizardex_6'), P2, 'activePokemonArea')
        await ctx.ability.effect(ctx)
        self.assertEqual(ctx.deal_damage.call_args.args[0], 90)

    async def test_guardian_burst_requires_both_named_bench_pokemon(self):
        rig, e, ctx = self.ctx('SV08.Mesprit_79', 'Guardian Burst')
        ctx.deal_damage = AsyncMock(return_value=0)
        await ctx.ability.effect(ctx)
        ctx.deal_damage.assert_not_awaited()

        self.add(rig, fixtures.definition('SV08.Uxie_78'), P1, 'bench')
        await ctx.ability.effect(ctx)
        ctx.deal_damage.assert_not_awaited()
        self.add(rig, fixtures.definition('SV08.Azelf_80'), P1, 'bench')
        await ctx.ability.effect(ctx)
        self.assertEqual(ctx.deal_damage.call_args.args[0], 160)

    async def test_fickle_spitting_requires_three_or_four_opponent_prizes(self):
        rig, e, ctx = self.ctx('SV09.HopsCramorant_138', 'Fickle Spitting')
        ctx.deal_damage = AsyncMock(return_value=0)
        self.count_zone(rig, P2, 'prizePile', 5)
        await ctx.ability.effect(ctx)
        ctx.deal_damage.assert_not_awaited()

        self.count_zone(rig, P2, 'prizePile', 4)
        await ctx.ability.effect(ctx)
        self.assertEqual(ctx.deal_damage.call_args.args[0], 120)

    async def test_stadium_owner_controls_bonus_or_healing(self):
        for owner in (None, P1, P2):
            rig, e, ctx = self.ctx('XY8.Mamoswine_82', 'Primordial Boom')
            stadium = self.add(rig, fixtures.definition('BW4.SkyarrowBridge_91'), owner or P1, 'hand')
            ctx.stadium_in_play = lambda: stadium if owner else None
            ctx.source.set_attribute(AttrID.HP, ctx.max_hp(ctx.source) - 60)
            ctx.deal_damage = AsyncMock(return_value=0)
            await ctx.ability.effect(ctx)
            self.assertEqual(ctx.deal_damage.call_args.args[0], ctx.ability.damage + (40 if owner == P1 else 0))
            self.assertEqual(ctx.source.get_attribute(AttrID.HP), ctx.max_hp(ctx.source) - (20 if owner == P2 else 60))

    async def test_bonus_per_damage_counter_is_conditional(self):
        for prizes in (5, 6):
            rig, e, ctx = self.ctx('Promo_SM.DawnWingsNecrozma_106', 'Gulf Stream')
            self.count_zone(rig, P1, 'prizePile', prizes)
            ctx.source.set_attribute(AttrID.HP, ctx.max_hp(ctx.source) - 30)
            ctx.deal_damage = AsyncMock(return_value=0)
            await ctx.ability.effect(ctx)
            self.assertEqual(ctx.deal_damage.call_args.args[0], ctx.ability.damage + (60 if prizes == 6 else 0))

    async def test_field_energy_threshold_counts_only_matching_provided_units(self):
        for count in (2, 3):
            rig, e, ctx = self.ctx('SV065.Absol_30', 'Darkfall')
            for pokemon in ctx.my_pokemon_in_play():
                for energy in rig.board.attached_energies(pokemon):
                    rig.to_area(energy, P1, 'discard')
            for _ in range(count):
                energy = self.add(rig, def_for(self.energies[PokemonTypes.DARKNESS.value]), P1, 'hand')
                rig.attach(energy, ctx.my_bench()[0])
            wrong = self.add(rig, def_for(self.energies[PokemonTypes.FIRE.value]), P1, 'hand')
            rig.attach(wrong, ctx.source)
            ctx.deal_damage = AsyncMock(return_value=0)
            await ctx.ability.effect(ctx)
            self.assertEqual(ctx.deal_damage.call_args.args[0], ctx.ability.damage + (50 if count == 3 else 0))

    async def test_improvisational_performance_branches_are_exclusive(self):
        for count in (0, 1, 2, 3, 4, 6, 7):
            rig, e, ctx = self.ctx('SM12.Kricketune_14', 'Improvisational Performance')
            self.count_zone(rig, P1, 'hand', count)
            ctx.deal_damage = AsyncMock(return_value=0)
            await ctx.ability.effect(ctx)
            calls = ctx.deal_damage.call_args_list
            self.assertEqual(calls[0].args[0], 130 if count == 1 else 30)
            self.assertEqual(len(calls) - 1, len(ctx.opponent_bench()) if count == 6 else 0)
            for call in calls[1:]:
                self.assertEqual(call.args[0], 30)
                self.assertIn(call.kwargs['target'], ctx.opponent_bench())
            self.assertEqual('Confused' in (ctx.defender.get_attribute(AttrID.SPECIAL_CONDITIONS) or []), count == 3)

    async def test_tool_attachment_bonus_records_hand_not_other_zones(self):
        for zone in ('hand', 'discard'):
            rig, e, ctx = self.ctx('SV4.Mienshao_97', 'Whip Expert')
            tool = self.add(rig, fixtures.definition('XY3.FocusSash_91'), P1, zone)
            self.assertTrue(await ctx.attach_card(tool, ctx.source))
            self.assertEqual(ctx.source.entity_id in rig.session.turn_state.tools_attached_from_hand, zone == 'hand')
            ctx.deal_damage = AsyncMock(return_value=0)
            await ctx.ability.effect(ctx)
            bonus = 70 if zone == 'hand' else 0
            self.assertEqual(ctx.deal_damage.call_args.args[0], ctx.ability.damage + bonus)
            rig.session.turn_state.begin_turn(P2)
            self.assertFalse(rig.session.turn_state.tools_attached_from_hand)

    async def test_attack_ko_bonus_excludes_checkup_and_ability_knockouts(self):
        rig, e, ctx = self.ctx('BW1.Snivy_1', 'Tackle')
        clause = "any of your fighting pokémon were knocked out by damage from an attack during your opponent's last turn"
        state = rig.session.turn_state
        record = {'archetype_id': ctx.source.archetype_id, 'pokemon_types': [PokemonTypes.FIGHTING.value]}
        state.kos_suffered_last_turn[P1] = [record]
        self.assertFalse(public_attack_condition(ctx, clause))
        state.kos_by_attack_last_turn[P2] = [record]
        self.assertFalse(public_attack_condition(ctx, clause))
        state.kos_by_attack_last_turn[P1] = [record]
        self.assertTrue(public_attack_condition(ctx, clause))
        self.assertFalse(public_attack_condition(ctx, clause.replace('fighting', 'water')))

    async def test_extra_energy_compares_to_cost_not_just_number_attached(self):
        rig, e, ctx = self.ctx('ME1.Tangrowth_7', 'Pumped-Up Whip')
        for energy in list(rig.board.attached_energies(ctx.source)):
            rig.to_area(energy, P1, 'discard')
        required = sum(ctx.ability.cost.values())
        for _ in range(required + 1):
            energy = self.add(rig, def_for(self.energies[PokemonTypes.GRASS.value]), P1, 'hand')
            rig.attach(energy, ctx.source)
        clause = "this pokémon has at least 2 extra energy attached (in addition to this attack's cost)"
        self.assertFalse(public_attack_condition(ctx, clause))
        extra = self.add(rig, def_for(self.energies[PokemonTypes.GRASS.value]), P1, 'hand')
        rig.attach(extra, ctx.source)
        self.assertTrue(public_attack_condition(ctx, clause))

    async def test_active_attack_damage_history_ignores_counters_and_bench(self):
        rig, e, ctx = self.ctx('BW1.Snivy_1', 'Tackle')
        from spirit.game.session.effects import EffectContext
        opponent = EffectContext(rig.session, P2, ctx.defender, ctx.ability)
        await opponent.deal_damage(10, target=ctx.source, as_counters=True, is_attack=False)
        state = rig.session.turn_state
        self.assertNotIn(ctx.source.entity_id, state.active_attack_damage_taken)
        await opponent.deal_damage(10, target=ctx.my_bench()[0])
        self.assertNotIn(ctx.my_bench()[0].entity_id, state.active_attack_damage_taken)
        await opponent.deal_damage(10, target=ctx.source)
        self.assertIn(ctx.source.entity_id, state.active_attack_damage_taken)
        state.begin_turn(P1)
        self.assertTrue(public_attack_condition(ctx,
            "this pokémon was damaged by an attack during your opponent's last turn while it was your active pokémon"))

    async def test_burning_icicles_requires_fire_before_hitting_bench(self):
        for fire in (False, True):
            rig, e, ctx = self.ctx('XY10.WhiteKyurem_21', 'Burning Icicles')
            for energy in list(ctx.attached_energies(ctx.source)):
                rig.to_area(energy, P1, 'discard')
            if fire:
                energy = self.add(rig, def_for(self.energies[PokemonTypes.FIRE.value]), P1, 'hand')
                rig.attach(energy, ctx.source)
            ctx.choose_pokemon = AsyncMock(side_effect=lambda pool, *args, **kwargs: pool[0])
            ctx.deal_damage = AsyncMock(return_value=0)
            await ctx.ability.effect(ctx)
            bench_calls = [c for c in ctx.deal_damage.call_args_list if c.kwargs.get('target') in ctx.opponent_bench()]
            self.assertEqual(len(bench_calls), 2 if fire else 0)

    async def test_legacy_named_condition_and_status_cleanup(self):
        rig, e, ctx = self.ctx('COL.Seviper_51', 'Poison Effect')
        ctx.source.set_attribute(AttrID.SPECIAL_CONDITIONS, ['Poisoned', 'Confused'])
        ctx.deal_damage = AsyncMock(return_value=0)
        await ctx.ability.effect(ctx)
        self.assertEqual(ctx.deal_damage.call_args.args[0], 80)
        self.assertEqual(ctx.source.get_attribute(AttrID.SPECIAL_CONDITIONS), ['Confused'])
        rig, e, ctx = self.ctx('XY1.Conkeldurr_67', 'Wake-Up Slap')
        ctx.defender.set_attribute(AttrID.SPECIAL_CONDITIONS, ['Poisoned', 'Asleep'])
        ctx.deal_damage = AsyncMock(return_value=0)
        await ctx.ability.effect(ctx)
        self.assertEqual(ctx.deal_damage.call_args.args[0], ctx.ability.damage + 60)
        self.assertFalse(ctx.defender.get_attribute(AttrID.SPECIAL_CONDITIONS))

    async def test_unified_beatdown_cannot_be_declared_on_second_players_first_turn(self):
        rig, e, ctx = self.ctx('ME2PT5.Terapagosex_179', 'Unified Beatdown')
        for turn in (2, 3, 4):
            rig.session.turn_state.turn_number = turn
            self.assertEqual(ctx.ability.condition(rig.board, P1, ctx.source), turn != 2)


if __name__ == '__main__':
    unittest.main()
