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
