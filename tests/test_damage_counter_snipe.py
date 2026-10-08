"""Damage-scaled snipes use the printed source of the counters and target."""
import unittest
from unittest.mock import AsyncMock

from spirit.game.attributes import AttrID, PokemonTypes

from tests import test_hgss_rules as fixtures


class DamageCounterSnipeTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx

    async def test_roaring_scream_uses_attacker_counters_and_can_hit_bench(self):
        rig, entries, ctx = self.ctx('SV085.ScreamTail_42', 'Roaring Scream')
        attacker = entries['target']
        target = ctx.opponent_bench()[0]
        attacker.set_attribute(AttrID.HP, ctx.max_hp(attacker) - 30)
        target.set_attribute(AttrID.HP, ctx.max_hp(target) - 10)
        target.set_attribute(AttrID.WEAKNESS_TYPES, [PokemonTypes.PSYCHIC.value])
        target.set_attribute(AttrID.WEAKNESS_AMOUNT, 2)
        ctx.choose_pokemon = AsyncMock(return_value=target)

        await ctx.ability.effect(ctx)

        self.assertEqual(target.get_attribute(AttrID.HP), ctx.max_hp(target) - 70)
        self.assertEqual(entries['p2_active'].get_attribute(AttrID.HP),
                         ctx.max_hp(entries['p2_active']))
        self.assertEqual(attacker.get_attribute(AttrID.HP), ctx.max_hp(attacker) - 30)
        self.assertIn(target, ctx.choose_pokemon.await_args.args[0])

    async def test_roaring_scream_applies_weakness_to_active_target(self):
        rig, entries, ctx = self.ctx('SV085.ScreamTail_42', 'Roaring Scream')
        attacker = entries['target']
        target = entries['p2_active']
        attacker.set_attribute(AttrID.HP, ctx.max_hp(attacker) - 20)
        target.set_attribute(AttrID.WEAKNESS_TYPES, [PokemonTypes.PSYCHIC.value])
        target.set_attribute(AttrID.WEAKNESS_AMOUNT, 2)
        ctx.choose_pokemon = AsyncMock(return_value=target)

        await ctx.ability.effect(ctx)

        self.assertEqual(target.get_attribute(AttrID.HP), ctx.max_hp(target) - 80)

    async def test_ear_kinesis_uses_chosen_benched_targets_counters(self):
        rig, entries, ctx = self.ctx('SM10.Espurr_79', 'Ear Kinesis')
        attacker = entries['target']
        target = ctx.opponent_bench()[0]
        attacker.set_attribute(AttrID.HP, ctx.max_hp(attacker) - 10)
        target.set_attribute(AttrID.HP, ctx.max_hp(target) - 30)
        ctx.choose_pokemon = AsyncMock(return_value=target)

        await ctx.ability.effect(ctx)

        self.assertEqual(target.get_attribute(AttrID.HP), ctx.max_hp(target) - 90)
        self.assertEqual(entries['p2_active'].get_attribute(AttrID.HP),
                         ctx.max_hp(entries['p2_active']))
        self.assertEqual(ctx.choose_pokemon.await_args.args[0], ctx.opponent_bench())


if __name__ == '__main__':
    unittest.main()
