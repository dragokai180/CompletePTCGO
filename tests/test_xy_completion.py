"""XY follow-up: assertions on results, legal candidates and effect lifetimes."""
import unittest
from unittest.mock import AsyncMock
from tests import test_hgss_rules as fixtures
from tests.test_hgss_rules import definition
from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.session.effects import EffectContext
from spirit.game.session.passives import TurnDamageModifier, effective_max_hp
from spirit.tools.effect_smoke import P1, P2


class XyCompletionTests(unittest.IsolatedAsyncioTestCase):

    async def test_trick_shovel_allows_either_nonempty_deck(self):
        rig, e, ctx = self.trainer('XY2.TrickShovel_98')
        for card in list(ctx.deck()):
            rig.to_area(card, P1, 'discard')
        self.assertTrue(self.legal(rig, ctx, 'XY2.TrickShovel_98'))
        for card in list(ctx.deck(P2)):
            rig.to_area(card, P2, 'discard')
        self.assertFalse(self.legal(rig, ctx, 'XY2.TrickShovel_98'))


    async def test_hand_control_supporter_draws_for_opponent(self):
        rig, e, ctx = self.ctx('XY3.Hypno_36', 'Hand Control')
        supporter = self.add(rig, definition('XY0.Tierno_39'), P2, 'hand')
        before = len(ctx.hand(P2))
        own = len(ctx.hand())
        ctx.choose_cards = AsyncMock(return_value=[supporter])
        await ctx.ability.effect(ctx)
        self.assertEqual(len(ctx.hand(P2)), before - 1 + 3)
        self.assertEqual(len(ctx.hand()), own)
        self.assertIn(supporter, ctx.discard_pile(P2))
        self.assertEqual(ctx.player_id, P1)
        self.assertEqual(ctx.source, ctx.attacker)

    async def test_hand_control_attacker_decides_opponents_supporter_target(self):
        rig, e, ctx = self.ctx('XY3.Hypno_36', 'Hand Control')
        supporter = self.add(rig, definition('XY4.AZ_91'), P2, 'hand')
        target = ctx.opponent_bench()[0]
        ctx.choose_cards = AsyncMock(return_value=[supporter])
        rig.session.prompt_entity_picker = AsyncMock(return_value=[target.entity_id])
        await ctx.ability.effect(ctx)
        self.assertIn(target, ctx.hand(P2))
        self.assertIn(supporter, ctx.discard_pile(P2))
        self.assertEqual(rig.session.prompt_entity_picker.await_args.args[0], P1)

    async def test_hand_control_filters_unplayable_supporter_and_can_decline(self):
        rig, e, ctx = self.ctx('XY3.Hypno_36', 'Hand Control')
        supporter = self.add(rig, definition('XY5.MaxiesHiddenBallTrick_133'), P2, 'hand')
        ctx.choose_cards = AsyncMock(return_value=[])
        ctx.reveal_cards = AsyncMock()
        await ctx.ability.effect(ctx)
        self.assertNotIn(supporter, ctx.choose_cards.await_args.args[0])
        self.assertIn(supporter, ctx.hand(P2))
        ctx.reveal_cards.assert_awaited_once()


    async def test_trick_shovel_either_deck_and_declining_discard(self):
        for side in (0, 1):
            for discard in (False, True):
                rig, e, ctx = self.trainer('XY2.TrickShovel_98')
                pid = (P1, P2)[side]
                top = ctx.deck_top(1, player_id=pid)[0]
                other = ctx.deck_top(1, player_id=(P2, P1)[side])[0]
                ctx.choose = AsyncMock(return_value=side)
                ctx.ask_yes_no = AsyncMock(return_value=discard)
                ctx.reveal_cards = AsyncMock()
                await definition('XY2.TrickShovel_98').effect(ctx)
                ctx.reveal_cards.assert_awaited_once_with([top], to_player=P1)
                self.assertIn(top, ctx.discard_pile(pid) if discard else ctx.deck(pid))
                self.assertIn(other, ctx.deck((P2, P1)[side]))


    async def test_xy_special_energy_providers_and_attachment_types(self):
        from spirit.game.session.passives import energy_provided_options
        cases = [
            ('XY3.HerbalEnergy_103', PokemonTypes.GRASS),
            ('XY3.StrongEnergy_104', PokemonTypes.FIGHTING),
            ('XY10.StrongEnergy_115', PokemonTypes.FIGHTING),
            ('XY4.MysteryEnergy_112', PokemonTypes.PSYCHIC),
            ('XY5.ShieldEnergy_143', PokemonTypes.METAL),
            ('XY5.WonderEnergy_144', PokemonTypes.FAIRY),
            ('XY7.DangerousEnergy_82', PokemonTypes.DARKNESS),
            ('XY7.FlashEnergy_83', PokemonTypes.LIGHTNING),
            ('XY8.BurningEnergy_151', PokemonTypes.FIRE),
            ('XY9.SplashEnergy_113', PokemonTypes.WATER),
        ]
        for path, kind in cases:
            with self.subTest(path=path):
                rig, e, ctx = self.ctx('BW1.Snivy_1', 'Tackle')
                d = definition(path)
                card = self.add(rig, d, P1, 'hand')
                target = ctx.attacker
                target.set_attribute(AttrID.POKEMON_TYPES, [kind.value])
                self.assertTrue(d.attach_to(target))
                rig.attach(card, target)
                self.assertIn([kind.value], energy_provided_options(rig.board, card))
                target.set_attribute(AttrID.POKEMON_TYPES, [PokemonTypes.COLORLESS.value])
                self.assertFalse(d.attach_to(target))

    async def test_strong_shield_mystery_flash_and_wonder_scope(self):
        from spirit.game.session.passives import compute_damage, effective_retreat_cost, attack_effects_blocked
        from spirit.game.attributes import SpecialConditions
        for path, kind in (
            ('XY3.StrongEnergy_104', PokemonTypes.FIGHTING),
            ('XY5.ShieldEnergy_143', PokemonTypes.METAL),
            ('XY4.MysteryEnergy_112', PokemonTypes.PSYCHIC),
            ('XY7.FlashEnergy_83', PokemonTypes.LIGHTNING),
            ('XY5.WonderEnergy_144', PokemonTypes.FAIRY),
        ):
            rig, e, ctx = self.ctx('BW1.Snivy_1', 'Tackle')
            target = ctx.attacker
            target.set_attribute(AttrID.POKEMON_TYPES, [kind.value])
            target.set_attribute(AttrID.WEAKNESS_TYPES, [PokemonTypes.GRASS.value])
            ctx.defender.set_attribute(AttrID.WEAKNESS_TYPES, [])
            ctx.defender.set_attribute(AttrID.RESISTANCE_TYPES, [])
            before_cost = effective_retreat_cost(rig.board, target)
            energy = self.add(rig, definition(path), P1, 'hand')
            rig.attach(energy, target)
            if 'Strong' in path:
                self.assertEqual(compute_damage(rig.board, target, ctx.defender, 20).amount, 40)
                bench = ctx.opponent_bench()[0]
                self.assertEqual(compute_damage(rig.board, target, bench, 20, apply_modifiers=False).amount, 20)
            elif 'Shield' in path:
                target.set_attribute(AttrID.WEAKNESS_TYPES, [])
                self.assertEqual(compute_damage(rig.board, ctx.defender, target, 30).amount, 20)
            elif 'Mystery' in path:
                self.assertEqual(effective_retreat_cost(rig.board, target), max(0, before_cost - 2))
            elif 'Flash' in path:
                ctx.defender.set_attribute(AttrID.POKEMON_TYPES, [PokemonTypes.GRASS.value])
                self.assertEqual(compute_damage(rig.board, ctx.defender, target, 20).amount, 20)
            else:
                self.assertTrue(attack_effects_blocked(rig.board, target))

    async def test_burning_energy_reattaches_after_own_attack_not_trainer(self):
        for from_attack in (False, True):
            rig, e, ctx = self.ctx('BW1.Snivy_1', 'Tackle')
            ctx.attacker.set_attribute(AttrID.POKEMON_TYPES, [PokemonTypes.FIRE.value])
            energy = self.add(rig, definition('XY8.BurningEnergy_151'), P1, 'hand')
            rig.attach(energy, ctx.attacker)
            acting = ctx if from_attack else EffectContext(rig.session, P1, ctx.source, None)
            await acting.discard_cards([energy])
            self.assertIn(energy, acting.discard_pile())
            for action in list(acting.deferred_actions):
                await action()
            self.assertEqual(energy in ctx.attached_energies(ctx.attacker), from_attack)

    async def test_rainbow_and_double_dragon_provided_units(self):
        from spirit.game.session.passives import energy_provided_options
        for path, units in (('XY1.RainbowEnergy_131', 1), ('XY8.RainbowEnergy_152', 1),
                            ('XY6.DoubleDragonEnergy_97', 2)):
            rig, e, ctx = self.ctx('BW1.Snivy_1', 'Tackle')
            ctx.attacker.set_attribute(AttrID.POKEMON_TYPES, [PokemonTypes.DRAGON.value])
            energy = self.add(rig, definition(path), P1, 'hand')
            rig.attach(energy, ctx.attacker)
            options = energy_provided_options(rig.board, energy)
            self.assertTrue(options)
            self.assertTrue(all(len(option) == units for option in options))
            self.assertTrue(any(PokemonTypes.FIRE.value in option for option in options))
            if units == 2:
                from spirit.game.session.legal_actions import attack_cost_satisfied
                self.assertTrue(attack_cost_satisfied({'Fire': 1, 'Water': 1}, [energy], rig.board))
                self.assertFalse(attack_cost_satisfied({'Fire': 1, 'Water': 2}, [energy], rig.board))


    async def test_solar_birth_attaches_to_the_pokemon_just_benched(self):
        rig, e, ctx = self.ctx('XY7.Volcarona_17', 'Solar Birth')
        pokemon = self.add(rig, definition('BW1.Snivy_1'), P1, 'deck')
        energies = [self.add(rig, definition('BW1.FireEnergy_106'), P1, 'deck') for _ in range(2)]
        ctx.search_deck = AsyncMock(side_effect=[[pokemon], energies])
        self.choose_first(ctx)
        await ctx.ability.effect(ctx)
        self.assertIn(pokemon, ctx.my_bench())
        self.assertTrue(all(c in ctx.attached_energies(pokemon) for c in energies))

    async def test_jagged_saber_heals_only_successful_recipients(self):
        rig, e, ctx = self.ctx('XY7.MSceptileEX_8', 'Jagged Saber')
        energies = [self.add(rig, definition('BW1.GrassEnergy_105'), P1, 'hand') for _ in range(2)]
        for p in ctx.my_pokemon_in_play():
            p.set_attribute(AttrID.HP, ctx.max_hp(p) - 20)
        targets = ctx.my_bench()[:2]
        ctx.choose_cards = AsyncMock(return_value=energies)
        ctx.choose_pokemon = AsyncMock(side_effect=targets)
        ctx.deal_damage = AsyncMock(return_value=0)
        await ctx.ability.effect(ctx)
        for card, target in zip(energies, targets):
            self.assertIn(card, ctx.attached_energies(target))
            self.assertEqual(target.get_attribute(AttrID.HP), ctx.max_hp(target))
        self.assertEqual(ctx.attacker.get_attribute(AttrID.HP), ctx.max_hp(ctx.attacker) - 20)

    async def test_burning_icicles_requires_fire_and_two_different_targets(self):
        for attached in (False, True):
            rig, e, ctx = self.ctx('XY10.WhiteKyurem_21', 'Burning Icicles')
            for card in list(ctx.attached_energies(ctx.attacker)):
                rig.to_area(card, P1, 'discard')
            if attached:
                rig.attach_energy_type(P1, ctx.attacker, PokemonTypes.FIRE.value)
            ctx.deal_damage = AsyncMock(return_value=0)
            self.choose_first(ctx)
            await ctx.ability.effect(ctx)
            secondary = [c for c in ctx.deal_damage.call_args_list if c.args[0] == 20]
            self.assertEqual(len(secondary), 2 if attached else 0)

    async def test_lock_on_applies_bonus_after_weakness(self):
        from spirit.game.session.passives import compute_damage
        rig, e, ctx = self.ctx('XY11.ClawitzerBREAK_35', 'Lock-On')
        ctx.defender.set_attribute(AttrID.WEAKNESS_TYPES, [PokemonTypes.WATER.value])
        ctx.attacker.set_attribute(AttrID.POKEMON_TYPES, [PokemonTypes.WATER.value])
        await ctx.ability.effect(ctx)
        rig.session.turn_state.begin_turn(P2, rig.board)
        rig.session.turn_state.begin_turn(P1, rig.board)
        value = compute_damage(rig.board, ctx.attacker, ctx.defender, 20)
        self.assertEqual(value.amount, 160)  # 20 x 2 + 120, not (20 + 120) x 2.

    async def test_dragon_dance_does_not_stack_and_ranger_removes_bonus(self):
        from spirit.game.session.passives import compute_damage
        rig, e, ctx = self.ctx('XY8.Haxorus_111', 'Dragon Dance')
        ctx.defender.set_attribute(AttrID.WEAKNESS_TYPES, [])
        ctx.defender.set_attribute(AttrID.RESISTANCE_TYPES, [])
        await ctx.ability.effect(ctx)
        await ctx.ability.effect(ctx)
        self.assertEqual(compute_damage(rig.board, ctx.attacker, ctx.defender, 10).amount, 110)
        await definition('XY11.PokmonRanger_104').effect(EffectContext(rig.session, P1, ctx.attacker, None))
        self.assertEqual(compute_damage(rig.board, ctx.attacker, ctx.defender, 10).amount, 10)

    async def test_vanishing_strike_ignores_protection_only_with_stadium(self):
        from spirit.game.card_effects.bw_era import _BWTurnShield
        for stadium_present in (False, True):
            rig, e, ctx = self.ctx('XY8.MMewtwoEX_63', 'Vanishing Strike')
            ctx.add_passive_through_opponents_turn(ctx.defender, _BWTurnShield(prevent_all=True))
            if stadium_present:
                stadium = self.add(rig, definition('XY5.RoughSeas_137'), P1, 'hand')
                rig.board.move_card(stadium.entity_id, rig.board.find_global_area('activeStadium').entity_id)
                stadium.owning_player_id = P1
            ctx.deal_damage = AsyncMock(return_value=0)
            await ctx.ability.effect(ctx)
            primary = ctx.deal_damage.call_args_list[0]
            self.assertEqual(primary.args[0], 200 if stadium_present else 150)
            self.assertEqual(primary.kwargs.get('ignore_target_effects', False), stadium_present)

    async def test_rare_candy_xy_printing_obeys_timing_and_stage_two(self):
        path = 'XY5.RareCandy_135'
        rig, e, ctx = self.trainer(path)
        rig.to_area(ctx.my_active(), P1, 'discard')
        self.add(rig, definition('BW1.Snivy_1'), P1, 'activePokemonArea')
        self.assertFalse(self.legal(rig, ctx, path))
        stage2 = self.add(rig, definition('BW1.Serperior_5'), P1, 'hand')
        self.assertTrue(self.legal(rig, ctx, path))
        rig.session.turn_state.turn_number = 1
        self.assertFalse(self.legal(rig, ctx, path))
        rig.session.turn_state.turn_number = 3
        self.choose_first(ctx)
        await definition(path).effect(ctx)
        self.assertIs(ctx.my_active(), stage2)


    async def test_stardust_shield_requires_successful_special_discard(self):
        for present in (False, True):
            rig, e, ctx = self.ctx('Promo_XY.Jirachi_67', 'Stardust')
            if present:
                card = self.add(rig, definition('XY1.DoubleColorlessEnergy_130'), P2, 'hand')
                rig.attach(card, ctx.defender)
            self.choose_first(ctx)
            ctx.deal_damage = AsyncMock(return_value=10)
            await ctx.ability.effect(ctx)
            self.assertEqual(bool(rig.board.temporary_passives), present)
            if present:
                self.assertIn(card, ctx.discard_pile(P2))

    async def test_magical_symphony_requires_supporter_for_bench_damage(self):
        for supporter in (False, True):
            rig, e, ctx = self.ctx('XY10.MAudinoEX_85', 'Magical Symphony')
            rig.session.turn_state.supporter_played = supporter
            target = ctx.opponent_bench()[0]
            ctx.choose_pokemon = AsyncMock(return_value=target)
            ctx.deal_damage = AsyncMock(return_value=0)
            await ctx.ability.effect(ctx)
            hits = [call for call in ctx.deal_damage.call_args_list
                    if call.kwargs.get('target') is target
                    or len(call.args) > 1 and call.args[1] is target]
            self.assertEqual(len(hits), int(supporter))
            if hits:
                self.assertEqual(hits[0].args[0], 50)

    async def test_link_fusion_adds_distinct_named_bench_bonuses(self):
        rig, e, ctx = self.ctx('XY10.Reuniclus_35', 'Link Fusion')
        for p in list(ctx.my_bench()):
            rig.to_area(p, P1, 'discard')
        ctx.deal_damage = AsyncMock(return_value=0)
        for path, expected in (
            (None, 10), ('XY10.Solosis_33', 40), ('XY10.Duosion_34', 100),
            ('XY10.Reuniclus_35', 190),
        ):
            if path:
                self.add(rig, definition(path), P1, 'bench')
            ctx.deal_damage.reset_mock()
            await ctx.ability.effect(ctx)
            self.assertEqual(ctx.deal_damage.call_args_list[0].args[0], expected)

    async def test_energy_glide_switch_only_after_attachment(self):
        for success in (False, True):
            rig, e, ctx = self.ctx('XY1.EmolgaEX_46', 'Energy Glide')
            card = self.add(rig, definition('BW1.LightningEnergy_108'), P1, 'deck')
            ctx.search_deck = AsyncMock(return_value=[card] if success else [])
            ctx.attach_energy = AsyncMock(return_value=True)
            ctx.switch_active = AsyncMock()
            ctx.choose_pokemon = AsyncMock(return_value=ctx.my_bench()[0])
            await ctx.ability.effect(ctx)
            self.assertEqual(ctx.switch_active.await_count, int(success))

    async def test_metal_rain_allows_repeated_target_per_discarded_card(self):
        rig, e, ctx = self.ctx('XY10.BronzongBREAK_62', 'Metal Rain')
        metal = [self.add(rig, definition('BW1.MetalEnergy_112'), P1, 'hand') for _ in range(2)]
        for c in metal:
            rig.attach(c, ctx.attacker)
        ctx.choose_cards = AsyncMock(return_value=metal)
        target = ctx.opponent_bench()[0]
        ctx.choose_pokemon = AsyncMock(return_value=target)
        ctx.deal_damage = AsyncMock(return_value=0)
        await ctx.ability.effect(ctx)
        self.assertTrue(all(c in ctx.discard_pile() for c in metal))
        hits = ctx.deal_damage.call_args_list
        self.assertEqual(sum(c.args[0] for c in hits), 60)
        for c in hits:
            self.assertIs(c.kwargs.get('target', c.args[1] if len(c.args)>1 else None), target)
            self.assertFalse(c.kwargs.get('apply_modifiers', True))

    async def test_tidal_storm_bench_damage_only_uppercase_ex(self):
        rig, e, ctx = self.ctx('XY5.PrimalKyogreEX_55', 'Tidal Storm')
        old_ex = self.add(rig, definition('BW7.KeldeoEX_49'), P2, 'bench')
        new_ex = self.add(rig, definition('SV05.IronCrownex_81'), P2, 'bench')
        ctx.deal_damage = AsyncMock(return_value=0)
        self.choose_first(ctx)
        await ctx.ability.effect(ctx)
        hits = ctx.deal_damage.call_args_list
        targets = [c.kwargs.get('target', c.args[1] if len(c.args)>1 else ctx.defender) for c in hits]
        self.assertIn(old_ex, targets)
        self.assertNotIn(new_ex, targets)
        for target in ctx.opponent_bench():
            if target is not old_ex:
                self.assertNotIn(target, targets)

    async def test_coordinate_chooses_two_distinct_tool_free_bench_targets(self):
        rig, e, ctx = self.ctx('XY4.Leavanny_7', 'Coordinate')
        available = ctx.my_bench()
        tools = [self.add(rig, definition('XY1.MuscleBand_121'), P1, 'deck') for _ in range(2)]
        ctx.choose_pokemon = AsyncMock(side_effect=lambda pool, *a, **kw: list(pool)[0])
        ctx.search_deck = AsyncMock(side_effect=lambda *a, **kw: [tools.pop(0)] if tools else [])
        await ctx.ability.effect(ctx)
        self.assertEqual(sum(bool(p.children and any(
            c.archetype_id == definition('XY1.MuscleBand_121').guid for c in p.children))
            for p in available), 2)

    async def test_flare_up_requires_ten_fire_and_shuffles_exactly_ten(self):
        for count in (9, 10, 11):
            rig, e, ctx = self.ctx('XY11.Infernape_20', 'Flare Up')
            for c in list(ctx.discard_pile()):
                rig.to_area(c, P1, 'deck')
            cards = [self.add(rig, definition('BW1.FireEnergy_106'), P1, 'discard') for _ in range(count)]
            self.choose_first(ctx)
            ctx.deal_damage = AsyncMock(return_value=0)
            await ctx.ability.effect(ctx)
            self.assertEqual(ctx.deal_damage.await_count, int(count >= 10))
            self.assertEqual(sum(c in ctx.deck() for c in cards), 10 if count >= 10 else 0)


    async def test_position_gated_abilities_all_printings(self):
        for path, title in (
            ('XY3.Jynx_37', 'Victory Kiss'), ('TwentiethAnn.Jynx_36', 'Victory Kiss'),
            ('XY7.Unown_30', 'Farewell Letter'), ('XY8.Zoroark_91', 'Stand In'),
            ('XY11.Klefki_80', 'Wonder Lock'),
        ):
            with self.subTest(path=path):
                rig, e, ctx = self.ctx(path, title)
                self.assertFalse(ctx.ability.condition(rig.board, P1, ctx.source))
                rig.to_area(ctx.source, P1, 'bench')
                active = self.add(rig, definition('BW1.Snivy_1'), P1, 'activePokemonArea')
                active.set_attribute(AttrID.HP, 20)
                self.assertTrue(ctx.ability.condition(rig.board, P1, ctx.source))
                self.choose_first(ctx)
                before_hand = len(ctx.hand())
                ctx.ask_yes_no = AsyncMock(return_value=True)
                await ctx.ability.effect(ctx)
                if title == 'Victory Kiss':
                    self.assertEqual(active.get_attribute(AttrID.HP), 30)
                elif title == 'Farewell Letter':
                    self.assertIn(ctx.source, ctx.discard_pile())
                    self.assertEqual(len(ctx.hand()), before_hand + 1)
                elif title == 'Stand In':
                    self.assertIs(ctx.my_active(), ctx.source)
                    self.assertIn(active, ctx.my_bench())
                else:
                    self.assertIs(ctx.source.parent, active)

    async def test_tool_return_abilities_only_legal_holders(self):
        for path, title in (
            ('XY10.GenesectEX_64', 'Drive Change'),
            ('XY10.GenesectEX_120', 'Drive Change'),
            ('XY11.Weavile_61', 'Tear Away'),
        ):
            with self.subTest(path=path):
                rig, e, ctx = self.ctx(path, title)
                self.assertFalse(ctx.ability.condition(rig.board, P1, ctx.source))
                target = ctx.source if title == 'Drive Change' else ctx.my_bench()[0]
                tool = self.add(rig, definition('XY1.MuscleBand_121'), P1, 'hand')
                rig.attach(tool, target)
                self.assertTrue(ctx.ability.condition(rig.board, P1, ctx.source))
                self.choose_first(ctx)
                await ctx.ability.effect(ctx)
                self.assertIn(tool, ctx.hand())
                self.assertFalse(ctx.ability.condition(rig.board, P1, ctx.source))

    async def test_purifying_fire_requires_basic_fire_and_damage(self):
        for path in ('XY9.HoOhEX_92', 'XY9.HoOhEX_121'):
            rig, e, ctx = self.ctx(path, 'Purifying Fire')
            self.assertFalse(ctx.ability.condition(rig.board, P1, ctx.source))
            ctx.source.set_attribute(AttrID.HP, ctx.max_hp(ctx.source) - 60)
            self.assertFalse(ctx.ability.condition(rig.board, P1, ctx.source))
            rig.attach_energy_type(P1, ctx.source, PokemonTypes.FIRE.value)
            self.assertTrue(ctx.ability.condition(rig.board, P1, ctx.source))
            await ctx.ability.effect(ctx)
            self.assertEqual(ctx.source.get_attribute(AttrID.HP), ctx.max_hp(ctx.source) - 10)

    async def test_mega_boost_and_mega_turbo_restrict_targets(self):
        for path in ('XY11.Clawitzer_34', 'Promo_XY.Clawitzer_146'):
            rig, e, ctx = self.ctx(path, 'Mega Boost')
            self.assertFalse(ctx.ability.condition(rig.board, P1, ctx.source))
            special = self.add(rig, definition('XY1.DoubleColorlessEnergy_130'), P1, 'hand')
            mega = self.add(rig, definition('XY10.MAltariaEX_69'), P1, 'bench')
            self.assertTrue(ctx.ability.condition(rig.board, P1, ctx.source))
            self.choose_first(ctx)
            await ctx.ability.effect(ctx)
            self.assertIn(special, ctx.attached_energies(mega))
            self.assertFalse(rig.session.turn_state.energy_attached)
        rig, e, ctx = self.trainer('XY6.MegaTurbo_86')
        self.assertFalse(self.legal(rig, ctx, 'XY6.MegaTurbo_86'))
        mega = self.add(rig, definition('XY10.MAltariaEX_69'), P1, 'bench')
        self.assertTrue(self.legal(rig, ctx, 'XY6.MegaTurbo_86'))
        self.choose_first(ctx)
        before = len(ctx.attached_energies(mega))
        await definition('XY6.MegaTurbo_86').effect(ctx)
        self.assertEqual(len(ctx.attached_energies(mega)), before + 1)

    async def test_burning_road_tracks_active_entry_and_moves_fire_only(self):
        rig, e, ctx = self.ctx('XY12.Arcanine_18', 'Burning Road')
        state = rig.session.turn_state
        self.assertFalse(ctx.ability.condition(rig.board, P1, ctx.source))
        donor = ctx.my_bench()[0]
        fire = self.add(rig, definition('BW1.FireEnergy_106'), P1, 'hand')
        rig.attach(fire, donor)
        state.became_active_turn[ctx.source.entity_id] = state.turn_number
        self.assertTrue(ctx.ability.condition(rig.board, P1, ctx.source))
        ctx.move_energy_freely = AsyncMock()
        await ctx.ability.effect(ctx)
        donors, targets = ctx.move_energy_freely.call_args.args[:2]
        self.assertIn(donor, donors)
        self.assertEqual(targets, [ctx.source])
        predicate = ctx.move_energy_freely.call_args.kwargs['predicate']
        self.assertTrue(predicate(fire))
        self.assertFalse(predicate(self.add(rig, definition('BW1.WaterEnergy_107'), P1, 'hand')))

    async def test_buddy_buddy_rescue_opponent_chooses_first(self):
        rig, e, ctx = self.trainer('XY8.BuddyBuddyRescue_135')
        self.assertFalse(self.legal(rig, ctx, 'XY8.BuddyBuddyRescue_135'))
        ours = self.add(rig, definition('BW1.Snivy_1'), P1, 'discard')
        theirs = self.add(rig, definition('BW1.Snivy_1'), P2, 'discard')
        self.assertTrue(self.legal(rig, ctx, 'XY8.BuddyBuddyRescue_135'))
        self.choose_first(ctx)
        await definition('XY8.BuddyBuddyRescue_135').effect(ctx)
        self.assertIn(ours, ctx.hand())
        self.assertIn(theirs, ctx.hand(P2))
        self.assertEqual(ctx.choose_cards.call_args_list[0].kwargs['player_id'], P2)

    async def test_devolution_spray_removes_only_top_stage(self):
        for path in ('XY10.DevolutionSpray_95', 'XY12.DevolutionSpray_76'):
            rig, e, ctx = self.trainer(path)
            self.assertFalse(self.legal(rig, ctx, path))
            basic = ctx.my_active()
            # A real Basic -> Stage 1 -> Stage 2 stack.
            stage1 = self.add(rig, definition('BW1.Servine_3'), P1, 'hand')
            stage2 = self.add(rig, definition('BW1.Serperior_5'), P1, 'hand')
            await ctx.evolve_pokemon(basic, stage1)
            await ctx.evolve_pokemon(stage1, stage2)
            self.assertTrue(self.legal(rig, ctx, path))
            self.choose_first(ctx)
            await definition(path).effect(ctx)
            self.assertIs(ctx.my_active(), stage1)
            self.assertIn(stage2, ctx.hand())
            self.assertNotIn(stage1, ctx.hand())


    def trainer(self, path):
        rig, e = self.rig(path, 'trainer')
        ctx = EffectContext(rig.session, P1, e['target'], None)
        # The physical Trainer is already on the table during resolution.
        rig.board.move_card(ctx.source.entity_id, rig.board.find_global_area('activeTrainer').entity_id)
        ctx.source.owning_player_id = P1
        return rig, e, ctx

    def legal(self, rig, ctx, path):
        from spirit.game.session.legal_actions import trainer_condition_met
        return trainer_condition_met(definition(path).condition, rig.board, P1, ctx.source)

    def choose_first(self, ctx):
        ctx.choose_cards = AsyncMock(side_effect=lambda pool, count=1, **kw: list(pool)[:count])
        ctx.choose_pokemon = AsyncMock(side_effect=lambda pool, *a, **kw: list(pool)[0] if pool else None)

    async def test_recovery_families_all_printings(self):
        families = [
            (['XY1.MaxRevive_120', 'TwentiethAnn.MaxRevive_65'], 'BW1.Snivy_1', 'deck', 1),
            (['XY2.PalPad_92'], 'XY0.Tierno_39', 'deck', 2),
            (['XY2.SacredAsh_96'], 'BW1.Snivy_1', 'deck', 5),
            (['XY4.VSSeeker_109', 'XY6.VSSeeker_110'], 'XY0.Tierno_39', 'hand', 1),
            (['XY7.EcoArm_71'], 'XY1.MuscleBand_121', 'deck', 3),
            (['XY11.SpecialCharge_105'], 'XY1.DoubleColorlessEnergy_130', 'deck', 2),
            (['TwentiethAnn.Revitalizer_70'], 'BW1.Snivy_1', 'hand', 2),
            (['XY10.FossilExcavationKit_101'], 'XY10.DomeFossilKabuto_96', 'hand', 2),
            (['Promo_XY.Karen_177', 'Promo_XY.Karen_214'], 'BW1.Snivy_1', 'deck', 3),
        ]
        for paths, candidate_path, destination, amount in families:
            for path in paths:
                with self.subTest(path=path):
                    rig, e, ctx = self.trainer(path)
                    for c in list(ctx.discard_pile()):
                        if c is not ctx.source:
                            rig.to_area(c, P1, 'deck')
                    self.assertFalse(self.legal(rig, ctx, path))
                    wanted = [self.add(rig, definition(candidate_path), P1, 'discard') for _ in range(amount)]
                    self.assertTrue(self.legal(rig, ctx, path))
                    self.choose_first(ctx)
                    await definition(path).effect(ctx)
                    pile = rig.board.find_player_area(P1, destination).children
                    for card in wanted:
                        self.assertIn(card, pile)
                    self.assertIn(ctx.source, rig.board.find_global_area('activeTrainer').children)

    async def test_blacksmith_all_printings_partial_supply_and_type(self):
        for path in ('XY2.Blacksmith_88', 'XY2.Blacksmith_111'):
            for count in (1, 2):
                with self.subTest(path=path, count=count):
                    rig, e, ctx = self.trainer(path)
                    self.assertFalse(self.legal(rig, ctx, path))
                    target = ctx.my_active()
                    target.set_attribute(AttrID.POKEMON_TYPES, [PokemonTypes.FIRE.value])
                    for c in list(ctx.discard_pile()):
                        if c is not ctx.source:
                            rig.to_area(c, P1, 'deck')
                    fire = [self.add(rig, definition('BW1.FireEnergy_106'), P1, 'discard') for _ in range(count)]
                    self.assertTrue(self.legal(rig, ctx, path))
                    self.choose_first(ctx)
                    await definition(path).effect(ctx)
                    self.assertTrue(all(c in ctx.attached_energies(target) for c in fire))

    async def test_target_whistle_revive_and_mega_catcher(self):
        for path, owner, target_path, destination in (
            ('XY4.TargetWhistleTeamFlareGear_106', P2, 'BW1.Snivy_1', 'bench'),
            ('XY6.Revive_88', P1, 'BW1.Snivy_1', 'bench'),
            ('XY12.Revive_85', P1, 'BW1.Snivy_1', 'bench'),
            ('XY10.MegaCatcher_104', P2, 'XY10.MAltariaEX_69', 'activePokemonArea'),
        ):
            with self.subTest(path=path):
                rig, e, ctx = self.trainer(path)
                self.assertFalse(self.legal(rig, ctx, path))
                target = self.add(rig, definition(target_path), owner,
                                  'bench' if 'Catcher' in path else 'discard')
                self.assertTrue(self.legal(rig, ctx, path))
                self.choose_first(ctx)
                await definition(path).effect(ctx)
                self.assertIn(target, rig.board.find_player_area(owner, destination).children)

    async def test_tools_and_enhanced_hammer(self):
        cases = [
            ('XY2.StartlingMegaphone_97', P2, 'XY1.MuscleBand_121', 'discard'),
            ('XY3.ToolRetriever_101', P1, 'XY1.MuscleBand_121', 'hand'),
            ('XY4.Xerosic_110', P1, 'XY1.MuscleBand_121', 'discard'),
            ('XY4.Xerosic_119', P2, 'XY1.DoubleColorlessEnergy_130', 'discard'),
            ('XY4.EnhancedHammer_94', P2, 'XY1.DoubleColorlessEnergy_130', 'discard'),
            ('XY5.EnhancedHammer_162', P2, 'XY1.DoubleColorlessEnergy_130', 'discard'),
        ]
        for path, owner, attachment_path, destination in cases:
            with self.subTest(path=path):
                rig, e, ctx = self.trainer(path)
                self.assertFalse(self.legal(rig, ctx, path))
                card = self.add(rig, definition(attachment_path), owner, 'hand')
                rig.attach(card, rig.board.active_pokemon(owner))
                self.assertTrue(self.legal(rig, ctx, path))
                self.choose_first(ctx)
                await definition(path).effect(ctx)
                self.assertIn(card, rig.board.find_player_area(owner, destination).children)

    async def test_full_heal_fairy_drop_and_ace_trainer(self):
        for path in ('XY3.FullHeal_93', 'XY12.FullHeal_78'):
            rig, e, ctx = self.trainer(path)
            self.assertFalse(self.legal(rig, ctx, path))
            ctx.my_active().set_attribute(AttrID.SPECIAL_CONDITIONS, ['Poisoned', 'Asleep'])
            self.assertTrue(self.legal(rig, ctx, path))
            await definition(path).effect(ctx)
            self.assertFalse(ctx.my_active().get_attribute(AttrID.SPECIAL_CONDITIONS))
        rig, e, ctx = self.trainer('XY10.FairyDrop_99')
        target = ctx.my_active()
        target.set_attribute(AttrID.HP, 10)
        self.assertFalse(self.legal(rig, ctx, 'XY10.FairyDrop_99'))
        rig.attach_energy_type(P1, target, PokemonTypes.FAIRY.value)
        self.assertTrue(self.legal(rig, ctx, 'XY10.FairyDrop_99'))
        self.choose_first(ctx)
        await definition('XY10.FairyDrop_99').effect(ctx)
        self.assertEqual(target.get_attribute(AttrID.HP), min(60, ctx.max_hp(target)))
        rig, e, ctx = self.trainer('XY7.AceTrainer_69')
        self.assertFalse(self.legal(rig, ctx, 'XY7.AceTrainer_69'))
        prize = rig.board.find_player_area(P2, 'prizePile').children[0]
        rig.to_area(prize, P2, 'hand')
        self.assertTrue(self.legal(rig, ctx, 'XY7.AceTrainer_69'))
        await definition('XY7.AceTrainer_69').effect(ctx)
        self.assertEqual(len(ctx.hand()), 6)
        self.assertEqual(len(ctx.hand(P2)), 3)

    async def test_delinquent_discards_stadium_then_opponent_chooses(self):
        for path in ('XY9.Delinquent_98', 'XY9.Delinquent_127', 'XY9.Delinquent_128'):
            rig, e, ctx = self.trainer(path)
            self.assertFalse(self.legal(rig, ctx, path))
            stadium = self.add(rig, definition('XY5.RoughSeas_137'), P2, 'hand')
            rig.board.move_card(stadium.entity_id, rig.board.find_global_area('activeStadium').entity_id)
            stadium.owning_player_id = P2
            self.assertTrue(self.legal(rig, ctx, path))
            self.choose_first(ctx)
            before = len(ctx.hand(P2))
            await definition(path).effect(ctx)
            self.assertIn(stadium, ctx.discard_pile(P2))
            self.assertEqual(len(ctx.hand(P2)), before - 3)
            self.assertEqual(ctx.choose_cards.call_args.kwargs['player_id'], P2)

    async def test_puzzle_single_does_not_require_discard_or_recover(self):
        path = 'XY9.PuzzleofTime_109'
        rig, e, ctx = self.trainer(path)
        for c in list(ctx.discard_pile()):
            if c is not ctx.source:
                rig.to_area(c, P1, 'deck')
        self.assertTrue(self.legal(rig, ctx, path))
        ctx.reorder_deck_top = AsyncMock()
        ctx.put_in_hand = AsyncMock()
        await definition(path).effect(ctx)
        ctx.reorder_deck_top.assert_awaited_once_with(3)
        ctx.put_in_hand.assert_not_awaited()

    async def test_puzzle_pair_recovers_two_not_played_copies(self):
        path = 'XY9.PuzzleofTime_109'
        rig, e, ctx = self.trainer(path)
        second = self.add(rig, definition(path), P1, 'hand')
        self.choose_first(ctx)
        ctx.ask_yes_no = AsyncMock(return_value=True)
        ctx.reorder_deck_top = AsyncMock()
        before = list(ctx.hand())
        await definition(path).effect(ctx)
        self.assertNotIn(second, ctx.hand())
        ctx.reorder_deck_top.assert_not_awaited()
        self.assertEqual(len([c for c in ctx.hand() if c not in before]), 2)
        pool = ctx.choose_cards.call_args_list[-1].args[0]
        self.assertNotIn(second, pool)
        self.assertNotIn(ctx.source, pool)

    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx
    add = fixtures.HgssRulesTests.add

    async def test_ranger_removes_all_restriction_collections_not_history(self):
        rig, e, ctx = self.ctx('BW1.Snivy_1', 'Tackle')
        state = rig.session.turn_state
        target = ctx.defender
        ctx.lock_plays(P2, lambda card: True)
        ctx.restrict_attachments(target)
        ctx.lock_retreat(target)
        ctx.require_attack_flip(target)
        ctx.require_trainer_flip(P2)
        ctx.end_turn_if_energy_attached_to(target)
        ctx.force_coins_through_next_turn(P2, False)
        ctx.lock_gx_attacks(P2)
        state.lock_attack(target.entity_id, 'attack')
        ctx.add_turn_damage_modifier(TurnDamageModifier(20, P1))
        ctx.add_extra_prize_watcher()
        state.gx_used.add(P2)
        state.retreat_locks['unrelated'] = 100
        target.set_attribute(AttrID.HP, 30)
        target.set_attribute(AttrID.SPECIAL_CONDITIONS, ['Poisoned'])
        await definition('XY11.PokmonRanger_104').effect(
            EffectContext(rig.session, P1, ctx.attacker, None))
        for name in ('attack_locks', 'play_locks', 'attach_restrictions',
                     'attack_flip_checks', 'trainer_flip_checks',
                     'attach_ends_turn_checks', 'forced_coins_through_turn',
                     'gx_locked_players', 'damage_modifiers', 'extra_prize_watchers'):
            self.assertFalse(getattr(state, name), name)
        self.assertEqual(state.retreat_locks, {'unrelated': 100})
        self.assertEqual(state.gx_used, {P2})
        self.assertEqual(target.get_attribute(AttrID.HP), 30)
        self.assertEqual(target.get_attribute(AttrID.SPECIAL_CONDITIONS), ['Poisoned'])

    async def test_ranger_preserves_nonattack_locks_and_boosts(self):
        rig, e, ctx = self.ctx('BW1.Snivy_1', 'Tackle')
        state = rig.session.turn_state
        trainer = EffectContext(rig.session, P1, ctx.attacker, None)
        trainer.lock_plays(P2, lambda card: True)
        trainer.lock_retreat(ctx.defender)
        trainer.restrict_attachments(ctx.defender)
        trainer.require_attack_flip(ctx.defender)
        trainer.require_trainer_flip(P2)
        trainer.end_turn_if_energy_attached_to(ctx.defender)
        trainer.force_coins_through_next_turn(P2, True)
        trainer.add_turn_damage_modifier(TurnDamageModifier(20, P1))
        trainer.add_extra_prize_watcher()
        ctx.lock_plays(P2, lambda card: True)
        await definition('XY11.PokmonRanger_113').effect(trainer)
        self.assertEqual(len(state.play_locks[P2]), 1)
        for name in ('retreat_locks', 'attach_restrictions', 'attack_flip_checks',
                     'trainer_flip_checks', 'attach_ends_turn_checks',
                     'forced_coins_through_turn', 'damage_modifiers', 'extra_prize_watchers'):
            self.assertTrue(getattr(state, name), name)

    async def test_grass_fire_discards_only_opposing_active_grass(self):
        rig, e, ctx = self.ctx('XY5.Slugma_22', 'Grass Fire')
        grass = rig.pull_guid(P2, self.energies[PokemonTypes.GRASS.value])
        rig.attach(grass, ctx.defender)
        others = [card for card in ctx.attached_energies(ctx.defender) if card is not grass]
        await ctx.ability.effect(ctx)
        self.assertIn(grass, ctx.discard_pile(P2))
        for card in others:
            self.assertIn(card, ctx.attached_energies(ctx.defender))

    async def test_mist_purge_special_energy_bonus_and_heal_all_allies(self):
        for special in (False, True):
            rig, e, ctx = self.ctx('XY10.MAltariaEX_69', 'Mist Purge')
            if special:
                energy = self.add(rig, definition('XY1.DoubleColorlessEnergy_130'), P1, 'hand')
                rig.attach(energy, ctx.attacker)
            for p in ctx.my_pokemon_in_play() + ctx.opponent_pokemon_in_play():
                p.set_attribute(AttrID.HP, effective_max_hp(rig.board, p) - 40)
            ctx.deal_damage = AsyncMock(return_value=0)
            await ctx.ability.effect(ctx)
            self.assertEqual(ctx.deal_damage.call_args_list[0].args[0], 130 if special else 100)
            for p in ctx.my_pokemon_in_play():
                self.assertEqual(p.get_attribute(AttrID.HP), effective_max_hp(rig.board, p) - (10 if special else 40))
            for p in ctx.opponent_pokemon_in_play():
                self.assertEqual(p.get_attribute(AttrID.HP), effective_max_hp(rig.board, p) - 40)
