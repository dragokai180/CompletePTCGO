"""Magnetic Metal Energy provides Metal only while attached."""
import unittest
from unittest.mock import AsyncMock, Mock

from tests import test_hgss_rules as fixtures
from spirit.game.attributes import PokemonTypes
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.trainers import is_metal_energy_card
from spirit.game.session.effects import EffectContext, is_energy_of_type
from spirit.tools.effect_smoke import P1


class MagneticMetalEnergyZoneTests(unittest.IsolatedAsyncioTestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig
    add = fixtures.HgssRulesTests.add

    def test_other_special_energy_types_depend_on_zone(self):
        cases = (
            ('ME4.MagneticMetalEnergy_85', PokemonTypes.METAL, False),
            ('SWSH4.CoatingMetalEnergy_163', PokemonTypes.METAL, False),
            ('SWSH2.SpeedLightningEnergy_173', PokemonTypes.LIGHTNING, False),
            ('SWSH1.AuroraEnergy_186', PokemonTypes.METAL, False),
            ('SM1.DoubleColorlessEnergy_136', PokemonTypes.COLORLESS, True),
            ('HGSS3.MetalEnergy_80', PokemonTypes.METAL, True),
        )
        for path, kind, outside_matches in cases:
            with self.subTest(card=path):
                rig, entities = self.rig('BW1.Snivy_1')
                energy = self.add(rig, fixtures.definition(path), P1, 'discard')
                self.assertEqual(is_energy_of_type(energy, kind), outside_matches)
                self.assertEqual(energy_provides_type(energy, kind.value),
                                 outside_matches)
                rig.attach(energy, entities['target'])
                self.assertTrue(is_energy_of_type(energy, kind))
                self.assertTrue(energy_provides_type(energy, kind.value))

    async def test_metal_saucer_excludes_unattached_magnetic_energy(self):
        path = 'SWSH1.MetalSaucer_170'
        rig, entities = self.rig(path, 'trainer')
        for card in list(rig.board.find_player_area(P1, 'discard').children):
            rig.to_area(card, P1, 'hand')
        bench = self.add(rig, fixtures.definition('SWSH1.ZacianV_138'),
                         P1, 'bench')
        magnetic = self.add(rig, fixtures.definition('ME4.MagneticMetalEnergy_85'),
                            P1, 'discard')
        saucer = fixtures.definition(path)

        self.assertFalse(is_metal_energy_card(magnetic))
        self.assertFalse(saucer.condition(rig.board, P1))

        basic = self.add(rig, fixtures.definition('BW1.MetalEnergy_112'),
                         P1, 'discard')
        self.assertTrue(is_metal_energy_card(basic))
        self.assertTrue(saucer.condition(rig.board, P1))
        ctx = EffectContext(rig.session, P1, entities['target'], None)
        ctx.choose_cards = AsyncMock(return_value=[basic])
        ctx.choose_pokemon = AsyncMock(return_value=bench)
        await saucer.effect(ctx)
        self.assertEqual(ctx.choose_cards.await_args.args[0], [basic])
        self.assertIn(basic, rig.board.attached_energies(bench))
        rig.attach(magnetic, bench)
        self.assertTrue(is_metal_energy_card(magnetic))
        self.assertTrue(is_energy_of_type(magnetic, PokemonTypes.METAL))

    async def test_intrepid_sword_adds_magnetic_energy_to_hand(self):
        path = 'SWSH1.ZacianV_138'
        rig, entities = self.rig(path)
        magnetic = self.add(rig, fixtures.definition('ME4.MagneticMetalEnergy_85'),
                            P1, 'deck')
        basic = self.add(rig, fixtures.definition('BW1.MetalEnergy_112'),
                         P1, 'deck')
        ability = next(a for a in fixtures.definition(path).abilities
                       if a.title == 'Intrepid Sword')
        ctx = EffectContext(rig.session, P1, entities['target'], ability)
        ctx.deck_top = Mock(return_value=[magnetic, basic])
        ctx.choose_cards = AsyncMock(return_value=[basic])

        await ability.effect(ctx)

        self.assertEqual(ctx.choose_cards.await_args.args[0], [basic])
        self.assertEqual(ctx.choose_cards.await_args.kwargs['display_cards'],
                         [magnetic, basic])
        self.assertIn(basic, rig.board.attached_energies(entities['target']))
        self.assertIn(magnetic, ctx.hand())


if __name__ == '__main__':
    unittest.main()
