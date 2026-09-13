"""Sword & Shield gallery print identities in their parent expansions.

The client uses numeric slots after the parent's secret rares. Printed TG/GG
numbers remain in COLLECTOR_NUMBER_TEXT and in the upstream artwork URLs.
"""

# Upstream catalog -> (parent set code, last non-gallery slot, gallery size).
GALLERY_SETS = {
    "swsh9tg": ("SWSH9", 186, 30),
    "swsh10tg": ("SWSH10", 216, 30),
    "swsh11tg": ("SWSH11", 217, 30),
    "swsh12tg": ("SWSH12", 215, 30),
    "swsh12pt5gg": ("CZ", 160, 70),
}


def gallery_number(data_stem: str, printed: str) -> int:
    prefix = "GG" if data_stem.endswith("gg") else "TG"
    _, offset, size = GALLERY_SETS[data_stem]
    if not printed.startswith(prefix) or not printed[len(prefix):].isdigit():
        raise ValueError(f"Invalid gallery collector number: {printed!r}")
    number = int(printed[len(prefix):])
    if not 1 <= number <= size:
        raise ValueError(f"Gallery collector number out of range: {printed!r}")
    return offset + number
