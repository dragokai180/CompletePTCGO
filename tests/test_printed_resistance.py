"""Printed resistance values survive catalog import and damage calculation."""
import ast
import unittest
from unittest.mock import patch

from tests import test_hgss_rules as fixtures
from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.data_utils import CARD_DEFS_BY_GUID, PokemonCardDef, reprint
from spirit.game.scripts.cards import loader
from spirit.game.session.passives import compute_damage
from spirit.tools.import_set import render_script
from spirit.tools.import_standard_sets import render_pokemon
from spirit.tools.audit_printed_resistance import (
    DATA_ROOT, attribute_resistance, audit, load_sources, printed_resistance,
)


class PrintedResistanceTests(unittest.TestCase):
    setUpClass = classmethod(fixtures.HgssRulesTests.setUpClass.__func__)
    rig = fixtures.HgssRulesTests.rig

    def test_all_bw_resistances_are_explicitly_twenty(self):
        checked = 0
        for d in CARD_DEFS_BY_GUID.values():
            if not isinstance(d, PokemonCardDef) or d.guid.lower() not in loader.cards_by_guid:
                continue
            if d.set_code not in {*(f'BW{i}' for i in range(1, 12)), 'PROMO_BW'}:
                continue
            attrs = d.extra_attributes
            resistance = attrs.get(str(AttrID.RESISTANCE_TYPES.value), {}).get('value')
            if resistance is None or resistance == PokemonTypes.UNSET.value:
                continue
            with self.subTest(card=d.display_name, set=d.set_code, number=d.collector_number):
                self.assertEqual(attrs[str(AttrID.RESISTANCE_AMOUNT.value)]['value'], 20)
            checked += 1
        self.assertGreaterEqual(checked, 369)

    def test_snivy_reduces_water_damage_by_twenty(self):
        rig, e = self.rig('BW1.Snivy_1')
        target, attacker = e['target'], e['p2_active']
        attacker.set_attribute(AttrID.POKEMON_TYPES, [PokemonTypes.WATER.value])
        self.assertEqual(target.get_attribute(AttrID.RESISTANCE_AMOUNT), 20)
        calc = compute_damage(rig.board, attacker, target, 100)
        self.assertTrue(calc.resistance_hit)
        self.assertEqual(calc.amount, 80)
        self.assertEqual(compute_damage(rig.board, attacker, target, 100,
                                       ignore_resistance=True).amount, 100)

    def test_modern_resistance_remains_thirty(self):
        rig, e = self.rig('SWSH1.IndeedeeV_91')
        target, attacker = e['target'], e['p2_active']
        attacker.set_attribute(AttrID.POKEMON_TYPES, [target.get_attribute(AttrID.RESISTANCE_TYPES)])
        calc = compute_damage(rig.board, attacker, target, 100)
        self.assertEqual(target.get_attribute(AttrID.RESISTANCE_AMOUNT), 30)
        self.assertTrue(calc.resistance_hit)
        self.assertEqual(calc.amount, 70)

    def test_all_pre_swsh_resistances_remain_twenty_in_client(self):
        checked = 0
        old_specials = {'COL', 'DV', 'TATM', 'TwentiethAnn', 'SL', 'DM', 'HF',
                        'GUM', 'Promo_HGSS', 'PROMO_BW', 'Promo_XY', 'Promo_SM'}
        for guid, model in loader.cards_by_guid.items():
            d = CARD_DEFS_BY_GUID.get(guid)
            if not isinstance(d, PokemonCardDef):
                continue
            if not (d.set_code.startswith(('HGSS', 'BW', 'XY', 'SM'))
                    or d.set_code in old_specials):
                continue
            kind, amount = attribute_resistance(d.extra_attributes)
            if kind == PokemonTypes.UNSET.value:
                continue
            with self.subTest(card=loader.script_by_guid[guid]):
                self.assertEqual(amount, 20)
                self.assertEqual(attribute_resistance(model.attributes), (kind, 20))
                self.assertEqual(attribute_resistance(model.to_archetype_attributes('test')), (kind, 20))
            checked += 1
        self.assertGreaterEqual(checked, 1918)

    def test_reprints_keep_original_resistance_even_across_eras(self):
        for module, expected, destination in (
            ('BW1.Snivy_1', 20, 'SWSH1'),
            ('SWSH1.IndeedeeV_91', 30, 'BW1'),
        ):
            with self.subTest(module=module):
                base = fixtures.definition(module)
                with patch.dict(CARD_DEFS_BY_GUID):
                    copy = reprint(base, collector_number=999, set_code=destination)
                    self.assertEqual(attribute_resistance(copy.extra_attributes)[1], expected)

    @unittest.skipUnless((DATA_ROOT / 'bw1.json').is_file(), 'Optional printed metadata snapshot not installed')
    def test_every_available_printed_source_matches_runtime_and_client(self):
        report = audit(load_sources([DATA_ROOT]))
        self.assertGreater(report['checked'], 0)
        self.assertEqual(report['mismatches'], [])


class ResistanceAuditTests(unittest.TestCase):
    def test_missing_amount_is_reported_instead_of_defaulting_to_thirty(self):
        attrs = {str(AttrID.RESISTANCE_TYPES.value): {'value': PokemonTypes.WATER.value}}
        self.assertEqual(attribute_resistance(attrs), (PokemonTypes.WATER.value, None))

    def test_source_without_resistance_is_not_given_one(self):
        self.assertEqual(printed_resistance({'id': 'test-1'}), (PokemonTypes.UNSET.value, 0))

    def test_source_accepts_both_printed_values_and_unicode_minus(self):
        for text in ('-20', '-30', '−20'):
            self.assertEqual(printed_resistance({'id': 'test-1', 'resistances': [
                {'type': 'Water', 'value': text}]}),
                (PokemonTypes.WATER.value, abs(int(text.replace('−', '-')))))


class ResistanceImportTests(unittest.TestCase):
    def imported_kwargs(self, resistance, renderer=render_script):
        card = {'id': 'resistance-test-1', 'name': 'Resistance Test', 'number': '1',
                'supertype': 'Pokémon', 'subtypes': ['Basic'], 'hp': '60',
                'types': ['Grass'], 'rarity': 'Common', 'resistances': resistance}
        tree = ast.parse(renderer(card))
        call = next(n for n in ast.walk(tree) if isinstance(n, ast.Call)
                    and isinstance(n.func, ast.Name) and n.func.id == 'PokemonCardDef')
        return {k.arg: k.value for k in call.keywords}

    def test_importer_preserves_minus_twenty_and_minus_thirty(self):
        for value in ('-20', '-30', '−20'):
            with self.subTest(value=value):
                kwargs = self.imported_kwargs([{'type': 'Water', 'value': value}])
                self.assertEqual(ast.literal_eval(kwargs['resistance_amount']),
                                 abs(int(value.replace('−', '-'))))

    def test_importer_does_not_invent_resistance(self):
        kwargs = self.imported_kwargs([])
        self.assertNotIn('resistance_type', kwargs)
        self.assertNotIn('resistance_amount', kwargs)

    def test_shared_era_importer_preserves_printed_values(self):
        for code in ('HGSS1', 'BW1', 'XY1', 'SM1', 'SWSH1', 'SV1', 'ME1'):
            for value in ('-20', '-30'):
                with self.subTest(set_code=code, value=value):
                    kwargs = self.imported_kwargs([{'type': 'Water', 'value': value}],
                        lambda c: render_pokemon(c, code, {}))
                    self.assertEqual(ast.literal_eval(kwargs['resistance_amount']), abs(int(value)))
