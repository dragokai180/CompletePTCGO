"""Damage formulas must count the side and Pokémon described by the card."""

import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures
from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.card_effects.bw_era import _formula_damage, _norm
from spirit.tools.effect_smoke import P1, P2


class InPlayDamageCountTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    ctx = fixtures.HgssRulesTests.ctx
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    def formula(self, ctx):
        return _formula_damage(ctx, _norm(ctx.ability.game_text))

    def test_scopes_and_qualifiers(self):
        cases = (
            ('ME2.Alcremie_44', 'Sweet Circle', 80),
            ('HGSS1.Jumpluff_6', 'Mass Attack', 70),
            ('ZSV10PT5.Reuniclus_39', 'Evo-Lariat', 120),
            ('SM7.Ludicolo_38', 'Circular Steps', 130),
            ('SV08.Passimian_111', 'Coordinated Throwing', 80),
            ('ME2PT5.ErikasVictreebel_6', 'Flower Garden Rondo', 80),
            ('BW5.Zoroark_71', 'Brutal Bash', 40),
            ('BW3.Reuniclus_52', 'Net Force', 80),
            ('SV1.Maushold_161', 'Family Attack', 140),
            ('ME4.Beedrillex_3', 'Rumbling Bees', 220),
            ('SV07.Drifblim_61', 'Everyone Explode Now', 100),
            ('Promo_SM.NaganadelGX_125', 'Beast Raid', 40),
            ('HGSS3.Umbreon_86', 'Evoblast', 70),
            ('Promo_XY.EmpoleonBREAK_134', "Emperor's Command", 90),
        )
        for path, title, expected in cases:
            with self.subTest(path=path):
                _, _, ctx = self.ctx(path, title)
                self.assertEqual(self.formula(ctx), expected)

    def test_type_and_ability_filters(self):
        _, _, ctx = self.ctx('SV05.Torterraex_12', 'Forest March')
        for pokemon in ctx.my_bench()[1:]:
            pokemon.set_attribute(AttrID.POKEMON_TYPES,
                                  [PokemonTypes.WATER.value])
        for pokemon in ctx.opponent_pokemon_in_play():
            pokemon.set_attribute(AttrID.POKEMON_TYPES,
                                  [PokemonTypes.GRASS.value])
        self.assertEqual(self.formula(ctx), 60)

        rig, _, ctx = self.ctx('SV3.Scizor_141', 'Punishing Scissors')
        self.add(rig, fixtures.definition('SV3.Pidgeotex_164'), P2, 'bench')
        self.assertEqual(self.formula(ctx), 60)

    def test_named_pokemon_on_both_sides(self):
        rig, _, ctx = self.ctx('SV10.TeamRocketsWeezing_126',
                               'Explode Together Now')
        self.add(rig, fixtures.definition('SV10.TeamRocketsKoffing_125'),
                 P2, 'bench')
        self.assertEqual(self.formula(ctx), 120)

    def test_evolution_dragon_requires_both_qualifiers(self):
        rig, _, ctx = self.ctx('SM7.Latios_108', 'Dragon Fleet')
        shelgon = fixtures.definition('SM7.Shelgon_105')
        self.add(rig, shelgon, P1, 'bench')
        self.add(rig, shelgon, P2, 'bench')
        self.assertEqual(self.formula(ctx), 50)

    def test_rule_box_categories_keep_ex_and_old_ex_distinct(self):
        rig, _, ctx = self.ctx('SV065.Zoroark_32', 'Illusory Hijacking')
        for path in ('SV1.Koraidonex_125', 'SWSH1.ZacianV_138',
                     'SM1.LaprasGX_35'):
            self.add(rig, fixtures.definition(path), P2, 'bench')
        self.assertEqual(self.formula(ctx), 120)

        rig, _, ctx = self.ctx('SM12.MegaLopunnyJigglypuffGX_165',
                               'Jumping Balloon')
        for path in ('SM1.LaprasGX_35', 'XY1.VenusaurEX_1',
                     'SV1.Koraidonex_125'):
            self.add(rig, fixtures.definition(path), P2, 'bench')
        self.assertEqual(self.formula(ctx), 180)

    async def test_distinct_bench_types_include_dual_types_once_each(self):
        for path, title, expected in (
            ('XY8.Xerneas_107', 'Rainbow Force', 100),
            ('SV3.Toxtricity_72', 'Loud Mix', 140),
            ('SM5.Eevee_105', 'Palette of Friends', 30),
        ):
            with self.subTest(path=path):
                _, _, ctx = self.ctx(path, title)
                for pokemon, types in zip(ctx.my_bench(), (
                        [PokemonTypes.GRASS.value],
                        [PokemonTypes.GRASS.value],
                        [PokemonTypes.WATER.value, PokemonTypes.METAL.value],
                )):
                    pokemon.set_attribute(AttrID.POKEMON_TYPES, types)
                self.assertEqual(self.formula(ctx), expected)
                ctx.deal_damage = AsyncMock(return_value=0)
                await ctx.ability.effect(ctx)
                self.assertEqual(ctx.deal_damage.call_args.args[0], expected)

        _, _, ctx = self.ctx('Promo_XY.Magearna_165', 'Prismatic Wave')
        for pokemon, kind in zip(ctx.opponent_bench(), (
                PokemonTypes.GRASS, PokemonTypes.GRASS)):
            pokemon.set_attribute(AttrID.POKEMON_TYPES, [kind.value])
        self.assertEqual(self.formula(ctx), 20)

        rig, _, ctx = self.ctx('XY8.Xerneas_107', 'Rainbow Force')
        for pokemon in list(ctx.my_bench()):
            rig.to_area(pokemon, P1, 'hand')
        self.assertEqual(self.formula(ctx), 10)

    async def test_actual_attack_uses_scoped_count(self):
        _, _, ctx = self.ctx('ME2.Alcremie_44', 'Sweet Circle')
        ctx.deal_damage = AsyncMock(return_value=0)
        await ctx.ability.effect(ctx)
        self.assertEqual(ctx.deal_damage.call_args.args[0], 80)


if __name__ == '__main__':
    unittest.main()
