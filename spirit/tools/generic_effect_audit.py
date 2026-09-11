"""Inventory card behaviors routed through the shared text interpreters.

Unlike ``effect_coverage``, this scanner does not call a generic fallback
"implemented" merely because it is callable.  It groups the exact printed
text, title and fallback kind so every family can be reviewed once while all
of its printings remain visible.

Usage::

    python -m spirit.tools.generic_effect_audit --kind ability --top 50
    python -m spirit.tools.generic_effect_audit --json generic-effects.json
"""
from __future__ import annotations

import argparse
import ast
import json
from collections import defaultdict
from pathlib import Path


ROOT = Path("spirit/game/scripts/cards")
CARD_CALLS = {
    "PokemonCardDef", "ItemCardDef", "SupporterCardDef", "StadiumCardDef",
    "PokemonToolCardDef", "EnergyCardDef", "FossilItemCardDef",
}


def _name(node):
    return node.id if isinstance(node, ast.Name) else None


def _literal(node, default="", constants=None):
    if isinstance(node, ast.Name) and constants is not None:
        return constants.get(node.id, default)
    try:
        value = ast.literal_eval(node)
    except (ValueError, TypeError, SyntaxError):
        return default
    return value if isinstance(value, str) else default


def _kwargs(call):
    return {kw.arg: kw.value for kw in call.keywords if kw.arg}


def _norm(text):
    return " ".join(
        (text or "").replace("Pok�mon", "Pokémon")
        .replace("pok�mon", "pokémon").replace("’", "'").lower().split()
    )


def scan():
    rows = []
    for path in ROOT.rglob("*.py"):
        if path.name == "__init__.py" or "__pycache__" in path.parts:
            continue
        try:
            tree = ast.parse(path.read_text(encoding="utf-8"), str(path))
        except (OSError, SyntaxError, UnicodeDecodeError):
            continue
        constants = {}
        for statement in tree.body:
            if not isinstance(statement, (ast.Assign, ast.AnnAssign)):
                continue
            value_node = statement.value
            try:
                value = ast.literal_eval(value_node)
            except (ValueError, TypeError, SyntaxError):
                continue
            if not isinstance(value, str):
                continue
            targets = statement.targets if isinstance(statement, ast.Assign) \
                else [statement.target]
            for target in targets:
                if isinstance(target, ast.Name):
                    constants[target.id] = value
        card_call = next((
            node.value for node in ast.walk(tree)
            if isinstance(node, ast.Assign) and isinstance(node.value, ast.Call)
            and _name(node.value.func) in CARD_CALLS
        ), None)
        if card_call is None:
            continue
        card_kw = _kwargs(card_call)
        display = _literal(
            card_kw.get("display_name"), path.stem.rsplit("_", 1)[0], constants
        )
        set_code = path.parent.name

        effect = card_kw.get("effect")
        if isinstance(effect, ast.Call) and _name(effect.func) == "standard_trainer_effect":
            text = _literal(effect.args[0], constants=constants) if effect.args else ""
            rows.append(("trainer", display, "(on play)", text, set_code, str(path)))
        passive = card_kw.get("passive")
        if isinstance(passive, ast.Call) and _name(passive.func) == "standard_passive":
            text = _literal(passive.args[0], constants=constants) if passive.args else ""
            rows.append(("passive", display, "(card passive)", text, set_code, str(path)))

        for node in ast.walk(card_call):
            if not isinstance(node, ast.Call) or _name(node.func) not in {"Ability", "Attack"}:
                continue
            kw = _kwargs(node)
            passive = kw.get("passive")
            if isinstance(passive, ast.Call) and _name(passive.func) == "standard_passive":
                text = _literal(passive.args[0], constants=constants) if passive.args else ""
                title = _literal(kw.get("title"), "(untitled)", constants)
                rows.append(("passive", display, title, text, set_code, str(path)))
            effect = kw.get("effect")
            fallback = _name(effect)
            if fallback not in {"standard_ability", "standard_attack"}:
                continue
            title = _literal(kw.get("title"), "(untitled)", constants)
            text = _literal(kw.get("game_text"), "", constants)
            kind = "ability" if fallback == "standard_ability" else "attack"
            rows.append((kind, display, title, text, set_code, str(path)))
    return rows


def grouped(rows):
    groups = defaultdict(list)
    for kind, card, title, text, set_code, path in rows:
        groups[(kind, title, _norm(text))].append({
            "card": card, "set": set_code, "path": path,
        })
    return groups


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--kind", choices=("trainer", "ability", "attack", "passive"))
    parser.add_argument("--top", type=int, default=40)
    parser.add_argument("--json")
    args = parser.parse_args()
    groups = grouped(scan())
    selected = [
        (key, copies) for key, copies in groups.items()
        if args.kind is None or key[0] == args.kind
    ]
    selected.sort(key=lambda row: (-len(row[1]), row[0][1], row[0][2]))
    by_kind = defaultdict(lambda: [0, 0])
    for (kind, _, _), copies in selected:
        by_kind[kind][0] += 1
        by_kind[kind][1] += len(copies)
    for kind in sorted(by_kind):
        families, printings = by_kind[kind]
        print(f"{kind:8} {families:5} families {printings:5} direct printings")
    for (kind, title, text), copies in selected[:args.top]:
        cards = ", ".join(sorted({row['card'] for row in copies})[:4])
        sets = ",".join(sorted({row['set'] for row in copies}))
        print(f"\n[{kind}] {len(copies)}x {title} -- {cards} ({sets})")
        print(f"  {text}")
    if args.json:
        payload = [
            {"kind": key[0], "title": key[1], "text": key[2],
             "printings": copies}
            for key, copies in selected
        ]
        Path(args.json).write_text(json.dumps(payload, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
