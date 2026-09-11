"""Replace generated BW Trainer stubs with working same-name reprints.

Trainer cards keep their rules identity across printings.  The project already
contains many later printings with tested effects, so a thin ``reprint`` is
safer than duplicating that behavior in every Black & White set.
"""

from __future__ import annotations

import argparse
import ast
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CARDS = ROOT / "spirit" / "game" / "scripts" / "cards"
BW_SETS = {
    "BW1", "BW2", "BW3", "BW4", "BW5", "BW6", "DV", "BW7", "BW8",
    "BW9", "BW11", "PROMO_BW",
}
TRAINER_CLASSES = {
    "ItemCardDef", "SupporterCardDef", "StadiumCardDef", "PokemonToolCardDef",
    "FossilItemCardDef",
}


def card_call(tree: ast.AST) -> ast.Call | None:
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and isinstance(node.value, ast.Call):
            func = node.value.func
            if isinstance(func, ast.Name) and func.id in TRAINER_CLASSES:
                return node.value
    return None


def kwargs(call: ast.Call) -> dict[str, ast.expr]:
    return {kw.arg: kw.value for kw in call.keywords if kw.arg}


def literal(node: ast.expr | None, default=None):
    try:
        return ast.literal_eval(node) if node is not None else default
    except (TypeError, ValueError):
        return default


def dotted(node: ast.expr | None, default: str) -> str:
    if node is None:
        return default
    try:
        return ast.unparse(node)
    except Exception:
        return default


def inspect(path: Path):
    source = path.read_text(encoding="utf-8")
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return None
    call = card_call(tree)
    if call is None:
        return None
    fields = kwargs(call)
    return {
        "path": path,
        "class": call.func.id,
        "name": literal(fields.get("display_name"), ""),
        "number": int(literal(fields.get("collector_number"), 0) or 0),
        "rarity": dotted(fields.get("rarity"), "Rarities.Common"),
        "implemented": "unimplemented" not in source,
    }


def source_text(target, source) -> str:
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

    records = [r for path in CARDS.glob("*/*.py") if path.name != "__init__.py"
               if (r := inspect(path))]
    sources: dict[tuple[str, str], list] = {}
    for record in records:
        if record["implemented"] and record["name"]:
            sources.setdefault((record["class"], record["name"]), []).append(record)

    linked = []
    for target in records:
        if target["path"].parent.name not in BW_SETS or target["implemented"]:
            continue
        candidates = sources.get((target["class"], target["name"]), [])
        if not candidates:
            continue
        candidates.sort(key=lambda r: (r["path"].parent.name in BW_SETS,
                                       str(r["path"])))
        source = candidates[0]
        linked.append((target, source))
        if args.apply:
            target["path"].write_text(source_text(target, source), encoding="utf-8")

    for target, source in linked:
        print(f'{target["path"].relative_to(CARDS)} <- {source["path"].relative_to(CARDS)}')
    print(f"{len(linked)} Trainer reprints {'linked' if args.apply else 'available'}")


if __name__ == "__main__":
    main()
