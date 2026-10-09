"""Splitting Arrow must ask only for Benched targets that exist."""
import unittest
from unittest.mock import AsyncMock

from tests import test_hgss_rules as fixtures
from spirit.game.attributes import AttrID
from spirit.tools.effect_smoke import P1, P2


class SplittingArrowTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    ctx = fixtures.HgssRulesTests.ctx
    add = fixtures.HgssRulesTests.add

    async def test_bench_targets_match_available_pokemon(self):
        for card_path in ('SWSH3.Decidueye_13', 'SWSH45.Decidueye_8'):
            for bench_count in (0, 1, 2, 3):
                with self.subTest(card=card_path, bench=bench_count):
                    rig, _, ctx = self.ctx(card_path, 'Splitting Arrow')
                    for pokemon in list(ctx.opponent_bench()):
                        rig.to_area(pokemon, P2, 'deck')
                    bench = [self.add(rig, self.filler, P2, 'bench')
                             for _ in range(bench_count)]
                    for pokemon in bench:
                        pokemon.set_attribute(AttrID.HP, 200)
                    active = ctx.opponent_active()
                    active.set_attribute(AttrID.HP, 200)

                    async def pick(player_id, source_id, candidates, count,
                                   minimum, prompt, **kwargs):
                        self.assertEqual(player_id, P1)
                        self.assertEqual(candidates, bench)
                        self.assertEqual(count, min(2, bench_count))
                        self.assertIsNone(minimum)
                        return [p.entity_id for p in candidates[:count]]

                    rig.session.prompt_entity_picker = AsyncMock(side_effect=pick)
                    await ctx.ability.effect(ctx)

                    self.assertEqual(active.get_attribute(AttrID.HP), 110)
                    self.assertEqual([p.get_attribute(AttrID.HP) for p in bench],
                                     [180] * min(2, bench_count)
                                     + [200] * max(0, bench_count - 2))
                    self.assertEqual(rig.session.prompt_entity_picker.await_count,
                                     int(bench_count > 0))
