"""Complete English SWSH promos, preserving existing scripts and V-UNION parts."""
import argparse
import json

from spirit.tools.import_standard_sets import (
    ROOT, clean_name, mechanics_signature, module_for, numeric,
    render_pokemon, render_reprint, render_trainer, existing_named_modules, guid_for,
)
from spirit.tools.install_recent_card_art import DATA_ROOT, RECENT_SETS


def plan():
    scripts = ROOT / 'spirit/game/scripts/cards'
    existing = {(p.parent.name, numeric(p.stem.rsplit('_', 1)[-1])): p
                for p in scripts.glob('*/*.py') if p.stem != '__init__'}
    signatures = {}
    named = existing_named_modules()
    by_name = {}
    for stem, entry in RECENT_SETS.items():
        path = DATA_ROOT / (stem + '.json')
        if not path.exists() or stem == 'swshp':
            continue
        for row in json.loads(path.read_text(encoding='utf-8')):
            by_name.setdefault(row['name'], row)
            printed = str(row.get('number', ''))
            if not printed.isdigit():
                continue
            base = existing.get((entry.set_code, int(printed)))
            if base and row['supertype'] == 'Pokémon':
                signatures.setdefault(mechanics_signature(row), module_for(base))
    promos = json.loads((DATA_ROOT / 'swshp.json').read_text(encoding='utf-8'))
    by_name.update({r['name']: r for r in promos})
    result = []
    for row in promos:
        number = numeric(row['number'])
        if ('Promo_SWSH', number) in existing:
            continue
        path = scripts / 'Promo_SWSH' / f"{clean_name(row['name'])}_{number}.py"
        base = signatures.get(mechanics_signature(row))
        if row['supertype'] == 'Trainer':
            base = named.get(('trainer', row['name']))
        row = dict(row, _collector_number_text=row['number'])
        if 'V-UNION' in row.get('subtypes', []):
            source = ('from spirit.game.vunion import make_vunion\n\n'
                      f"card = make_vunion('Morpeko', {number})\n")
        elif base:
            source = render_reprint(row, 'Promo_SWSH', base)
        elif row['supertype'] == 'Pokémon':
            source = render_pokemon(row, 'Promo_SWSH', by_name)
        elif row['supertype'] == 'Trainer':
            source = render_trainer(row, 'Promo_SWSH')
        else:
            raise ValueError(f'Unsupported promo: {row["id"]}')
        if base or row['supertype'] == 'Trainer':
            source += f"\ncard.extra_attributes['200790'] = {{'type': 'string', 'value': {row['number']!r}}}\n"
        if number == 135:
            source = source.replace('stage=PokemonStage.BASIC', 'stage=PokemonStage.LEVELUP')
        if not base and row['supertype'] == 'Pokémon' and 'V-UNION' not in row.get('subtypes', []):
            source += ('\nfrom spirit.game.card_effects.swsh_promos import configure_promo\n'
                       'configure_promo(card)\n')
        result.append((row, path, source, base))
        signatures.setdefault(mechanics_signature(row), module_for(path))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    rows = plan()
    print(f'Missing: {len(rows)}; linked reprints: {sum(bool(x[3]) for x in rows)}')
    for row, path, source, base in rows:
        if args.apply:
            path.write_text(source, encoding='utf-8')
        if not base and not args.apply:
            print(row['number'], row['name'], json.dumps(
                [row.get('abilities', []), row.get('attacks', []), row.get('rules', [])], ensure_ascii=False))
    if args.apply:
        promos = json.loads((DATA_ROOT / 'swshp.json').read_text(encoding='utf-8'))
        path = ROOT / 'spirit/database/json_data/sets.json'
        sets = json.loads(path.read_text(encoding='utf-8'))
        for entry in sets:
            if entry['name'] == 'Promo_SWSH':
                entry['count'] = max(numeric(row['number']) for row in promos)
        path.write_text(json.dumps(sets, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
        # Anniversary novelty promos explicitly say they cannot be used at
        # official tournaments. Keep them collectible, outside deck formats.
        illegal = [guid_for(row['id']) for row in promos if any(
            'cannot be used at official tournaments' in r for r in row.get('rules', []))]
        path = ROOT / 'spirit/database/json_data/formats.json'
        formats = json.loads(path.read_text(encoding='utf-8'))
        for fmt in formats['formats']:
            fmt['bannedCards'] = list(dict.fromkeys(fmt.get('bannedCards', []) + illegal))
        path.write_text(json.dumps(formats, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
