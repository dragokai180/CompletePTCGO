"""Regressions for counter targets, zone-dependent Energy types and Ranger."""
import unittest
from unittest.mock import AsyncMock
from tests import test_hgss_rules as fixtures
from tests.test_hgss_rules import definition
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.session.effects import EffectContext
from spirit.game.session.legal_actions import trainer_condition_met, EffectExpiry
from spirit.game.session.passives import energy_provided_options, Passive
from spirit.tools.effect_smoke import P1, P2


class CounterEnergyAuditTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx
    add = fixtures.HgssRulesTests.add

    async def test_giant_water_shuriken_all_six_on_one_pokemon(self):
        rig, e, ctx = self.ctx('XY9.GreninjaBREAK_41', 'Giant Water Shuriken')
        water = rig.pull_guid(P1, self.energies[PokemonTypes.WATER.value])
        rig.to_area(water, P1, 'hand')
        splash = self.add(rig, definition('XY9.SplashEnergy_113'), P1, 'hand')
        target = ctx.opponent_bench()[0]
        before = {p.entity_id: p.get_attribute(AttrID.HP) for p in ctx.opponent_pokemon_in_play()}
        ctx.choose_cards = AsyncMock(return_value=[water])
        ctx.choose_pokemon = AsyncMock(return_value=target)
        ctx.place_damage_counters = AsyncMock()
        self.assertTrue(ctx.ability.condition(rig.board, P1, ctx.source))
        await ctx.ability.effect(ctx)
        self.assertIn(water, ctx.discard_pile())
        self.assertIn(splash, ctx.hand())
        self.assertNotIn(splash, ctx.choose_cards.await_args.args[0])
        ctx.place_damage_counters.assert_not_awaited()
        for p in ctx.opponent_pokemon_in_play():
            self.assertEqual(p.get_attribute(AttrID.HP),
                             before[p.entity_id] - (60 if p is target else 0))

    async def test_splash_alone_does_not_enable_shuriken(self):
        rig, e, ctx = self.ctx('XY9.GreninjaBREAK_41', 'Giant Water Shuriken')
        for card in list(ctx.hand()):
            rig.to_area(card, P1, 'deck')
        self.add(rig, definition('XY9.SplashEnergy_113'), P1, 'hand')
        self.assertFalse(ctx.ability.condition(rig.board, P1, ctx.source))

    async def test_restricted_energy_has_no_type_outside_play(self):
        cases = [
            ('XY3.HerbalEnergy_103', PokemonTypes.GRASS),
            ('XY3.StrongEnergy_104', PokemonTypes.FIGHTING),
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
                energy = self.add(rig, definition(path), P1, 'hand')
                for zone in ('hand', 'deck', 'discard'):
                    rig.to_area(energy, P1, zone)
                    self.assertFalse(energy_provides_type(energy, kind.value))
                    self.assertEqual(energy_provided_options(rig.board, energy), [])
                ctx.attacker.set_attribute(AttrID.POKEMON_TYPES, [kind.value])
                rig.attach(energy, ctx.attacker)
                self.assertTrue(energy_provides_type(energy, kind.value))
                ctx.attacker.set_attribute(AttrID.POKEMON_TYPES, [PokemonTypes.COLORLESS.value])
                self.assertFalse(energy_provides_type(energy, kind.value))

    async def test_prism_rainbow_blend_unit_outside_colorless_inside_typed(self):
        for path in ('BW4.PrismEnergy_93', 'HGSS1.RainbowEnergy_104', 'XY1.RainbowEnergy_131',
                     'BW6.BlendEnergyGrassFirePsychicDarkness_117',
                     'SM5.UnitEnergyGrassFireWater_137'):
            with self.subTest(path=path):
                rig, e, ctx = self.ctx('BW1.Snivy_1', 'Tackle')
                energy = self.add(rig, definition(path), P1, 'hand')
                self.assertFalse(energy_provides_type(energy, PokemonTypes.GRASS.value))
                self.assertTrue(energy_provides_type(energy, PokemonTypes.COLORLESS.value))
                self.assertEqual(energy_provided_options(rig.board, energy), [[PokemonTypes.COLORLESS.value]])
                rig.attach(energy, ctx.attacker)
                self.assertTrue(energy_provides_type(energy, PokemonTypes.GRASS.value))
                if 'Prism' in path:
                    ctx.attacker.set_attribute(AttrID.STAGE, PokemonStage.STAGE1.value)
                    self.assertFalse(energy_provides_type(energy, PokemonTypes.GRASS.value))
                if 'Unit' in path:
                    self.assertFalse(energy_provides_type(energy, PokemonTypes.PSYCHIC.value))

    async def test_beast_only_supplies_all_types_to_ultra_beast(self):
        for path, title, expected in (
            ('BW1.Snivy_1', 'Tackle', False),
            ('Promo_SM.Blacephalon_221', 'Fireworks Bomb', True),
        ):
            rig, e, ctx = self.ctx(path, title)
            energy = self.add(rig, definition('SM6.BeastEnergy_117'), P1, 'hand')
            self.assertFalse(energy_provides_type(energy, PokemonTypes.WATER.value))
            rig.attach(energy, ctx.attacker)
            self.assertEqual(energy_provides_type(energy, PokemonTypes.WATER.value), expected)

    async def test_suppressed_energy_does_not_keep_typed_options(self):
        class Suppression(Passive):
            def suppresses_special_energy(self, energy, carrier):
                return True
        rig, e, ctx = self.ctx('BW1.Snivy_1', 'Tackle')
        energy = self.add(rig, definition('SM5.UnitEnergyGrassFireWater_137'), P1, 'hand')
        rig.attach(energy, ctx.attacker)
        self.assertTrue(energy_provides_type(energy, PokemonTypes.WATER.value))
        ctx.add_temporary_passive(ctx.defender, Suppression())
        self.assertFalse(energy_provides_type(energy, PokemonTypes.WATER.value))
        self.assertTrue(energy_provides_type(energy, PokemonTypes.COLORLESS.value))

    async def test_disabled_dusknoir_does_not_reduce_double_energy_to_one(self):
        rig, e, ctx = self.ctx('BW1.Snivy_1', 'Tackle')
        energy = self.add(rig, definition('XY1.DoubleColorlessEnergy_130'), P1, 'hand')
        rig.attach(energy, ctx.attacker)
        colorless = PokemonTypes.COLORLESS.value
        self.assertEqual(energy_provided_options(rig.board, energy), [[colorless, colorless]])
        self.add(rig, definition('SWSH4.Dusknoir_71'), P2, 'bench')
        self.assertEqual(energy_provided_options(rig.board, energy), [[colorless]])
        state = rig.session.turn_state
        state.abilities_disabled_through_turn = state.turn_number + 1
        self.assertEqual(energy_provided_options(rig.board, energy), [[colorless, colorless]])

    async def test_single_target_counter_attacks_do_not_distribute(self):
        for path, title, counters in (
            ('BW6.Drifblim_51', 'Plentiful Placement', 4),
            ('HGSS4.Haunter_35', 'Sneaky Placement', 2),
        ):
            rig, e, ctx = self.ctx(path, title)
            target = ctx.opponent_bench()[0]
            before = target.get_attribute(AttrID.HP)
            ctx.choose_pokemon = AsyncMock(return_value=target)
            ctx.place_damage_counters = AsyncMock()
            await ctx.ability.effect(ctx)
            self.assertEqual(target.get_attribute(AttrID.HP), before - counters * 10)
            ctx.place_damage_counters.assert_not_awaited()

    async def test_fireworks_distribution_uses_prize_count(self):
        for prizes, expected in ((3, 12), (4, 4)):
            rig, e, ctx = self.ctx('Promo_SM.Blacephalon_221', 'Fireworks Bomb')
            area = rig.board.find_player_area(P2, 'prizePile')
            while len(area.children) > prizes:
                rig.to_area(area.children[0], P2, 'hand')
            ctx.place_damage_counters = AsyncMock()
            await ctx.ability.effect(ctx)
            self.assertEqual(ctx.place_damage_counters.await_args.args[0], expected)

    async def test_variable_spread_counts_pokemon(self):
        for path, title, mode in (
            ('Promo_SM.Oricorio_19', 'Supernatural Dance', 'discard'),
            ('SM7.Banette_65', 'Enemy Show', 'field'),
            ('SM9.Jynx_68', 'Mysterious Dance', 'bench'),
        ):
            rig, e, ctx = self.ctx(path, title)
            self.add(rig, definition('BW1.Snivy_1'), P2, 'discard')
            self.add(rig, definition('BW1.Snivy_1'), P2, 'discard')
            from spirit.game.session.effects import is_pokemon_card
            expected = (sum(is_pokemon_card(c) for c in ctx.discard_pile(P2)) if mode == 'discard'
                        else len(ctx.opponent_bench()) if mode == 'bench'
                        else len(ctx.opponent_pokemon_in_play()))
            ctx.place_damage_counters = AsyncMock()
            await ctx.ability.effect(ctx)
            self.assertEqual(ctx.place_damage_counters.await_args.args[0], expected)

    async def test_rebrew_single_target_then_recovers_all_basic_grass(self):
        rig, e, ctx = self.ctx('SV06.Sinistchaex_23', 'Re-Brew')
        for c in list(ctx.discard_pile()):
            rig.to_area(c, P1, 'deck')
        cards = []
        for _ in range(2):
            card = rig.pull_guid(P1, self.energies[PokemonTypes.GRASS.value])
            rig.to_area(card, P1, 'discard')
            cards.append(card)
        target = ctx.opponent_bench()[0]
        before = target.get_attribute(AttrID.HP)
        ctx.choose_pokemon = AsyncMock(return_value=target)
        ctx.place_damage_counters = AsyncMock()
        await ctx.ability.effect(ctx)
        self.assertEqual(target.get_attribute(AttrID.HP), before - 40)
        self.assertTrue(all(card in ctx.deck() for card in cards))
        ctx.place_damage_counters.assert_not_awaited()

    async def test_assassins_magic_requires_condition_and_only_bench(self):
        for condition in ([], ['Poisoned']):
            rig, e, ctx = self.ctx('ME2PT5.Mismagius_86', "Assassin's Magic")
            ctx.defender.set_attribute(AttrID.SPECIAL_CONDITIONS, condition)
            target = ctx.opponent_bench()[0]
            ctx.choose_pokemon = AsyncMock(return_value=target)
            ctx.deal_damage = AsyncMock(return_value=0)
            await ctx.ability.effect(ctx)
            counters = [call for call in ctx.deal_damage.await_args_list if call.kwargs.get('as_counters')]
            self.assertEqual(len(counters), bool(condition))
            if condition:
                self.assertNotIn(ctx.defender, ctx.choose_pokemon.await_args.args[0])
                self.assertEqual(counters[0].args[0], 60)

    async def test_final_hour_uses_one_target_not_distribution(self):
        rig, e, ctx = self.ctx('SM6.Honedge_46', 'Final Hour')
        ctx.ko_from_attack = True
        ctx.was_active_at_ko = True
        ctx.ko_attacker = ctx.defender
        target = ctx.opponent_bench()[0]
        before = target.get_attribute(AttrID.HP)
        ctx.choose_pokemon = AsyncMock(return_value=target)
        ctx.place_damage_counters = AsyncMock()
        await ctx.ability.passive.on_knocked_out(ctx, ctx.source, ctx.source)
        self.assertEqual(target.get_attribute(AttrID.HP), before - 30)
        ctx.place_damage_counters.assert_not_awaited()

    async def test_shocking_light_only_targets_pokemon_ex(self):
        rig, e, ctx = self.ctx('XY11.Ampharos_40', 'Shocking Light')
        self.assertFalse(ctx.ability.condition(rig.board, P1, ctx.source))
        target = self.add(rig, definition('BW4.MewtwoEX_54'), P2, 'bench')
        self.assertTrue(ctx.ability.condition(rig.board, P1, ctx.source))
        before = target.get_attribute(AttrID.HP)
        ctx.choose_cards = AsyncMock(return_value=[target])
        await ctx.ability.effect(ctx)
        self.assertEqual(ctx.choose_cards.await_args.args[0], [target])
        self.assertEqual(target.get_attribute(AttrID.HP), before - 30)

    async def test_ranger_requires_live_removable_attack_effect(self):
        for path in ('XY11.PokmonRanger_104', 'XY11.PokmonRanger_113'):
            rig, e, ctx = self.ctx('BW1.Snivy_1', 'Tackle')
            ranger = self.add(rig, definition(path), P1, 'hand')
            legal = lambda: trainer_condition_met(definition(path).condition, rig.board, P1, ranger)
            self.assertFalse(legal())
            ctx.defender.set_attribute(AttrID.SPECIAL_CONDITIONS, ['Poisoned'])
            ctx.defender.set_attribute(AttrID.HP, 20)
            rig.session.turn_state.gx_used.add(P1)
            self.assertFalse(legal())
            ability_ctx = EffectContext(rig.session, P1, ctx.attacker, None)
            ability_ctx.lock_retreat(ctx.defender)
            self.assertFalse(legal())
            ctx.lock_retreat(ctx.defender)
            self.assertTrue(legal())
            await definition(path).effect(ability_ctx)
            self.assertFalse(legal())

    async def test_ranger_expired_locks_and_temporary_passives(self):
        rig, e, ctx = self.ctx('BW1.Snivy_1', 'Tackle')
        card = self.add(rig, definition('XY11.PokmonRanger_104'), P1, 'hand')
        legal = lambda: trainer_condition_met(definition('XY11.PokmonRanger_104').condition, rig.board, P1, card)
        state = rig.session.turn_state
        state.retreat_locks[ctx.defender.entity_id] = EffectExpiry(state.turn_number - 1, True)
        self.assertFalse(legal())
        ctx.add_temporary_player_passive(P2, Passive(), state.turn_number + 1)
        self.assertTrue(legal())
        await definition('XY11.PokmonRanger_104').effect(EffectContext(rig.session, P1, card, None))
        self.assertFalse(legal())


if __name__ == '__main__':
    unittest.main()
