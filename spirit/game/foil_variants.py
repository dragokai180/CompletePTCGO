"""Exact native mask identities for Premium Trainer's XY Collection prints.

Verified against BW/SM cache Texture2D names and the original Rotom export's
variant (10020), foil effect (200610), mask (200620) and FullArt (201000).
Internal slots are server identities, not printed collector numbers.
"""

PREMIUM_XY_FOIL_VARIANTS = {
    "XY2": {"111": "088xy"},
    "XY4": {"126": "065xy"},
    "XY6": {"113": "077xy"},
    "XY7": {"102": "075xy"},
    # 98b is the full-art 098xy; 098ya is the different regular 98a print.
    "XY9": {"128": "098xy"},
    "XY10": {"130": "043xy", "132": "105xy", "133": "111xy"},
    "TWENTIETHANN": {"134": "073xy"},
    "PROMO_XY": {
        "212": "067xy", "213": "150xy", "214": "177xy",
        "215": "198xy", "216": "200xy",
    },
}
