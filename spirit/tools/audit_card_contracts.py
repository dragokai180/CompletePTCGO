"""Audit printed Pokemon data and catalog identity across every loaded set.

This checks declarations, not effect semantics. Run the scenario regressions and
semantic_effect_audit separately; a matched text/cost is not a working effect.
No card definitions, assets or accounts are changed by this command.
"""
import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes
from spirit.game.data_utils import ABILITIES_BY_ID, Attack, PokemonCardDef, def_for, prize_value
from spirit.game.scripts.cards import loader
from spirit.tools.audit_printed_resistance import load_sources, normalized_name
from spirit.tools.install_recent_card_art import DATA_ROOT


def value(attrs, attr, default=None):
    entry = attrs.get(str(attr.value), {})
    result = entry.get("value", default)
    if entry.get("type") == "json" and isinstance(result, str):
        return json.loads(result)
    return result


def audit(source_dirs, external_catalog_dir=None):
    loader.load_all()
    sources = load_sources(source_dirs)
    if external_catalog_dir:
        from spirit.tools.import_standard_sets import STANDARD_SETS, fallback_api_card
        for stem, (api_stem, code) in STANDARD_SETS.items():
            path = Path(external_catalog_dir) / (stem + "-cards.js")
            if not path.is_file():
                continue
            match = re.search(r"=\s*(\{.*\})\s*;\s*\n\s*if \(typeof window",
                              path.read_text(encoding="utf-8"), re.S)
            if match is None:
                raise ValueError("Unrecognized external catalog: " + str(path))
            for raw in json.loads(match.group(1))["cards"]:
                if raw.get("kind") != "pokemon":
                    continue
                identity = (code, int(raw["n"]), normalized_name(raw["name"]))
                if identity not in sources:
                    card = fallback_api_card(raw, api_stem)
                    card["_prize_count"] = int(raw.get("prizeCards", 1))
                    sources[identity] = [card]
    evolution_names = defaultdict(set)
    for model in loader.cards:
        definition = def_for(model.guid)
        if definition.display_name:
            evolution_names[normalized_name(definition.display_name)].add(
                normalized_name(model.get_attribute_value(AttrID.EVOLUTION_LOGIC_NAME)))
    # Both LEGEND halves represent one Pokemon. Some source records for the
    # top half omit the second Weakness printed on the bottom half.
    legend_weaknesses = defaultdict(dict)
    for (code, _, name), records in sources.items():
        for record in records:
            if "LEGEND" in record.get("subtypes", []):
                for weakness in record.get("weaknesses", []):
                    legend_weaknesses[(code, name)][weakness["type"]] = weakness
    issues, unmatched = [], []
    counts = Counter()
    images, collectors = defaultdict(list), defaultdict(list)

    def check(label, field, expected, actual):
        if expected != actual:
            issues.append(dict(card=label, field=field, expected=expected, actual=actual))

    for model in loader.cards:
        definition = def_for(model.guid)
        label = str(Path(loader.script_by_guid[model.guid]).relative_to(loader.scripts_dir))
        images[(definition.set_code, model.get_attribute_value(AttrID.IMAGE_URL))].append(label)
        collectors[(definition.set_code, definition.collector_number)].append(label)
        for ability in getattr(definition, "abilities", []):
            check(label, "registry/" + ability.title, True,
                  ABILITIES_BY_ID.get(ability.ability_id) is ability)
            if not isinstance(ability, Attack):
                # These rules are implemented by setup/entry legality or by
                # Cafe Master's resolver, rather than an executable Ability.
                external_rules = {"Gale Wings", "Explosiveness", "Shell Survival", "Additional Order"}
                check(label, "ability_implementation/" + ability.title, True,
                      ability.effect is not None or ability.passive is not None
                      or ability.title in external_rules)
        name = definition.display_name or (definition.name.split(".")[-2]
                if "." in definition.name else definition.name)
        identity = (definition.set_code, int(definition.collector_number), normalized_name(name))
        matches = sources.get(identity, [])
        if not matches:
            if isinstance(definition, PokemonCardDef):
                unmatched.append(label)
            continue
        printed = Path(label).stem.rsplit("_", 1)[-1].upper()
        exact = [c for c in matches if str(c["number"]).upper() == printed]
        card = (exact or matches)[0]
        counts[definition.set_code] += 1
        expected = {}
        if str(card.get("hp", "")).isdigit():
            expected[AttrID.HP] = int(card["hp"])
        if "retreatCost" in card or "convertedRetreatCost" in card:
            expected[AttrID.RETREAT_COST] = int(card.get("convertedRetreatCost", len(card.get("retreatCost", []))))
        if card.get("types"):
            expected[AttrID.POKEMON_TYPES] = [PokemonTypes[t.upper()].value for t in card["types"]]
        weaknesses = card.get("weaknesses") or []
        if "LEGEND" in card.get("subtypes", []):
            weaknesses = list(legend_weaknesses[(definition.set_code, normalized_name(name))].values())
        expected[AttrID.WEAKNESS_TYPES] = [PokemonTypes[w["type"].upper()].value for w in weaknesses]
        if weaknesses:
            expected[AttrID.WEAKNESS_AMOUNT] = int(re.sub(r"\D", "", weaknesses[0]["value"]))
        resistance = (card.get("resistances") or [{}])[0]
        expected[AttrID.RESISTANCE_TYPES] = (PokemonTypes[resistance["type"].upper()].value
                                           if resistance else PokemonTypes.UNSET.value)
        if resistance:
            expected[AttrID.RESISTANCE_AMOUNT] = int(re.sub(r"\D", "", resistance["value"]))
        subtypes = card.get("subtypes", [])
        for word, stage in (("Basic", PokemonStage.BASIC), ("Stage 1", PokemonStage.STAGE1),
                            ("Stage 2", PokemonStage.STAGE2)):
            if word in subtypes:
                expected[AttrID.STAGE] = stage.value
        # Read the actual rule box. Single-Pokemon LEGEND cards give one
        # Prize; dual LEGEND cards give two. Mega ex rules override ex's two.
        prize_rules = [int(n) for rule in card.get("rules", []) for n in
                       re.findall(r"opponent takes (\d+) prize cards", rule.lower())]
        subtype_prizes = (3 if "MEGA" in subtypes and "ex" in subtypes else
                          3 if any(s in subtypes for s in ("TAG TEAM", "VMAX", "SV_Mega")) else
                          2 if any(s in subtypes for s in ("EX", "ex", "GX", "V", "VSTAR", "V-UNION")) else 1)
        expected_prizes = max(prize_rules, default=card.get("_prize_count", subtype_prizes))
        check(label, "prizes/rule_box", expected_prizes, prize_value(definition.guid))
        for layer, attrs in (("definition", definition.extra_attributes),
                             ("model", model.attributes),
                             ("client", model.to_archetype_attributes("audit"))):
            for attr, wanted in expected.items():
                check(label, layer + "/" + attr.name, wanted, value(attrs, attr))
            if card.get("evolvesFrom"):
                # Match the actual base's engine identity (e.g. Flabebe's
                # historic internal "Flabb"), not a newly invented spelling.
                base_name = normalized_name(card["evolvesFrom"])
                valid = evolution_names.get(base_name) or {base_name}
                check(label, layer + "/evolves_from", True,
                      normalized_name(value(attrs, AttrID.EVOLUTION_LOGIC_FROM, "")) in valid)
        attacks = [a for a in getattr(definition, "abilities", []) if isinstance(a, Attack)]
        check(label, "attack_count", len(card.get("attacks", [])), len(attacks))
        for printed_attack, attack in zip(card.get("attacks", []), attacks):
            if printed_attack.get("text"):
                check(label, "attack_text_present/" + attack.title, True, bool(attack.game_text))
            check(label, "attack_name/" + attack.title,
                  normalized_name(printed_attack["name"]), normalized_name(attack.title))
            costs = dict(Counter(PokemonTypes[t.upper()].value for t in printed_attack.get("cost", [])
                                 if t.lower() != "free"))
            actual = {getattr(t, "value", t): n for t, n in attack.cost.items() if n}
            check(label, "attack_cost/" + attack.title, costs, actual)
            damage = str(printed_attack.get("damage", ""))
            digits = "".join(c for c in damage if c.isdigit())
            # Text-targeted attacks can keep their damage operand in the
            # engine's damage field even when no number is printed at right.
            if digits:
                check(label, "attack_damage/" + attack.title, int(digits), attack.damage or 0)
        printed_titles = {normalized_name(a["name"]) for a in card.get("abilities", [])}
        actual_titles = {normalized_name(a.title) for a in getattr(definition, "abilities", [])
                         if not isinstance(a, Attack)}
        check(label, "ability_names", sorted(printed_titles), sorted(actual_titles))
    collisions = {}
    for kind, mapping in (("image", images), ("collector", collectors)):
        collisions[kind] = [{"identity": list(k), "cards": v} for k, v in mapping.items() if len(v) > 1]
    return dict(catalog_cards=len(loader.cards), compared=sum(counts.values()),
                sets=dict(sorted(counts.items())), issues=issues, collisions=collisions,
                unmatched=unmatched)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", type=Path, action="append", default=[])
    parser.add_argument("--external-catalog-dir", type=Path)
    parser.add_argument("--json", type=Path, required=True)
    args = parser.parse_args()
    result = audit([DATA_ROOT, *args.source_dir], args.external_catalog_dir)
    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({k: v for k, v in result.items()
                      if k not in ("sets", "issues", "unmatched")}, ensure_ascii=False))
    print("Compared:", result["compared"], "Issues:", len(result["issues"]),
          "Unmatched:", len(result["unmatched"]))
    return int(bool(result["issues"] or result["unmatched"]
                    or any(result["collisions"].values())))


if __name__ == "__main__":
    raise SystemExit(main())
