"""Compare every loaded Pokemon's resistance with its printed catalog entry.

Run with ``python -m spirit.tools.audit_printed_resistance``. Supply additional
local metadata snapshots with repeatable ``--source-dir`` arguments. This is
read-only, never downloads artwork, and reports unmatched prints explicitly.
"""
from __future__ import annotations

import argparse
import json
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.data_utils import CARD_DEFS_BY_GUID, PokemonCardDef
from spirit.game.gallery_catalog import GALLERY_SETS, gallery_number
from spirit.game.scripts.cards import loader
from spirit.tools.install_recent_card_art import DATA_ROOT, RECENT_SETS, RecentSet


def normalized_name(value):
    return re.sub(r'[^a-z0-9]', '', unicodedata.normalize('NFKD', value or '').lower())


def printed_resistance(card):
    entries = card.get('resistances') or []
    if not entries:
        return PokemonTypes.UNSET.value, 0
    if len(entries) != 1:
        raise ValueError(f"Multiple resistances require review: {card['id']}")
    entry = entries[0]
    return (PokemonTypes[entry['type'].upper()].value,
            abs(int(str(entry['value']).replace('\N{MINUS SIGN}', '-'))))


def attribute_resistance(attributes):
    def get(key, default):
        return attributes.get(str(key.value), {}).get('value', default)
    kind = get(AttrID.RESISTANCE_TYPES, PokemonTypes.UNSET.value)
    # Missing values must not silently inherit the modern default during audit.
    return kind, get(AttrID.RESISTANCE_AMOUNT, None) if kind != PokemonTypes.UNSET.value else 0


def load_sources(directories, *, pokemon_only=True):
    """First directory wins for duplicate IDs; later directories fill gaps."""
    catalogs = defaultdict(dict)
    specs = {s.data_stem: s for s in RECENT_SETS.values()
             if s.set_code not in {'Free_Energy', 'SWSH_Energy'}}
    for stem, code in [('sma', 'HF'), ('swsh45sv', 'SWSH45'), ('cel25c', 'CEL25')]:
        specs[stem] = RecentSet('special', stem, code)
    for stem, (code, _, _) in GALLERY_SETS.items():
        specs[stem] = RecentSet('gallery', stem, code)
    for directory in directories:
        for stem in specs:
            path = Path(directory) / f'{stem}.json'
            if not path.is_file():
                continue
            cards = json.loads(path.read_text(encoding='utf-8'))
            if not isinstance(cards, list):
                raise ValueError(f'Expected a card list: {path}')
            for card in cards:
                catalogs[stem].setdefault(card['id'], card)
    index = defaultdict(list)
    for stem, by_id in catalogs.items():
        spec = specs[stem]
        cards = list(by_id.values())
        numbers = {}
        if spec.era == 'hgss':
            from spirit.tools.import_hgss_sets import internal_number
            numbers = {c['id']: internal_number(c, stem) for c in cards}
        elif spec.era == 'xy':
            from spirit.tools.import_xy_sets import internal_number
            numbers = {c['id']: internal_number(c, stem) for c in cards}
        elif spec.era == 'sm' or stem == 'sma':
            from spirit.tools.import_sm_sets import number_map
            numbers = number_map(cards, stem)
        elif stem == 'me55':
            # Share verified upstream corrections (Murkrow's mislabelled
            # resistance) and the main set's R/G/B protocol numbering.
            from spirit.tools.import_thirtieth_celebration import normalized_card
            cards = [normalized_card(c) for c in cards]
            numbers = {c['id']: int(c['number']) for c in cards}
        for card in cards:
            if pokemon_only and card.get('supertype') != 'Pokémon':
                continue
            if stem in GALLERY_SETS:
                number = gallery_number(stem, card['number'])
            elif card['id'] in numbers:
                number = numbers[card['id']]
            else:
                # BW/RC/promos preserve their printed prefix in filenames, but
                # expose a numeric collector number over the client protocol.
                raw = card['id'].removeprefix(stem + '-') if spec.era in {'sv', 'mega'} else str(card['number'])
                match = re.search(r'\d+', raw)
                if match is None:
                    continue
                number = int(match.group())
                if spec.set_code == 'BW11' and raw.upper().startswith('RC'):
                    number += 115
            index[(spec.set_code, int(number), normalized_name(card['name']))].append(card)
    return index


def add_external_sources(index, directory):
    """Fill unpublished promo metadata from the original expansion catalogs.

    Never replace a printed JSON record and never assume a missing resistance
    value is 30. These files are data only; no JavaScript is executed.
    """
    from spirit.tools.import_standard_sets import STANDARD_SETS
    for stem, (_, code) in STANDARD_SETS.items():
        path = Path(directory) / f'{stem}-cards.js'
        if not path.is_file():
            continue
        match = re.search(r'=\s*(\{.*\})\s*;\s*\n\s*if \(typeof window',
                          path.read_text(encoding='utf-8'), re.S)
        if match is None:
            raise ValueError(f'Unrecognized external catalog: {path}')
        for card in json.loads(match.group(1))['cards']:
            if card.get('kind') != 'pokemon':
                continue
            identity = (code, int(card['n']), normalized_name(card['name']))
            if identity in index:
                continue
            resistances = []
            if card.get('resist'):
                resistances = [{'type': card['resist'].title(),
                                'value': card['resistValue']}]
            index[identity] = [{'id': f"{stem}-{card['n']}",
                                'number': str(card['n']), 'name': card['name'],
                                'resistances': resistances}]


def audit(index):
    loader.load_all()
    counts = Counter()
    resistant = Counter()
    mismatches, unmatched = [], []
    for guid, model in loader.cards_by_guid.items():
        definition = CARD_DEFS_BY_GUID.get(guid)
        if not isinstance(definition, PokemonCardDef):
            continue
        name = definition.display_name
        if not name:
            name = definition.name.split('.')[-2]
        identity = (definition.set_code, int(definition.collector_number), normalized_name(name))
        candidates = index.get(identity, [])
        path = Path(loader.script_by_guid[guid])
        printed = path.stem.rsplit('_', 1)[-1].upper()
        exact = [c for c in candidates if str(c['number']).upper() == printed]
        if exact:
            candidates = exact
        values = {printed_resistance(c) for c in candidates}
        label = f'{definition.set_code}/{path.stem}'
        if len(values) != 1:
            unmatched.append(label)
            continue
        expected = next(iter(values))
        counts[definition.set_code] += 1
        if expected[1]:
            resistant[expected[1]] += 1
        # Public card datasets repeat the whole V-UNION's characteristics on
        # all four entries. Only the assembled Pokemon has that Resistance;
        # checking a fragment against it would manufacture stats outside play.
        assembled_layers = []
        if getattr(definition, 'vunion_part', False):
            from spirit.game.vunion import assembled_definition
            from spirit.game.models.card import PokemonCard
            combined = assembled_definition(definition.vunion_name)
            raw = combined.to_archetype_dict()
            combined_model = PokemonCard(combined.guid, combined.key, raw['attributes'])
            assembled_layers = [
                ('assembled-definition', combined.extra_attributes, expected),
                ('assembled-model', combined_model.attributes, expected),
                ('assembled-client', combined_model.to_archetype_attributes('resistance-audit'), expected),
            ]
            expected = (PokemonTypes.UNSET.value, 0)
        # Validate mechanics, loaded model and client serialization separately.
        layers = [(layer, attrs, expected) for layer, attrs in (
            ('definition', definition.extra_attributes),
            ('model', model.attributes),
            ('client', model.to_archetype_attributes('resistance-audit')),
        )]
        for layer, attrs, expected in [*layers, *assembled_layers]:
            actual = attribute_resistance(attrs)
            if actual != expected:
                mismatches.append({'card': label, 'layer': layer,
                                   'expected': expected, 'actual': actual})
    return {'checked': sum(counts.values()), 'sets': dict(sorted(counts.items())),
            'resistant': dict(sorted(resistant.items())),
            'mismatches': mismatches, 'unmatched': unmatched}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-dir', action='append', type=Path, default=[])
    parser.add_argument('--external-catalog-dir', type=Path)
    args = parser.parse_args()
    index = load_sources([DATA_ROOT, *args.source_dir])
    if args.external_catalog_dir:
        add_external_sources(index, args.external_catalog_dir)
    result = audit(index)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 1 if result['mismatches'] or result['unmatched'] else 0


if __name__ == '__main__':
    raise SystemExit(main())
