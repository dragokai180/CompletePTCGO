"""Complete the current Standard catalog without replacing bespoke cards.

Sources, in priority order:
  * an external expansion catalog (which cards belong to the project format);
  * pokemon-tcg-data JSON (printed stats, text, rarity and image URL);
  * existing Python card modules (authoritative mechanics for reprints).

The command is intentionally idempotent.  Existing scripts and artwork are
never overwritten, making it safe to rerun after a card receives a manual
implementation.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import uuid
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any, Dict, Iterable, Optional

import requests

from spirit.game.text_encoding import fix_mojibake as fix_text


ROOT = Path(__file__).resolve().parents[2]
LEGACY_CATALOG_ROOT = ROOT.parent
SOURCE_ROOT = LEGACY_CATALOG_ROOT / "work" / "standard-current"

# External catalog stem -> (pokemon-tcg-data filename, server set code)
STANDARD_SETS = {
    "tef": ("sv5", "SV05"),
    "twm": ("sv6", "SV06"),
    "sfa": ("sv6pt5", "SV065"),
    "scr": ("sv7", "SV07"),
    "ssp": ("sv8", "SV08"),
    "pre": ("sv8pt5", "SV085"),
    "jtg": ("sv9", "SV09"),
    "dri": ("sv10", "SV10"),
    "wht": ("rsv10pt5", "RSV10PT5"),
    "blk": ("zsv10pt5", "ZSV10PT5"),
    "svp": ("svp", "SVP"),
    "meg": ("me1", "ME1"),
    "pfl": ("me2", "ME2"),
    "asc": ("me2pt5", "ME2PT5"),
    "por": ("me3", "ME3"),
    "cri": ("me4", "ME4"),
    "pbl": ("me5", "ME5"),
    "mep": ("mep", "MEP"),
}

TYPE_MAP = {
    "Grass": "PokemonTypes.GRASS",
    "Fire": "PokemonTypes.FIRE",
    "Water": "PokemonTypes.WATER",
    "Lightning": "PokemonTypes.LIGHTNING",
    "Psychic": "PokemonTypes.PSYCHIC",
    "Fighting": "PokemonTypes.FIGHTING",
    "Darkness": "PokemonTypes.DARKNESS",
    "Metal": "PokemonTypes.METAL",
    "Colorless": "PokemonTypes.COLORLESS",
    "Dragon": "PokemonTypes.DRAGON",
    "Fairy": "PokemonTypes.FAIRY",
}

STAGE_MAP = {
    "Basic": "PokemonStage.BASIC",
    "Stage 1": "PokemonStage.STAGE1",
    "Stage 2": "PokemonStage.STAGE2",
    "VMAX": "PokemonStage.VMAX",
    "VSTAR": "PokemonStage.VSTAR",
    "V-UNION": "PokemonStage.VUNION",
    "BREAK": "PokemonStage.BREAK",
    "Restored": "PokemonStage.RESTORED",
    "LEGEND": "PokemonStage.LEGEND",
    # XY Mega Evolution cards evolve from their matching Pokemon-EX.  The
    # client has no separate MEGA stage enum, so the original game represents
    # that step as Stage 1 plus EVOLUTION_LOGIC_FROM.
    "MEGA": "PokemonStage.STAGE1",
}

RARITY_MAP = {
    "Common": "Rarities.Common",
    "Uncommon": "Rarities.Uncommon",
    "Rare": "Rarities.Rare",
    "Rare Holo": "Rarities.RareHolo",
    "Rare Holo EX": "Rarities.RareHoloEX",
    "Rare Holo GX": "Rarities.RareHoloGX",
    "Rare Ultra": "Rarities.RareUltra",
    "Rare Secret": "Rarities.RareSecret",
    "Rare Rainbow": "Rarities.RareRainbow",
    "Rare Shiny": "Rarities.Shining",
    "Rare Shiny GX": "Rarities.RareHoloGX",
    "Rare Prime": "Rarities.RarePrime",
    "LEGEND": "Rarities.Legendary",
    "Rare Prism Star": "Rarities.Prism",
    "Rare Shining": "Rarities.Shining",
    "Double Rare": "Rarities.RareHoloEX",
    "Illustration Rare": "Rarities.ChrRareHolo",
    "Ultra Rare": "Rarities.RareUltra",
    "Special Illustration Rare": "Rarities.RareSecret",
    "Hyper Rare": "Rarities.RareRainbow",
    "ACE SPEC Rare": "Rarities.Ace",
    "Rare BREAK": "Rarities.BreakRare",
    "Mega Hyper Rare": "Rarities.RareSecret",
    "MEGA_ATTACK_RARE": "Rarities.RareUltra",
    "Black White Rare": "Rarities.RareSecret",
    "Promo": "Rarities.RarePromo",
}

REMINDER_PREFIXES = (
    "you may play any number of item cards",
    "you may play only 1 supporter card",
    "you may play only 1 stadium card",
    "you may attach any number of pok",
    "attach a pok",
    "pokémon ex rule:",
    "mega evolution ex rule:",
    "tera:",
)


def clean_name(name: str) -> str:
    return re.sub(r"[^A-Za-z0-9]", "", fix_text(name or "Unknown"))


def py(value: Any) -> str:
    # Python source literal (unlike JSON, this correctly renders None/booleans).
    return repr(value)


def guid_for(card_id: str) -> str:
    return str(uuid.uuid5(uuid.NAMESPACE_DNS, f"spirit.ptcgo.{card_id}"))


def numeric(value: Any, default: int = 0) -> int:
    match = re.search(r"\d+", str(value or ""))
    return int(match.group()) if match else default


def api_collector_number(card: dict, api_stem: str) -> str:
    """Return the print number, preferring the stable suffix in the API id.

    A malformed Black Bolt row identifies Antique Cover Fossil as
    ``zsv10pt5-80`` but repeats Escavalier's ``number: 60``.  Indexing only by
    the latter silently replaces Escavalier and gives both cards the same
    GUID.  The upstream id and image paths still carry the correct number.
    """
    card_id = str(card.get("id") or "")
    prefix = f"{api_stem}-"
    if card_id.startswith(prefix):
        suffix = card_id[len(prefix):]
        if suffix.isdigit():
            return suffix
    return str(card.get("number"))


def load_external_catalog(stem: str) -> Dict[str, Any]:
    path = LEGACY_CATALOG_ROOT / "outputs" / f"{stem}-cards.js"
    source = path.read_text(encoding="utf-8")
    match = re.search(
        r"=\s*(\{.*\})\s*;\s*\n\s*if \(typeof window", source, re.S
    )
    if not match:
        raise ValueError(f"Could not parse {path}")
    return json.loads(match.group(1))


def load_api_cards(stem: str) -> list[dict]:
    path = SOURCE_ROOT / f"{stem}.json"
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, list):
        raise ValueError(f"Expected a card list in {path}")
    return payload


def fallback_api_card(pobre_card: dict, api_stem: str) -> dict:
    """Build the small number of promo/fossil rows absent from the API dump."""
    number = str(pobre_card["n"])
    kind = pobre_card.get("kind")
    card: dict = {
        "id": f"{api_stem}-{number}",
        "name": fix_text(pobre_card.get("name", "Unknown")),
        "number": number,
        "rarity": "Promo" if api_stem == "svp" else "Uncommon",
        "regulationMark": pobre_card.get("regulationMark"),
        "images": {"large": pobre_card.get("image") or (
            f"https://images.pokemontcg.io/{api_stem}/{number}_hires.png"
        )},
    }
    if kind == "pokemon":
        subtypes = [pobre_card.get("stage") or "Basic"]
        if pobre_card.get("isEx"):
            subtypes.append("ex")
        if pobre_card.get("isMegaEx"):
            subtypes.extend(s for s in ("ex", "SV_Mega") if s not in subtypes)
        if pobre_card.get("isTera"):
            subtypes.append("Tera")
        if pobre_card.get("isAncient"):
            subtypes.append("Ancient")
        if pobre_card.get("isFuture"):
            subtypes.append("Future")
        card.update({
            "supertype": "Pokémon",
            "subtypes": subtypes,
            "hp": str(pobre_card.get("hp", 0)),
            "types": [str(pobre_card.get("type", "colorless")).title()],
            "evolvesFrom": pobre_card.get("from"),
            "attacks": [
                {
                    "name": fix_text(attack.get("name", "Attack")),
                    "cost": [str(value).title() for value in attack.get("cost", [])],
                    "damage": fix_text(attack.get("damage", "")),
                    "text": fix_text(attack.get("text", "")),
                }
                for attack in pobre_card.get("attacks", [])
            ],
            "weaknesses": ([{
                "type": str(pobre_card["weak"]).title(), "value": "×2"
            }] if pobre_card.get("weak") else []),
            "resistances": ([{
                "type": str(pobre_card["resist"]).title(),
                "value": str(pobre_card.get("resistValue", -30)),
            }] if pobre_card.get("resist") else []),
            "convertedRetreatCost": int(pobre_card.get("retreat", 0) or 0),
            "rules": [],
        })
        if pobre_card.get("ability"):
            card["abilities"] = [{
                "name": fix_text(pobre_card.get("abilityName", "Ability")),
                "text": fix_text(pobre_card.get("abilityText", "")),
                "type": "Ability",
            }]
    elif kind == "trainer":
        trainer_type = pobre_card.get("trainerType", "item")
        subtype = {
            "supporter": "Supporter",
            "stadium": "Stadium",
        }.get(trainer_type, "Item")
        subtypes = [subtype]
        if pobre_card.get("trainerSubtype") == "tool":
            subtypes = ["Pokémon Tool"]
        rules = []
        if pobre_card.get("actsAsPokemon"):
            rules.append(
                f"Play this card as if it were a {pobre_card.get('hp', 60)}-HP "
                "Basic Colorless Pokémon. This card can't be affected by any "
                "Special Conditions and can't retreat."
            )
            if pobre_card.get("abilityText"):
                rules.append(fix_text(pobre_card["abilityText"]))
        card.update({
            "supertype": "Trainer", "subtypes": subtypes,
            "rules": rules, "attacks": pobre_card.get("attacks", []),
        })
    elif kind == "energy":
        special = pobre_card.get("energyKind") == "special"
        card.update({
            "supertype": "Energy",
            "subtypes": ["Special" if special else "Basic"],
            "rules": [],
        })
    return card


def module_for(path: Path) -> str:
    return ".".join(path.relative_to(ROOT).with_suffix("").parts)


def existing_named_modules() -> Dict[tuple[str, str], str]:
    """(kind, display name) -> authoritative existing module."""
    found: Dict[tuple[str, str], str] = {}
    scripts = ROOT / "spirit" / "game" / "scripts" / "cards"
    pattern = re.compile(r"display_name\s*=\s*([\"'])(.*?)\1", re.S)
    for path in scripts.rglob("*.py"):
        try:
            source = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            continue
        match = pattern.search(source)
        if not match:
            continue
        name = match.group(2)
        kind = (
            "trainer" if "CardDef" in source and any(token in source for token in (
                "ItemCardDef", "SupporterCardDef", "StadiumCardDef",
                "PokemonToolCardDef", "FossilItemCardDef",
            ))
            else "energy" if "EnergyCardDef" in source
            else "pokemon" if "PokemonCardDef" in source
            else ""
        )
        if kind:
            found.setdefault((kind, name), module_for(path))
    return found


def existing_guid_scripts() -> Dict[str, Path]:
    """Index already registered prints, including files with legacy names.

    A few hand-written modules use a correctly accented/ASCII filename while
    an upstream catalog spelling produces a different generated filename.  A
    card GUID is the stable identity, so it must win over the filename.
    """
    found: Dict[str, Path] = {}
    scripts = ROOT / "spirit" / "game" / "scripts" / "cards"
    pattern = re.compile(r"\bguid\s*=\s*([\"'])([0-9a-fA-F-]{36})\1")
    for path in scripts.rglob("*.py"):
        try:
            source = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            continue
        match = pattern.search(source)
        if match:
            found.setdefault(match.group(2).lower(), path)
    return found


def existing_print_scripts() -> Dict[tuple[str, int], Path]:
    """Index physical prints by set and collector number.

    Legacy hand-written reprints can intentionally derive their GUID from a
    sibling rather than spelling it in the module.  Set/number is therefore
    the final identity fallback used to prevent duplicate definitions.
    """
    found: Dict[tuple[str, int], Path] = {}
    scripts = ROOT / "spirit" / "game" / "scripts" / "cards"
    pattern = re.compile(r"\bcollector_number\s*=\s*(\d+)")
    for path in scripts.rglob("*.py"):
        try:
            source = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            continue
        match = pattern.search(source)
        if match:
            found.setdefault((path.parent.name, int(match.group(1))), path)
    return found


def mechanics_signature(card: dict) -> str:
    keys = (
        "name", "supertype", "subtypes", "hp", "types", "evolvesFrom",
        "abilities", "ancientTrait", "attacks", "weaknesses", "resistances",
        "convertedRetreatCost", "rules",
    )
    data = {key: card.get(key) for key in keys}
    return json.dumps(data, sort_keys=True, ensure_ascii=False)


def main_rules(card: dict) -> str:
    rules = []
    for raw in card.get("rules") or []:
        fixed = fix_text(raw).strip()
        low = fixed.lower()
        if not fixed or low.startswith(REMINDER_PREFIXES):
            continue
        if fixed not in rules:
            rules.append(fixed)
    return " ".join(rules)


def rarity(card: dict) -> str:
    return RARITY_MAP.get(card.get("rarity"), "Rarities.Rare")


def damage_parts(value: Any) -> tuple[int, str]:
    match = re.match(r"\s*(\d+)\s*(.*)", fix_text(str(value or "")))
    if not match:
        return 0, ""
    return int(match.group(1)), match.group(2).replace("×", "x").strip()


def cost_source(cost: Iterable[str]) -> str:
    counts: Dict[str, int] = {}
    for name in cost or []:
        ref = TYPE_MAP.get(fix_text(name))
        if ref:
            counts[ref] = counts.get(ref, 0) + 1
    return "{" + ", ".join(f"{key}: {value}" for key, value in counts.items()) + "}"


def family_id(card: dict, by_name: Dict[str, dict]) -> Optional[int]:
    current, visited = card, set()
    while current.get("evolvesFrom") and current.get("evolvesFrom") not in visited:
        previous = fix_text(current["evolvesFrom"])
        visited.add(previous)
        current = by_name.get(previous, current)
        if current is card:
            break
    numbers = current.get("nationalPokedexNumbers") or card.get("nationalPokedexNumbers") or []
    return numeric(numbers[0]) if numbers else None


def trigger_expr(text: str) -> tuple[Optional[str], Optional[str], Optional[str]]:
    normalized = " ".join(fix_text(text).lower().split())
    from spirit.game.card_effects.standard_era import standard_ability_source_zone
    usable_from = standard_ability_source_zone(normalized)

    trigger = None
    if "when you play this pokémon from your hand onto your bench" in normalized:
        trigger = "Triggers.ON_PLAY"
    elif "when you play this pokémon from your hand to evolve" in normalized:
        trigger = "Triggers.ON_EVOLVE"
    elif "when this pokémon is knocked out" in normalized:
        trigger = "Triggers.ON_KNOCKED_OUT"
    elif "damaged by an attack" in normalized and "attacking pokémon" in normalized:
        trigger = "Triggers.ON_DAMAGED_BY_ATTACK"
    elif "whenever" in normalized and "attaches an energy" in normalized:
        trigger = "Triggers.ON_ENERGY_ATTACHED"
    elif "moves to the active spot" in normalized:
        trigger = "Triggers.ON_MOVE_TO_ACTIVE"
    elif "at the end of your turn" in normalized:
        trigger = "Triggers.END_OF_TURN"
    elif "between turns" in normalized or "during pokémon checkup" in normalized:
        trigger = "Triggers.BETWEEN_TURNS"

    activation = None
    if "as often as you like during your turn" in normalized:
        activation = "Activations.UNLIMITED"
    elif (
        "once during your turn" in normalized
        or "you can use this ability once during your turn" in normalized
    ):
        activation = "Activations.ONCE_PER_TURN"
    return trigger, activation, usable_from


def ability_source(ability: dict, indent: str = "        ") -> list[str]:
    title = fix_text(ability.get("name", "Ability"))
    text = fix_text(ability.get("text", ""))
    trigger, activation, usable_from = trigger_expr(text)
    passive = trigger is None and activation is None and usable_from is None
    lines = [f"{indent}Ability(", f"{indent}    title={py(title)},",
             f"{indent}    game_text={py(text)},"]
    ability_type = fix_text(ability.get("type", "")).casefold()
    if ability_type in ("poke-power", "poké-power"):
        lines.append(f"{indent}    ability_type=AbilityTypes.POKE_POWER,")
    elif ability_type in ("poke-body", "poké-body"):
        lines.append(f"{indent}    ability_type=AbilityTypes.POKE_BODY,")
    if passive:
        lines.append(f"{indent}    passive=standard_passive({py(text)}),")
    else:
        lines.append(f"{indent}    effect=standard_ability,")
        if trigger:
            lines.append(f"{indent}    trigger={trigger},")
        if activation:
            lines.append(f"{indent}    activation={activation},")
        if usable_from:
            lines.append(f"{indent}    usable_from={py(usable_from)},")
    lines.append(f"{indent}),")
    return lines


def attack_source(attack: dict, indent: str = "        ") -> list[str]:
    title = fix_text(attack.get("name", "Attack"))
    text = fix_text(attack.get("text", "") or "").strip()
    damage, operator = damage_parts(attack.get("damage"))
    lines = [f"{indent}Attack(", f"{indent}    title={py(title)},"]
    if text:
        lines.append(f"{indent}    game_text={py(text)},")
    lines.append(f"{indent}    cost={cost_source(attack.get('cost') or [])},")
    if damage:
        lines.append(f"{indent}    damage={damage},")
    if operator:
        lines.append(f"{indent}    damage_operator={py(operator)},")
    if text:
        lines.append(f"{indent}    effect=standard_attack,")
    if "can't use" in text.lower() and "next turn" in text.lower():
        lines.append(f"{indent}    locks_next_turn=True,")
    if "even if you go first" in text.lower():
        lines.append(f"{indent}    usable_first_turn=True,")
    # Sun & Moon's once-per-game restriction belongs to the attack itself,
    # regardless of whether the printed text repeats the reminder sentence.
    if re.search(r"(?:-|\s)GX$", title, re.IGNORECASE):
        lines.append(f"{indent}    gx=True,")
    lines.append(f"{indent}),")
    return lines


def render_pokemon(card: dict, set_code: str, by_name: Dict[str, dict]) -> str:
    name = fix_text(card["name"])
    subtypes = [fix_text(value) for value in card.get("subtypes") or []]
    # Some promo data has a correct rule box but omits its ex/GX subtype.
    # Read that explicit text rather than silently importing a one-Prize card.
    rules = " ".join(card.get("rules") or [])
    if "Mega Evolution ex Rule" in rules:
        subtypes.extend(s for s in ("ex", "SV_Mega") if s not in subtypes)
    elif "Pokémon ex rule" in rules and "ex" not in subtypes:
        subtypes.append("ex")
    if "Pokémon-GX rule" in rules and "GX" not in subtypes:
        subtypes.append("GX")
    # Only the modern lower-case Pokemon ex use the three-prize SV_Mega rule.
    # XY's upper-case Pokemon-EX Mega Evolutions remain two-prize Pokemon-EX.
    if "MEGA" in subtypes and "ex" in subtypes and "SV_Mega" not in subtypes:
        subtypes.append("SV_Mega")
    stage = next((STAGE_MAP[s] for s in subtypes if s in STAGE_MAP),
                 "PokemonStage.BASIC")
    abilities = []
    for item in card.get("abilities") or []:
        abilities.extend(ability_source(item))
    for item in card.get("attacks") or []:
        abilities.extend(attack_source(item))
    weak = (card.get("weaknesses") or [{}])[0]
    resist = (card.get("resistances") or [{}])[0]
    weakness_type = TYPE_MAP.get(fix_text(weak.get("type", "")))
    resistance_type = TYPE_MAP.get(fix_text(resist.get("type", "")))
    number = numeric(card.get("number"))
    search = [name, *subtypes, clean_name(name)]
    imports = ["Attack", "Ability", "PokemonCardDef", "Activations", "Triggers"]
    lines = [
        f"from spirit.game.data_utils import {', '.join(imports)}",
        "from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities",
        "from spirit.game.card_effects.standard_era import (",
        "    standard_ability, standard_attack, standard_passive,",
        ")",
    ]
    tera = "Tera" in subtypes
    if tera:
        lines.append("from spirit.game.card_effects.pokemon import TeraRulePassive")
    lines.extend(["", "", "card = PokemonCardDef(",
        f"    guid={py(guid_for(card.get('id') or f'{set_code}-{number}'))},",
        f"    key={py(set_code)},",
        f"    name={py('com.direwolfdigital.cake.data.archetypes.pokemon.' + clean_name(name) + '.Name')},",
        f"    display_name={py(name)},",
        f"    searchable_by={py(search)},",
        f"    subtypes={py(subtypes)},",
        f"    collector_number={number},",
        f"    set_code={py(set_code)},",
        f"    regulation_mark={py(card.get('regulationMark'))},",
        f"    rarity={rarity(card)},",
        f"    hp={numeric(card.get('hp'))},",
        "    elements=[" + ", ".join(
            TYPE_MAP.get(fix_text(value), "PokemonTypes.COLORLESS")
            for value in card.get("types") or ["Colorless"]
        ) + "],",
        f"    stage={stage},",
        f"    retreat_cost={numeric(card.get('convertedRetreatCost'))},",
    ])
    collector_text = fix_text(card.get("_collector_number_text", "")).strip()
    if collector_text:
        lines.append(
            f"    attributes={py({200790: {'type': 'string', 'value': collector_text}})},"
        )
    if weakness_type:
        lines.append(f"    weakness_type={weakness_type},")
        lines.append(f"    weakness_amount={numeric(weak.get('value'), 2)},")
        if len(card.get("weaknesses") or []) > 1:
            types = [TYPE_MAP[fix_text(entry["type"])] for entry in card["weaknesses"]]
            lines.append("    weakness_types=[" + ", ".join(types) + "],")
    if resistance_type:
        lines.append(f"    resistance_type={resistance_type},")
        lines.append(f"    resistance_amount={numeric(resist.get('value'), 30)},")
    if card.get("evolvesFrom"):
        previous = clean_name(fix_text(card["evolvesFrom"]))
        lines.append(
            "    evolves_from=" + py(
                f"com.direwolfdigital.cake.data.archetypes.pokemon.{previous}.Name"
            ) + ","
        )
    family = family_id(card, by_name)
    if family:
        lines.append(f"    family_id={family},")
    if abilities:
        lines.append("    abilities=[")
        lines.extend(abilities)
        lines.append("    ],")
    ancient_trait = card.get("ancientTrait") or {}
    ancient_text = fix_text(ancient_trait.get("text", "")).strip()
    if ancient_text:
        lines.append(f"    passive=standard_passive({py(ancient_text)}),")
    if tera:
        lines.append("    passive=TeraRulePassive(),")
    lines.append(")")
    return "\n".join(lines) + "\n"


def render_trainer(card: dict, set_code: str) -> str:
    name = fix_text(card["name"])
    subtypes = [fix_text(value) for value in card.get("subtypes") or []]
    number = numeric(card.get("number"))
    text = main_rules(card)
    search = [name, *subtypes, clean_name(name)]
    tool = any("Tool" in subtype for subtype in subtypes)
    fossil = (
        "play this card as if it were" in text.lower()
        and re.search(r"\d+-?hp basic", text.lower()) is not None
    )
    if fossil:
        klass = "FossilItemCardDef"
    elif "Supporter" in subtypes:
        klass = "SupporterCardDef"
    elif "Stadium" in subtypes:
        klass = "StadiumCardDef"
    elif tool:
        klass = "PokemonToolCardDef"
    else:
        klass = "ItemCardDef"

    imports = [klass]
    if tool and card.get("attacks"):
        imports.append("Attack")
    lines = [
        f"from spirit.game.data_utils import {', '.join(imports)}",
        "from spirit.game.attributes import PokemonTypes, Rarities",
        "from spirit.game.card_effects.standard_era import (",
        "    standard_attack, standard_passive, standard_stadium_ability,",
        "    standard_trainer_condition, standard_trainer_effect,",
        ")",
        "",
        "",
        f"card = {klass}(",
        f"    guid={py(guid_for(card.get('id') or f'{set_code}-{number}'))},",
        f"    key={py(set_code)},",
        f"    name={py('com.direwolfdigital.cake.data.archetypes.trainer.' + clean_name(name) + '.Name')},",
        f"    display_name={py(name)},",
        f"    searchable_by={py(search)},",
        f"    subtypes={py(subtypes)},",
        f"    collector_number={number},",
        f"    set_code={py(set_code)},",
        f"    regulation_mark={py(card.get('regulationMark'))},",
        f"    rarity={rarity(card)},",
    ]
    collector_text = fix_text(card.get("_collector_number_text", "")).strip()
    if collector_text:
        lines.append(
            f"    attributes={py({200790: {'type': 'string', 'value': collector_text}})},"
        )
    if fossil:
        hp_match = re.search(r"(\d+)-?hp basic", text.lower())
        hp = numeric(hp_match.group(1), 60) if hp_match else 60
        lines.append(f"    hp={hp},")
        lines.append(f"    passive=standard_passive({py(text)}),")
    elif klass in ("ItemCardDef", "SupporterCardDef"):
        lines.append(f"    effect=standard_trainer_effect({py(text)}),")
        lines.append(f"    condition=standard_trainer_condition({py(text)}),")
    elif klass == "StadiumCardDef":
        lines.append(f"    passive=standard_passive({py(text)}),")
        lines.append(f"    ability=standard_stadium_ability({py(text)}),")
    elif klass == "PokemonToolCardDef":
        lines.append(f"    passive=standard_passive({py(text)}),")
        if card.get("attacks"):
            lines.append("    granted_abilities=[")
            for attack in card["attacks"]:
                lines.extend(attack_source(attack))
            lines.append("    ],")
    lines.append(")")
    return "\n".join(lines) + "\n"


def energy_options(pobre_card: dict, api_card: dict) -> tuple[str, Optional[str]]:
    provided = pobre_card.get("provides") or []
    alternatives = pobre_card.get("providesAnyOf") or []
    if alternatives:
        refs = [TYPE_MAP.get(word.title()) for word in alternatives]
        refs = [ref for ref in refs if ref]
        return "[[" + "], [".join(refs) + "]]", refs[0] if refs else None
    options = []
    for value in provided:
        value = str(value)
        if value.startswith("any:"):
            refs = [TYPE_MAP.get(word.title()) for word in value[4:].split(",")]
            refs = [ref for ref in refs if ref]
            options.append(refs)
        else:
            ref = TYPE_MAP.get(value.title())
            if ref:
                options.append([ref])
    if not options:
        for word, ref in TYPE_MAP.items():
            if word in fix_text(api_card.get("name", "")):
                options = [[ref]]
                break
    if not options:
        options = [["PokemonTypes.COLORLESS"]]
    return "[" + ", ".join("[" + ", ".join(o) + "]" for o in options) + "]", options[0][0]


def render_energy(card: dict, pobre_card: dict, set_code: str) -> str:
    name = fix_text(card["name"])
    subtypes = [fix_text(value) for value in card.get("subtypes") or []]
    number = numeric(card.get("number"))
    special = "Special" in subtypes or pobre_card.get("energyKind") == "special"
    options, primary = energy_options(pobre_card, card)
    text = main_rules(card)
    lines = [
        "from spirit.game.data_utils import EnergyCardDef",
        "from spirit.game.attributes import PokemonTypes, Rarities",
        "from spirit.game.card_effects.standard_era import (",
        "    energy_attach_to, energy_on_attach, splash_energy_on_ko, standard_passive,",
        ")",
        "",
        "",
        "card = EnergyCardDef(",
        f"    guid={py(guid_for(card.get('id') or f'{set_code}-{number}'))},",
        f"    key={py(set_code)},",
        f"    name={py(name)},",
        f"    display_name={py(name)},",
        f"    searchable_by={py([name, *subtypes, clean_name(name)])},",
        f"    subtypes={py(subtypes)},",
        f"    collector_number={number},",
        f"    set_code={py(set_code)},",
        f"    regulation_mark={py(card.get('regulationMark'))},",
        f"    rarity={rarity(card)},",
        f"    energy_type={primary or 'PokemonTypes.COLORLESS'},",
        f"    is_special={special},",
        f"    provides={options},",
    ]
    collector_text = fix_text(card.get("_collector_number_text", "")).strip()
    if collector_text:
        lines.append(
            f"    attributes={py({200790: {'type': 'string', 'value': collector_text}})},"
        )
    if name == "Burning Energy":
        lines.insert(5, "from spirit.game.card_effects.energies import boomerang_reattach")
    if special and text:
        lines.append(f"    passive=standard_passive({py(text)}),")
        if "can only be attached to" in text.lower():
            lines.append(f"    attach_to=energy_attach_to({py(text)}),")
            lines.append("    discard_if_invalid=True,")
        if "when you attach this card" in text.lower():
            lines.append(f"    on_attach=energy_on_attach({py(text)}),")
        if name == "Burning Energy":
            lines.append("    on_discarded_by_carrier_attack=boomerang_reattach,")
        if name in ("Splash Energy", "Rescue Energy"):
            lines.append("    on_carrier_knocked_out=splash_energy_on_ko,")
    lines.append(")")
    return "\n".join(lines) + "\n"


def render_reprint(card: dict, set_code: str, base_module: str) -> str:
    number = numeric(card.get("number"))
    return "\n".join([
        f"from {base_module} import card as base_card",
        "from spirit.game.data_utils import reprint",
        "from spirit.game.attributes import Rarities",
        "",
        "",
        "card = reprint(",
        "    base_card,",
        f"    collector_number={number},",
        f"    rarity={rarity(card)},",
        f"    guid={py(guid_for(card.get('id') or f'{set_code}-{number}'))},",
        f"    set_code={py(set_code)},",
        f"    key={py(set_code)},",
        f"    regulation_mark={py(card.get('regulationMark'))},",
        ")",
        "",
    ])


def download_one(task: tuple[str, Path]) -> tuple[bool, str]:
    url, destination = task
    if destination.exists():
        return True, str(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    try:
        response = requests.get(
            url,
            timeout=45,
            headers={"User-Agent": "Mozilla/5.0 CompletePTCGO/1.0"},
        )
        response.raise_for_status()
        if not response.content.startswith(b"\x89PNG"):
            raise ValueError("response was not a PNG")
        temporary = destination.with_suffix(".png.part")
        temporary.write_bytes(response.content)
        os.replace(temporary, destination)
        return True, str(destination)
    except Exception as exc:  # diagnostics belong in importer output
        return False, f"{url}: {exc}"


def update_metadata(counts: Dict[str, int]) -> None:
    sets_path = ROOT / "spirit" / "database" / "json_data" / "sets.json"
    payload = json.loads(sets_path.read_text(encoding="utf-8"))
    by_name = {entry["name"]: entry for entry in payload}
    for code, count in counts.items():
        if code in by_name:
            by_name[code]["count"] = count
            by_name[code]["filter"] = True
            continue
        if code == "MEP":
            payload.append({
                "name": "MEP", "externalId": "PR-ME", "number": 1340,
                "count": count, "filter": True, "block": "NONE",
                "legalFormats": [
                    "6402e830-7fed-4cd1-b172-2a320047c2bb",
                    "98c83df9-ec82-4193-84a8-104115ce4e25",
                    "6a1dec5a-34db-4cee-a503-4ee759304135",
                ],
                "featuredArchetypes": [], "visibleUnfilterable": False,
                "promo": True,
            })
    sets_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
                         encoding="utf-8")

    formats_path = ROOT / "spirit" / "database" / "json_data" / "formats.json"
    formats = json.loads(formats_path.read_text(encoding="utf-8"))
    for fmt in formats.get("formats", []):
        if fmt.get("key") in ("Standard", "StandardNightly", "Expanded") \
                and "MEP" not in fmt["sets"]:
            fmt["sets"].append("MEP")
    formats_path.write_text(json.dumps(formats, indent=2, ensure_ascii=False) + "\n",
                            encoding="utf-8")


def run(selected: set[str], download_images: bool, workers: int) -> None:
    named_modules = existing_named_modules()
    guid_scripts = existing_guid_scripts()
    print_scripts = existing_print_scripts()
    generated_signatures: Dict[str, str] = {}
    image_tasks: list[tuple[str, Path]] = []
    counts: Dict[str, int] = {}
    created = reprints = skipped = 0

    # Seed exact Pokemon signatures for already implemented Standard cards.
    source_cache: Dict[str, list[dict]] = {}
    for catalog_stem, (api_stem, code) in STANDARD_SETS.items():
        api_cards = load_api_cards(api_stem)
        source_cache[api_stem] = api_cards
        catalog_names = {
            str(entry["n"]): fix_text(entry.get("name", ""))
            for entry in load_external_catalog(catalog_stem)["cards"]
        }
        for card in api_cards:
            number = api_collector_number(card, api_stem)
            preferred_name = catalog_names.get(number, fix_text(card.get("name", "")))
            path = ROOT / "spirit" / "game" / "scripts" / "cards" / code / (
                f"{clean_name(preferred_name)}_{number}.py"
            )
            if path.exists() and fix_text(card.get("supertype", "")).startswith("Pok"):
                generated_signatures.setdefault(mechanics_signature(card), module_for(path))

    for catalog_stem, (api_stem, code) in STANDARD_SETS.items():
        if selected and catalog_stem not in selected and code.lower() not in selected:
            continue
        catalog = load_external_catalog(catalog_stem)
        wanted = {str(card["n"]): card for card in catalog["cards"]}
        api_cards = source_cache[api_stem]
        api_by_number = {
            api_collector_number(card, api_stem): card for card in api_cards
        }
        by_name = {
            fix_text(card.get("name", "")): card
            for card in api_cards
            if fix_text(card.get("supertype", "")).startswith("Pok")
        }
        counts[code] = len(wanted)
        scripts_dir = ROOT / "spirit" / "game" / "scripts" / "cards" / code
        assets_dir = ROOT / "spirit" / "assets" / "cards" / code
        scripts_dir.mkdir(parents=True, exist_ok=True)
        assets_dir.mkdir(parents=True, exist_ok=True)

        for number, pobre_card in sorted(wanted.items(), key=lambda item: numeric(item[0])):
            card = api_by_number.get(number) or fallback_api_card(pobre_card, api_stem)
            # Pobre's catalogs repair the replacement-character mojibake found
            # in a few upstream Trainer names (notably "Pokémon ...").
            card = dict(card)
            name = fix_text(pobre_card.get("name") or card.get("name", "Unknown"))
            card["name"] = name
            card["number"] = number
            stem = f"{clean_name(name)}_{number}"
            script_path = scripts_dir / f"{stem}.py"
            card_guid = guid_for(card.get("id") or f"{code}-{number}")
            registered_path = (
                guid_scripts.get(card_guid.lower())
                or print_scripts.get((code, numeric(number)))
            )
            asset_stem = (
                registered_path.stem
                if registered_path is not None and registered_path.parent == scripts_dir
                else stem
            )
            asset_path = assets_dir / f"{asset_stem}.png"
            supertype = fix_text(card.get("supertype", ""))
            kind = "pokemon" if supertype.startswith("Pok") else supertype.lower()

            if registered_path is not None or script_path.exists():
                skipped += 1
            else:
                base_module = None
                if kind == "pokemon":
                    base_module = generated_signatures.get(mechanics_signature(card))
                elif kind in ("trainer", "energy"):
                    base_module = named_modules.get((kind, name))

                if base_module:
                    source = render_reprint(card, code, base_module)
                    reprints += 1
                elif kind == "pokemon":
                    source = render_pokemon(card, code, by_name)
                elif kind == "trainer":
                    source = render_trainer(card, code)
                elif kind == "energy":
                    source = render_energy(card, pobre_card, code)
                else:
                    raise ValueError(f"Unknown supertype {supertype!r} for {code}/{number}")
                script_path.write_text(source, encoding="utf-8")
                guid_scripts[card_guid.lower()] = script_path
                print_scripts[(code, numeric(number))] = script_path
                created += 1
                if kind == "pokemon":
                    generated_signatures.setdefault(mechanics_signature(card), module_for(script_path))
                else:
                    named_modules.setdefault((kind, name), module_for(script_path))

            if not asset_path.exists():
                url = (card.get("images") or {}).get("large") or pobre_card.get("image")
                if url:
                    image_tasks.append((url, asset_path))

        print(
            f"{catalog_stem.upper():4} -> {code:10}: {len(wanted):3} cards, "
            f"{len(list(scripts_dir.glob('*.py'))):3} scripts"
        )

    update_metadata(counts)
    print(f"Scripts created: {created} ({reprints} linked reprints); existing: {skipped}")

    if not download_images:
        print(f"Images still missing: {len(image_tasks)} (rerun with --download-images)")
        return
    failures = []
    done = 0
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = [pool.submit(download_one, task) for task in image_tasks]
        for future in as_completed(futures):
            ok, detail = future.result()
            done += 1
            if not ok:
                failures.append(detail)
            if done % 100 == 0 or done == len(futures):
                print(f"Images: {done}/{len(futures)} ({len(failures)} failures)")
    if failures:
        print("Image download failures:")
        for failure in failures:
            print("  " + failure)
        raise SystemExit(2)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "sets", nargs="*",
        help="Optional catalog stem or server code (default: every Standard set)",
    )
    parser.add_argument("--download-images", action="store_true")
    parser.add_argument("--workers", type=int, default=20)
    args = parser.parse_args()
    run({value.lower() for value in args.sets}, args.download_images, args.workers)


if __name__ == "__main__":
    main()
