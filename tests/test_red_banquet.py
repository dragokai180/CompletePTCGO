"""Attack Prize bonuses must remain independent of either player's GX effect."""
import unittest
from unittest.mock import AsyncMock, patch

from tests import test_hgss_rules as fixtures
from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.session.effects import EffectContext
from spirit.tools.effect_smoke import P1, P2


class RedBanquetTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    async def setup_case(self, altered=(), victim=None, hp=100):
        rig, e = self.rig('SM12.Guzzlord_136')
        attacker = e['target']
        # Activate the actual GX attack for the requested side(s).
        for pid in altered:
            adp_def = fixtures.definition('SM12.ArceusDialgaPalkiaGX_156')
            adp = self.add(rig, adp_def, pid, 'bench')
            for kind in (PokemonTypes.METAL, PokemonTypes.WATER):
                rig.attach_energy_type(pid, adp, kind.value)
            gx = next(a for a in adp_def.abilities if a.title == 'Altered Creation-GX')
            await gx.effect(EffectContext(rig.session, pid, adp, gx))
        defender = rig.board.active_pokemon(P2)
        if victim:
            rig.to_area(defender, P2, 'hand')
            defender = self.add(rig, fixtures.definition(victim), P2, 'activePokemonArea')
        defender.set_attribute(AttrID.HP, hp)
        defender.set_attribute(AttrID.WEAKNESS_TYPES, [])
        defender.set_attribute(AttrID.RESISTANCE_TYPES, [])
        attack = next(a for a in fixtures.definition('SM12.Guzzlord_136').abilities
                      if a.title == 'Red Banquet')
        return rig, EffectContext(rig.session, P1, attacker, attack), defender

    async def test_bonus_with_neither_either_or_both_altered_creation_effects(self):
        for altered, expected in (((), 2), ((P2,), 2), ((P1,), 3), ((P1, P2), 3)):
            with self.subTest(altered=altered):
                rig, ctx, defender = await self.setup_case(altered)
                with patch.object(rig.session, '_take_prizes', AsyncMock()) as prizes:
                    await ctx.ability.effect(ctx)
                    await rig.session.resolve_knockouts(ctx)
                prizes.assert_awaited_once_with(P1, expected, destination='hand')
                self.assertIn(defender, ctx.discard_pile(P2))
                self.assertIsNotNone(rig.board.active_pokemon(P2))

    async def test_tag_team_prize_value_stacks_with_red_banquet(self):
        rig, ctx, _ = await self.setup_case((P2,), 'SM12.ArceusDialgaPalkiaGX_156')
        with patch.object(rig.session, '_take_prizes', AsyncMock()) as prizes:
            await ctx.ability.effect(ctx)
            await rig.session.resolve_knockouts(ctx)
        prizes.assert_awaited_once_with(P1, 4, destination='hand')

    async def test_nonlethal_attack_does_not_leave_a_prize_bonus(self):
        rig, ctx, defender = await self.setup_case((P2,), hp=200)
        with patch.object(rig.session, '_take_prizes', AsyncMock()) as prizes:
            await ctx.ability.effect(ctx)
            await rig.session.resolve_knockouts(ctx)
        prizes.assert_not_awaited()
        self.assertEqual(defender.get_attribute(AttrID.HP), 80)
        self.assertEqual(ctx.extra_prizes, 0)

    async def test_no_prize_pokemon_still_awards_none(self):
        rig, ctx, _ = await self.setup_case((P1, P2), 'SM12.LilliesPokDoll_197', hp=30)
        with patch.object(rig.session, '_take_prizes', AsyncMock()) as prizes:
            await ctx.ability.effect(ctx)
            await rig.session.resolve_knockouts(ctx)
        prizes.assert_not_awaited()

    async def test_ordinary_attack_after_red_banquet_does_not_keep_its_bonus(self):
        rig, ctx, _ = await self.setup_case((P2,))
        with patch.object(rig.session, '_take_prizes', AsyncMock()) as prizes:
            await ctx.ability.effect(ctx)
            await rig.session.resolve_knockouts(ctx)
            from spirit.game.data_utils import Attack
            ordinary = EffectContext(rig.session, P1, ctx.attacker,
                                     Attack(title='Audit hit', cost={}, damage=1000))
            await ordinary.deal_damage()
            await rig.session.resolve_knockouts(ordinary)
        self.assertEqual([c.args for c in prizes.await_args_list], [(P1, 2), (P1, 1)])


if __name__ == '__main__':
    unittest.main()
