"""Exercise every registered printing; record evidence, never semantic approval.

Run with --jsonl audits/results/catalog-campaign.jsonl. Each row is one
printing/behavior/coin branch. PASS means execution and tree invariants passed,
not that every clause of the printed text has been independently proved.
"""
import argparse
import asyncio
import json
import re
from collections import Counter
from pathlib import Path

from spirit.game.data_utils import CARD_DEFS_BY_GUID, Ability, EnergyCardDef
from spirit.game.scripts.cards import loader
from spirit.tools.effect_smoke import (
    _plan_tests, run_one, pick_filler_basic, pick_filler_item, basic_energy_guids,
)
from spirit.tools.semantic_effect_audit import (
    _Trace, _EVENTS, _semantic_scenario,
)
from spirit.tools.audit_printed_resistance import load_sources, normalized_name
from spirit.tools.install_recent_card_art import DATA_ROOT


def tree_errors(board):
    errors, seen = [], set()
    def visit(entity):
        if entity.entity_id in seen:
            errors.append('duplicate/cyclic entity: ' + entity.entity_id)
            return
        seen.add(entity.entity_id)
        if board.get_entity(entity.entity_id) is not entity:
            errors.append('tree/cache mismatch: ' + entity.entity_id)
        for child in entity.children:
            if child.parent is not entity or child.parent_id != entity.entity_id:
                errors.append('parent mismatch: ' + child.entity_id)
            visit(child)
    visit(board.playmat)
    return errors


async def audit(args):
    loader.load_all()
    printed = load_sources([DATA_ROOT], pokemon_only=False)
    cards = sorted({d.guid: d for d in CARD_DEFS_BY_GUID.values()
                    if re.fullmatch(args.set_pattern, d.set_code, re.I)}.values(),
                   key=lambda d: (d.set_code, str(d.collector_number), d.guid))
    filler, energies, item = pick_filler_basic(), basic_energy_guids(), pick_filler_item()
    if args.retry_report:
        previous = [json.loads(line) for line in args.retry_report.read_text(encoding='utf8').splitlines()]
        wanted = {row['guid'] for row in previous if row['status'] != 'PASS'}
        cards = [d for d in cards if d.guid in wanted]
    counts = Counter()
    args.jsonl.parent.mkdir(parents=True, exist_ok=True)
    with args.jsonl.open('w', encoding='utf8') as output, _Trace():
        for index, definition in enumerate(cards, 1):
            plans = _plan_tests(definition)
            if isinstance(definition, EnergyCardDef) and not any(p[0] == 'energy-attach' for p in plans):
                plans.append(('energy-attach', '(attach)', 'energy-attach', True))
            if not plans:
                output.write(json.dumps({'guid': definition.guid, 'set': definition.set_code,
                    'number': definition.collector_number, 'card': definition.display_name,
                    'status': 'UNPLANNED'}) + '\n')
                counts['UNPLANNED'] += 1
            for kind, title, runner, scripted in plans:
                text = getattr(runner, 'game_text', '') or ''
                if not text and not isinstance(runner, Ability):
                    source = printed.get((definition.set_code, definition.collector_number,
                        normalized_name(definition.display_name or definition.name)), [])
                    if source:
                        text = ' '.join(source[0].get('rules') or [])
                category = 'attack' if kind == 'attack' else 'ability' if (
                    'ability' in kind or 'trigger' in kind) else 'trainer'
                coins = (True, False) if re.search(r'coin|heads|tails', text, re.I) else (None,)
                for coin in coins:
                    events, captured = [], []
                    setup = _semantic_scenario(category, text.lower(), forced_coin=coin)
                    def prepare(rig, entities, behavior):
                        captured.append(rig)
                        if setup:
                            setup(rig, entities, behavior)
                    token = _EVENTS.set(events)
                    try:
                        result = await run_one(definition.display_name, definition, kind,
                            title, runner, filler, energies, scripted, args.timeout, item,
                            scenario_setup=prepare)
                    finally:
                        _EVENTS.reset(token)
                    errors = tree_errors(captured[0].board) if captured else ['no board']
                    status = 'INVARIANT_FAIL' if errors else result.status
                    row = {'guid': definition.guid, 'set': definition.set_code,
                           'number': definition.collector_number, 'card': definition.display_name,
                           'kind': kind, 'title': title, 'text': text, 'coin': coin,
                           'status': status, 'detail': result.detail,
                           'tree_errors': errors, 'events': dict(Counter(events))}
                    output.write(json.dumps(row, ensure_ascii=False) + '\n')
                    counts[status] += 1
            output.flush()
            if index % 100 == 0:
                print(f'{index}/{len(cards)} printings: {dict(counts)}', flush=True)
    print({'printings': len(cards), 'probes': sum(counts.values()), 'statuses': dict(counts)}, flush=True)
    return int(any(status != 'PASS' and count for status, count in counts.items()))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--jsonl', type=Path, required=True)
    parser.add_argument('--set-pattern', default='.*')
    parser.add_argument('--timeout', type=float, default=3)
    parser.add_argument('--retry-report', type=Path)
    raise SystemExit(asyncio.run(audit(parser.parse_args())))


if __name__ == '__main__':
    main()
