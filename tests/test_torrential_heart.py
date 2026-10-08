"""Torrential Heart pays its counter cost and boosts only its own attack."""
import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures
from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.session.effects import EffectContext
from spirit.tools.effect_smoke import P1


class TorrentialHeartTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx

    async def test_pays_five_counters_and_boosts_giant_wave(self):
        rig, entries, ctx = self.ctx('SV05.Feraligatr_41',
                                     'Torrential Heart')
        source = entries['target']
        defender = entries['p2_active']
        source_hp = source.get_attribute(AttrID.HP)
        source.set_attribute(AttrID.WEAKNESS_TYPES,
                             [PokemonTypes.WATER.value])
        defender.set_attribute(AttrID.HP, 500)
        attack = next(a for a in fixtures.definition('SV05.Feraligatr_41').abilities
                      if a.title == 'Giant Wave')

        await ctx.ability.effect(ctx)
        attack_ctx = EffectContext(rig.session, P1, source, attack)
        await attack.effect(attack_ctx)

        self.assertEqual(source.get_attribute(AttrID.HP), source_hp - 50)
        self.assertEqual(defender.get_attribute(AttrID.HP), 220)
        self.assertEqual(len(rig.session.turn_state.damage_modifiers), 1)
        self.assertEqual(rig.session.turn_state.damage_modifiers[0].source_entity_id,
                         source.entity_id)

    async def test_blocked_counter_payment_does_not_grant_boost(self):
        rig, _, ctx = self.ctx('SV05.Feraligatr_41', 'Torrential Heart')
        ctx.deal_damage = AsyncMock(return_value=0)

        await ctx.ability.effect(ctx)

        self.assertEqual(len(rig.session.turn_state.damage_modifiers), 0)


if __name__ == '__main__':
    unittest.main()
