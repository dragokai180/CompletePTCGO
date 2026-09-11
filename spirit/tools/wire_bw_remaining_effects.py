"""Wire generated BW-era ``unimplemented`` markers to shared mechanics.

This is intentionally an idempotent source migration.  Hand-written effects
are never touched; only the exact generated marker is replaced.
"""

from __future__ import annotations

import ast
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CARD_ROOT = ROOT / "spirit" / "game" / "scripts" / "cards"
SETS = ("BW1", "BW2", "BW3", "BW4", "BW5", "BW6", "DV", "BW7",
        "BW8", "BW9", "BW10", "BW11", "PROMO_BW")
BW_IMPORT = (
    "from spirit.game.card_effects.bw_era import "
    "bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, "
    "bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, "
    "bw_stadium_ability, bw_stadium_triggers\n"
)


def _blocks(source: str, token: str):
    start = 0
    while True:
        pos = source.find(token + "(", start)
        if pos < 0:
            return
        depth = 0
        quote = None
        escaped = False
        for i in range(pos + len(token), len(source)):
            ch = source[i]
            if quote:
                if escaped:
                    escaped = False
                elif ch == "\\":
                    escaped = True
                elif ch == quote:
                    quote = None
                continue
            if ch in "'\"":
                quote = ch
            elif ch == "(":
                depth += 1
            elif ch == ")":
                depth -= 1
                if depth == 0:
                    yield pos, i + 1, source[pos:i + 1]
                    start = i + 1
                    break
        else:
            return


def _display_name(source: str) -> str:
    match = re.search(r"display_name\s*=\s*(\"(?:\\.|[^\"])*\"|'(?:\\.|[^'])*')", source)
    return ast.literal_eval(match.group(1)) if match else ""


def _wire_pokemon(source: str) -> tuple[str, int]:
    replacements = []
    for token in ("Attack", "Ability"):
        for start, end, block in _blocks(source, token):
            if token == "Attack" and "effect=unimplemented" in block:
                new = block.replace("effect=unimplemented", "effect=bw_legacy_attack")
            elif token == "Ability" and "effect=unimplemented" in block \
                    and 'title="Victory Star"' in block:
                game_text = re.search(
                    r"game_text\s*=\s*(\"(?:\\.|[^\"])*\"|'(?:\\.|[^'])*')",
                    block,
                )
                literal = game_text.group(1) if game_text else "''"
                new = re.sub(r"\s*activation\s*=\s*[^,\n]+,?", "", block)
                new = new.replace(
                    "effect=unimplemented", f"passive=bw_legacy_passive({literal})"
                )
            elif token == "Ability" and "effect=unimplemented" in block \
                    and ("trigger=" in block or "activation=" in block):
                new = block.replace("effect=unimplemented", "effect=bw_legacy_ability")
            elif token == "Ability" and "effect=unimplemented" in block:
                game_text = re.search(
                    r"game_text\s*=\s*(\"(?:\\.|[^\"])*\"|'(?:\\.|[^'])*')",
                    block,
                )
                literal = game_text.group(1) if game_text else "''"
                new = block.replace(
                    "effect=unimplemented", f"passive=bw_legacy_passive({literal})"
                )
            elif token == "Ability" and "passive=bw_legacy_passive" in block:
                game_text = re.search(
                    r"game_text\s*=\s*(\"(?:\\.|[^\"])*\"|'(?:\\.|[^'])*')",
                    block,
                )
                passive = re.search(
                    r"passive=bw_legacy_passive\((\"(?:\\.|[^\"])*\"|'(?:\\.|[^'])*')\)",
                    block,
                )
                if not game_text or not passive:
                    continue
                text = " ".join(ast.literal_eval(game_text.group(1)).lower().split())
                title_match = re.search(
                    r"title\s*=\s*(\"(?:\\.|[^\"])*\"|'(?:\\.|[^'])*')", block
                )
                title = ast.literal_eval(title_match.group(1)) if title_match else ""
                if title == "Victory Star":
                    continue
                mode = None
                if text.startswith("as often as you like during your turn"):
                    mode = 'activation="unlimited"'
                elif text.startswith("once during your turn"):
                    mode = 'activation="once_per_turn"'
                elif text.startswith("at any time between turns") \
                        or text.startswith("at any times between turns"):
                    mode = 'trigger="between_turns"'
                elif text.startswith("when you play this pokémon from your hand to evolve"):
                    mode = 'trigger="on_evolve"'
                elif text.startswith("when you play this pokémon from your hand onto your bench"):
                    mode = 'trigger="on_play"'
                elif "damaged by an opponent's attack" in text \
                        and "attacking pokémon" in text:
                    mode = 'trigger="on_damaged_by_attack"'
                elif "knocked out by damage from an opponent's attack" in text:
                    mode = 'trigger="on_knocked_out"'
                elif "whenever your opponent attaches an energy" in text \
                        and "put 3 damage counters" in text:
                    mode = 'trigger="on_energy_attached"'
                elif text.startswith("during your turn (before your attack), you may put a basic pokémon"):
                    mode = 'activation="once_per_turn"'
                if mode is None:
                    continue
                new = block[:passive.start()] + \
                    f"{mode},\n            effect=bw_legacy_ability" + block[passive.end():]
            elif token == "Ability" and "effect=bw_legacy_ability" in block \
                    and 'title="Victory Star"' in block:
                game_text = re.search(
                    r"game_text\s*=\s*(\"(?:\\.|[^\"])*\"|'(?:\\.|[^'])*')",
                    block,
                )
                literal = game_text.group(1) if game_text else "''"
                new = re.sub(r"\s*activation\s*=\s*[^,\n]+,?", "", block)
                new = new.replace(
                    "effect=bw_legacy_ability", f"passive=bw_legacy_passive({literal})"
                )
            else:
                continue
            replacements.append((start, end, new))
    # Attack and Ability blocks may alternate in a card.  Apply every edit by
    # absolute source position (not by token group), otherwise growing an
    # earlier Ability invalidates the offsets of a later Attack.
    for start, end, new in sorted(replacements, key=lambda item: item[0], reverse=True):
        source = source[:start] + new + source[end:]
    return source, len(replacements)


def _wire_trainer(source: str) -> tuple[str, int]:
    if "effect=unimplemented" not in source:
        return source, 0
    name = _display_name(source)
    literal = repr(name)
    if "PokemonToolCardDef(" in source:
        replacement = (
            f"passive=bw_trainer_passive({literal}),\n"
            f"    granted_abilities=bw_tool_abilities({literal})"
        )
    elif "StadiumCardDef(" in source:
        replacement = (
            f"passive=bw_trainer_passive({literal}),\n"
            f"    ability=bw_stadium_ability({literal}),\n"
            f"    abilities=bw_stadium_triggers({literal})"
        )
    else:
        replacement = "effect=bw_trainer_effect"
    return source.replace("effect=unimplemented", replacement), 1


def _clean_import(source: str) -> str:
    if "unimplemented" in source.split("\n", 1)[1]:
        return source
    source = re.sub(r",\s*unimplemented\b", "", source)
    source = re.sub(r"\bunimplemented\s*,\s*", "", source)
    return source


def main() -> None:
    changed = markers = 0
    for set_code in SETS:
        folder = CARD_ROOT / set_code
        if not folder.exists():
            continue
        for path in folder.glob("*.py"):
            source = path.read_text(encoding="utf-8")
            updated, count = _wire_pokemon(source)
            updated, trainer_count = _wire_trainer(updated)
            count += trainer_count
            if not count:
                cleaned = _clean_import(updated)
                if cleaned != source:
                    path.write_text(cleaned, encoding="utf-8")
                    changed += 1
                continue
            if "spirit.game.card_effects.bw_era" not in updated:
                lines = updated.splitlines(keepends=True)
                insert = 0
                while insert < len(lines) and lines[insert].startswith("from "):
                    insert += 1
                lines.insert(insert, BW_IMPORT)
                updated = "".join(lines)
            updated = _clean_import(updated)
            path.write_text(updated, encoding="utf-8")
            changed += 1
            markers += count
    print(f"wired {markers} effects in {changed} BW-era card scripts")


if __name__ == "__main__":
    main()
