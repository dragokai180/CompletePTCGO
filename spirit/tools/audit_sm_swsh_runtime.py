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
from spirit.tools.audit_printed_resistance import load_sources, normalized_name
from spirit.tools.install_recent_card_art import DATA_ROOT

ERA_PATTERN = r"(SM[0-9]+|Promo_SM|SL|DM|HF|GUM|SWSH[0-9]+|Promo_SWSH|SWSH_Energy|CEL25|PGO|CZ)"


async def audit(set_pattern=ERA_PATTERN):
    loader.load_all()
    printed = load_sources([DATA_ROOT], pokemon_only=False)

    def rule_text(definition, runner):
        text = getattr(runner, 'game_text', '') or ''
        if not text and not isinstance(runner, Ability):
            name = definition.display_name or definition.name
            candidates = printed.get((definition.set_code, definition.collector_number,
                                      normalized_name(name)), [])
            if candidates:
                text = ' '.join(candidates[0].get('rules') or [])
        return text

    groups = {}
    cards = [d for d in CARD_DEFS_BY_GUID.values()
             if re.fullmatch(set_pattern, d.set_code, re.I)]
    for definition in cards:
        for kind, title, runner, scripted in _plan_tests(definition):
            text = rule_text(definition, runner)
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
            text = rule_text(definition, runner)
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
    parser.add_argument('--set-pattern', default=ERA_PATTERN,
                        help='Use .* to include all registered expansions.')
    args = parser.parse_args()
    report = asyncio.run(audit(args.set_pattern))
    args.json.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding='utf8')
    print({k: v for k, v in report.items() if k != 'rows'})
    for row in report['rows']:
        if row['status'] not in ('PASS', 'SKIP'):
            print(row['status'], row['card'], row['title'], row['detail'])


if __name__ == '__main__':
    main()
