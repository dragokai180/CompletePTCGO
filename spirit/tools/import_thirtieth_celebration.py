"""Import the main 30th Celebration set (never the separate Classic Collection)."""
from __future__ import annotations

import argparse
import json
from concurrent.futures import ThreadPoolExecutor

import requests

from spirit.tools.import_standard_sets import (
    ROOT, clean_name, download_one, existing_named_modules, mechanics_signature,
    render_pokemon, render_reprint, render_trainer,
)

DATA = ROOT / 'tools/card-builder/data/pokemon-tcg-data/cards/en/me55.json'
SOURCE = 'https://raw.githubusercontent.com/PokemonTCG/pokemon-tcg-data/master/cards/en/me55.json'
RGB_NUMBERS = {'R': 159, 'G': 160, 'B': 161}


def normalized_card(original):
    card = json.loads(json.dumps(original))
    number = card['number']
    if number in RGB_NUMBERS:
        card['_collector_number_text'] = number
        card['number'] = str(RGB_NUMBERS[number])
    # Verified against the English prints / TCGdex 30th-093 and 30th-096.
    if card['name'] == 'Murkrow':
        card['resistances'] = [{'type': 'Fighting', 'value': '-30'}]
    if card['name'] == 'Zoroark':
        card['evolvesFrom'] = 'Zorua'
    for field in ('attacks', 'abilities'):
        for effect in card.get(field, []):
            effect['text'] = effect.get('text', '').replace('oppoennt', 'opponent').replace('Knocket Out', 'Knocked Out').replace('Fire Energy attaches', 'Fire Energy attached').replace('2 Stadium card,', '2 Stadium cards,')
    return card


def run(refresh=False, download=False):
    if refresh or not DATA.exists():
        response = requests.get(SOURCE, timeout=60)
        response.raise_for_status()
        cards = response.json()
        if not isinstance(cards, list) or not all(c['id'].startswith('me55-') for c in cards):
            raise ValueError('Expected the main me55 catalog, not me55c.')
        DATA.parent.mkdir(parents=True, exist_ok=True)
        DATA.write_text(json.dumps(cards, ensure_ascii=False, indent=2) + '\n', encoding='utf8')
    originals = json.loads(DATA.read_text(encoding='utf8'))
    cards = [normalized_card(c) for c in originals]
    by_name = {c['name']: c for c in cards}
    named = existing_named_modules()
    signatures = {}
    scripts = ROOT / 'spirit/game/scripts/cards/ME55'
    assets = ROOT / 'spirit/assets/cards/ME55'
    scripts.mkdir(parents=True, exist_ok=True)
    assets.mkdir(parents=True, exist_ok=True)
    tasks = []
    for card, original in zip(cards, originals):
        stem = f"{clean_name(card['name'])}_{card['number']}"
        path = scripts / (stem + '.py')
        sig = mechanics_signature(card)
        base = signatures.get(sig)
        if card['supertype'] == 'Trainer':
            base = named.get(('trainer', card['name']))
        if base:
            source = render_reprint(card, 'ME55', base)
            if card.get('_collector_number_text'):
                source += f"\ncard.extra_attributes['200790'] = {{'type': 'string', 'value': {card['_collector_number_text']!r}}}\n"
        elif card['supertype'] == 'Pokémon':
            source = render_pokemon(card, 'ME55', by_name)
            source += '\nfrom spirit.game.card_effects.thirtieth_celebration import configure\nconfigure(card)\n'
        else:
            source = render_trainer(card, 'ME55')
        if not path.exists():
            path.write_text(source, encoding='utf8')
        signatures.setdefault(sig, f'spirit.game.scripts.cards.ME55.{stem}')
        target = assets / (stem + '.png')
        if not target.exists():
            tasks.append((original['images']['large'], target))
    sets_path = ROOT / 'spirit/database/json_data/sets.json'
    sets = json.loads(sets_path.read_text(encoding='utf8'))
    if not any(s['name'] == 'ME55' for s in sets):
        sets.append(dict(name='ME55', externalId='30C', number=1350, count=len(cards),
            filter=True, block='NONE', legalFormats=[
                '6402e830-7fed-4cd1-b172-2a320047c2bb',
                '98c83df9-ec82-4193-84a8-104115ce4e25',
                '6a1dec5a-34db-4cee-a503-4ee759304135'],
            featuredArchetypes=[], visibleUnfilterable=False, promo=False))
        sets_path.write_text(json.dumps(sets, indent=2, ensure_ascii=False)+'\n', encoding='utf8')
    formats_path = ROOT / 'spirit/database/json_data/formats.json'
    formats = json.loads(formats_path.read_text(encoding='utf8'))
    for fmt in formats['formats']:
        if fmt['key'] in ('Standard', 'StandardNightly', 'Expanded', 'Unlimited') and 'ME55' not in fmt['sets']:
            fmt['sets'].append('ME55')
    formats_path.write_text(json.dumps(formats, indent=2, ensure_ascii=False)+'\n', encoding='utf8')
    print(f'ME55: {len(cards)} prints; {len(tasks)} missing images.', flush=True)
    if download:
        with ThreadPoolExecutor(max_workers=8) as pool:
            results = list(pool.map(download_one, tasks))
        failed = [detail for ok, detail in results if not ok]
        print(f'Images downloaded: {len(results)-len(failed)}; failures: {len(failed)}', flush=True)
        for detail in failed:
            print(detail)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--refresh', action='store_true')
    parser.add_argument('--download-missing', action='store_true')
    args = parser.parse_args()
    run(args.refresh, args.download_missing)
