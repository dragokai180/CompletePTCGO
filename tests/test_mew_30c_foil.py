"""Only the requested Mew/Mewtwo prints receive the Live approximation."""
import unittest
from unittest.mock import patch

from spirit.game import data_utils
from spirit.game.attributes import AttrID, FoilEffects, FoilMasks, Rarities
from spirit.game.foil_corrections import client_foil_record


class MewCelebrationFoilTests(unittest.TestCase):
    def record(self):
        return {'effect': 'SvUltra', 'mask': 'Etched', 'full_art': True,
                'intensity': 201}

    def test_uses_existing_material_with_the_original_mask_slot(self):
        original = self.record()
        with patch.dict(data_utils._PRINT_FOIL_METADATA, {'ME55': {'158': original}}):
            known, foil = data_utils._print_foil('me55', 158, Rarities.Rare, ['ex'])
        self.assertTrue(known)
        self.assertEqual(foil.effects, [FoilEffects.RAINBOW])
        self.assertEqual(foil.mask, FoilMasks.ETCHED)
        self.assertEqual(foil.mask_kind(), 'std')
        self.assertEqual(foil.style, 'full')
        attrs = foil.to_attributes()
        self.assertEqual(attrs[str(AttrID.FOIL_EFFECT.value)]['value'], 3)
        self.assertEqual(attrs[str(AttrID.FOIL_MASK.value)]['value'], 4)
        self.assertEqual(attrs[str(AttrID.FOIL_EFFECTS.value)]['value'], '[]')
        self.assertEqual(original, self.record())

    def test_other_prints_and_materials_are_not_adapted(self):
        original = self.record()
        for code, number in [('ME55', 64), ('ME55', 66), ('ME55', 156), ('ME55', 159), ('SV1', 250)]:
            self.assertIs(client_foil_record(code, number, original), original)
        for fields in [{'effect': 'SunPillar'}, {'mask': 'Holo'},
                       {'full_art': False}, {'effects': ['FlatSilver']}]:
            record = {**original, **fields}
            self.assertIs(client_foil_record('ME55', 158, record), record)

    def test_mewtwo_157_keeps_its_own_image_and_foil_identity(self):
        original = self.record()
        with patch.dict(data_utils._PRINT_FOIL_METADATA, {'ME55': {'157': original}}):
            card = data_utils.CardDefinition(
                guid='00000000-0000-0000-0000-000000000157', key='ME55',
                name='Mewtwo ex', collector_number=157, set_code='ME55',
                rarity=Rarities.Rare)
        attrs = card.to_archetype_dict()['attributes']
        self.assertEqual(attrs[str(AttrID.IMAGE_URL.value)]['value'], '157')
        self.assertEqual(card.foil.mask_kind(), 'std')
        self.assertEqual(card.foil.effects, [FoilEffects.RAINBOW])
        self.assertEqual(card.foil.mask, FoilMasks.ETCHED)
        self.assertEqual(original, self.record())

    def test_does_not_invent_a_foil_without_imported_metadata(self):
        for records in [{}, {'158': None}]:
            with patch.dict(data_utils._PRINT_FOIL_METADATA, {'ME55': records}):
                self.assertIsNone(data_utils._print_foil('ME55', 158, Rarities.Rare, ['ex'])[1])

    def test_scarlet_violet_stays_disabled(self):
        with patch.dict(data_utils._PRINT_FOIL_METADATA, {'SV1': {'158': self.record()}}):
            self.assertEqual(data_utils._print_foil('SV1', 158, Rarities.Rare, ['ex']), (True, None))


if __name__ == '__main__':
    unittest.main()
