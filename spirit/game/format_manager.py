import json
import logging
import os
import re
import time
import unicodedata
from typing import Any, Dict, List, Optional, Set, Tuple

from spirit.game.attributes import AttrID, CardType, DeckFormat
from spirit.game.models.formats import GameFormat, FORMAT_WIRE_NAMES
from spirit.game.set_utils import card_script_counts
from spirit.game.scripts.cards import loader as card_loader

FORMATS_PATH = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', 'database', 'json_data', 'formats.json'
))

LEGACY_SETS = {
    "Free_Energy", "Promo_HGSS", "HGSS1", "HGSS2", "HGSS3", "HGSS4", "COL",
    *(f"BW{i}" for i in range(1, 12)), "DV", "PROMO_BW", "BW_Energy",
}
CURRENT_STANDARD_SETS = {
    "Free_Energy", "SV05", "SV06", "SV065", "SV07", "SV08", "SV085",
    "SV09", "SV10", "RSV10PT5", "ZSV10PT5", "SVP", "ME1", "ME2",
    "ME2PT5", "ME3", "ME4", "ME5", "MEP",
}


def is_basic_energy_card(card) -> bool:
    ct = card.get_attribute_value(AttrID.CARD_TYPE)
    if ct != CardType.ENERGY.value:
        return False
    return not card.get_attribute_value(AttrID.IS_SPECIAL_ENERGY)


def _reprint_text(value) -> str:
    """Normalize typography and old reminder wording, not gameplay clauses."""
    text = unicodedata.normalize("NFKD", str(value or ""))
    text = "".join(c for c in text if not unicodedata.combining(c)).casefold()
    text = text.replace("’", "'").replace("×", "x")
    text = text.replace("(before your attack)", "")
    # Named Energy types in old text already mean Basic Energy cards.
    text = re.sub(
        r"\bbasic (grass|fire|water|lightning|psychic|fighting|darkness|metal|fairy) energy",
        r"\1 energy", text,
    )
    return " ".join(text.split()).replace(" ,", ",")


def _legacy_reprint_key(card):
    """Printing-independent identity; same-name Pokemon are NOT reprints."""
    from spirit.game.data_utils import def_for

    definition = def_for(card.guid)
    name = getattr(definition, "display_name", None)
    if not name:
        return None
    card_type = card.get_attribute_value(AttrID.CARD_TYPE)
    key = (card_type, _reprint_text(name))
    # Trainers and Energy use their current errata, like Standard reprints.
    # Keep Trainer categories distinct (e.g. Item vs Supporter).
    if card_type == CardType.TRAINER.value:
        return key + (card.get_attribute_value(AttrID.TRAINER_TYPE),)
    if card_type == CardType.ENERGY.value:
        return key + (bool(card.get_attribute_value(AttrID.IS_SPECIAL_ENERGY)),)
    if card_type != CardType.POKEMON.value:
        return None

    stats = tuple(card.get_attribute_value(attr) for attr in (
        AttrID.HP, AttrID.STAGE, AttrID.POKEMON_TYPES, AttrID.RETREAT_COST,
        AttrID.WEAKNESS_TYPES, AttrID.WEAKNESS_OPERATOR, AttrID.WEAKNESS_AMOUNT,
        AttrID.RESISTANCE_TYPES, AttrID.RESISTANCE_OPERATOR, AttrID.RESISTANCE_AMOUNT,
        AttrID.EVOLUTION_LOGIC_FROM,
    ))
    abilities = []
    for ability in getattr(definition, "abilities", ()):
        data = ability.to_dict()
        data.pop("abilityID", None)  # Different for every printing.
        data["title"] = _reprint_text(ability.title)
        data["gameText"] = _reprint_text(ability.game_text)
        abilities.append(data)
    # JSON canonicalization handles list/dict-valued wire attributes too.
    return key + (json.dumps(
        [stats, sorted(definition.subtypes or []), abilities],
        sort_keys=True, ensure_ascii=True,
    ),)


def _default_formats() -> List[GameFormat]:
    """Build safe defaults when the editable format configuration is absent."""
    loaded = sorted(card_script_counts().keys())
    standard = [s for s in loaded if s in CURRENT_STANDARD_SETS]
    legacy = [s for s in loaded if s in LEGACY_SETS or s == "Free_Energy"]
    return [
        GameFormat(
            "Standard", DeckFormat.STANDARD.value, "Modified",
            sets=standard, regulation_marks=["H", "I", "J"],
        ),
        GameFormat("Expanded", DeckFormat.EXPANDED.value, "Expanded", sets=loaded),
        GameFormat("Legacy", DeckFormat.LEGACY.value, "Legacy", sets=legacy),
        GameFormat("Unlimited", DeckFormat.UNLIMITED.value, "Unlimited", all_sets=True),
    ]


def validate_formats(data: Any) -> Tuple[Optional[List[dict]], Optional[str]]:
    """Round-trips a formats payload; returns (normalized list, None) or (None, error)."""
    if not isinstance(data, list) or not data:
        return None, "'formats' must be a non-empty list"
    normalized, seen_guids, seen_keys = [], set(), set()
    known_sets = set(card_script_counts().keys())
    for entry in data:
        try:
            fmt = GameFormat.from_dict(entry)
        except (ValueError, TypeError) as e:
            return None, str(e)
        if fmt.guid in seen_guids:
            return None, f"duplicate format guid {fmt.guid}"
        if fmt.key in seen_keys:
            return None, f"duplicate format key {fmt.key}"
        seen_guids.add(fmt.guid)
        seen_keys.add(fmt.key)
        for s in fmt.sets:
            if s not in known_sets:
                logging.warning(f"[Formats] Format '{fmt.key}' lists unknown set '{s}'")
        normalized.append(fmt.to_dict())
    return normalized, None


class FormatManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(FormatManager, cls).__new__(cls, *args, **kwargs)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self._initialized = True
        self.formats: List[GameFormat] = []
        self._by_guid: Dict[str, GameFormat] = {}
        self._ref_cache: Dict[tuple, Tuple[Set[str], Set[str]]] = {}
        self._ref_cache_stamp = -1
        self._legacy_reprint_cache = {}
        self.load_formats()

    def load_formats(self):
        self._legacy_reprint_cache = {}
        self._ref_cache.clear()
        self._ref_cache_stamp = -1
        if os.path.exists(FORMATS_PATH):
            try:
                with open(FORMATS_PATH, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                self.formats = [GameFormat.from_dict(e) for e in data.get("formats", [])]
                if not self.formats:
                    raise ValueError("formats.json contains no formats")
                logging.info(f"[Formats] Loaded {len(self.formats)} formats from {FORMATS_PATH}")
            except (OSError, ValueError, TypeError, json.JSONDecodeError) as e:
                logging.error(f"[Formats] Failed to load formats.json, using defaults: {e}")
                self.formats = _default_formats()
        else:
            self.formats = _default_formats()
            try:
                with open(FORMATS_PATH, 'w', encoding='utf-8') as f:
                    json.dump({"formats": [fmt.to_dict() for fmt in self.formats]}, f, indent=2)
                logging.info(f"[Formats] Wrote default formats.json to {FORMATS_PATH}")
            except OSError as e:
                logging.error(f"[Formats] Could not write default formats.json: {e}")
        self._by_guid = {fmt.guid: fmt for fmt in self.formats}

    def by_guid(self, format_guid: str) -> Optional[GameFormat]:
        return self._by_guid.get((format_guid or "").lower())

    def resolve_format_guid(self, value: str) -> Optional[str]:
        """Resolves a format GUID, config key, or client wire name to its GUID."""
        normalized = str(value or "").strip().lower()
        if not normalized:
            return None
        fmt = self.by_guid(normalized)
        if fmt:
            return fmt.guid
        for fmt in self.formats:
            if normalized in (fmt.key.lower(), fmt.format_name.lower()):
                return fmt.guid
        return None

    def format_name(self, format_guid: str) -> str:
        fmt = self.by_guid(format_guid)
        if fmt:
            return fmt.format_name
        return FORMAT_WIRE_NAMES.get((format_guid or "").lower(), "Modified")

    def play_format_guids(self) -> List[str]:
        return [fmt.guid for fmt in self.formats]

    def legal_format_guids_for_set(self, set_code: str) -> List[str]:
        return [fmt.guid for fmt in self.formats if fmt.allows_set(set_code)]

    def _resolve_card_ref(self, ref: str) -> Optional[str]:
        if "/" in ref:
            set_code, _, num = ref.partition("/")
            for c in card_loader.cards:
                if c.key.upper() == set_code.upper() and \
                        str(c.get_attribute_value(AttrID.COLLECTOR_NUMBER)) == num.strip():
                    return c.guid.lower()
            logging.warning(f"[Formats] Card ref '{ref}' matched no loaded card")
            return None
        return ref.lower()

    def _resolved_refs(self, fmt: GameFormat) -> Tuple[Set[str], Set[str]]:
        # "SET/num" refs need the card scripts; re-resolve if the loader reloaded.
        stamp = (id(card_loader.cards), len(card_loader.cards))
        if self._ref_cache_stamp != stamp:
            self._ref_cache.clear()
            self._ref_cache_stamp = stamp
        key = (fmt.guid, tuple(fmt.banned_cards), tuple(fmt.extra_legal_cards))
        cached = self._ref_cache.get(key)
        if cached is None:
            banned = {g for g in map(self._resolve_card_ref, fmt.banned_cards) if g}
            extra = {g for g in map(self._resolve_card_ref, fmt.extra_legal_cards) if g}
            cached = (banned, extra)
            self._ref_cache[key] = cached
        return cached

    def _legacy_reprints(self, fmt: GameFormat):
        """Index once per catalog/configuration, not once per displayed card."""
        stamp = (
            id(card_loader.cards), len(card_loader.cards), tuple(fmt.sets), fmt.all_sets,
            tuple(fmt.banned_cards), tuple(fmt.extra_legal_cards),
            tuple(sorted(fmt.legal_from.items())),
        )
        cached = self._legacy_reprint_cache.get(fmt.guid)
        if cached is not None and cached[0] == stamp:
            return cached[1]
        banned, extra = self._resolved_refs(fmt)
        index = {}
        for source in card_loader.cards:
            guid = source.guid.lower()
            set_code = source.get_attribute_value(AttrID.SET_KEY) or source.key
            if guid in banned or not (fmt.allows_set(set_code) or guid in extra):
                continue
            key = _legacy_reprint_key(source)
            if key is not None:
                start = fmt.legal_from.get(set_code, 0)
                index[key] = min(index.get(key, start), start)
        self._legacy_reprint_cache[fmt.guid] = (stamp, index)
        return index

    def is_card_eventually_legal(self, format_guid: str, card) -> bool:
        """Legality ignoring any legalFrom time gate (the formatLegality bool slot)."""
        fmt = self.by_guid(format_guid)
        if fmt is None:
            return False
        if is_basic_energy_card(card):
            return True
        banned, extra = self._resolved_refs(fmt)
        guid = card.guid.lower()
        if guid in banned:
            return False
        if guid in extra:
            return True
        set_code = card.get_attribute_value(AttrID.SET_KEY) or card.key
        if not fmt.regulation_marks:
            return fmt.allows_set(set_code) or (
                fmt.guid in (DeckFormat.LEGACY.value, DeckFormat.EXPANDED.value)
                and _legacy_reprint_key(card) in self._legacy_reprints(fmt)
            )

        # The loader's wire Card does not carry server-only regulation data;
        # definitions are registered globally by data_utils.
        from spirit.game.data_utils import CARD_DEFS_BY_GUID, def_for
        definition = def_for(guid)
        mark = str(getattr(definition, "regulation_mark", "") or "").upper()
        if fmt.allows_set(set_code) and mark in fmt.regulation_marks:
            return True

        # Older printings of Trainer/Special Energy cards remain legal when a
        # current printing with the same name is legal.  Basic Energy returned
        # above, while Pokémon always require their own regulation mark.
        card_type = card.get_attribute_value(AttrID.CARD_TYPE)
        if card_type not in (CardType.TRAINER.value, CardType.ENERGY.value):
            return False
        display_name = getattr(definition, "display_name", None)
        if not display_name:
            return False
        return any(
            other is not definition
            and getattr(other, "display_name", None) == display_name
            and str(getattr(other, "regulation_mark", "") or "").upper()
                in fmt.regulation_marks
            and fmt.allows_set(getattr(other, "set_code", None))
            for other in CARD_DEFS_BY_GUID.values()
        )

    def is_card_legal(self, format_guid: str, card, now_ms: Optional[int] = None) -> bool:
        if not self.is_card_eventually_legal(format_guid, card):
            return False
        start = self.legal_time_ms(format_guid, card)
        return start <= (now_ms if now_ms is not None else int(time.time() * 1000))

    def legal_time_ms(self, format_guid: str, card) -> int:
        fmt = self.by_guid(format_guid)
        if fmt is None:
            return 0
        set_code = card.get_attribute_value(AttrID.SET_KEY) or card.key
        start = fmt.legal_from.get(set_code, 0)
        if fmt.guid in (DeckFormat.LEGACY.value, DeckFormat.EXPANDED.value) \
                and not fmt.allows_set(set_code):
            source_start = self._legacy_reprints(fmt).get(_legacy_reprint_key(card), 0)
            return max(start, source_start)
        return start
