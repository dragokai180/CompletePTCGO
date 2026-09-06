import json
import logging
import os
import re
import uuid

from spirit.game.attributes import AttrID, ProductType
from spirit.game.set_utils import eligible_booster_sets
from spirit.game.scripts.cards import loader as card_loader
from spirit.game.scripts.products import loader as product_loader
from spirit.database.player_data import (
    save_deck, add_many_to_collection, update_wallet,
    STARTING_COINS, STARTING_GEMS, STARTING_TICKETS,
)

STARTER_BOOSTER_PACK_COUNT = 10

# Default cosmetics granted to every new account (basic coin/sleeve/deck box)
STARTER_COIN_GUID = "B9A4EA96-949E-11E1-890F-EFB676C7909C"
STARTER_SLEEVE_GUID = "e079c0d3-b934-4fbd-b021-545106c75693"
STARTER_DECK_BOX_GUID = "e129b0d3-b934-4fbd-b021-545106c75694"
STARTER_COSMETICS = [STARTER_COIN_GUID, STARTER_SLEEVE_GUID, STARTER_DECK_BOX_GUID]

_SETS_JSON = os.path.join(
    os.path.dirname(__file__), "..", "database", "json_data", "sets.json"
)

# PTCGO / Limitless exports: "* 3 Dunsparce JTG 120" or "3 Dunsparce JTG 120"
_TCGO_CARD_LINE = re.compile(
    r"^\s*\*?\s*(\d+)\s+.+\s+(\S+)\s+(\d+)\s*$"
)


def _load_set_code_map() -> dict:
    """externalId (JTG, SSH, Energy, …) and local name (SV09, SWSH1, …) -> local set code."""
    mapping = {}
    try:
        with open(_SETS_JSON, encoding="utf-8") as f:
            entries = json.load(f)
    except OSError as e:
        logging.warning(f"[Starter] Could not load set codes from {_SETS_JSON}: {e}")
        return mapping
    for entry in entries:
        name = (entry.get("name") or "").strip()
        ext = (entry.get("externalId") or "").strip()
        if not name:
            continue
        mapping[name.upper()] = name
        if ext and ext.upper() != "N/A":
            mapping[ext.upper()] = name
    return mapping


SET_CODE_MAP = _load_set_code_map()


def parse_tcgo_decklist(text: str) -> list:
    """Parses a PTCGO / Limitless export into (count, set code, collector number) tuples."""
    entries = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or line.lower().startswith("total "):
            continue
        match = _TCGO_CARD_LINE.match(line)
        if not match:
            continue
        entries.append((int(match.group(1)), match.group(2), int(match.group(3))))
    return entries


# Paste a PTCGO / Limitless export (or keep (count, set, number) tuples).
ALAKAZAM_DECKLIST = """
* 3 Dunsparce JTG 120
* 3 Dudunsparce TEF 129
* 1 Fezandipiti ex ASC 142
* 1 Shaymin DRI 10
* 1 Genesect SFA 40
* 4 Abra MEG 54
* 1 Dedenne SSP 87
* 1 Elgyem BLK 40
* 4 Kadabra MEG 55
* 3 Alakazam MEG 56
* 4 Dawn PFL 87
* 3 Hilda WHT 84
* 2 Boss's Orders MEG 114
* 1 Lana's Aid TWM 155
* 4 Buddy-Buddy Poffin TEF 144
* 4 Poké Pad POR 81
* 3 Rare Candy MEG 125
* 2 Enhanced Hammer TWM 148
* 1 Sacred Ash DRI 168
* 1 Night Stretcher ASC 196
* 1 Lucky Helmet TWM 158
* 1 Handheld Fan TWM 150
* 1 Air Balloon ASC 181
* 4 Nighttime Mine ASC 197
* 4 Telepathic Psychic Energy POR 88
* 1 Psychic Energy Energy 5
* 1 Enriching Energy SSP 191
"""

# MEW_VMAX_DECKLIST = """
# * 1 Oricorio FST 42
# * 4 Genesect V FST 185
# * 4 Mew V FST 251
# * 3 Mew VMAX FST 114
# * 3 Judge FST 235
# * 2 Boss's Orders RCL 189
# * 1 Roxanne ASR 188
# * 1 Cyllene ASR 183
# * 4 Ultra Ball BRS 186
# * 4 Quick Ball SSH 216
# * 4 Battle VIP Pass FST 225
# * 4 Power Tablet FST 281
# * 4 Cram-o-matic FST 229
# * 2 Lost Vacuum LOR 162
# * 2 Escape Rope BST 125
# * 2 Rotom Phone CPA 64
# * 1 Pal Pad SSH 172
# * 1 Switch SSH 183
# * 1 Fan of Waves BST 127
# * 2 Forest Seal Stone SIT 156
# * 1 Choice Belt BRS 135
# * 1 Big Parasol DAA 157
# * 2 Path to the Peak CRE 148
# * 2 Lost City LOR 161
# * 4 Double Turbo Energy BRS 151
# """

# LOST_ZONE_BOX_DECKLIST = """
# * 1 Crobat V SHF 44
# * 1 Drapion V LOR 118
# * 1 Dragonite V EVS 192
# * 1 Aerodactyl V LOR 92
# * 1 Aerodactyl VSTAR LOR 93
# * 1 Zeraora VIV 61
# * 4 Comfey LOR 79
# * 2 Sableye LOR 70
# * 1 Cramorant LOR 50
# * 1 Lumineon V BRS 40
# * 1 Manaphy BRS 41
# * 1 Radiant Greninja ASR 46
# * 4 Colress's Experiment LOR 155
# * 1 Klara CRE 145
# * 4 Mirage Gate LOR 163
# * 4 Battle VIP Pass FST 225
# * 4 Scoop Up Net RCL 165
# * 3 Escape Rope BST 125
# * 2 Switch Cart ASR 154
# * 2 Quick Ball SSH 179
# * 2 Ultra Ball BRS 186
# * 2 Lost Vacuum LOR 162
# * 1 Ordinary Rod SSH 171
# * 1 Energy Recycler BST 124
# * 1 Hisuian Heavy Ball ASR 146
# * 2 Forest Seal Stone SIT 156
# * 1 Air Balloon SSH 156
# * 1 Training Court RCL 169
# * 4 Water Energy Energy 3
# * 2 Psychic Energy Energy 5
# * 2 Lightning Energy Energy 4
# * 1 Fighting Energy Energy 6
# """

# REGIGIGAS_DECKLIST = """
# * 3 Regigigas ASR 130
# * 2 Regidrago ASR 118
# * 1 Regidrago EVS 124
# * 2 Regirock ASR 75
# * 1 Regieleki ASR 51
# * 1 Regieleki EVS 60
# * 2 Registeel ASR 108
# * 2 Regice ASR 37
# * 4 Professor's Research CEL 24
# * 4 Marnie SSH 200
# * 1 Serena SIT 193
# * 1 Boss's Orders RCL 189
# * 4 Scoop Up Net RCL 165
# * 4 Quick Ball SSH 216
# * 3 Trekking Shoes ASR 156
# * 3 Ordinary Rod SSH 171
# * 2 Ultra Ball BRS 150
# * 1 Hisuian Heavy Ball ASR 146
# * 1 Escape Rope BST 125
# * 3 Choice Belt BRS 135
# * 4 Path to the Peak CRE 148
# * 4 Aurora Energy SSH 186
# * 2 Twin Energy RCL 174
# * 2 Gift Energy LOR 171
# * 1 Speed Lightning Energy RCL 173
# * 1 Fire Energy Energy 2
# * 1 Capture Energy RCL 171
# """

STARTER_DECKS = [
    ("Alakazam", ALAKAZAM_DECKLIST)
]

_CARD_INDEX = None


def _ensure_cards_loaded():
    if not card_loader.cards:
        card_loader.load_all()


def _ensure_products_loaded():
    if not product_loader.products:
        product_loader.load_all()


def _card_index():
    """{(set_code, collector_number): guid} over every loaded card script."""
    global _CARD_INDEX
    if _CARD_INDEX is None:
        _ensure_cards_loaded()
        index = {}
        for card in card_loader.cards:
            num = card.get_attribute_value(AttrID.COLLECTOR_NUMBER)
            if num is None:
                continue
            try:
                index[(card.key.upper(), int(num))] = card.guid
            except (ValueError, TypeError):
                continue
        _CARD_INDEX = index
    return _CARD_INDEX


def resolve_decklist(decklist) -> list:
    """Expands a PTCGO export string or (count, set, number) tuples into GUIDs."""
    if isinstance(decklist, str):
        decklist = parse_tcgo_decklist(decklist)
    guids = []
    index = _card_index()
    for count, live_code, number in decklist:
        set_code = SET_CODE_MAP.get(str(live_code).upper(), live_code)
        guid = index.get((str(set_code).upper(), number))
        if not guid:
            logging.warning(f"[Starter] Card not found: {live_code} {number} (set {set_code})")
            continue
        guids.extend([guid] * count)
    return guids


def build_deck_data(deck_name: str, decklist) -> dict:
    """Builds a client-shaped SerializableDeck dict for the given decklist."""
    return {
        "deckID": str(uuid.uuid4()),
        "deckName": deck_name,
        "piles": {"deck": resolve_decklist(decklist)},
        "attributes": [
            {"name": AttrID.SELECTED_COIN.value, "value": "B9A4EA96-949E-11E1-890F-EFB676C7909C"},
            {"name": AttrID.SELECTED_SLEEVE.value, "value": "e079c0d3-b934-4fbd-b021-545106c75693"},
            {"name": AttrID.SELECTED_DECK_BOX.value, "value": "e129b0d3-b934-4fbd-b021-545106c75694"},
        ],
    }


def starter_booster_packs() -> list:
    """Booster pack products for every set with more than 10 scripted cards."""
    _ensure_products_loaded()
    eligible = {code.upper() for code in eligible_booster_sets()}
    return [
        p for p in product_loader.products
        if p.product_type == ProductType.PACKS.value and p.key.upper() in eligible
    ]


def grant_starter_content(account_id: str) -> bool:
    """Grants the starter decks and booster packs to a freshly created account."""

    try:
        update_wallet(account_id, STARTING_COINS, STARTING_GEMS, STARTING_TICKETS)

        # Aggregate every non-tradable grant (deck cards + packs + cosmetics) and
        # write them in ONE transaction instead of ~140 per-row round trips.
        grants: dict[str, int] = {}
        for deck_name, decklist in STARTER_DECKS:
            deck_data = build_deck_data(deck_name, decklist)
            deck_guids = deck_data["piles"]["deck"]
            if len(deck_guids) != 60:
                logging.warning(f"[Starter] Deck '{deck_name}' resolved {len(deck_guids)}/60 cards.")
            save_deck(account_id, deck_data["deckID"], deck_name, deck_data, is_avatar=False)
            for guid in deck_guids:
                grants[guid] = grants.get(guid, 0) + 1

        for pack in starter_booster_packs():
            grants[pack.guid] = grants.get(pack.guid, 0) + STARTER_BOOSTER_PACK_COUNT

        for cosmetic_guid in STARTER_COSMETICS:
            grants[cosmetic_guid] = grants.get(cosmetic_guid, 0) + 1

        add_many_to_collection(account_id, grants, is_tradable=False)

        logging.info(f"[Starter] Granted starter decks, booster packs, and cosmetics to account {account_id}.")
        return True
    except Exception as e:
        logging.error(f"[Starter] Failed to grant starter content to {account_id}: {e}")
        return False
