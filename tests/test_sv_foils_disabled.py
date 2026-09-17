"""Scarlet & Violet foil rendering is disabled without affecting other eras."""
import unittest
from unittest.mock import patch

from spirit.game import data_utils
from spirit.game.attributes import AttrID, FoilEffects, FoilMasks, Rarities
from spirit.game.foil_corrections import FOIL_DISABLED_SETS
from spirit.tools.import_sv_sets import SV_SETS


class ScarletVioletFoilsDisabledTests(unittest.TestCase):
    def test_covers_every_scarlet_violet_set(self):
        self.assertEqual(FOIL_DISABLED_SETS, {v[0] for v in SV_SETS.values()})

    def test_blocks_metadata_explicit_foils_and_raw_attributes(self):
        foil = data_utils.Foil(mask=FoilMasks.ETCHED, effects=[FoilEffects.RAINBOW])
        for code in FOIL_DISABLED_SETS:
            with self.subTest(code=code), patch.dict(data_utils._PRINT_FOIL_METADATA, {
                    code: {'1': {'effect': 'Rainbow', 'mask': 'Etched', 'full_art': True}}}):
                card = data_utils.CardDefinition(
                    guid='00000000-0000-0000-0000-00000000f012', key=code,
                    name='test', collector_number=1, set_code=code,
                    rarity=Rarities.RareHolo, foil=foil, attributes=foil.to_attributes())
                self.assertIsNone(card.foil)
                attrs = card.to_archetype_dict()['attributes']
                for attr in (AttrID.FOIL_EFFECT, AttrID.FOIL_EFFECTS,
                             AttrID.FOIL_MASK, AttrID.FOIL_INTENSITY):
                    self.assertNotIn(str(attr.value), attrs)
                self.assertEqual(attrs[str(AttrID.IMAGE_URL.value)]['value'], '001')

    def test_unknown_sv_print_cannot_use_explicit_fallback(self):
        with patch.dict(data_utils._PRINT_FOIL_METADATA, {}, clear=True):
            self.assertEqual(data_utils._print_foil('sv1', 999, Rarities.RareHolo, []), (True, None))

    def test_other_eras_keep_foil(self):
        for code in ('HGSS1', 'BW1', 'XY1', 'SM1', 'SWSH1', 'ME1'):
            with self.subTest(code=code), patch.dict(data_utils._PRINT_FOIL_METADATA, {
                    code: {'1': {'effect': 'Rainbow', 'mask': 'Etched', 'full_art': True}}}):
                known, foil = data_utils._print_foil(code, 1, Rarities.RareHolo, [])
                self.assertTrue(known)
                self.assertIsNotNone(foil)
