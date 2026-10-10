"""Bench attacks must only offer targets named by their printed restrictions."""
import unittest
from unittest.mock import AsyncMock

from spirit.game.card_effects.bw_era import _bench_rulebox_targets
from spirit.game.attributes import AttrID, PokemonTypes
from tests import test_hgss_rules as fixtures
from spirit.tools.effect_smoke import P2


class BenchDamageTargetRestrictionTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx
    add = fixtures.HgssRulesTests.add

    def bench_classes(self, rig):
        paths = {
            "GX": "Promo_SM.UmbreonDarkraiGX_241",
            "EX": "XY5.PrimalKyogreEX_55",
            "ex": "SV10.Arbolivaex_23",
            "V": "CZ.DeoxysVSTAR_206",
        }
        return {label: self.add(rig, fixtures.definition(path), P2, "bench")
                for label, path in paths.items()}

    async def test_named_rulebox_classes_are_the_only_bench_damage_choices(self):
        cases = (
            ("Promo_SM.UmbreonDarkraiGX_241", "Black Lance", {"GX", "EX"}),
            ("SM10.HonchkrowGX_109", "Feather Storm", {"GX", "EX"}),
            ("XY8.Yveltal_94", "Pitch-Black Spear", {"EX"}),
            ("SV05.Shaymin_13", "Pinpoint Dive", {"ex", "V"}),
        )
        for path, title, allowed in cases:
            with self.subTest(attack=title):
                rig, _, ctx = self.ctx(path, title)
                classes = self.bench_classes(rig)
                choices = []

                async def choose(pool, *_args, **_kwargs):
                    choices.append(list(pool))
                    return list(pool[:1])

                ctx.choose_cards = AsyncMock(side_effect=choose)
                ctx.deal_damage = AsyncMock(return_value=0)
                await ctx.ability.effect(ctx)
                self.assertTrue(choices)
                self.assertEqual(set(choices[0]), {classes[label] for label in allowed})
                damaged = [call.kwargs.get("target")
                           for call in ctx.deal_damage.call_args_list
                           if call.kwargs.get("target") is not None]
                self.assertEqual(damaged, choices[0][:1])

    def test_spread_rulebox_wording_filters_exact_ex_generation(self):
        rig, _ = self.rig("XY5.PrimalKyogreEX_55")
        classes = self.bench_classes(rig)
        pool = list(rig.board.pokemon_in_play(P2))[1:]
        self.assertEqual(
            _bench_rulebox_targets(pool, "-ex. (don't apply weakness)"),
            [classes["EX"]],
        )

    async def test_black_lance_keeps_active_hit_with_no_eligible_bench(self):
        _, _, ctx = self.ctx("Promo_SM.UmbreonDarkraiGX_241", "Black Lance")
        ctx.choose_cards = AsyncMock(return_value=[])
        ctx.deal_damage = AsyncMock(return_value=0)
        await ctx.ability.effect(ctx)
        ctx.choose_cards.assert_not_awaited()
        ctx.deal_damage.assert_awaited_once()
        self.assertEqual(ctx.deal_damage.call_args.args[0], 150)

    async def test_same_type_spread_skips_other_benched_types(self):
        rig, _, ctx = self.ctx("SM3.Bruxish_38", "Synchronoise")
        bench = ctx.opponent_bench()
        ctx.defender.set_attribute(AttrID.POKEMON_TYPES, [PokemonTypes.FIRE.value])
        bench[0].set_attribute(AttrID.POKEMON_TYPES, [PokemonTypes.FIRE.value])
        bench[1].set_attribute(AttrID.POKEMON_TYPES, [PokemonTypes.WATER.value])
        ctx.deal_damage = AsyncMock(return_value=0)
        await ctx.ability.effect(ctx)
        targets = [call.kwargs.get("target") for call in ctx.deal_damage.call_args_list]
        self.assertIn(bench[0], targets)
        self.assertNotIn(bench[1], targets)

    async def test_repeated_rulebox_selection_excludes_other_pokemon(self):
        rig, _, ctx = self.ctx("SM9.HoopaGX_96", "Devilish Hands-GX")
        classes = self.bench_classes(rig)
        offered = []

        async def choose(pool, *_args, **_kwargs):
            offered.append(list(pool))
            return pool[0]

        ctx.choose_pokemon = AsyncMock(side_effect=choose)
        ctx.deal_damage = AsyncMock(return_value=0)
        await ctx.ability.effect(ctx)
        self.assertEqual(len(offered), 6)
        for pool in offered:
            self.assertEqual(set(pool), {classes["GX"], classes["EX"]})
