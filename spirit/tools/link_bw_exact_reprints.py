"""Link mechanically identical Black & White cards to implemented printings.

Unlike the Trainer-only linker, this compares the complete printed Pokemon
identity (stats and every attack/Ability text field).  Effect callables are
deliberately ignored: they are precisely what the reprint inherits.
"""

from __future__ import annotations

import argparse
import ast
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CARDS = ROOT / "spirit" / "game" / "scripts" / "cards"
BW_SETS = {
    "BW1", "BW2", "BW3", "BW4", "BW5", "BW6", "DV", "BW7", "BW8",
    "BW9", "BW11", "PROMO_BW",
}
CARD_CLASSES = {
    "PokemonCardDef", "ItemCardDef", "SupporterCardDef", "StadiumCardDef",
    "PokemonToolCardDef", "FossilItemCardDef", "EnergyCardDef",
}
IGNORED_ABILITY_FIELDS = {
    "effect", "passive", "condition", "ability_id", "is_granted",
}
IGNORED_CARD_FIELDS = {
    "guid", "key", "collector_number", "set_code", "rarity",
    "regulation_mark", "effect", "passive", "condition", "ability",
    "companion", "granted_abilities", "on_attach", "attach_condition",
    "attach_cost", "on_carrier_knocked_out", "on_discarded_by_carrier_attack",
}


def _call_name(call: ast.Call) -> str:
    return call.func.id if isinstance(call.func, ast.Name) else ""


def _card_call(tree: ast.AST) -> ast.Call | None:
    for node in ast.walk(tree):
        if not isinstance(node, ast.Assign) or not isinstance(node.value, ast.Call):
            continue
        if _call_name(node.value) in CARD_CLASSES:
            return node.value
    return None


def _norm_text(value: str) -> str:
    return re.sub(r"\s+", " ", value.replace("Pokémon", "Pokemon")).strip().casefold()


def _value(node: ast.expr):
    try:
        value = ast.literal_eval(node)
        if isinstance(value, str):
            return _norm_text(value)
        if isinstance(value, list):
            return tuple(value)
        if isinstance(value, dict):
            return tuple(sorted(value.items()))
        return value
    except (ValueError, TypeError):
        return ast.unparse(node).replace(" ", "")


def _ability_signature(node: ast.expr):
    if not isinstance(node, ast.Call):
        return ast.unparse(node)
    fields = []
    for kw in node.keywords:
        if kw.arg and kw.arg not in IGNORED_ABILITY_FIELDS:
            fields.append((kw.arg, _value(kw.value)))
    return (_call_name(node), tuple(sorted(fields)))


def _card_signature(call: ast.Call):
    fields = []
    for kw in call.keywords:
        if not kw.arg or kw.arg in IGNORED_CARD_FIELDS:
            continue
        if kw.arg == "abilities" and isinstance(kw.value, ast.List):
            value = tuple(_ability_signature(item) for item in kw.value.elts)
        else:
            value = _value(kw.value)
        fields.append((kw.arg, value))
    return (_call_name(call), tuple(sorted(fields)))


def _literal(call: ast.Call, name: str, default=None):
    for kw in call.keywords:
        if kw.arg == name:
            try:
                return ast.literal_eval(kw.value)
            except (ValueError, TypeError):
                return default
    return default


def _dotted(call: ast.Call, name: str, default: str) -> str:
    for kw in call.keywords:
        if kw.arg == name:
            return ast.unparse(kw.value)
    return default


def inspect(path: Path):
    source = path.read_text(encoding="utf-8")
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return None
    call = _card_call(tree)
    if call is None:
        return None
    return {
        "path": path,
        "signature": _card_signature(call),
        "number": int(_literal(call, "collector_number", 0) or 0),
        "rarity": _dotted(call, "rarity", "Rarities.Common"),
        "implemented": "unimplemented" not in source,
    }


def _source_text(target, source) -> str:
    rel = source["path"].relative_to(CARDS).as_posix()
    target_set = target["path"].parent.name
    source_set = source["path"].parent.name
    ref = source["path"].name if target_set == source_set else f"../{rel}"
    lines = [
        "from spirit.game.data_utils import reprint, sibling_card",
        "from spirit.game.attributes import Rarities",
        "",
        f'card = reprint(sibling_card(__file__, "{ref}"),',
        f'               collector_number={target["number"]}, rarity={target["rarity"]}',
    ]
    if target_set != source_set:
        lines[-1] += ","
        lines.append(f'               set_code="{target_set}", key="{target_set}"')
    lines[-1] += ")"
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    records = [record for path in CARDS.glob("*/*.py")
               if path.name != "__init__.py" and (record := inspect(path))]
    sources = {}
    for record in records:
        if record["implemented"]:
            sources.setdefault(record["signature"], []).append(record)
    linked = []
    for target in records:
        if target["path"].parent.name not in BW_SETS or target["implemented"]:
            continue
        candidates = [candidate for candidate in sources.get(target["signature"], [])
                      if candidate["path"] != target["path"]]
        if not candidates:
            continue
        candidates.sort(key=lambda item: (
            item["path"].parent.name in BW_SETS, str(item["path"])
        ))
        source = candidates[0]
        linked.append((target, source))
        if args.apply:
            target["path"].write_text(_source_text(target, source), encoding="utf-8")
    for target, source in linked:
        print(f'{target["path"].relative_to(CARDS)} <- {source["path"].relative_to(CARDS)}')
    print(f"{len(linked)} exact reprints {'linked' if args.apply else 'available'}")


if __name__ == "__main__":
    main()
