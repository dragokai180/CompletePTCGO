"""Runtime dispatch audit for SM/SWSH, including authored and inherited effects.

This detects crashes/missing dispatch and records rule operations. A passing
probe is NOT a proof of target, timing, or arithmetic correctness.
"""
import argparse
import asyncio
import json
import re
from collections import Counter
from pathlib import Path

from spirit.game.data_utils import CARD_DEFS_BY_GUID, Ability
from spirit.game.scripts.cards import loader
from spirit.tools.effect_smoke import (
    _plan_tests, run_one, pick_filler_basic, pick_filler_item, basic_energy_guids,
)
from spirit.tools.semantic_effect_audit import _Trace, _EVENTS, _semantic_scenario

ERA_PATTERN = r"(SM[0-9]+|Promo_SM|SL|DM|HF|GUM|SWSH[0-9]+|Promo_SWSH|SWSH_Energy|CEL25|PGO|CZ)"


async def audit():
    loader.load_all()
    groups = {}
    cards = [d for d in CARD_DEFS_BY_GUID.values()
             if re.fullmatch(ERA_PATTERN, d.set_code, re.I)]
    for definition in cards:
        for kind, title, runner, scripted in _plan_tests(definition):
            text = getattr(runner, 'game_text', '') or ''
            effect = getattr(runner, 'effect', None) if isinstance(runner, Ability) else getattr(definition, 'effect', None)
            # Shared text families have a separate semantic report. Include
            # authored effects and every passive/energy hook here.
            if getattr(effect, '__name__', '') in ('bw_legacy_attack', 'bw_legacy_ability', 'standard_ability'):
                continue
            key = (definition.display_name, kind, title, text,
                   getattr(runner, 'damage', None), str(getattr(runner, 'cost', '')),
                   getattr(effect, '__module__', ''), getattr(effect, '__qualname__', ''))
            if key not in groups:
                groups[key] = [definition, (kind, title, runner, scripted), []]
            groups[key][2].append({'set': definition.set_code, 'number': definition.collector_number,
                                  'guid': definition.guid})
    filler, energies, item = pick_filler_basic(), basic_energy_guids(), pick_filler_item()
    rows = []
    with _Trace():
        for i, (definition, plan, copies) in enumerate(groups.values(), 1):
            kind, title, runner, scripted = plan
            text = getattr(runner, 'game_text', '') or ''
            events = []
            token = _EVENTS.set(events)
            try:
                result = await run_one(definition.display_name, definition, kind, title, runner,
                                       filler, energies, scripted, 3, item,
                                       scenario_setup=_semantic_scenario(
                                           'attack' if kind == 'attack' else
                                           'ability' if 'ability' in kind or 'trigger' in kind else 'trainer',
                                           text.lower()))
            finally:
                _EVENTS.reset(token)
            rows.append({'card': definition.display_name, 'kind': kind, 'title': title,
                         'text': text, 'status': result.status, 'detail': result.detail,
                         'events': dict(Counter(events)), 'printings': copies})
            if i % 100 == 0:
                print(f"Runtime probes {i}/{len(groups)}", flush=True)
    return {'cards_in_scope': len(cards), 'probes': len(rows),
            'statuses': dict(Counter(r['status'] for r in rows)), 'rows': rows}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--json', type=Path, required=True)
    args = parser.parse_args()
    report = asyncio.run(audit())
    args.json.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding='utf8')
    print({k: v for k, v in report.items() if k != 'rows'})
    for row in report['rows']:
        if row['status'] not in ('PASS', 'SKIP'):
            print(row['status'], row['card'], row['title'], row['detail'])


if __name__ == '__main__':
    main()
