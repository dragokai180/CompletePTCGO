"""Temple of Sinnoh suppresses attached Energy effects, not attach costs."""

import unittest

from tests import test_hgss_rules as fixtures
from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.session.effects import (
    resolve_energy_attach_cost, resolve_energy_on_attach,
)
from spirit.game.session.passives import energy_provided_options
from spirit.tools.effect_smoke import P1


class TempleRainbowEnergyTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    ctx = fixtures.HgssRulesTests.ctx
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    def play_temple(self, rig):
        stadium = self.add(rig, fixtures.definition(
            'SWSH10.TempleofSinnoh_155'), P1, 'hand')
        rig.board.move_card(
            stadium.entity_id,
            rig.board.find_global_area('activeStadium').entity_id,
        )
        return stadium

    async def test_rainbow_counter_only_without_temple(self):
        for path in ('HGSS1.RainbowEnergy_104', 'XY1.RainbowEnergy_131'):
            for temple in (False, True):
                with self.subTest(path=path, temple=temple):
                    rig, _, ctx = self.ctx('BW1.Snivy_1', 'Tackle')
                    pokemon = ctx.attacker
                    pokemon.set_attribute(AttrID.HP, 100)
                    stadium = self.play_temple(rig) if temple else None
                    energy = self.add(rig, fixtures.definition(path), P1, 'hand')
                    rig.attach(energy, pokemon)

                    await resolve_energy_on_attach(
                        rig.session, P1, energy, pokemon)

                    self.assertEqual(pokemon.get_attribute(AttrID.HP),
                                     100 if temple else 90)
                    if stadium is not None:
                        self.assertEqual(energy_provided_options(
                            rig.board, energy), [[PokemonTypes.COLORLESS.value]])
                        rig.board.move_card(
                            stadium.entity_id,
                            rig.board.find_player_area(P1, 'discard').entity_id,
                        )
                        self.assertEqual(pokemon.get_attribute(AttrID.HP), 100)

    async def test_aurora_attachment_cost_still_applies_under_temple(self):
        rig, _, ctx = self.ctx('BW1.Snivy_1', 'Tackle')
        self.play_temple(rig)
        energy = self.add(rig, fixtures.definition(
            'SWSH1.AuroraEnergy_186'), P1, 'hand')
        before = len(ctx.hand())

        paid = await resolve_energy_attach_cost(
            rig.session, P1, energy, ctx.attacker)

        self.assertIsNotNone(paid)
        self.assertEqual(len(ctx.hand()), before - 1)
        self.assertIn(energy, ctx.hand())


if __name__ == '__main__':
    unittest.main()
