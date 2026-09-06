"""Repair cp1252/UTF-8 mojibake in card names; keep the real 'Pokémon' spelling."""
from __future__ import annotations

import unicodedata
from typing import Iterable, List, Optional


def fix_mojibake(s: Optional[str]) -> str:
    """Repair cp1252 mojibake (e.g. 'PokÃ©mon' -> 'Pokémon').

    The pokemontcg.io JSON (and some generated scripts) stored UTF-8 bytes
    decoded as Windows-1252, so 'é' (U+00E9) became 'Ã' + '©'. Encoding back
    through cp1252 recovers the original UTF-8. Already-correct strings are
    left unchanged.
    """
    if not s:
        return s or ""
    prev = None
    cur = s
    # Double-encoded names show up occasionally; a couple of passes is enough.
    for _ in range(3):
        if cur == prev:
            break
        prev = cur
        try:
            repaired = cur.encode("cp1252").decode("utf-8")
        except (UnicodeEncodeError, UnicodeDecodeError):
            break
        if repaired == cur:
            break
        cur = repaired
    return cur


def ascii_fold(s: Optional[str]) -> str:
    """Accent-insensitive form for import/search aliases ('Pokémon' -> 'Pokemon')."""
    repaired = fix_mojibake(s)
    return (
        unicodedata.normalize("NFKD", repaired)
        .encode("ascii", "ignore")
        .decode("ascii")
    )


def client_localization_value(s: Optional[str]) -> str:
    """Canonical card name sent to the client: repaired UTF-8, accent kept."""
    return fix_mojibake(s)


def with_ascii_aliases(
    values: Optional[Iterable[str]], display_name: Optional[str] = None
) -> List[str]:
    """Keep accented names and append ASCII spellings so 'Pokemon Catcher' matches."""
    out: List[str] = []
    seen = set()
    for item in list(values or []) + ([display_name] if display_name else []):
        if not item or item in seen:
            continue
        out.append(item)
        seen.add(item)
        folded = ascii_fold(item)
        if folded and folded not in seen:
            out.append(folded)
            seen.add(folded)
    return out


def fix_mojibake_list(values: Optional[Iterable[str]]) -> List[str]:
    return [fix_mojibake(v) for v in (values or [])]
