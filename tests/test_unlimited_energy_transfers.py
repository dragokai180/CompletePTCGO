"""Unlimited Energy movers keep their type and destination rules in one use."""
import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures
from spirit.game.attributes import PokemonTypes
from spirit.game.data_utils import def_for
from spirit.tools.effect_smoke import P1


class UnlimitedEnergyTransferTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx
    add = fixtures.HgssRulesTests.add

    def clear_energy(self, rig, ctx):
        for pokemon in ctx.my_pokemon_in_play():
            for energy in list(ctx.attached_energies(pokemon)):
                rig.to_area(energy, P1, "discard")

    def attach_basic(self, rig, pokemon, kind):
        energy = self.add(rig, def_for(self.energies[kind.value]), P1, "hand")
        rig.attach(energy, pokemon)
        return energy

    async def move_two(self, ctx, destination):
        offered = []

        async def choose(cards, *_args, **_kwargs):
            offered.append(list(cards))
            return [cards[0]] if len(offered) <= 2 else []

        ctx.choose_cards = AsyncMock(side_effect=choose)
        ctx.choose_pokemon = AsyncMock(return_value=destination)
        await ctx.ability.effect(ctx)
        return offered

    async def test_both_metal_transfer_printings_move_multiple_matching_cards(self):
        for path in ("SWSH5.Bronzong_102", "SWSH6.Bronzong_223"):
            with self.subTest(card=path):
                rig, _, ctx = self.ctx(path, "Metal Transfer")
                self.clear_energy(rig, ctx)
                destination = ctx.my_bench()[0]
                metal = self.attach_basic(rig, ctx.source, PokemonTypes.METAL)
                rainbow = self.add(rig, fixtures.definition(
                    "SM1.RainbowEnergy_137"), P1, "hand")
                rig.attach(rainbow, ctx.source)
                water = self.attach_basic(rig, ctx.source, PokemonTypes.WATER)
                offered = await self.move_two(ctx, destination)
                self.assertTrue(all(water not in pool for pool in offered))
                self.assertEqual({metal, rainbow}.intersection(
                    ctx.attached_energies(destination)), {metal, rainbow})

    async def test_shadow_connection_uses_the_same_continuous_flow(self):
        rig, _, ctx = self.ctx("SM11.WeavileGX_132", "Shadow Connection")
        self.clear_energy(rig, ctx)
        destination = ctx.my_bench()[0]
        darkness = [self.attach_basic(rig, ctx.source, PokemonTypes.DARKNESS)
                    for _ in range(2)]
        rainbow = self.add(rig, fixtures.definition(
            "SM1.RainbowEnergy_137"), P1, "hand")
        rig.attach(rainbow, ctx.source)
        offered = await self.move_two(ctx, destination)
        self.assertTrue(all(rainbow not in pool for pool in offered))
        self.assertTrue(all(card in ctx.attached_energies(destination)
                            for card in darkness))

    async def test_special_transfer_moves_multiple_special_cards_only(self):
        rig, _, ctx = self.ctx("SWSH9.Dusknoir_62", "Special Transfer")
        self.clear_energy(rig, ctx)
        destination = ctx.my_bench()[0]
        specials = []
        for _ in range(2):
            energy = self.add(rig, fixtures.definition(
                "SM1.RainbowEnergy_137"), P1, "hand")
            rig.attach(energy, ctx.source)
            specials.append(energy)
        basic = self.attach_basic(rig, ctx.source, PokemonTypes.METAL)
        offered = await self.move_two(ctx, destination)
        self.assertTrue(all(basic not in pool for pool in offered))
        self.assertTrue(all(card in ctx.attached_energies(destination)
                            for card in specials))

    async def test_irresistible_force_moves_only_from_other_pokemon(self):
        rig, _, ctx = self.ctx("SWSH12.HisuianArcanineV_90",
                               "Irresistible Force")
        self.clear_energy(rig, ctx)
        donor = ctx.my_bench()[0]
        fighting = [self.attach_basic(rig, donor, PokemonTypes.FIGHTING)
                    for _ in range(2)]
        metal = self.attach_basic(rig, donor, PokemonTypes.METAL)
        offered = await self.move_two(ctx, ctx.source)
        self.assertTrue(all(metal not in pool for pool in offered))
        self.assertTrue(all(card in ctx.attached_energies(ctx.source)
                            for card in fighting))

    async def test_solar_transfer_repeats_but_only_for_basic_grass(self):
        rig, _, ctx = self.ctx("ME1.MegaVenusaurex_3", "Solar Transfer")
        self.clear_energy(rig, ctx)
        destination = ctx.my_bench()[0]
        grass = [self.attach_basic(rig, ctx.source, PokemonTypes.GRASS)
                 for _ in range(2)]
        rainbow = self.add(rig, fixtures.definition(
            "SM1.RainbowEnergy_137"), P1, "hand")
        rig.attach(rainbow, ctx.source)
        offered = await self.move_two(ctx, destination)
        self.assertTrue(all(rainbow not in pool for pool in offered))
        self.assertTrue(all(card in ctx.attached_energies(destination)
                            for card in grass))

    async def test_hgss_repeated_powers_keep_once_per_turn_exception(self):
        cases = (("HGSS2.Blastoise_13", "Wash Out", None),
                 ("HGSS3.Raichu_83", "Voltage Increase", None),
                 ("HGSS1.Meganium_109", "Leaf Trans", None),
                 ("HGSS2.Mismagius_5", "Magical Trans", 1))
        for path, title, expected_limit in cases:
            with self.subTest(card=path):
                _, _, ctx = self.ctx(path, title)
                ctx.move_energy_freely = AsyncMock(return_value=[])
                await ctx.ability.effect(ctx)
                self.assertEqual(ctx.move_energy_freely.call_args.kwargs[
                    "max_count"], expected_limit)

    async def test_attached_to_one_transfer_abilities_move_multiple_typed_energies(self):
        cases = (
            ("BW1.Klinklang_76", "Shift Gear", PokemonTypes.METAL),
            ("BW6.Hydreigon_97", "Dark Trance", PokemonTypes.DARKNESS),
            ("BW11.Hydreigon_99", "Dark Trance", PokemonTypes.DARKNESS),
            ("XY1.Aromatisse_93", "Fairy Transfer", PokemonTypes.FAIRY),
        )
        for path, title, energy_type in cases:
            with self.subTest(card=path):
                rig, _, ctx = self.ctx(path, title)
                self.clear_energy(rig, ctx)
                destination = ctx.my_bench()[0]
                matching = [self.attach_basic(rig, ctx.source, energy_type)
                            for _ in range(2)]
                other = self.attach_basic(rig, ctx.source, PokemonTypes.WATER)
                offered = await self.move_two(ctx, destination)
                self.assertTrue(all(other not in pool for pool in offered))
                self.assertTrue(all(energy in ctx.attached_energies(destination)
                                    for energy in matching))

    async def test_hyper_transfer_moves_multiple_basic_energies(self):
        rig, _, ctx = self.ctx("XY9.GolduckBREAK_18", "Hyper Transfer")
        self.clear_energy(rig, ctx)
        destination = ctx.my_bench()[0]
        basics = [self.attach_basic(rig, ctx.source, PokemonTypes.WATER)
                  for _ in range(2)]
        special = self.add(rig, fixtures.definition(
            "SM1.RainbowEnergy_137"), P1, "hand")
        rig.attach(special, ctx.source)
        offered = await self.move_two(ctx, destination)
        self.assertTrue(all(special not in pool for pool in offered))
        self.assertTrue(all(energy in ctx.attached_energies(destination)
                            for energy in basics))

    async def test_plasma_transfer_moves_multiple_plasma_energy_cards(self):
        for path in ("BW10.PorygonZ_74", "PROMO_BW.PorygonZ_BW84"):
            with self.subTest(card=path):
                rig, _, ctx = self.ctx(path, "Plasma Transfer")
                self.clear_energy(rig, ctx)
                destination = ctx.my_bench()[0]
                plasma = []
                for _ in range(2):
                    energy = self.add(rig, fixtures.definition(
                        "BW10.PlasmaEnergy_91"), P1, "hand")
                    rig.attach(energy, ctx.source)
                    plasma.append(energy)
                basic = self.attach_basic(rig, ctx.source, PokemonTypes.METAL)
                offered = await self.move_two(ctx, destination)
                self.assertTrue(all(basic not in pool for pool in offered))
                self.assertTrue(all(energy in ctx.attached_energies(destination)
                                    for energy in plasma))

    async def test_other_generic_repeated_movers_keep_their_routes(self):
        cases = (
            ("SM1.LunalaGX_66", "Psychic Transfer", PokemonTypes.PSYCHIC,
             False, False),
            ("XY5.Eelektross_65", "Energy Connect", PokemonTypes.WATER,
             True, True),
            ("SV1.Armarouge_41", "Fire Off", PokemonTypes.FIRE,
             True, True),
            ("ME2PT5.Azumarillex_84", "Bubble Gathering", PokemonTypes.WATER,
             True, False),
        )
        for path, title, energy_type, bench_source, active_target in cases:
            with self.subTest(card=path):
                rig, _, ctx = self.ctx(path, title)
                self.clear_energy(rig, ctx)
                donor = ctx.my_bench()[0] if bench_source else ctx.source
                destination = ctx.my_active() if active_target else (
                    ctx.source if bench_source else ctx.my_bench()[0])
                cards = [self.attach_basic(rig, donor, energy_type)
                         for _ in range(2)]
                await self.move_two(ctx, destination)
                self.assertTrue(all(card in ctx.attached_energies(destination)
                                    for card in cards))
