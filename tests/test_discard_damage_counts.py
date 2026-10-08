"""Damage formulas count the specified cards in the specified discard pile."""
import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures
from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.card_effects.bw_era import _formula_damage, _norm
from spirit.game.data_utils import def_for
from spirit.tools.effect_smoke import P1, P2


class DiscardDamageCountTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx
    add = fixtures.HgssRulesTests.add

    def clear_discard(self, rig, player_id):
        pile = rig.board.find_player_area(player_id, 'discard')
        for card in list(pile.children):
            rig.to_area(card, player_id, 'deck')

    def add_discard(self, rig, player_id, path):
        return self.add(rig, fixtures.definition(path), player_id, 'discard')

    async def test_vengeance_fletching_counts_all_ancient_card_types(self):
        rig, _, ctx = self.ctx('SV05.RoaringMoon_109', 'Vengeance Fletching')
        self.clear_discard(rig, P1)
        for path in ('SV05.RoaringMoon_109',
                     'SV05.ExplorersGuidance_147',
                     'SV05.AncientBoosterEnergyCapsule_140',
                     'SV05.IronHands_61',
                     'SV05.FutureBoosterEnergyCapsule_149',
                     'SWSH12.Serena_164'):
            self.add_discard(rig, P1, path)
        ctx.deal_damage = AsyncMock(return_value=0)

        await ctx.ability.effect(ctx)

        self.assertEqual(ctx.deal_damage.await_args.args[0], 100)

    async def test_discard_filters_and_caps(self):
        cases = (
            # Source, attack, counted pile, cards in that pile, expected damage.
            ('SM2.Garbodor_51', 'Trashalanche', P2,
             ('SV065.EarthenVessel_96',
              'SV05.AncientBoosterEnergyCapsule_140'), 20),
            ('XY12.Raticate_67', 'Shadowy Bite', P2,
             ('SWSH9.DoubleTurboEnergy_151',), 60),
            ('SV1.Houndstone_106', 'Last Respects', P1,
             ('SV1.Greavard_104', 'SV05.RoaringMoon_109'), 90),
            ('SWSH12.Braixen_26', 'Flare Parade', P1,
             ('SWSH12.Serena_164', 'SV05.ExplorersGuidance_147'), 60),
            ('SWSH3.Polteageist_83', 'Mad Party', P1,
             ('SWSH3.Bunnelby_150', 'SV05.RoaringMoon_109'), 20),
            ('SV4.Orbeetle_12', 'Satellite Beam', P2,
             ('SWSH9.DoubleTurboEnergy_151',), 30),
            ('SM3.Gyarados_33', 'Venting Anger', P1,
             ('SM3.Magikarp_32', 'SV05.RoaringMoon_109'), 50),
            ('SV1.Dondozo_61', 'Release Rage', P1,
             ('SV1.Tatsugiri_62', 'SV08.Tatsugiriex_142'), 50),
            ('SM12.AlolanNinetales_145', 'Rubbish Blizzard', P1,
             ('SV05.AncientBoosterEnergyCapsule_140',
              'SV065.EarthenVessel_96'), 10),
            ('XY4.Joltik_26', 'Night March', P1,
             ('XY4.Pumpkaboo_44', 'SV05.RoaringMoon_109'), 20),
            ('SM12.Armaldo_112', 'Ancient Blast', P1,
             ('SM6.UnidentifiedFossil_116', 'SWSH12.Serena_164'), 70),
            ('SV10.TeamRocketsPorygonZ_155', 'R Command', P1,
             ('SV10.TeamRocketsGiovanni_174',
              'SWSH12.Serena_164'), 20),
            ('SM10.PersianGX_149', 'Vengeance', P1,
             ('SV05.RoaringMoon_109',) * 10, 190),
            ('SM9.Zoroark_91', 'Night Punishment', P1,
             ('SV05.RoaringMoon_109',) * 11, 200),
        )
        for path, title, side, additions, expected in cases:
            with self.subTest(attack=path):
                rig, _, ctx = self.ctx(path, title)
                self.clear_discard(rig, side)
                for card_path in additions:
                    self.add_discard(rig, side, card_path)
                actual = _formula_damage(ctx, _norm(ctx.ability.game_text))
                self.assertEqual(actual, expected)
                ctx.deal_damage = AsyncMock(return_value=0)
                await ctx.ability.effect(ctx)
                self.assertEqual(ctx.deal_damage.await_args.args[0], expected)

    async def test_distinct_basic_energy_types_and_bonus_cap(self):
        rig, _, ctx = self.ctx('SM6.AlolanExeggutor_2', 'Tropical Shake')
        self.clear_discard(rig, P1)
        water = def_for(self.energies[PokemonTypes.WATER.value])
        fire = def_for(self.energies[PokemonTypes.FIRE.value])
        self.add(rig, water, P1, 'discard')
        self.add(rig, water, P1, 'discard')
        self.add(rig, fire, P1, 'discard')
        self.assertEqual(
            _formula_damage(ctx, _norm(ctx.ability.game_text)), 60)

    async def test_upstream_spirits_counts_then_shuffles_only_basic_energy(self):
        rig, _, ctx = self.ctx('SWSH11.HisuianBasculegion_45',
                               'Upstream Spirits')
        self.clear_discard(rig, P1)
        water = self.add(rig,
            def_for(self.energies[PokemonTypes.WATER.value]), P1, 'discard')
        fire = self.add(rig,
            def_for(self.energies[PokemonTypes.FIRE.value]), P1, 'discard')
        special = self.add_discard(rig, P1, 'SWSH9.DoubleTurboEnergy_151')
        ctx.deal_damage = AsyncMock(return_value=0)

        await ctx.ability.effect(ctx)

        self.assertEqual(ctx.deal_damage.await_args.args[0], 40)
        self.assertEqual(water._containing_area_name(), 'deck')
        self.assertEqual(fire._containing_area_name(), 'deck')
        self.assertEqual(special._containing_area_name(), 'discard')

    async def test_united_thunder_counts_discard_without_hitting_active(self):
        rig, entries, ctx = self.ctx('SV045.Kilowattrel_22', 'United Thunder')
        self.clear_discard(rig, P1)
        self.add_discard(rig, P1, 'SV2.Flamigo_170')
        self.add_discard(rig, P1, 'SV05.RoaringMoon_109')
        target = ctx.opponent_bench()[0]
        before = target.get_attribute(AttrID.HP)
        active_before = entries['p2_active'].get_attribute(AttrID.HP)
        ctx.choose_pokemon = AsyncMock(return_value=target)

        await ctx.ability.effect(ctx)

        self.assertEqual(target.get_attribute(AttrID.HP), before - 10)
        self.assertEqual(entries['p2_active'].get_attribute(AttrID.HP),
                         active_before)
        self.assertIn(target, ctx.choose_pokemon.await_args.args[0])


if __name__ == '__main__':
    unittest.main()
