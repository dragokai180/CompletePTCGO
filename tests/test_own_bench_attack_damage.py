"""Attacks that select the user's own Bench must actually damage it."""
import re
import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures

from spirit.game.attributes import AttrID, PokemonTypes


class OwnBenchAttackDamageTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx

    async def test_grenade_hammer_hits_two_chosen_benched_pokemon(self):
        rig, _, ctx = self.ctx('XY3.SeismitoadEX_20', 'Grenade Hammer')
        bench = list(ctx.my_bench())
        targets = bench[:2]
        defender = ctx.defender
        defender.set_attribute(AttrID.HP, 500)
        defender.set_attribute(AttrID.WEAKNESS_TYPES, [])
        defender.set_attribute(AttrID.RESISTANCE_TYPES, [])
        for pokemon in bench:
            pokemon.set_attribute(AttrID.HP, 200)
            pokemon.set_attribute(AttrID.WEAKNESS_TYPES,
                                  [PokemonTypes.WATER.value])
        opposing_hp = [p.get_attribute(AttrID.HP)
                       for p in ctx.opponent_bench()]
        ctx.choose_cards = AsyncMock(return_value=targets)

        await ctx.ability.effect(ctx)

        self.assertEqual(defender.get_attribute(AttrID.HP), 370)
        self.assertEqual([p.get_attribute(AttrID.HP) for p in bench],
                         [170, 170, 200])
        self.assertEqual([p.get_attribute(AttrID.HP)
                          for p in ctx.opponent_bench()], opposing_hp)
        ctx.choose_cards.assert_awaited_once()
        self.assertEqual(ctx.choose_cards.call_args.kwargs['minimum'], 2)

    async def test_grenade_hammer_hits_available_bench_without_extra_choice(self):
        rig, _, ctx = self.ctx('XY3.SeismitoadEX_20', 'Grenade Hammer')
        bench = list(ctx.my_bench())
        for pokemon in bench[1:]:
            rig.to_area(pokemon, ctx.player_id, 'discard')
        target = bench[0]
        target.set_attribute(AttrID.HP, 200)
        ctx.choose_cards = AsyncMock(
            side_effect=AssertionError('no target choice with one Pokemon'))

        await ctx.ability.effect(ctx)

        self.assertEqual(target.get_attribute(AttrID.HP), 170)
        ctx.choose_cards.assert_not_awaited()

    async def test_other_attacks_select_own_bench_only(self):
        cases = (
            ('XY8.Pinsir_3', 'Overhead Throw'),
            ('ME5.Zarude_56', 'Overhead Throw'),
            ('MEP.Zarude_88', 'Overhead Throw'),
            ('XY6.Zapdos_23', 'Raging Thunder'),
            ('SM2.Heliolisk_44', 'Raging Thunder'),
            ('SM10.Stunfisk_56', 'Raging Thunder'),
            ('SM11.Thundurus_68', 'Raging Thunder'),
            ('SV4.Zekrom_66', 'Raging Thunder'),
            ('SV3.Pupitar_106', 'Blasting Tackle'),
            ('SV10.Manectric_76', 'Flash Impact'),
            ('SV06.Girafarig_83', 'Dual Headbutt'),
        )
        for path, title in cases:
            with self.subTest(path=path):
                _, _, ctx = self.ctx(path, title)
                bench = list(ctx.my_bench())
                target = bench[1]
                target.set_attribute(AttrID.HP, 200)
                others = [p.get_attribute(AttrID.HP)
                          for p in bench if p is not target]
                opponent = [p.get_attribute(AttrID.HP)
                            for p in ctx.opponent_bench()]
                ctx.choose_cards = AsyncMock(return_value=[target])
                amount = int(re.search(
                    r'does (\d+) damage to 1 of your Benched',
                    ctx.ability.game_text).group(1))

                await ctx.ability.effect(ctx)

                self.assertEqual(target.get_attribute(AttrID.HP), 200 - amount)
                self.assertEqual([p.get_attribute(AttrID.HP)
                                  for p in bench if p is not target], others)
                self.assertEqual([p.get_attribute(AttrID.HP)
                                  for p in ctx.opponent_bench()], opponent)
                ctx.choose_cards.assert_awaited_once()

    async def test_existing_spread_and_split_bench_attacks(self):
        _, _, spread = self.ctx('XY4.Diggersby_88', 'Earthquake')
        bench = list(spread.my_bench())
        before = [p.get_attribute(AttrID.HP) for p in bench]
        await spread.ability.effect(spread)
        self.assertEqual([p.get_attribute(AttrID.HP) for p in bench],
                         [hp - 10 for hp in before])

        _, _, split = self.ctx('SWSH4.Eelektross_59',
                               'Electro Sprinkler')
        mine, theirs = split.my_bench()[0], split.opponent_bench()[0]
        mine_hp = mine.get_attribute(AttrID.HP)
        theirs_hp = theirs.get_attribute(AttrID.HP)
        split.choose_pokemon = AsyncMock(side_effect=[mine, theirs])
        await split.ability.effect(split)
        self.assertEqual(mine.get_attribute(AttrID.HP), mine_hp - 30)
        self.assertEqual(theirs.get_attribute(AttrID.HP), theirs_hp - 30)


if __name__ == '__main__':
    unittest.main()
