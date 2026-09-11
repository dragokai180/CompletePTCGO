"""Exercise shared text effects and report families that make no rule action.

``effect_smoke`` is deliberately a crash detector.  A generic interpreter can
return successfully without recognizing a card, though, which used to make a
large imported set look implemented.  This audit records the rule primitives
used while one representative of each exact-text family resolves.

Examples::

    python -m spirit.tools.semantic_effect_audit --kind ability --json ability.json
    python -m spirit.tools.semantic_effect_audit --kind trainer --only-problems
"""
from __future__ import annotations

import argparse
import asyncio
import contextvars
import inspect
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

from spirit.game.attributes import (
    AttrID, CLIENT_SPECIAL_CONDITION_NAMES, PokemonStage, PokemonTypes,
    SpecialConditions, TrainerType,
)
from spirit.game.data_utils import (
    Ability, Attack, CARD_DEFS_BY_GUID, EnergyCardDef, ItemCardDef, PokemonCardDef,
    PokemonToolCardDef, StadiumCardDef, SupporterCardDef, evolves_from,
    evolves_from_chain,
)
from spirit.game.models.board import PokemonEntity, create_card_entity
from spirit.game.scripts.cards import loader as card_loader
from spirit.game.session.effects import (
    EffectContext, is_basic_energy, is_basic_pokemon, is_special_energy,
)
from spirit.game.session.legal_actions import TurnState
from spirit.game.session.passives import effective_max_hp
from spirit.tools.effect_smoke import (
    FAIL,
    PASS,
    P1,
    P2,
    GUID_RE,
    _plan_tests,
    _def_attr,
    basic_energy_guids,
    pick_filler_basic,
    pick_filler_item,
    run_one,
)
from spirit.tools.generic_effect_audit import _norm, grouped, scan


_EVENTS = contextvars.ContextVar("semantic_effect_events", default=None)

# Choices alone are not evidence that a rule effect completed.  These are the
# primitives that mutate game state, reveal private information, or establish
# a temporary rule.  A coin flip counts because tails may correctly leave the
# board unchanged.
TRACE_METHODS = (
    "deal_damage", "knock_out", "heal", "apply_special_condition",
    "cure_all_conditions", "cure_condition", "add_turn_damage_modifier",
    "add_extra_prize_watcher", "add_temporary_passive",
    "add_temporary_player_passive", "force_next_coin_result",
    "force_coins_through_next_turn", "lock_gx_attacks",
    "require_trainer_flip", "end_turn_if_energy_attached_to",
    "set_supporter_limit",
    "add_passive_through_opponents_turn", "add_passive_through_own_next_turn",
    "lock_retreat", "lock_plays", "restrict_attachments",
    "require_attack_flip", "ignore_own_target_effects", "take_extra_turn",
    "schedule_at_checkup", "schedule_discard_at_checkup", "use_attack",
    "flip_coins", "flip_until_tails",
    "place_damage_counters", "set_damage_counters", "move_damage_counters",
    "search_deck", "search_deck_groups", "discard_from_hand", "draw_cards",
    "draw_until", "put_in_hand", "reveal_cards", "reveal_hand",
    "discard_cards", "discard_energy_from", "discard_energy_units_from",
    "move_to_lost_zone", "look_at_prizes_take_basic", "shuffle_deck",
    "shuffle_into_deck", "hand_to_bottom_of_deck", "reorder_deck_top",
    "shuffle_deck_below", "put_on_top_of_deck", "put_on_bottom_of_deck",
    "bench_pokemon", "evolve_pokemon", "devolve_pokemon", "identity_swap",
    "attach_card", "attach_energy", "move_energy", "move_energy_freely", "switch_active",
    "take_prizes", "put_in_prizes", "shuffle_prizes", "win_game",
    "discard_stadium",
)

# A few rule locks are deliberately written straight into TurnState instead
# of going through EffectContext.  Trace them as well; otherwise fully working
# attacks such as Giga Impact and Corner look incomplete to the semantic audit.
TURN_STATE_TRACE_METHODS = (
    "lock_attack", "lock_retreat", "lock_plays", "restrict_attachments",
    "require_trainer_flip", "require_attach_ends_turn",
    "set_attack_flip_check",
)


def _expected_event_groups(kind: str, text: str):
    """Conservative state-operation expectations inferred from printed text.

    A callable generic effect is not complete merely because it changed one
    value.  Multi-clause cards are the common failure mode in bulk imports, so
    the semantic report also records broad operations explicitly promised by
    their text.  Alternatives in a group represent equivalent engine paths
    (for example a deck search may put the selected card in hand internally).

    This intentionally avoids damage/discard phrases behind coin flips or
    other optional outcomes; those need richer branch exploration rather than
    being mislabeled as definite failures in a single deterministic run.
    """
    groups = []

    def add(label, methods):
        if not any(existing[0] == label for existing in groups):
            groups.append((label, frozenset(methods)))

    sentences = [part.strip(" ,") for part in re.split(r"[.!?]+", text)]
    draw_commands = [part for part in sentences if re.search(
        r"(?:^|\bthen,? )draw (?:a|\d+|until|cards?|a number)", part
    ) and not part.startswith("for each heads")
       and not part.startswith("your opponent may draw")]
    if draw_commands:
        add("draw cards", {"draw_cards", "draw_until"})
    if "search your deck" in text and "choose 1:" not in text:
        add("search the deck", {"search_deck", "search_deck_groups"})
    if re.search(r"(?:^|[.!?]\s)(?:then,? )?(?:you may )?attach\b", text) \
            and "energy" in text:
        add("attach Energy", {"attach_energy", "attach_card", "move_energy"})
    if "heal " in text:
        add("heal damage", {"heal"})
    if re.search(r"is now (?:asleep|burned|confused|paralyzed|poisoned)", text) \
            and "if the defending pokémon" not in text:
        add("apply a Special Condition", {"apply_special_condition"})
    if "switch" in text and "pokémon" in text and "deck" not in text \
            and "switch all damage counters" not in text:
        add("switch Pokémon", {"switch_active", "identity_swap"})
    if re.search(r"(?:^|[.!?]\s)(?:then,? )?(?:you may )?move\b", text) \
            and "energy" in text:
        add("move Energy", {"move_energy", "move_energy_freely"})
    if "before you put it into your hand" not in text and re.search(
            r"(?:put|return) .+ (?:into|to) (?:your|its owner's|their) hand", text
    ) and "shuffle your hand" not in text:
        alternatives = {"put_in_hand", "draw_cards", "draw_until"}
        if "you may reveal" in text and "find there" in text:
            # A private-zone search may legally fail; presenting the complete
            # inspected zone proves the optional branch was offered.
            alternatives.add("reveal_cards")
        if "search your deck" in text:
            alternatives.update({"search_deck", "search_deck_groups"})
        if "devolve" in text:
            alternatives.add("devolve_pokemon")
        add("put cards into a hand", alternatives)
    if re.search(r"put .+ (?:on top of|on the bottom of|at the bottom of) .+deck", text):
        boundary_methods = {
            "put_on_top_of_deck", "put_on_bottom_of_deck",
            "hand_to_bottom_of_deck", "shuffle_deck_below",
            "reorder_deck_top",
        }
        if "put the other card back on top of your deck" in text:
            # After one of the inspected top two enters the hand, the other
            # is already the top card; no redundant wire move is required.
            boundary_methods.add("put_in_hand")
        add("put cards at a deck boundary", boundary_methods)
    shuffle_commands = [part for part in sentences if re.search(
        r"(?:^|\bthen,? |\bopponent )shuffle\b", part
    ) and not part.startswith("if ") and " or shuffle " not in part]
    if shuffle_commands and "choose 1:" not in text:
        add("shuffle cards", {
            "shuffle_deck", "shuffle_into_deck", "shuffle_deck_below",
            "hand_to_bottom_of_deck", "put_on_bottom_of_deck",
            "put_in_prizes", "shuffle_prizes",
        })
    discard_commands = [part for part in sentences if re.match(
        r"(?:then,? )?(?:you may )?discard\b", part
    )]
    if discard_commands:
        add("discard cards", {
            "discard_cards", "discard_from_hand", "discard_energy_from",
            "discard_energy_units_from", "discard_stadium",
            "schedule_discard_at_checkup",
        })
    if re.search(r"(?:^|[.!?]\s)(?:then,? )?(?:you may )?attach\b", text) \
            and "pokémon tool" in text:
        add("attach a Pokémon Tool", {"attach_card"})
    counter_commands = [part for part in sentences if re.match(
        r"(?:then,? )?(?:you may )?(?:put|place|move) "
        r"(?:up to )?(?:a|an|\d+|all|any number of) damage counters?\b",
        part,
    )]
    if counter_commands:
        counter_methods = {
            "deal_damage", "place_damage_counters", "set_damage_counters",
            "move_damage_counters",
        }
        if "damage counters instead of" in text:
            counter_methods.add("apply_special_condition")
        add("place/move damage counters", counter_methods)
    if any(re.match(r"(?:then,? )?(?:put|send|move)\b", part)
           and "lost zone" in part for part in sentences):
        add("move cards to the Lost Zone", {"move_to_lost_zone"})
    if any(re.match(
            r"(?:then,? )?(?:you may )?take "
            r"(?:an?|one|\d+|up to \d+) prize cards?\b", part,
    ) for part in sentences):
        add("take Prize cards", {"take_prizes"})
    if "reveal" in text or "show " in text:
        add("reveal cards", {
            "reveal_cards", "reveal_hand", "search_deck", "put_in_hand",
            # Moving a formerly hidden hand card to the public discard pile
            # is itself a reveal (Busybody and equivalent hand powers).
            "discard_cards", "discard_from_hand",
            # Cards shuffled from a public discard pile stay public throughout
            # the move; the grouped move itself is the required reveal.
            "shuffle_into_deck",
        })
    if "devolve" in text:
        add("devolve Pokémon", {"devolve_pokemon"})
    elif re.search(r"(?:^|[.!?]\s)(?:then,? )?(?:you may )?evolve\b", text) \
            and "can't evolve" not in text:
        add("evolve Pokémon", {"evolve_pokemon"})
    if "can't play any" in text or "cannot play any" in text:
        add("lock card plays", {"lock_plays", "add_temporary_player_passive"})
    if re.search(r"(?:can't|cannot) (?:attack|use any attacks)", text):
        add("lock attacks", {
            "lock_attack",
            "add_temporary_passive", "add_temporary_player_passive",
            "add_passive_through_opponents_turn", "add_passive_through_own_next_turn",
            "card_passive",
        })
    if re.search(r"(?:can't|cannot) retreat", text):
        add("lock retreat", {
            "lock_retreat", "add_temporary_passive",
            "add_temporary_player_passive", "card_passive",
        })
    if re.search(r"prevent all (?:damage|effects of attacks)", text):
        add("prevent future damage/effects", {
            "add_temporary_passive", "add_temporary_player_passive",
            "add_passive_through_opponents_turn", "add_passive_through_own_next_turn",
            "card_passive",
        })
    if "take another turn after this one" in text:
        add("take another turn", {"take_extra_turn"})
    if re.search(r"(?:you|that player) win(?:s)? (?:the )?game", text):
        add("win the game", {"win_game"})
    direct_ko_clauses = [
        part for part in sentences
        if re.search(r"(?:it|that pokémon|the defending pokémon) is knocked out", part)
        and "during your next turn" not in part
        and "at the end of" not in part
        and "even if it is knocked out" not in part
    ]
    if direct_ko_clauses:
        add("Knock Out a Pokémon", {"knock_out", "deal_damage"})
    return groups


def _missing_expected_events(kind: str, text: str, events):
    seen = set(events)
    return [label for label, alternatives in _expected_event_groups(kind, text)
            if not seen.intersection(alternatives)]


class _Trace:
    def __init__(self):
        self.originals = {}
        self.turn_state_originals = {}

    def __enter__(self):
        for name in TRACE_METHODS:
            original = getattr(EffectContext, name, None)
            if original is None:
                continue
            self.originals[name] = original
            if inspect.iscoroutinefunction(original):
                async def async_wrapper(ctx, *args, _name=name,
                                        _original=original, **kwargs):
                    events = _EVENTS.get()
                    if events is not None:
                        events.append(_name)
                    return await _original(ctx, *args, **kwargs)
                setattr(EffectContext, name, async_wrapper)
            else:
                def wrapper(ctx, *args, _name=name, _original=original, **kwargs):
                    events = _EVENTS.get()
                    if events is not None:
                        events.append(_name)
                    return _original(ctx, *args, **kwargs)
                setattr(EffectContext, name, wrapper)
        for name in TURN_STATE_TRACE_METHODS:
            original = getattr(TurnState, name, None)
            if original is None:
                continue
            self.turn_state_originals[name] = original
            if inspect.iscoroutinefunction(original):
                async def async_wrapper(state, *args, _name=name,
                                        _original=original, **kwargs):
                    events = _EVENTS.get()
                    if events is not None:
                        events.append(_name)
                    return await _original(state, *args, **kwargs)
                setattr(TurnState, name, async_wrapper)
            else:
                def wrapper(state, *args, _name=name,
                            _original=original, **kwargs):
                    events = _EVENTS.get()
                    if events is not None:
                        events.append(_name)
                    return _original(state, *args, **kwargs)
                setattr(TurnState, name, wrapper)
        return self

    def __exit__(self, *_):
        for name, original in self.originals.items():
            setattr(EffectContext, name, original)
        for name, original in self.turn_state_originals.items():
            setattr(TurnState, name, original)


def _definition(copy: dict):
    """Resolve an audit printing without depending on its source layout.

    Imported cards can be normalized at load time (notably a passive-looking
    Ability becoming a triggered Ability).  Those runtime families may not be
    visible to the AST inventory, and generated reprints need not contain a
    literal GUID in their module.  Keep the old path lookup as a compatibility
    fallback for static trainer/attack rows.
    """
    guid = (copy.get("guid") or "").lower()
    if guid:
        definition = CARD_DEFS_BY_GUID.get(guid)
        if definition is not None:
            return definition
    path = copy.get("path")
    if not path:
        return None
    text = Path(path).read_text(encoding="utf-8")
    match = GUID_RE.search(text)
    return CARD_DEFS_BY_GUID.get(match.group(1).lower()) if match else None


def _runtime_shared_ability_groups():
    """Inventory every Ability still delegated to the shared interpreter.

    The source scanner intentionally reports how modules were authored.  The
    semantic audit must instead exercise what the server actually registered:
    standard normalization infers event triggers for many imported cards and
    routes them through ``bw_legacy_ability`` only after loading.  Auditing the
    runtime definitions closes that otherwise invisible coverage gap.
    """
    groups = defaultdict(list)
    source_by_guid = {}
    root = Path("spirit/game/scripts/cards")
    for path in root.rglob("*.py"):
        if path.name == "__init__.py" or "__pycache__" in path.parts:
            continue
        try:
            source = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        for match in GUID_RE.finditer(source):
            source_by_guid.setdefault(match.group(1).lower(), str(path))

    for guid, definition in CARD_DEFS_BY_GUID.items():
        if not isinstance(definition, PokemonCardDef) \
                and not getattr(definition, "plays_as_pokemon", False):
            continue
        for ability in getattr(definition, "abilities", ()) or ():
            if isinstance(ability, Attack):
                continue
            effect_name = getattr(getattr(ability, "effect", None), "__name__", "")
            if effect_name not in {"standard_ability", "bw_legacy_ability"}:
                continue
            key = ("ability", ability.title, _norm(ability.game_text))
            groups[key].append({
                "card": getattr(definition, "display_name", "") or definition.name,
                "set": getattr(definition, "set_code", "") or definition.key,
                "path": source_by_guid.get(guid.lower(), ""),
                "guid": guid.lower(),
            })
    return groups


def _runner(definition, kind: str, title: str, text: str):
    plans = _plan_tests(definition)
    if kind == "trainer":
        return next((plan for plan in plans if plan[2] == "trainer"), None)
    if kind == "ability":
        matching = next((
            ability for ability in (getattr(definition, "abilities", ()) or ())
            if isinstance(ability, Ability)
            and _norm(ability.title) == _norm(title)
            and _norm(ability.game_text) == text
        ), None)
        if matching is not None and matching.effect is None \
                and matching.passive is not None:
            return ("passive", title, "passive", True)
    for plan in plans:
        key = plan[2]
        if not isinstance(key, Ability):
            continue
        if _norm(key.title) == _norm(title) and _norm(key.game_text) == text:
            return plan
    return None


def _semantic_scenario(kind: str, text: str, forced_coin=None):
    """Return a deterministic board enricher for conditional effect families.

    The smoke rig deliberately starts generic.  That is excellent for crashes,
    but a semantic audit must also supply the public preconditions printed on
    the card; otherwise a correctly implemented conditional effect is reported
    as a no-op.  All mutations here happen before tracing the card's behavior.
    """
    if kind not in ("attack", "ability", "trainer"):
        return None
    # Match the runtime interpreter's normalization of API energy glyphs.
    text = re.sub(r"\[\s*\[\s*([a-z]+)\s*\]\s*\]", r"\1", text)

    def setup(rig, entities, runner_key):
        board = rig.board
        if forced_coin is not None:
            # Run the same exact-text family under both possible first flip
            # results.  This exposes missing tails riders without relying on
            # whichever deterministic seed happened to be chosen.
            rig.session.turn_state.forced_coin_result = bool(forced_coin)

        def area(pid, name):
            return board.find_player_area(pid, name)

        def definition_name(definition):
            return (getattr(definition, "display_name", "") or "").casefold()

        def inject(pid, area_name, predicate):
            target_area = area(pid, area_name)
            if target_area is None:
                return None
            for definition in CARD_DEFS_BY_GUID.values():
                if not predicate(definition):
                    continue
                card_obj = card_loader.cards_by_guid.get(definition.guid.lower())
                if card_obj is None:
                    continue
                entity = create_card_entity(card_obj, owning_player_id=pid)
                board.add_card_to_area(entity, target_area)
                return entity
            return None

        def inject_many(pid, area_name, predicate, count):
            return [card for _ in range(max(0, count))
                    if (card := inject(pid, area_name, predicate)) is not None]

        type_words = {
            "grass": PokemonTypes.GRASS,
            "fire": PokemonTypes.FIRE,
            "water": PokemonTypes.WATER,
            "lightning": PokemonTypes.LIGHTNING,
            "psychic": PokemonTypes.PSYCHIC,
            "fighting": PokemonTypes.FIGHTING,
            "darkness": PokemonTypes.DARKNESS,
            "metal": PokemonTypes.METAL,
            "colorless": PokemonTypes.COLORLESS,
            "dragon": PokemonTypes.DRAGON,
        }

        def definition_types(definition):
            raw = _def_attr(definition, AttrID.POKEMON_TYPES, []) or []
            if isinstance(raw, str):
                try:
                    raw = json.loads(raw)
                except (TypeError, ValueError, json.JSONDecodeError):
                    raw = [raw]
            return {
                item.value if isinstance(item, PokemonTypes) else item
                for item in raw
            }

        def energy_of_type(definition, pokemon_type):
            if not isinstance(definition, EnergyCardDef):
                return False
            printed = getattr(definition, "energy_type", None)
            printed = printed.value if isinstance(printed, PokemonTypes) else printed
            return printed == pokemon_type.value

        def pokemon_of_type(definition, pokemon_type):
            return isinstance(definition, PokemonCardDef) \
                and pokemon_type.value in definition_types(definition)

        def replace_active(pid, predicate):
            active = area(pid, "activePokemonArea")
            discard = area(pid, "discard")
            if active is None:
                return None
            for old in list(active.children):
                board.move_card(old.entity_id, discard.entity_id)
            replacement = inject(pid, "activePokemonArea", predicate)
            if replacement is not None:
                entities["p1_active" if pid == P1 else "p2_active"] = replacement
            return replacement

        if kind == "trainer":
            # Generic Trainer scripts commonly depend on public cards outside
            # the deck.  Give the auditor legal representatives of exactly
            # the zones/types mentioned by the printing so a false condition
            # does not hide a missing implementation.
            if "discard pile" in text:
                if "trainer card" in text:
                    inject(P1, "discard", lambda d: isinstance(
                        d, (ItemCardDef, SupporterCardDef, StadiumCardDef,
                            PokemonToolCardDef)
                    ))
                if "supporter card" in text:
                    inject(P1, "discard", lambda d: isinstance(d, SupporterCardDef))
                if "item card" in text:
                    inject(P1, "discard", lambda d: type(d) is ItemCardDef)
                if "pokémon tool" in text:
                    inject(P1, "discard", lambda d: isinstance(d, PokemonToolCardDef))
                if "pokémon" in text:
                    inject(P1, "discard", lambda d: isinstance(d, PokemonCardDef))
                if "basic energy" in text:
                    inject(P1, "discard", lambda d: isinstance(d, EnergyCardDef)
                           and not bool(_def_attr(
                               d, AttrID.IS_SPECIAL_ENERGY, False)))
                if "special energy" in text:
                    inject(P1, "discard", lambda d: isinstance(d, EnergyCardDef)
                           and bool(_def_attr(d, AttrID.IS_SPECIAL_ENERGY, False)))

            if "opponent reveals" in text and "hand" in text \
                    or "look at your opponent's hand" in text:
                inject(P2, "hand", lambda d: isinstance(d, PokemonCardDef)
                       and _def_attr(d, AttrID.STAGE) == PokemonStage.BASIC.value)
                inject(P2, "hand", lambda d: type(d) is ItemCardDef)
                inject(P2, "hand", lambda d: isinstance(d, SupporterCardDef))
                inject(P2, "hand", lambda d: isinstance(d, EnergyCardDef))

            # Public board targets used by Tools, Stadium removals and swaps.
            if "stadium" in text:
                stadium = inject(P1, "hand", lambda d: isinstance(d, StadiumCardDef))
                stadium_slot = board.find_global_area("activeStadium")
                if stadium is not None and stadium_slot is not None:
                    board.move_card(stadium.entity_id, stadium_slot.entity_id)
            if 'has "ogerpon" in its name' in text:
                ogerpon = lambda d: isinstance(d, PokemonCardDef) \
                    and "ogerpon" in definition_name(d) \
                    and "ex" in {str(s).casefold() for s in (d.subtypes or [])}
                inject(P1, "discard", ogerpon)
                inject(P1, "bench", ogerpon)
            if "pokémon tool" in text and "attached" in text:
                tool = inject(P2, "hand", lambda d: isinstance(d, PokemonToolCardDef))
                targets = board.pokemon_in_play(P2)
                if tool is not None and targets:
                    board.attach_card(tool.entity_id, targets[-1].entity_id)
            if "special energy" in text and "attached" in text:
                energy = inject(P2, "hand", lambda d: isinstance(d, EnergyCardDef)
                                and bool(_def_attr(
                                    d, AttrID.IS_SPECIAL_ENERGY, False)))
                targets = board.pokemon_in_play(P2)
                if energy is not None and targets:
                    board.attach_card(energy.entity_id, targets[0].entity_id)

            # Public target shapes used by restrictive Trainer conditions.
            # The ordinary smoke board is intentionally neutral Colorless;
            # replace/add only what the printed restriction makes public.
            typed_attach_targets = {
                "fire pokémon": PokemonTypes.FIRE,
                "water pokémon": PokemonTypes.WATER,
                "dragon pokémon": PokemonTypes.DRAGON,
            }
            for phrase, ptype in typed_attach_targets.items():
                if phrase in text and "attach" in text:
                    inject(P1, "bench", lambda d, ptype=ptype:
                           pokemon_of_type(d, ptype)
                           and _def_attr(d, AttrID.STAGE) == PokemonStage.BASIC.value)
            if "future pokémon" in text:
                inject(P1, "bench", lambda d: isinstance(d, PokemonCardDef)
                       and "future" in {str(s).casefold()
                                        for s in (d.subtypes or [])})
            if "team aqua pokémon" in text:
                aqua = lambda d: isinstance(d, PokemonCardDef) and (
                    "team aqua" in {str(s).casefold() for s in (d.subtypes or [])}
                    or definition_name(d).startswith("team aqua's ")
                )
                replace_active(P1, aqua)
            if "stage 2 grass, fire, or water pokémon" in text:
                inject(P1, "bench", lambda d: isinstance(d, PokemonCardDef)
                       and _def_attr(d, AttrID.STAGE) == PokemonStage.STAGE2.value
                       and bool(definition_types(d).intersection({
                           PokemonTypes.GRASS.value, PokemonTypes.FIRE.value,
                           PokemonTypes.WATER.value,
                       })))
            if any(name in text for name in (
                    "geodude", "graveler", "golem", "onix-gx", "cubone",
                    "rhyhorn", "rhydon", "sudowoodo")) and "attach" in text:
                inject(P1, "bench", lambda d: definition_name(d) == "geodude")

            if text.startswith("choose 1 of your basic pokémon in play") \
                    and "counts as evolving" in text:
                basic = inject(P1, "bench", lambda d: definition_name(d) == "snivy")
                if basic is not None:
                    inject(P1, "hand", lambda d: definition_name(d) == "servine")
            if "basic darkness pokémon in your discard pile" in text:
                inject(P1, "discard", lambda d: isinstance(d, PokemonCardDef)
                       and _def_attr(d, AttrID.STAGE) == PokemonStage.BASIC.value
                       and PokemonTypes.DARKNESS.value in definition_types(d))

            if text.startswith("devolve 1 of your evolved"):
                if "psychic pokémon" in text:
                    evolution = inject(P1, "bench", lambda d:
                        isinstance(d, PokemonCardDef)
                        and _def_attr(d, AttrID.STAGE) == PokemonStage.STAGE1.value
                        and PokemonTypes.PSYCHIC.value in definition_types(d))
                    from_name = evolution.get_attribute(AttrID.EVOLUTION_LOGIC_FROM) \
                        if evolution is not None else None
                    base = inject(P1, "hand", lambda d, from_name=from_name:
                        isinstance(d, PokemonCardDef)
                        and _def_attr(d, AttrID.EVOLUTION_LOGIC_NAME) == from_name)
                else:
                    base = inject(P1, "hand", lambda d:
                                  definition_name(d) == "snivy")
                    evolution = inject(P1, "bench", lambda d:
                                       definition_name(d) == "servine")
                if base is not None and evolution is not None:
                    board.attach_card(base.entity_id, evolution.entity_id)

            if text.startswith("discard up to 2 of your benched pokémon"):
                for pokemon in board.pokemon_in_play(P1)[1:]:
                    pokemon.set_attribute(
                        AttrID.HP, effective_max_hp(board, pokemon)
                    )
            if "ultra beasts' attacks" in text or "your ultra beasts" in text:
                inject(P1, "bench", lambda d: isinstance(d, PokemonCardDef)
                       and "ultra beast" in {str(s).casefold()
                                              for s in (d.subtypes or [])})
            if "30 hp or less remaining" in text:
                active = board.active_pokemon(P1)
                if active is not None:
                    active.set_attribute(AttrID.HP, min(
                        30, max(10, effective_max_hp(board, active) - 10)
                    ))
            for phrase, ptype in (
                    ("fairy energy attached", PokemonTypes.FAIRY),
                    ("grass energy attached", PokemonTypes.GRASS)):
                if phrase in text:
                    target = board.active_pokemon(P1)
                    energy = inject(P1, "hand", lambda d, ptype=ptype:
                                    energy_of_type(d, ptype))
                    if target is not None and energy is not None:
                        board.attach_card(energy.entity_id, target.entity_id)
            if "active dragon pokémon" in text:
                dragon = replace_active(
                    P1, lambda d: pokemon_of_type(d, PokemonTypes.DRAGON)
                    and _def_attr(d, AttrID.STAGE) == PokemonStage.BASIC.value
                )
                if dragon is not None:
                    dragon.set_attribute(
                        AttrID.HP,
                        max(10, effective_max_hp(board, dragon) - 30),
                    )
            if text.startswith("move an energy from 1 of your benched pokémon"):
                bench = board.find_player_area(P1, "bench")
                if bench is not None and bench.children:
                    energy = inject(P1, "hand", lambda d: isinstance(d, EnergyCardDef))
                    if energy is not None:
                        board.attach_card(energy.entity_id, bench.children[0].entity_id)

            if "supporter and stadium cards from your discard pile" in text:
                inject(P1, "discard", lambda d: isinstance(d, SupporterCardDef))
                inject(P1, "discard", lambda d: isinstance(d, StadiumCardDef))
            if "benched mega evolution pokémon" in text:
                inject(P2, "bench", lambda d: isinstance(d, PokemonCardDef)
                       and "mega" in {str(s).casefold()
                                      for s in (d.subtypes or [])})
            if "switch your active water pokémon" in text:
                replace_active(P1, lambda d: pokemon_of_type(d, PokemonTypes.WATER)
                               and _def_attr(d, AttrID.STAGE)
                               == PokemonStage.BASIC.value)

            if "was knocked out during your opponent's last turn" in text:
                ko_entry = {"entity_id": "semantic-ko"}
                if "fairy pokémon" in text:
                    fairy = next((d for d in CARD_DEFS_BY_GUID.values()
                                  if pokemon_of_type(d, PokemonTypes.FAIRY)), None)
                    if fairy is not None:
                        ko_entry["archetype_id"] = fairy.guid
                rig.session.turn_state.kos_suffered_last_turn[P1] = [ko_entry]
                if "fairy pokémon" in text:
                    inject_many(P1, "discard", lambda d:
                                pokemon_of_type(d, PokemonTypes.FAIRY), 2)
            if "discard a darkness pokémon from your hand" in text:
                inject(P1, "hand", lambda d: pokemon_of_type(d, PokemonTypes.DARKNESS))
            if "discard dana, evelyn, and nita from your hand" in text:
                for wanted in ("dana", "evelyn", "nita"):
                    inject(P1, "hand", lambda d, wanted=wanted:
                           definition_name(d) == wanted)
            if text.startswith("you can play this card only if your active pokémon is a water"):
                replace_active(P1, lambda d: pokemon_of_type(d, PokemonTypes.WATER)
                               and _def_attr(d, AttrID.STAGE)
                               == PokemonStage.BASIC.value)
                inject(P2, "bench", lambda d: isinstance(d, PokemonCardDef)
                       and _def_attr(d, AttrID.STAGE) == PokemonStage.BASIC.value)
            if "opponent has exactly 3 prize cards remaining" in text:
                prizes = area(P2, "prizePile")
                deck = area(P2, "deck")
                if prizes is not None and deck is not None:
                    for card in list(prizes.children)[3:]:
                        board.move_card(card.entity_id, deck.entity_id)
            if "ultra beast card" in text and "prize cards" in text:
                inject(P1, "prizePile", lambda d: isinstance(d, PokemonCardDef)
                       and "Ultra Beast" in (getattr(d, "subtypes", ()) or ()))
            if "custom catcher cards at once" in text \
                    or "mixed herbs cards at once" in text:
                target = entities.get("target")
                if target is not None:
                    extra = create_card_entity(
                        card_loader.cards_by_guid[target.archetype_id.lower()],
                        owning_player_id=P1,
                    )
                    board.add_card_to_area(extra, area(P1, "hand"))
            if "only when it is the last card in your hand" in text:
                hand = area(P1, "hand")
                deck = area(P1, "deck")
                target = entities.get("target")
                if hand is not None and deck is not None:
                    for card in list(hand.children):
                        if card is not target:
                            board.move_card(card.entity_id, deck.entity_id)
                inject(P1, "discard", lambda d: pokemon_of_type(
                    d, PokemonTypes.FIGHTING))
            if "only if you go second" in text and "first turn" in text:
                rig.session.turn_state.turn_number = 2
                rig.session.first_player_id = P2

            if text.startswith("attach 2 fire energy cards from your discard pile"):
                inject_many(P1, "discard", lambda d:
                            energy_of_type(d, PokemonTypes.FIRE), 2)
            if "n's darmanitan" in text and "n's zekrom" in text:
                names = ("n's darmanitan", "n's zoroark ex", "n's vanilluxe",
                         "n's klinklang", "n's reshiram", "n's zekrom")
                # Six required Pokémon exactly fill Active + five Bench slots.
                old = list(board.pokemon_in_play(P1))
                discard = area(P1, "discard")
                for pokemon in old:
                    board.move_card(pokemon.entity_id, discard.entity_id)
                for index, wanted in enumerate(names):
                    inject(P1, "activePokemonArea" if index == 0 else "bench",
                           lambda d, wanted=wanted: definition_name(d) == wanted)
            if "knocked out during your opponent's last turn" in text \
                    and not rig.session.turn_state.kos_suffered_last_turn.get(P1):
                rig.session.turn_state.kos_suffered_last_turn[P1] = [
                    {"entity_id": "semantic-ko"}
                ]

        if kind != "trainer" and (
                "opponent reveal" in text and "hand" in text
                or "look at your opponent's hand" in text):
            inject(P2, "hand", lambda d: isinstance(d, PokemonCardDef)
                   and _def_attr(d, AttrID.STAGE) == PokemonStage.BASIC.value)
            inject(P2, "hand", lambda d: type(d) is ItemCardDef)
            inject(P2, "hand", lambda d: isinstance(d, SupporterCardDef))
            inject(P2, "hand", lambda d: isinstance(d, EnergyCardDef))

        source = entities.get("p1_active")
        p1_active = area(P1, "activePokemonArea")
        p1_bench = area(P1, "bench")
        p1_hand = area(P1, "hand")
        if isinstance(source, PokemonEntity) and (
                "this pokémon is in your hand" in text
                or "put unown from your hand" in text
                or "attach this card from your hand" in text):
            replacement = next((p for p in list(p1_bench.children)
                                if isinstance(p, PokemonEntity)), None)
            if replacement is not None:
                board.move_card(replacement.entity_id, p1_active.entity_id)
            board.move_card(source.entity_id, p1_hand.entity_id)
        elif isinstance(source, PokemonEntity) and any(phrase in text for phrase in (
                "this pokémon is on your bench", "this pokémon is on the bench",
                "moves from the active spot to the bench",
                "play this pokémon from your hand onto your bench",
                "put torkoal from your hand onto your bench",
                "if machamp is on your bench")):
            replacement = next((p for p in list(p1_bench.children)
                                if isinstance(p, PokemonEntity)), None)
            if replacement is not None:
                board.move_card(replacement.entity_id, p1_active.entity_id)
            board.move_card(source.entity_id, p1_bench.entity_id)
        discard_trigger = (
            "discarded with the effect of" in text
            or "discard this pokémon with the effect of" in text
        )
        if isinstance(source, PokemonEntity) and discard_trigger:
            discard = area(P1, "discard")
            if discard is not None:
                board.move_card(source.entity_id, discard.entity_id)

        # Named cards required in hand/deck by an Ability.
        for wanted, zone in (
                ("therapeutic energy", "hand"),
                ("vikavolt", "bench"),
                ("jumpluff", "deck"),
                ("shedinja", "discard"),
                ("palafin ex", "deck"),
                ("wishiwashi-gx", "hand")):
            if wanted in text:
                inject(P1, zone, lambda d, wanted=wanted:
                       definition_name(d) == wanted)

        # Self-attachment powers such as Buzzap Thunder need a *different*
        # Pokemon of the printed type.  The ordinary smoke board deliberately
        # uses a neutral filler, so build the public target explicitly.
        if "lightning pokémon" in text:
            inject(P1, "bench", lambda d: isinstance(d, PokemonCardDef)
                   and _def_attr(d, AttrID.STAGE) == PokemonStage.BASIC.value
                   and PokemonTypes.LIGHTNING.value in (
                       json.loads(_def_attr(d, AttrID.POKEMON_TYPES, "[]"))
                       if isinstance(_def_attr(d, AttrID.POKEMON_TYPES, "[]"), str)
                       else (_def_attr(d, AttrID.POKEMON_TYPES, []) or [])
                   ))

        if isinstance(source, PokemonEntity) and discard_trigger:
            cause = "roxie" if "roxie" in text else \
                "jessie & james" if "jessie & james" in text else ""
            if cause:
                source._smoke_discarded_by = inject(
                    P1, "hand", lambda d, cause=cause:
                    definition_name(d) == cause
                )

        if "opponent has any stage 2 pokémon in play" in text:
            inject(P2, "bench", lambda d: isinstance(d, PokemonCardDef)
                   and _def_attr(d, AttrID.STAGE) == PokemonStage.STAGE2.value)

        if "opponent's pokémon-gx and pokémon-ex" in text:
            inject(P2, "bench", lambda d: isinstance(d, PokemonCardDef)
                   and any(subtype in (getattr(d, "subtypes", []) or [])
                           for subtype in ("GX", "EX")))

        if "mega evolution pokémon" in text:
            inject(P1, "bench", lambda d: isinstance(d, PokemonCardDef)
                   and any(subtype in (getattr(d, "subtypes", []) or [])
                           for subtype in ("MEGA", "SV_Mega")))
        if "tera pokémon" in text:
            tera = inject(P1, "bench", lambda d: isinstance(d, PokemonCardDef)
                          and any("tera" in str(subtype).casefold()
                                  for subtype in (getattr(d, "subtypes", []) or [])))
            if isinstance(tera, PokemonEntity):
                maximum = effective_max_hp(board, tera)
                tera.set_attribute(AttrID.HP, max(10, maximum - 30))

        # Make an evolved target by placing a harmless evolution over an
        # existing opposing Bench Pokemon.  Evolution effects care about the
        # public Stage/stack, not the printed evolution chain of the fixture.
        if "evolved pokémon" in text or "stage 1 or stage 2 evolved" in text:
            bench = area(P2, "bench")
            base = next((p for p in list(bench.children)
                         if isinstance(p, PokemonEntity)), None) if bench else None
            evolution = inject(P2, "bench", lambda d: isinstance(d, PokemonCardDef)
                               and _def_attr(d, AttrID.STAGE) in (
                                   PokemonStage.STAGE1.value, PokemonStage.STAGE2.value)
                               and not getattr(d, "passive", None))
            if base is not None and evolution is not None:
                board.attach_card(base.entity_id, evolution.entity_id)

        # Public-zone card types used as costs/targets.
        if "supporter card from your discard pile" in text \
                or "supporter card from your hand" in text:
            inject(P1, "discard" if "discard pile" in text else "hand",
                   lambda d: isinstance(d, SupporterCardDef))
        if "supporter card from your opponent's discard pile" in text:
            inject(P2, "discard", lambda d: isinstance(d, SupporterCardDef))
        if "item card from your discard pile" in text:
            inject(P1, "discard", lambda d: type(d) is ItemCardDef)
        if "trainer card" in text and "discard pile" in text:
            inject(P1, "discard", lambda d: isinstance(
                d, (ItemCardDef, SupporterCardDef, StadiumCardDef,
                    PokemonToolCardDef)
            ))
        if "a card from your discard pile" in text:
            inject(P1, "discard", lambda d: isinstance(d, PokemonCardDef))
        if "stadium card in play" in text:
            stadium = inject(P1, "hand", lambda d: isinstance(d, StadiumCardDef))
            slot = board.find_global_area("activeStadium")
            if stadium is not None and slot is not None:
                board.move_card(stadium.entity_id, slot.entity_id)

        if "basic pokémon from your opponent's discard pile" in text:
            inject(P2, "discard", lambda d: isinstance(d, PokemonCardDef)
                   and _def_attr(d, AttrID.STAGE) == PokemonStage.BASIC.value)
        if "basic pokémon from your discard pile" in text:
            inject(P1, "discard", lambda d: isinstance(d, PokemonCardDef)
                   and _def_attr(d, AttrID.STAGE) == PokemonStage.BASIC.value
                   and int(_def_attr(d, AttrID.HP, 999) or 999) <= 70)
        if "basic pokémon with 70 hp or less from your discard pile" in text:
            inject(P1, "discard", lambda d: isinstance(d, PokemonCardDef)
                   and _def_attr(d, AttrID.STAGE) == PokemonStage.BASIC.value
                   and int(_def_attr(d, AttrID.HP, 999) or 999) <= 70)
        if "each player puts a basic pokémon from their discard pile" in text:
            for pid in (P1, P2):
                inject(pid, "discard", lambda d: isinstance(d, PokemonCardDef)
                       and _def_attr(d, AttrID.STAGE) == PokemonStage.BASIC.value)

        # Put a compatible Evolution into the hand for activated evolution
        # powers. Quick-Ripening Herb deliberately skips Stage 1.
        if isinstance(source, PokemonEntity) and (
                "in your hand that evolves from" in text
                or "card in your hand that evolves from this pokémon" in text):
            logic = source.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
            named = re.search(
                r"in your hand that evolves from ([a-z0-9 .'-]+?)"
                r"(?:,| you may|\.)", text,
            )
            if named and named.group(1) not in ("this pokémon", "that pokémon"):
                wanted = named.group(1).strip().casefold()
                base = next((
                    definition for definition in CARD_DEFS_BY_GUID.values()
                    if definition_name(definition) == wanted
                    and _def_attr(definition, AttrID.EVOLUTION_LOGIC_NAME)
                ), None)
                if base is not None:
                    logic = _def_attr(base, AttrID.EVOLUTION_LOGIC_NAME)
            inject(P1, "hand", lambda d: isinstance(d, PokemonCardDef)
                   and evolves_from(d.guid, logic))
        if isinstance(source, PokemonEntity) \
                and "card that evolves from 1 of your pokémon" in text:
            evolution = next((
                definition for definition in CARD_DEFS_BY_GUID.values()
                if isinstance(definition, PokemonCardDef)
                and _def_attr(definition, AttrID.STAGE) == PokemonStage.STAGE1.value
                and evolves_from_chain(definition.guid)
            ), None)
            if evolution is not None:
                base_logic = evolves_from_chain(evolution.guid)[0]
                inject(P1, "bench", lambda d: isinstance(d, PokemonCardDef)
                       and _def_attr(d, AttrID.STAGE) == PokemonStage.BASIC.value
                       and _def_attr(d, AttrID.EVOLUTION_LOGIC_NAME) == base_logic)
                inject(P1, "deck", lambda d, guid=evolution.guid: d.guid == guid)
        if "search your deck for a spewpa and a vivillon" in text:
            for wanted in ("spewpa", "vivillon"):
                inject(P1, "deck", lambda d, wanted=wanted:
                       definition_name(d) == wanted)
        if "stage 2 card in your hand that evolves from" in text:
            stage2 = next((
                definition for definition in CARD_DEFS_BY_GUID.values()
                if isinstance(definition, PokemonCardDef)
                and _def_attr(definition, AttrID.STAGE) == PokemonStage.STAGE2.value
                and len(evolves_from_chain(definition.guid)) >= 2
            ), None)
            if stage2 is not None:
                base_logic = evolves_from_chain(stage2.guid)[-1]
                basic = inject(P1, "bench", lambda d: isinstance(d, PokemonCardDef)
                               and _def_attr(d, AttrID.STAGE) == PokemonStage.BASIC.value
                               and _def_attr(d, AttrID.EVOLUTION_LOGIC_NAME)
                                   == base_logic)
                if basic is not None:
                    # The headless chooser takes the first legal target.
                    # Put the compatible Basic first so this is deterministic.
                    board.move_card(basic.entity_id, p1_bench.entity_id, 0)
                inject(P1, "hand", lambda d, guid=stage2.guid: d.guid == guid)

        p2_target = entities.get("p2_active")

        # Conditional attacks must see the printed target type.  Replace the
        # neutral filler with a real catalog card rather than merely changing
        # one attribute: subtype checks (Ultra Beast/EX/GX) consult the card
        # definition and would otherwise remain false.
        required_target_type = next((ptype for word, ptype in type_words.items()
                                     if f"active pokémon is a {word} pokémon" in text),
                                    None)
        if required_target_type is not None:
            p2_target = replace_active(
                P2, lambda d, ptype=required_target_type:
                _def_attr(d, AttrID.STAGE) == PokemonStage.BASIC.value
                and pokemon_of_type(d, ptype)
            ) or p2_target
        if "defending pokémon is a darkness or fairy pokémon" in text:
            p2_target = replace_active(
                P2, lambda d: isinstance(d, PokemonCardDef)
                and _def_attr(d, AttrID.STAGE) == PokemonStage.BASIC.value
                and pokemon_of_type(d, PokemonTypes.DARKNESS)
            ) or p2_target
        if "defending pokémon is a pokémon-ex" in text:
            p2_target = replace_active(
                P2, lambda d: isinstance(d, PokemonCardDef)
                and "EX" in set(getattr(d, "subtypes", ()) or ())
            ) or p2_target
        if "active pokémon is an ultra beast" in text:
            p2_target = replace_active(
                P2, lambda d: isinstance(d, PokemonCardDef)
                and _def_attr(d, AttrID.STAGE) == PokemonStage.BASIC.value
                and "Ultra Beast" in (getattr(d, "subtypes", ()) or ())
            ) or p2_target

        # Devolution text usually targets the Active, while a few families
        # target any Pokemon.  Build a genuine two-card stack in the requested
        # zone so the effect has a legal highest stage to remove.
        if isinstance(p2_target, PokemonEntity) and (
                "active pokémon is an evolved pokémon" in text):
            evolution = inject(P2, "hand", lambda d: isinstance(d, PokemonCardDef)
                               and _def_attr(d, AttrID.STAGE) in (
                                   PokemonStage.STAGE1.value,
                                   PokemonStage.STAGE2.value,
                               ))
            if evolution is not None:
                board.attach_card(p2_target.entity_id, evolution.entity_id)
                board.move_card(evolution.entity_id, area(P2, "activePokemonArea").entity_id)
                p2_target = evolution
                entities["p2_active"] = evolution
        if isinstance(p2_target, PokemonEntity) \
                and "defending pokémon is an evolution pokémon" in text:
            evolution = inject(P2, "hand", lambda d: isinstance(d, PokemonCardDef)
                               and _def_attr(d, AttrID.STAGE) in (
                                   PokemonStage.STAGE1.value,
                                   PokemonStage.STAGE2.value,
                               ))
            if evolution is not None:
                board.attach_card(p2_target.entity_id, evolution.entity_id)
                board.move_card(
                    evolution.entity_id, area(P2, "activePokemonArea").entity_id,
                )
                p2_target = evolution
                entities["p2_active"] = evolution

        if isinstance(p2_target, PokemonEntity) and (
                "affected by a special condition" in text or "is asleep" in text
                or "is confused" in text):
            p2_target.set_attribute(
                AttrID.SPECIAL_CONDITIONS,
                [CLIENT_SPECIAL_CONDITION_NAMES[
                    SpecialConditions.CONFUSED if "is confused" in text
                    else SpecialConditions.ASLEEP
                ]],
            )
        if isinstance(p2_target, PokemonEntity):
            exact = re.search(r"has exactly (\d+) damage counters", text)
            at_least = re.search(r"has (\d+) or more damage counters", text)
            count = int((exact or at_least).group(1)) if exact or at_least else None
            if count is not None:
                maximum = max(effective_max_hp(board, p2_target), count * 10 + 10)
                p2_target.attribute_originals[AttrID.HP.value] = maximum
                p2_target.set_attribute(
                    AttrID.HP,
                    maximum - count * 10,
                )
            if "50 hp or less remaining" in text:
                p2_target.set_attribute(AttrID.HP, 40)
            if "knocked out by damage from this attack" in text:
                p2_target.set_attribute(AttrID.HP, 10)

        if isinstance(source, PokemonEntity) and "heal" in text:
            source.set_attribute(
                AttrID.HP, max(10, int(source.get_attribute(AttrID.HP) or 100) - 30)
            )

        # Energy-moving/discarding effects need an actual attached card. Use
        # the rig's canonical basic Energy so art/type/entity behavior is real.
        if any(phrase in text for phrase in (
                "energy from your other pokémon", "energy from 1 of your pokémon",
                "all energy attached to 1 of your pokémon",
                "energy from your pokémon to your other pokémon",
                "energy from your benched pokémon to this pokémon",
                "move any amount of fire energy", "move any amount of metal energy",
                "move any number of fire energy", "move any number of metal energy")):
            holder = next((p for p in board.pokemon_in_play(P1)
                           if p is not source), source)
            required = next((ptype for word, ptype in type_words.items()
                             if f"{word} energy" in text), None)
            energy = inject(
                P1, "hand",
                (lambda d, required=required: energy_of_type(d, required))
                if required is not None else
                (lambda d: isinstance(d, EnergyCardDef)
                 and not bool(_def_attr(d, AttrID.IS_SPECIAL_ENERGY, False))),
            )
            if energy is not None and holder is not None:
                board.attach_card(energy.entity_id, holder.entity_id)
        if kind == "ability" and isinstance(source, PokemonEntity) and any(
                phrase in text for phrase in (
                    "was on the bench and became your active pokémon this turn",
                    "moves from your bench to become your active pokémon",
                )):
            active_area = area(P1, "activePokemonArea")
            current_active = board.active_pokemon(P1)
            bench_area = area(P1, "bench")
            if current_active is not None and current_active is not source:
                board.move_card(current_active.entity_id, bench_area.entity_id)
            board.move_card(source.entity_id, active_area.entity_id)
            state = getattr(board, "turn_state", None)
            if state is not None:
                state.became_active_turn[source.entity_id] = state.turn_number
        if "move all fighting energy attached to your active pokémon" in text:
            holder = board.active_pokemon(P1)
            energy = inject(P1, "hand", lambda d:
                            energy_of_type(d, PokemonTypes.FIGHTING))
            if energy is not None and holder is not None:
                board.attach_card(energy.entity_id, holder.entity_id)
        if "move any number of basic energy attached to your pokémon" in text:
            holder = next((p for p in board.pokemon_in_play(P1)
                           if p is not source), None)
            energy = inject(P1, "hand", lambda d: isinstance(d, EnergyCardDef)
                            and not bool(_def_attr(
                                d, AttrID.IS_SPECIAL_ENERGY, False)))
            if energy is not None and holder is not None:
                board.attach_card(energy.entity_id, holder.entity_id)
        typed_bench_move = re.search(
            r"move an? (grass|fire|water|lightning|psychic|fighting|darkness|metal) "
            r"energy from 1 of your benched pokémon", text,
        )
        if typed_bench_move:
            ptype = type_words[typed_bench_move.group(1)]
            holder = next((p for p in board.pokemon_in_play(P1)
                           if p is not source), None)
            energy = inject(P1, "hand", lambda d, ptype=ptype:
                            energy_of_type(d, ptype))
            if holder is not None and energy is not None:
                board.attach_card(energy.entity_id, holder.entity_id)
        if ("energy from your opponent's active pokémon" in text
                or "energy attached to your opponent's active" in text) \
                or "energy from 1 of your opponent's pokémon" in text:
            energy = inject(P2, "hand", lambda d: isinstance(d, EnergyCardDef))
            if energy is not None and p2_target is not None:
                board.attach_card(energy.entity_id, p2_target.entity_id)

        # Exact typed Energy payments.  The base smoke rig only pays the
        # attack's printed cost, which is insufficient for optional/additional
        # discards and for effects paid from a different zone.
        if isinstance(source, PokemonEntity):
            for match in re.finditer(
                    r"discard (?:up to )?(all|\d+|an|a|any number of)? ?"
                    r"(?:basic )?(grass|fire|water|lightning|psychic|fighting|"
                    r"darkness|metal)? ?energy(?: cards?)? "
                    r"(?:attached to|from) (?:this pokémon|[a-z0-9 &'’.-]+)",
                    text):
                raw_count, word = match.groups()
                count = 2 if raw_count in (None, "all", "any number of") \
                    else 1 if raw_count in ("a", "an") else int(raw_count)
                ptype = type_words.get(word)
                predicate = (lambda d, ptype=ptype: energy_of_type(d, ptype)) \
                    if ptype is not None else lambda d: isinstance(d, EnergyCardDef)
                for energy in inject_many(P1, "hand", predicate, count):
                    board.attach_card(energy.entity_id, source.entity_id)

        # Payments from any of the player's Pokemon need energy away from the
        # attacker as well.  Spread the requested cards across Bench holders.
        board_payment = re.search(
            r"discard (?:up to )?(all|\d+|any amount of|any number of)? ?"
            r"(?:basic )?(grass|fire|water|lightning|psychic|fighting|darkness|metal)?"
            r" ?energy from your (?:benched )?pokémon", text,
        )
        if board_payment:
            raw_count, word = board_payment.groups()
            count = 2 if raw_count in (None, "all", "any amount of", "any number of") \
                else int(raw_count)
            ptype = type_words.get(word)
            predicate = (lambda d, ptype=ptype: energy_of_type(d, ptype)) \
                if ptype is not None else lambda d: isinstance(d, EnergyCardDef)
            holders = [pokemon for pokemon in board.pokemon_in_play(P1)
                       if pokemon is not source] or ([source] if source else [])
            for index, energy in enumerate(inject_many(P1, "hand", predicate, count)):
                if holders:
                    board.attach_card(energy.entity_id,
                                      holders[index % len(holders)].entity_id)

        # Typed disruption of the opposing Active (Firefighting/Grass Fire).
        opponent_payment = re.search(
            r"discard (?:an?|\d+|all)? ?(grass|fire|water|lightning|psychic|"
            r"fighting|darkness|metal)? ?energy from your opponent's active",
            text,
        )
        if opponent_payment and isinstance(p2_target, PokemonEntity):
            ptype = type_words.get(opponent_payment.group(1))
            predicate = (lambda d, ptype=ptype: energy_of_type(d, ptype)) \
                if ptype is not None else lambda d: isinstance(d, EnergyCardDef)
            energy = inject(P2, "hand", predicate)
            if energy is not None:
                board.attach_card(energy.entity_id, p2_target.entity_id)

        if any(phrase in text for phrase in (
                "special energy attached", "special energy from",
                "discard a special energy")) \
                and isinstance(p2_target, PokemonEntity):
            special = inject(P2, "hand", lambda d: isinstance(d, EnergyCardDef)
                             and bool(_def_attr(d, AttrID.IS_SPECIAL_ENERGY, False)))
            if special is not None:
                board.attach_card(special.entity_id, p2_target.entity_id)

        # Poisonous Nest deliberately excludes Grass Pokemon.  Make the
        # opponent's Active a legal target without relying on which vanilla
        # filler happened to sort first in a growing catalog.
        if "except for grass pokémon" in text \
                and isinstance(p2_target, PokemonEntity):
            p2_target.set_attribute(
                AttrID.POKEMON_TYPES, [PokemonTypes.FIRE.value]
            )

        if "discard a special energy from this pokémon" in text \
                and isinstance(source, PokemonEntity):
            special = inject(P1, "hand", lambda d: isinstance(d, EnergyCardDef)
                             and bool(_def_attr(d, AttrID.IS_SPECIAL_ENERGY, False)))
            if special is not None:
                board.attach_card(special.entity_id, source.entity_id)
        if "pokémon tool" in text:
            for pid in (P1, P2):
                tool = inject(pid, "hand", lambda d: isinstance(d, PokemonToolCardDef))
                pokemon = board.pokemon_in_play(pid)
                if tool is not None and pokemon:
                    holder = source if pid == P1 and "this pokémon" in text \
                        and source in pokemon else pokemon[-1]
                    board.attach_card(tool.entity_id, holder.entity_id)

        if "number of heads from your discard pile into your hand" in text:
            inject_many(P1, "discard", lambda d: isinstance(d, PokemonCardDef), 3)
        if "when you attach a grass energy card from your hand to it" in text \
                and isinstance(source, PokemonEntity):
            energy = inject(P1, "hand", lambda d:
                            energy_of_type(d, PokemonTypes.GRASS))
            if energy is not None:
                board.attach_card(energy.entity_id, source.entity_id)
        if "all electropower cards from your discard pile" in text:
            inject_many(P1, "discard", lambda d:
                        definition_name(d) == "electropower", 2)
        if "reveal cards from the top of your deck until you reveal an item card" in text:
            item_card = inject(P1, "deck", lambda d: type(d) is ItemCardDef)
            deck = area(P1, "deck")
            if item_card is not None and deck is not None:
                board.move_card(item_card.entity_id, deck.entity_id, len(deck.children))
                # Leave one non-Item above it so the "other cards" shuffle is
                # exercised as well as the successful find.
                inject(P1, "deck", lambda d: isinstance(d, PokemonCardDef))
        if "top 5 cards of your deck" in text and "trainer card" in text:
            trainer = inject(P1, "deck", lambda d: type(d) is ItemCardDef)
            deck = area(P1, "deck")
            if trainer is not None and deck is not None:
                board.move_card(trainer.entity_id, deck.entity_id, len(deck.children))
        if "if you played lillie's full force from your hand during this turn" in text:
            rig.session.turn_state.trainers_played.append(
                ("semantic-lillie", "Lillie's Full Force", TrainerType.SUPPORTER.value)
            )

        # Hand-discard attacks often require more cards than the generic rig
        # carries.  Supply the exact public cost, including named-card and
        # retreat-cost families, so the mandatory branch is tested.
        hand_energy_cost = re.search(
            r"discard (\d+) (?:basic )?(grass|fire|water|lightning|psychic|"
            r"fighting|darkness|metal)? ?energy cards? from your hand", text,
        )
        if hand_energy_cost:
            count, word = int(hand_energy_cost.group(1)), hand_energy_cost.group(2)
            ptype = type_words.get(word)
            predicate = (lambda d, ptype=ptype: energy_of_type(d, ptype)) \
                if ptype is not None else lambda d: isinstance(d, EnergyCardDef)
            inject_many(P1, "hand", predicate, count)
        if "supporter cards from your hand" in text:
            inject_many(P1, "hand", lambda d: isinstance(d, SupporterCardDef), 3)
        if 'supporter cards that have "team rocket" in their name from your hand' in text:
            inject_many(P1, "hand", lambda d: isinstance(d, SupporterCardDef)
                        and "team rocket" in definition_name(d), 2)
        for wanted, count in (
                ("exeggcute", 3), ("honedge", 1), ("doublade", 1),
                ("aegislash", 1), ("moomoo milk", 2)):
            if wanted in text:
                inject_many(P1, "hand", lambda d, wanted=wanted:
                            definition_name(d) == wanted, count)
        if "pokémon with a retreat cost of exactly 4 from your hand" in text:
            inject_many(P1, "hand", lambda d: isinstance(d, PokemonCardDef)
                        and int(_def_attr(d, AttrID.RETREAT_COST, -1) or 0) == 4, 2)

        # The hand-disruption/copy families resolve against public revealed
        # candidates.  Keep at least six cards for size-based effects.
        if "opponent reveals" in text or "opponent reveal" in text \
                or "they reveal their hand" in text:
            opponent_hand = area(P2, "hand")
            while opponent_hand is not None and len(opponent_hand.children) < 6:
                if inject(P2, "hand", lambda d: isinstance(d, PokemonCardDef)
                          and _def_attr(d, AttrID.STAGE) == PokemonStage.BASIC.value) is None:
                    break

        # Stadium-dependent attacks should not rely on a Trainer-only setup.
        if "stadium" in text and "in play" in text:
            stadium_slot = board.find_global_area("activeStadium")
            if stadium_slot is not None and not stadium_slot.children:
                stadium = inject(P1, "hand", lambda d: isinstance(d, StadiumCardDef))
                if stadium is not None:
                    board.move_card(stadium.entity_id, stadium_slot.entity_id)

        # Recall needs an actual previous Evolution card carrying an attack.
        if isinstance(source, PokemonEntity) and "previous evolutions" in text:
            previous = inject(P1, "hand", lambda d: isinstance(d, PokemonCardDef)
                              and any(isinstance(a, Attack) for a in (
                                  getattr(d, "abilities", ()) or ())))
            if previous is not None:
                board.attach_card(previous.entity_id, source.entity_id)

        # Time Distortion targets the user's own evolved Bench rather than the
        # opponent fixture constructed above.
        if "devolve any number of your benched pokémon" in text:
            base = next((p for p in board.pokemon_in_play(P1)
                         if p is not source), None)
            evolution = inject(P1, "hand", lambda d: isinstance(d, PokemonCardDef)
                               and _def_attr(d, AttrID.STAGE) in (
                                   PokemonStage.STAGE1.value,
                                   PokemonStage.STAGE2.value,
                               ))
            if base is not None and evolution is not None:
                board.attach_card(base.entity_id, evolution.entity_id)
                board.move_card(evolution.entity_id, area(P1, "bench").entity_id)

        if "evolve from unidentified fossil from your discard pile" in text:
            inject(P1, "discard", lambda d: isinstance(d, PokemonCardDef)
                   and "unidentifiedfossil" in str(
                       _def_attr(d, AttrID.EVOLUTION_LOGIC_FROM, "") or ""
                   ).replace(" ", "").casefold())

        # Previous-turn copy/retaliation families need a concrete attack and
        # amount in the history ledger.
        if "used an attack" in text and "last turn" in text:
            opposing = entities.get("p2_active")
            attacks = [a for a in getattr(
                CARD_DEFS_BY_GUID.get(getattr(opposing, "archetype_id", "")),
                "abilities", ()) if isinstance(a, Attack)]
            if attacks:
                attack = attacks[0]
                rig.session.turn_state.attacks_used_last_turn = [(
                    opposing.entity_id, opposing.archetype_id, attack.title
                )]
        if "used a gx attack during their last turn" in text:
            gx_definition = next((
                definition for definition in CARD_DEFS_BY_GUID.values()
                if any(isinstance(attack, Attack) and getattr(attack, "gx", False)
                       for attack in (getattr(definition, "abilities", ()) or ()))
            ), None)
            if gx_definition is not None:
                gx_attack = next(attack for attack in gx_definition.abilities
                                 if isinstance(attack, Attack)
                                 and getattr(attack, "gx", False))
                rig.session.turn_state.attacks_used_last_turn = [(
                    getattr(p2_target, "entity_id", "semantic-gx"),
                    gx_definition.guid, gx_attack.title,
                )]
        if "was damaged by an attack during your opponent's last turn" in text \
                and isinstance(source, PokemonEntity):
            rig.session.turn_state.damage_taken_last_turn[source.entity_id] = 50

        if "exactly 1 prize card" in text or "only 1 prize card" in text:
            prizes = area(P1, "prizePile")
            deck = area(P1, "deck")
            while prizes is not None and len(prizes.children) > 1:
                board.move_card(prizes.children[-1].entity_id, deck.entity_id)
        if "more prize cards remaining than your opponent" in text:
            opposing = area(P2, "prizePile")
            deck = area(P2, "deck")
            if opposing is not None and deck is not None and opposing.children:
                board.move_card(opposing.children[-1].entity_id, deck.entity_id)
        if "number of prize cards your opponent has taken" in text:
            opposing = area(P2, "prizePile")
            hand = area(P2, "hand")
            if opposing is not None and hand is not None and opposing.children:
                board.move_card(opposing.children[-1].entity_id, hand.entity_id)

        if "35 or more cards in your hand" in text:
            hand = area(P1, "hand")
            deck = area(P1, "deck")
            while hand is not None and deck is not None and len(hand.children) < 35 \
                    and deck.children:
                board.move_card(deck.children[-1].entity_id, hand.entity_id)
        if "66 or more damage counters on your benched pokémon" in text:
            bench = board.find_player_area(P1, "bench")
            while bench is not None and len(bench.children) < 5:
                inject(P1, "bench", lambda d: isinstance(d, PokemonCardDef)
                       and _def_attr(d, AttrID.STAGE) == PokemonStage.BASIC.value)
            for pokemon in list(bench.children if bench is not None else []):
                if isinstance(pokemon, PokemonEntity):
                    # Alternate-win smoke state: 14 counters on each of five
                    # Benched Pokemon.  originalValue is the authoritative max
                    # HP read by effective_max_hp.
                    pokemon.attribute_originals[AttrID.HP.value] = 150
                    pokemon.set_attribute(AttrID.HP, 10)
        if "choose 3 of your benched pokémon" in text:
            inject(P1, "bench", lambda d: isinstance(d, PokemonCardDef)
                   and _def_attr(d, AttrID.STAGE) == PokemonStage.BASIC.value)

        if "special energy card from your hand" in text:
            inject(P1, "hand", lambda d: isinstance(d, EnergyCardDef)
                   and bool(_def_attr(d, AttrID.IS_SPECIAL_ENERGY, False)))
        if "12 or more supporter cards in the lost zone" in text:
            for _ in range(12):
                if inject(P2, "lostZone", lambda d: isinstance(d, SupporterCardDef)) is None:
                    break
        if "at least 3 more prize cards remaining" in text:
            prizes = area(P2, "prizePile")
            deck = area(P2, "deck")
            while prizes is not None and len(prizes.children) > 3:
                board.move_card(prizes.children[-1].entity_id, deck.entity_id)

        # Wide-board damage families need matching targets on both sides.
        if "each pokémon that has an ability" in text:
            for pid in (P1, P2):
                inject(pid, "bench", lambda d: isinstance(d, PokemonCardDef)
                       and any(isinstance(a, Ability) and not isinstance(a, Attack)
                               for a in (getattr(d, "abilities", ()) or ())))
        if "each pokémon-gx and pokémon-ex" in text:
            for pid in (P1, P2):
                inject(pid, "bench", lambda d: isinstance(d, PokemonCardDef)
                       and any(subtype in (getattr(d, "subtypes", ()) or ())
                               for subtype in ("GX", "EX")))
        if text.startswith("choose grass fire water lightning psychic fighting"):
            # The deterministic chooser selects Grass first.
            if isinstance(p2_target, PokemonEntity):
                p2_target.set_attribute(AttrID.POKEMON_TYPES,
                                        [PokemonTypes.GRASS.value])

        if "choose 3 of your opponent's benched pokémon" in text:
            while len(board.pokemon_in_play(P2)) - 1 < 4:
                if inject(P2, "bench", lambda d: isinstance(d, PokemonCardDef)
                          and _def_attr(d, AttrID.STAGE) == PokemonStage.BASIC.value) is None:
                    break

        # Sudden Shout explicitly checks both the stack and this-turn entry
        # stamp.  Put a real Loudred under the attacking Exploud.
        if isinstance(source, PokemonEntity) \
                and "didn't evolve from loudred during this turn" in text:
            loudred = inject(P1, "hand", lambda d: definition_name(d) == "loudred")
            if loudred is not None:
                board.attach_card(loudred.entity_id, source.entity_id)
                rig.session.turn_state.entered_play_turn[source.entity_id] = \
                    rig.session.turn_state.turn_number

        if "only if you go second" in text and "first turn" in text:
            rig.session.turn_state.turn_number = 2
            rig.session.first_player_id = P2

        # Named cards explicitly required by an effect.
        for wanted in re.findall(
                r"(?:search your deck for|switch this pokémon with an?|"
                r"put a) ([a-z0-9' -]+?)(?:,| in your hand| and| onto| from)", text):
            wanted = wanted.strip().casefold()
            if not wanted or wanted in ("card", "pokémon", "basic pokémon"):
                continue
            inject(P1, "hand", lambda d, wanted=wanted:
                   definition_name(d) == wanted)

    return setup


async def audit(args):
    card_loader.load_all()
    filler = pick_filler_basic()
    item = pick_filler_item()
    energies = basic_energy_guids()
    inventory = _runtime_shared_ability_groups() \
        if args.kind == "ability" else grouped(scan())
    families = [
        (key, copies) for key, copies in inventory.items()
        if key[0] == args.kind
    ]
    if args.set_pattern:
        set_matcher = re.compile(args.set_pattern, re.IGNORECASE)
        families = [
            (key, matching)
            for key, copies in families
            if (matching := [
                copy for copy in copies
                if set_matcher.fullmatch(str(copy.get("set", "")))
            ])
        ]
    if args.match:
        matcher = re.compile(args.match, re.IGNORECASE)
        families = [
            (key, copies) for key, copies in families
            if matcher.search(" ".join((key[1], key[2], *(
                copy["card"] for copy in copies
            ))))
        ]
    families.sort(key=lambda row: (-len(row[1]), row[0][1], row[0][2]))
    rows = []
    with _Trace():
        for index, ((kind, title, text), copies) in enumerate(families, 1):
            representative = copies[0]
            definition = _definition(representative)
            plan = _runner(definition, kind, title, text) if definition else None
            if plan is None:
                rows.append({
                    "kind": kind, "title": title, "text": text,
                    "status": "AUDIT_ERROR", "events": [],
                    "printings": copies,
                    "detail": "representative definition/behavior not found",
                })
                continue
            plan_kind, label, runner_key, scripted = plan
            if kind == "ability" and runner_key == "passive":
                rows.append({
                    "kind": kind, "title": title, "text": text,
                    "status": "PASSIVE_CLASSIFIED", "events": {},
                    "printings": copies,
                    "detail": "continuous text is registered as a Passive",
                })
                continue
            events = []
            results = []
            flip_variants = (True, False) if (
                "flip " in text or "if heads" in text or "if tails" in text
            ) else (None,)
            for forced_coin in flip_variants:
                variant_events = []
                token = _EVENTS.set(variant_events)
                try:
                    result = await run_one(
                        Path(representative["path"]).stem,
                        definition, plan_kind, label, runner_key, filler, energies,
                        scripted, args.timeout, item,
                        scenario_setup=_semantic_scenario(
                            kind, text, forced_coin=forced_coin
                        ),
                    )
                finally:
                    _EVENTS.reset(token)
                events.extend(variant_events)
                results.append(result)
            # A printed continuous rule lives on the card definition rather
            # than calling an EffectContext primitive during activation.  It
            # is still semantic evidence (notably for Pokemon Dolls whose
            # activated self-discard text shares a card with a retreat lock).
            if getattr(definition, "passive", None) is not None:
                events.append("card_passive")
            result = next(
                (candidate for candidate in results if candidate.status != PASS),
                results[0],
            )
            # Textless, zero-damage attacks are legitimate do-nothing attacks.
            allowed_empty = (
                kind == "attack" and not text
                and isinstance(runner_key, Attack)
                and not (getattr(runner_key, "damage", 0) or 0)
            )
            if result.status != PASS:
                status = result.status
            elif events or allowed_empty:
                status = "OBSERVED"
            else:
                status = "NO_EFFECT_OBSERVED"
            missing_expected = _missing_expected_events(kind, text, events) \
                if result.status == PASS else []
            if status == "OBSERVED" and missing_expected:
                status = "PARTIAL_SUSPECT"
            rows.append({
                "kind": kind, "title": title, "text": text,
                "status": status,
                "events": dict(Counter(events)),
                "missing_expected": missing_expected,
                "printings": copies,
                "detail": result.detail,
            })
            if args.progress and index % 25 == 0:
                print(f"audited {index}/{len(families)}", flush=True)
    return rows


def main():
    # Windows still defaults many PowerShell hosts to a legacy code page.  Card
    # names legitimately contain characters such as β, so make the diagnostic
    # output resilient without changing the UTF-8 JSON report.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(errors="backslashreplace")
    parser = argparse.ArgumentParser()
    parser.add_argument("--kind", required=True,
                        choices=("trainer", "ability", "attack"))
    parser.add_argument("--json")
    parser.add_argument("--only-problems", action="store_true")
    parser.add_argument("--progress", action="store_true")
    parser.add_argument(
        "--match",
        help="Only audit families whose title, text, or printing name matches this regex",
    )
    parser.add_argument(
        "--set-pattern",
        help="Only audit printings whose set code fully matches this regex",
    )
    parser.add_argument("--timeout", type=float, default=5.0)
    args = parser.parse_args()
    rows = asyncio.run(audit(args))
    counts = Counter(row["status"] for row in rows)
    print(f"{args.kind}: {len(rows)} exact-text families")
    print("  " + "  ".join(f"{key}={value}" for key, value in sorted(counts.items())))
    if args.json:
        Path(args.json).write_text(
            json.dumps(rows, indent=2, ensure_ascii=False), encoding="utf-8"
        )
    selected = [row for row in rows if row["status"] != "OBSERVED"] \
        if args.only_problems else rows
    for row in selected:
        print(f"[{row['status']}] {len(row['printings'])}x {row['title']}")
        if row.get("missing_expected"):
            print(f"  missing: {', '.join(row['missing_expected'])}")
        if row["detail"]:
            print(f"  {row['detail']}")


if __name__ == "__main__":
    main()
