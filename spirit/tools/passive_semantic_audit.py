"""Inventory runtime shared-passive text by the engine mechanisms it requires.

``effect_coverage`` proves that a callback exists; it cannot prove that a
continuous rule or event observer understands the printed text.  This audit
keeps that distinction explicit.  It groups exact-text printings, identifies
the engine subsystems demanded by each family, and flags event/zone-changing
text for manual semantic review.

The card loader first normalizes imported named rules into continuous
passives, event triggers, or clicked abilities.  Auditing the Python AST before
that pass produced hundreds of false positives (for example, an imported
once-per-turn Ability still looked like ``standard_passive`` in its source
file).  This tool deliberately inspects the authoritative, fully normalized
runtime registry instead.

The report is intentionally conservative: ``MECHANISM_MAPPED`` means that a
shared engine hook exists for every detected clause, not that every branch of
the card has been formally proven.

Usage::

    python -m spirit.tools.passive_semantic_audit --json passive.json
    python -m spirit.tools.passive_semantic_audit --only-problems --top 100
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

from spirit.game.data_utils import Attack, CARD_DEFS_BY_GUID
from spirit.game.scripts.cards import loader


# (label, textual evidence).  Labels correspond to concrete hooks in
# session/passives.py and _BWTextPassive, rather than card categories.
MECHANISMS = (
    ("damage dealt", r"(?:do|does|deal|deals) \d+ (?:more|less) damage|damage is \d+"),
    ("damage taken", r"takes? \d+ (?:more|less) damage|damage done .* reduced"),
    ("damage prevention", r"prevent all damage|prevent that damage|no damage done"),
    ("attack effects shield", r"prevent all effects .* attacks|unaffected by .* effects of attacks"),
    ("weakness", r"weakness|no weakness"),
    ("resistance", r"resistance|no resistance"),
    ("attack cost", r"attacks?.*cost|attack cost|ignore all (?:colorless )?energy in the costs? of|costs?.*less"),
    ("retreat cost", r"retreat cost|no retreat cost"),
    ("retreat lock", r"can(?:not|'t) retreat|can retreat even"),
    ("maximum HP", r"(?:gets?|have|has) [+-]\d+ hp|maximum hp|remaining hp"),
    ("Pokemon type", r"(?:becomes?|is also|are also|is now|is|are|type is) (?:a |an |both )?(?:grass|fire|water|lightning|psychic|fighting|darkness|metal|fairy|dragon|colorless|the same type)"),
    ("Energy provider", r"provides? .* energy|counts as .* energy|all energy .* are .* energy instead"),
    ("Energy attachment rule", r"attach .* energy|energy .* attached|extra energy"),
    ("Special Condition", r"asleep|burned|confused|paralyzed|poisoned|special conditions"),
    ("healing", r"heal \d+ damage|damage (?:can(?:not|'t)|isn't) be healed|double the amount healed"),
    ("ability lock", r"(?:has|have|lose|no) abilities|abilities? (?:can(?:not|'t)|has no)"),
    ("Trainer lock/shield", r"(?:item|supporter|trainer|stadium|ace spec|pokémon tool) cards?.*(?:can(?:not|'t)|prevent all effects)|can(?:not|'t) (?:play|attach) any (?:item|supporter|trainer|stadium|ace spec|pokémon tool)|can(?:not|'t) play any pokémon tool, special energy, or stadium"),
    ("bench capacity", r"(?:more than|up to) \d+ benched pokémon|number of benched pokémon"),
    ("evolution rule", r"evolve|devolve"),
    ("Prize replacement", r"prize cards?"),
    ("Knock Out replacement/event", r"knocked out|knock out"),
    ("discard replacement/protection", r"discard(?:ed)? .* instead|can(?:not|'t) be discarded|lost zone instead"),
    ("granted attacks", r"can use the attack|attacks of .* in your discard pile"),
    ("Pokemon Checkup", r"between turns|pokémon checkup"),
    ("turn-end event", r"at the end of (?:your|your opponent's|each player's|the) turn"),
    ("Energy-attached event", r"when(?:ever)? (?:you|any player) attach(?:es)? .* energy"),
    ("Tool-attached event", r"when(?:ever)? you attach a pokémon tool"),
    ("bench-play event", r"(?:put|puts|play) .* from (?:his or her|their|your) hand .* bench|play a pokémon .* from your hand"),
    ("evolution-play event", r"plays? a pokémon from .* hand to evolve|play .* from your hand to evolve"),
    ("Active-change event", r"moves? to the bench|switches? their .* active pokémon|active pokémon retreats"),
    ("damage reaction", r"is damaged by an attack|takes? \d+ or more damage from an attack"),
    ("ability effects shield", r"prevent all effects .* abilities|unaffected by .* abilities"),
    ("attack permission", r"attack twice|use an attack it has twice|can(?:not|'t) attack"),
    ("Tool capacity/suppression", r"may have up to \d+ pokémon tool|tool card.*(?:has|have) no effect"),
    ("healing lock", r"can(?:not|'t) be healed|damage counters can(?:not|'t) be removed"),
    ("coin override", r"treat it as tails|treat it as heads|ignore all (?:effects|results) of those coin flips and (?:begin|being) flipping"),
    ("defender-effects bypass", r"isn't affected by any effects on your opponent's active"),
    ("first-turn attack permission", r"can use attacks during your first turn"),
    ("setup exception", r"when you are setting up to play|put it face down as your active"),
    ("play-entry restriction", r"put this pokémon into play only with the effect of"),
    ("Pokemon play lock", r"can(?:not|'t) play any pokémon that has an ability"),
    ("supporter allowance", r"may play 2 supporter cards"),
    ("move-to-hand shield", r"can(?:not|'t) be put into .* hand"),
    ("Stadium effects shield", r"prevent all effects of any stadium"),
    ("Spirit Link", r"your turn does not end if .* becomes? (?:m |primal )"),
    ("typed attack grant", r"can (?:also )?use the (?:gx )?attack|can use .+ attack for"),
    ("Trainer end-turn replacement", r"turn does not end when you play"),
    ("physical-play instruction", r"throw (?:it|the card) .* horizontally|throw it as hard as you can"),
)

# These clauses have several timing/choice/hidden-information branches.  They
# stay in the problem queue even after a broad mechanism exists, until a card-
# level regression test or bespoke implementation proves the semantics.
HIGH_RISK = (
    ("optional branch", r"\byou may\b|\bmay (?:discard|put|move|attach|search|draw|switch)\b"),
    ("coin branch", r"flip (?:a|\d+) coins?|if heads|if tails"),
    ("random choice", r"\brandom\b"),
    ("hidden-zone choice", r"search (?:your|their) deck|look at .* (?:deck|hand)|from .* prize cards"),
    ("multi-target movement", r"in any way you like|move up to|move all|switch all"),
    ("delayed duration", r"during your opponent's next turn|until the end|for the rest of|next turn"),
    ("replacement timing", r"instead of|would be|before it evolves|even if .* knocked out"),
    ("nonstacking", r"does(?: not|n't) stack|can(?:not|'t) apply more than 1"),
)


def _norm(text):
    return " ".join(
        (text or "").replace("Pok�mon", "Pokémon")
        .replace("pok�mon", "pokémon").replace("’", "'").lower().split()
    )


def _runtime_families():
    """Return only shared passives which survive runtime normalization."""
    loader.load_all()
    families = defaultdict(list)
    seen = set()
    for definition in CARD_DEFS_BY_GUID.values():
        guid = (getattr(definition, "guid", "") or "").lower()
        if not guid or guid in seen:
            continue
        seen.add(guid)
        display = getattr(definition, "display_name", None) or \
            getattr(definition, "name", guid)
        set_code = getattr(definition, "set_code", "")
        path = loader.script_by_guid.get(getattr(definition, "guid", ""), "")
        candidates = []
        passive = getattr(definition, "passive", None)
        if passive is not None:
            delegated = []
            if getattr(definition, "ability", None) is not None:
                delegated.append("activated Stadium effect")
            if getattr(definition, "granted_abilities", None):
                delegated.append("granted attacks/abilities")
            if getattr(definition, "unplayable_from_hand", False):
                delegated.append("play-entry restriction")
            candidates.append(("(card passive)", passive, delegated))
        for ability in getattr(definition, "abilities", ()) or ():
            if isinstance(ability, Attack):
                continue
            passive = getattr(ability, "passive", None)
            if passive is not None:
                candidates.append((
                    getattr(ability, "title", "(untitled)"), passive, []
                ))
        for title, passive, delegated in candidates:
            if passive.__class__.__name__ != "_BWTextPassive":
                continue
            text = _norm(getattr(passive, "text", ""))
            families[("passive", title, text)].append({
                "card": display,
                "set": set_code,
                "path": path,
                "delegated": delegated,
            })
    return families


def analyze():
    families = _runtime_families()
    rows = []
    for (kind, title, text), printings in families.items():
        mechanisms = [label for label, pattern in MECHANISMS
                      if re.search(pattern, text)]
        mechanisms.extend(sorted({
            mechanism
            for printing in printings
            for mechanism in printing.get("delegated", [])
        }))
        # These sentences are card-type reminders rather than optional effect
        # branches.  Keeping them in HIGH_RISK made virtually every legacy
        # Tool look suspicious even when its only rule was a flat modifier.
        risk_text = re.sub(
            r"you may play as many item cards as you like during your turn"
            r" \(before your attack\)\.?", "", text,
        )
        risks = [label for label, pattern in HIGH_RISK
                 if re.search(pattern, risk_text)]
        if not mechanisms:
            status = "UNMAPPED_REVIEW"
        elif risks:
            status = "HIGH_RISK_REVIEW"
        else:
            status = "MECHANISM_MAPPED"
        rows.append({
            "status": status,
            "kind": kind,
            "title": title,
            "text": text,
            "mechanisms": mechanisms,
            "risks": risks,
            "printings": printings,
        })
    rows.sort(key=lambda row: (
        {"UNMAPPED_REVIEW": 0, "HIGH_RISK_REVIEW": 1,
         "MECHANISM_MAPPED": 2}[row["status"]],
        -len(row["printings"]), row["title"], row["text"],
    ))
    return rows


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(errors="backslashreplace")
    parser = argparse.ArgumentParser()
    parser.add_argument("--json")
    parser.add_argument("--only-problems", action="store_true")
    parser.add_argument("--top", type=int, default=60)
    args = parser.parse_args()

    rows = analyze()
    counts = Counter(row["status"] for row in rows)
    print(f"passive: {len(rows)} exact-text families / "
          f"{sum(len(row['printings']) for row in rows)} printings")
    for status in ("MECHANISM_MAPPED", "HIGH_RISK_REVIEW", "UNMAPPED_REVIEW"):
        print(f"  {status}={counts[status]}")

    selected = rows
    if args.only_problems:
        selected = [row for row in rows
                    if row["status"] != "MECHANISM_MAPPED"]
    for row in selected[:args.top]:
        cards = ", ".join(sorted({p["card"] for p in row["printings"]})[:5])
        print(f"\n[{row['status']}] {len(row['printings'])}x "
              f"{row['title']} -- {cards}")
        print(f"  mechanisms: {', '.join(row['mechanisms']) or '(none)'}")
        print(f"  risks: {', '.join(row['risks']) or '(none)'}")
        print(f"  {row['text']}")

    if args.json:
        Path(args.json).write_text(
            json.dumps(rows, indent=2, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
    main()
