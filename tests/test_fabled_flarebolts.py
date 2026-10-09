"""Fabled Flarebolts pays from the Bench and scales with cards discarded."""
import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures
from spirit.game.attributes import PokemonTypes
from spirit.game.data_utils import def_for
from spirit.game.session.effects import EffectContext
from spirit.tools.effect_smoke import P1


class FabledFlareboltsTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    async def test_only_matching_basic_energy_on_bench_scales_damage(self):
        for number in (157, 222, 259):
            with self.subTest(number=number):
                path = f'SM12.ReshiramZekromGX_{number}'
                rig, entities = self.rig(path)
                ability = next(a for a in fixtures.definition(path).abilities
                               if a.title == 'Fabled Flarebolts')
                ctx = EffectContext(rig.session, P1, entities['target'], ability)
                bench = rig.board.pokemon_in_play(P1)[1]

                def attach_basic(kind):
                    energy = self.add(rig, def_for(self.energies[kind]), P1, 'hand')
                    rig.attach(energy, bench)
                    return energy

                fire = attach_basic(PokemonTypes.FIRE.value)
                lightning = attach_basic(PokemonTypes.LIGHTNING.value)
                grass = attach_basic(PokemonTypes.GRASS.value)
                special = self.add(rig, fixtures.definition('SV05.MistEnergy_161'), P1, 'hand')
                rig.attach(special, bench)
                active_energy = list(ctx.attached_energies(ctx.source))

                async def choose(pool, maximum, **kwargs):
                    self.assertEqual(set(pool), {fire, lightning})
                    self.assertEqual(maximum, 2)
                    self.assertEqual(kwargs['minimum'], 0)
                    return [fire, lightning]

                ctx.choose_cards = AsyncMock(side_effect=choose)
                ctx.deal_damage = AsyncMock()
                await ability.effect(ctx)
                ctx.deal_damage.assert_awaited_once_with(180)
                self.assertIn(fire, ctx.discard_pile())
                self.assertIn(lightning, ctx.discard_pile())
                self.assertIn(grass, rig.board.attached_energies(bench))
                self.assertIn(special, rig.board.attached_energies(bench))
                self.assertTrue(all(e in ctx.attached_energies(ctx.source)
                                    for e in active_energy))
