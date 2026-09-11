"""Verified corrections to imperfect upstream foil-print metadata."""


# Rotom contains a Cosmos promotional variant under Brilliant Stars Mewtwo's
# collector number. The expansion printing itself is a regular non-holo card;
# its separately imported reverse-holo mask remains available in wp_ph.
PRINT_FOIL_CORRECTIONS = {
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
    # pokemon-tcg-data exposes five XY promo alternates with the same printed
    # collector number as their base card.  The importer assigns unique
    # internal slots 212..216; they retain the original printing's foil
    # material unless a dedicated cache record becomes available.
    promo = metadata.get("PROMO_XY")
    if promo:
        for internal, printed in {
            "212": "67", "213": "150", "214": "177",
            "215": "198", "216": "200",
        }.items():
            promo.setdefault(internal, promo.get(printed))
    for set_code, aliases in {
        "XY2": {"111": "88"},
        "XY3": {"114": "55"},
        "XY4": {"125": "24", "126": "65"},
        "XY6": {"113": "77", "114": "92"},
        "XY7": {"102": "75"},
        "XY8": {"166": "146"},
        "XY9": {"127": "98", "128": "98", "129": "107"},
        "TWENTIETHANN": {"133": "28", "134": "73"},
        "XY10": {"130": "43", "131": "54", "132": "105", "133": "111"},
    }.items():
        cards = metadata.get(set_code)
        if not cards:
            continue
        for internal, printed in aliases.items():
            cards.setdefault(internal, cards.get(printed))
    return metadata
