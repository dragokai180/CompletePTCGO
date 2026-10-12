"""Repeated target picks and discarded Energy units follow the card wording."""
import unittest
from unittest.mock import AsyncMock

from spirit.game.attributes import PokemonTypes
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.data_utils import def_for
from spirit.game.session.passives import energy_provided_options
from spirit.tools.effect_smoke import P1, P2
from tests import test_hgss_rules as fixtures


class RepeatedDamageEnergyTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx
    add = fixtures.HgssRulesTests.add

    async def test_electro_rain_counter_energy_gives_two_clicks(self):
        rig, entities, ctx = self.ctx('SM11.AlolanRaichu_57', 'Electro Rain')
        counter = self.add(rig, fixtures.definition('SM4.CounterEnergy_100'),
                           P1, 'deck')
        rig.attach(counter, entities['target'])
        prize = rig.board.find_player_area(P2, 'prizePile').children[0]
        rig.to_area(prize, P2, 'hand')
        self.assertEqual(max(option.count(PokemonTypes.LIGHTNING.value)
                             for option in energy_provided_options(rig.board, counter)), 2)
        basic = next(energy for energy in ctx.attached_energies(ctx.attacker)
                     if energy is not counter and energy_provides_type(
                         energy, PokemonTypes.LIGHTNING.value))

        async def choose(cards, count, **kwargs):
            self.assertIn(counter, cards)
            self.assertEqual(count, len(cards))
            return [counter, basic]

        ctx.choose_cards = AsyncMock(side_effect=choose)
        target = entities['p2_active']
        bench = ctx.opponent_bench()[0]
        rig.session.prompt_damage_counter_placement = AsyncMock(
            return_value={target.entity_id: 2, bench.entity_id: 1})
        ctx.deal_damage = AsyncMock(return_value=30)
        await ctx.ability.effect(ctx)

        args, kwargs = rig.session.prompt_damage_counter_placement.call_args
        self.assertEqual(args[3], 3)
        self.assertEqual(kwargs['amount_per_click'], 30)
        self.assertEqual(ctx.deal_damage.await_count, 3)
        self.assertEqual([call.kwargs['target'] for call in ctx.deal_damage.await_args_list],
                         [target, target, bench])
        self.assertTrue(all(call.kwargs['ignore_weakness'] and
                            call.kwargs['ignore_resistance']
                            for call in ctx.deal_damage.await_args_list))
        self.assertIn(counter, ctx.discard_pile())

    async def test_dragon_burst_counts_cards_even_with_burn_brightly(self):
        for path in ('BW6.RayquazaEX_85', 'BW6.RayquazaEX_123',
                     'PROMO_BW.RayquazaEX_BW47'):
            with self.subTest(path=path):
                rig, entities, ctx = self.ctx(path, 'Dragon Burst')
                self.add(rig, fixtures.definition('PGO.Charizard_10'), P1, 'bench')
                fire = [energy for energy in ctx.attached_energies(ctx.attacker)
                        if energy_provides_type(energy, PokemonTypes.FIRE.value)]
                self.assertTrue(fire)
                extra_fire = self.add(rig, def_for(fire[0].archetype_id), P1, 'deck')
                rig.attach(extra_fire, entities['target'])
                fire.append(extra_fire)
                self.assertTrue(all(max(option.count(PokemonTypes.FIRE.value)
                                        for option in energy_provided_options(
                                            rig.board, energy)) == 2
                                    for energy in fire))
                ctx.choose_cards = AsyncMock(return_value=[fire[0]])
                ctx.deal_damage = AsyncMock(return_value=0)
                await ctx.ability.effect(ctx)
                ctx.deal_damage.assert_awaited_once_with(60 * len(fire))
                self.assertTrue(all(energy in ctx.discard_pile() for energy in fire))

    async def test_energy_card_wording_keeps_one_hit_per_card(self):
        for path, title, energy_type in (
            ('SWSH8.Starmie_53', 'Multishot Star', PokemonTypes.WATER),
            ('XY10.BronzongBREAK_62', 'Metal Rain', PokemonTypes.METAL),
        ):
            with self.subTest(path=path):
                rig, entities, ctx = self.ctx(path, title)
                counter = self.add(rig, fixtures.definition('SM4.CounterEnergy_100'),
                                   P1, 'deck')
                rig.attach(counter, entities['target'])
                prize = rig.board.find_player_area(P2, 'prizePile').children[0]
                rig.to_area(prize, P2, 'hand')
                self.assertEqual(max(option.count(energy_type.value)
                                     for option in energy_provided_options(rig.board, counter)), 2)
                ctx.choose_cards = AsyncMock(return_value=[counter])
                rig.session.prompt_damage_counter_placement = AsyncMock(
                    return_value={entities['p2_active'].entity_id: 1})
                ctx.deal_damage = AsyncMock(return_value=30)
                await ctx.ability.effect(ctx)
                args, kwargs = rig.session.prompt_damage_counter_placement.call_args
                self.assertEqual(args[3], 1)
                self.assertEqual(kwargs['amount_per_click'], 30)
                self.assertEqual(ctx.deal_damage.await_count, 1)
                self.assertIn(counter, ctx.discard_pile())

    async def test_fixed_repeat_attacks_share_the_one_picker(self):
        for path, title, count, damage in (
            ('SV10.Arbolivaex_23', 'Oil Salvo', 6, 20),
            ('CZ.ZeraoraVSTAR_55', 'Lightning Storm Star', 4, 60),
        ):
            with self.subTest(path=path):
                rig, entities, ctx = self.ctx(path, title)
                target = entities['p2_active']
                rig.session.prompt_damage_counter_placement = AsyncMock(
                    return_value={target.entity_id: count})
                ctx.deal_damage = AsyncMock(return_value=damage)
                await ctx.ability.effect(ctx)
                rig.session.prompt_damage_counter_placement.assert_awaited_once()
                args, kwargs = rig.session.prompt_damage_counter_placement.call_args
                self.assertEqual(args[3], count)
                self.assertEqual(kwargs['amount_per_click'], damage)
                self.assertEqual(ctx.deal_damage.await_count, count)

    async def test_hoopa_restricts_repeat_picker_to_gx_ex(self):
        rig, entities, ctx = self.ctx('SM9.HoopaGX_96', 'Devilish Hands-GX')
        gx = self.add(rig, fixtures.definition('SM9.HoopaGX_96'), P2, 'bench')
        rig.session.prompt_damage_counter_placement = AsyncMock(
            return_value={gx.entity_id: 6})
        ctx.deal_damage = AsyncMock(return_value=30)
        await ctx.ability.effect(ctx)
        args, _ = rig.session.prompt_damage_counter_placement.call_args
        self.assertEqual(args[2], [gx])
        self.assertEqual(args[3], 6)
        self.assertEqual(ctx.deal_damage.await_count, 6)

    async def test_discarded_energy_units_scale_dark_burn_and_rock_stomp(self):
        for path, title, kind, expected in (
            ('XY11.Hydreigon_86', 'Dark Burn', PokemonTypes.DARKNESS, 100),
            ('TATM.TeamMagmasAggron_14', 'Rock Stomp', PokemonTypes.FIGHTING, 80),
        ):
            with self.subTest(path=path):
                rig, entities, ctx = self.ctx(path, title)
                counter = self.add(rig, fixtures.definition('SM4.CounterEnergy_100'),
                                   P1, 'deck')
                rig.attach(counter, entities['target'])
                prize = rig.board.find_player_area(P2, 'prizePile').children[0]
                rig.to_area(prize, P2, 'hand')
                self.assertEqual(max(option.count(kind.value)
                                     for option in energy_provided_options(rig.board, counter)), 2)
                ctx.choose_cards = AsyncMock(return_value=[counter])
                ctx.deal_damage = AsyncMock(return_value=expected)
                await ctx.ability.effect(ctx)
                ctx.deal_damage.assert_awaited_once_with(expected)
                self.assertIn(counter, ctx.discard_pile())

    async def test_top_burner_mills_one_card_per_fire_energy_unit(self):
        rig, entities, ctx = self.ctx('SM9.Moltres_19', 'Top Burner')
        self.add(rig, fixtures.definition('PGO.Charizard_10'), P1, 'bench')
        fire = [energy for energy in ctx.attached_energies(ctx.attacker)
                if energy_provides_type(energy, PokemonTypes.FIRE.value)]
        before = len(ctx.deck(P2))
        await ctx.ability.effect(ctx)
        self.assertEqual(len(ctx.deck(P2)), before - 2 * len(fire))
        self.assertTrue(all(energy in ctx.discard_pile() for energy in fire))

    async def test_rapid_blaster_counts_metal_energy_without_card_wording(self):
        rig, entities, ctx = self.ctx('XY10.GenesectEX_120', 'Rapid Blaster')
        metal = next(energy for energy in ctx.attached_energies(ctx.attacker)
                     if energy_provides_type(energy, PokemonTypes.METAL.value))
        ctx.choose_cards = AsyncMock(return_value=[metal])
        ctx.deal_damage = AsyncMock(return_value=120)
        await ctx.ability.effect(ctx)
        ctx.deal_damage.assert_awaited_once_with(120, ignore_weakness=False,
                                                  ignore_resistance=False,
                                                  ignore_target_effects=False)


if __name__ == '__main__':
    unittest.main()
