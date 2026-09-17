"""Verified corrections to imperfect upstream foil-print metadata."""

from spirit.game.foil_variants import PREMIUM_XY_FOIL_VARIANTS


# User preference: no foil rendering for the Scarlet & Violet era, including
# its mini-sets, promos and Energy prints. Keep native assets for reversibility.
FOIL_DISABLED_SETS = frozenset({
    "SVE", "SV1", "SV2", "SV3", "SV035", "SV4", "SV045", "SV05",
    "SV06", "SV065", "SV07", "SV08", "SV085", "SV09", "SV10",
    "RSV10PT5", "ZSV10PT5", "SVP",
})


def foil_disabled_for_set(set_code: str) -> bool:
    return (set_code or "").upper() in FOIL_DISABLED_SETS


# Rotom contains a Cosmos promotional variant under Brilliant Stars Mewtwo's
# collector number. The expansion printing itself is a regular non-holo card;
# its separately imported reverse-holo mask remains available in wp_ph.
PRINT_FOIL_CORRECTIONS = {
    # Crown Zenith's signed Bede is a regular illustration-window holo, not
    # a full-art print. The archived metadata's FullArt flag is incorrect.
    "CZ": {
        "124": {
            "effect": "SwHolo", "mask": "Holo", "intensity": 201,
            "full_art": False,
        },
    },
    # The metadata export omits the paired LEGEND halves even though the
    # original client cache contains their Cosmos masks.
    "HGSS1": {
        str(number): {
            "effect": "Cosmos", "mask": "Holo", "intensity": 201,
            "full_art": False,
        }
        for number in range(111, 115)
    },
    "HGSS2": {
        str(number): {
            "effect": "Cosmos", "mask": "Holo", "intensity": 201,
            "full_art": False,
        }
        for number in range(90, 96)
    },
    "HGSS3": {
        str(number): {
            "effect": "Cosmos", "mask": "Holo", "intensity": 201,
            "full_art": False,
        }
        for number in range(87, 91)
    },
    "HGSS4": {
        str(number): {
            "effect": "Cosmos", "mask": "Holo", "intensity": 201,
            "full_art": False,
        }
        for number in range(99, 103)
    },
    # The four Boundaries Crossed ACE SPEC cards use the original client's
    # Rainbow material with the wp_ph mask.  Rotom labels that mask
    # ``Reverse``; these are nevertheless the only/main ACE SPEC printings,
    # not optional reverse-holo variants.
    "BW7": {
        str(number): {
            "effect": "Rainbow",
            "mask": "Reverse",
            "intensity": 201,
            "full_art": False,
        }
        for number in range(137, 141)
    },
    # Dragon Vault is an all-foil mini-set.  Its ordinary Tinsel printings
    # carry the same ``Reverse`` mask label in the archived PTCGO data, while
    # the six exceptional Holo records (8-11, 16-17) are already represented
    # correctly by the generated metadata.
    "DV": {
        str(number): {
            "effect": "Tinsel",
            "mask": "Reverse",
            "intensity": 201,
            "full_art": False,
        }
        for number in (1, 2, 3, 4, 5, 6, 7, 12, 13, 14, 15, 18, 19, 20, 21)
    },
    "SWSH9": {
        "56": None,
    },
    # The ordinary Pokémon GO Pikachu 27 printing is non-foil in TCG Live.
    # Its separately cached parallel/reverse printing remains available.
    "PGO": {
        "27": None,
    },
}


def apply_foil_corrections(metadata: dict) -> dict:
    """Apply exact-print corrections in place and return *metadata*."""
    for set_code, cards in PRINT_FOIL_CORRECTIONS.items():
        metadata.setdefault(set_code, {}).update(cards)
    for set_code, aliases in {
        "XY3": {"114": "55"},
        "XY4": {"125": "24"},
        "XY6": {"114": "92"},
        "XY8": {"166": "146"},
        "XY9": {"127": "98", "129": "107"},
        "TWENTIETHANN": {"133": "28"},
        "XY10": {"131": "54"},
    }.items():
        cards = metadata.get(set_code)
        if not cards:
            continue
        for internal, printed in aliases.items():
            cards.setdefault(internal, cards.get(printed))
    # These alternate artworks have their OWN native mask/material. Never
    # inherit a regular/reverse printing's foil, including on metadata resync.
    for set_code, variants in PREMIUM_XY_FOIL_VARIANTS.items():
        cards = metadata.setdefault(set_code, {})
        for internal, native in variants.items():
            cards[internal] = {
                "effect": "Rainbow",
                "mask": "Holo" if set_code == "PROMO_XY" and native == "067xy" else "Etched",
                "intensity": 201,
                "full_art": True,
            }
    return metadata
