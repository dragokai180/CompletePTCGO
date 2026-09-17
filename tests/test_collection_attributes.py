"""Native collection filter predicates receive correctly typed card facets."""
import json
import unittest
from types import SimpleNamespace
from unittest.mock import patch

from spirit.game.collection_attributes import collection_attributes
from spirit.game import data_utils
from spirit.game.attributes import Rarities


class CollectionAttributeTests(unittest.TestCase):
    def attrs(self, subtypes=(), metadata=None, abilities=()):
        return collection_attributes(SimpleNamespace(subtypes=subtypes, abilities=abilities), metadata)

    def test_client_tags_for_all_battle_styles_and_rule_box_groups(self):
        cases = {'Ultra Beast': 'UltraBeast', 'TAG TEAM': 'TAG', 'Single Strike': 'SingleStrike',
                 'Rapid Strike': 'RapidStrike', 'Fusion Strike': 'FusionStrike',
                 'Shining': 'ShinyPokemon', 'Prism Star': 'PrismStar'}
        for subtype, expected in cases.items():
            with self.subTest(subtype=subtype):
                self.assertEqual(json.loads(self.attrs([subtype])['202200']['value']), [expected])
        self.assertNotIn('202200', self.attrs(['Basic', 'ex', 'Tera']))

    def test_all_v_forms_match_v_and_vmax_keeps_its_specific_tag(self):
        for subtype in ('V', 'VMAX', 'VSTAR', 'V-UNION'):
            self.assertIn('V', json.loads(self.attrs([subtype])['202200']['value']))
        self.assertEqual(json.loads(self.attrs(['VMAX'])['202200']['value']), ['V', 'VMAX'])

    def test_ex_is_not_modern_ex_and_legend_has_its_native_flag(self):
        self.assertTrue(self.attrs(['EX'])['201010']['value'])
        self.assertFalse(self.attrs(['ex'])['201010']['value'])
        self.assertTrue(self.attrs(['LEGEND'])['201030']['value'])
        self.assertFalse(self.attrs(['Basic'])['201030']['value'])

    def test_teams_and_gx_attacks_use_native_types_and_ids(self):
        for name, value in [('Team Plasma', 0), ('Team Aqua', 3), ('Team Magma', 4)]:
            self.assertEqual(json.loads(self.attrs([name])['200360']['value']), [value])
        abilities = [SimpleNamespace(gx=True, ability_id='gx-id'), SimpleNamespace(gx=False, ability_id='attack-id')]
        self.assertEqual(json.loads(self.attrs(['GX'], abilities=abilities)['202120']['value']), ['gx-id'])
        self.assertNotIn('202120', self.attrs(['Basic'], abilities=abilities))

    def test_full_art_is_independent_of_foil_coverage(self):
        self.assertTrue(self.attrs([], {'full_art': True})['201000']['value'])
        self.assertFalse(self.attrs(['VMAX'], {'full_art': False, 'mask': 'Etched'})['201000']['value'])
        self.assertTrue(self.attrs(['Full Art'])['201000']['value'])

    def test_shining_rarity_and_double_crisis_missing_subtypes(self):
        card = SimpleNamespace(subtypes=['Basic'], abilities=[], rarity=Rarities.Shining)
        self.assertIn('ShinyPokemon', json.loads(collection_attributes(card)['202200']['value']))
        for name, team in [("Team Aqua's Kyogre-EX", 3), ('Aqua Diffuser', 3),
                           ('Double Magma Energy', 4), ('Team Magma Admin', 4)]:
            card = SimpleNamespace(subtypes=[], abilities=[], set_code='TATM', display_name=name)
            self.assertEqual(json.loads(collection_attributes(card)['200360']['value']), [team])

    def test_wire_serialization_includes_facets_even_when_sv_foil_is_disabled(self):
        with patch.dict(data_utils._PRINT_FOIL_METADATA, {'SV1': {'1': {'full_art': True}}}):
            card = data_utils.CardDefinition(guid='filter-test', key='SV1', name='Test',
                collector_number=1, set_code='SV1', rarity=Rarities.Rare, subtypes=['ex'])
            attrs = card.to_archetype_dict()['attributes']
        self.assertTrue(attrs['201000']['value'])
        self.assertFalse(attrs['201010']['value'])
        self.assertNotIn('200610', attrs)


if __name__ == '__main__':
    unittest.main()
