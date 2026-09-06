"""Procedural foil-mask generation for cards with no original PTCGO mask.

Emulates the structure of the original wp_*_Foil2 mask textures (512x512
full-bleed over the card face, engraving pattern in the green channel,
coverage in alpha): a fine sine grating whose phase is modulated by the card
art's luminance produces the contour-following engraved look, near-white
print (text, borders) knocks the foil out, and the coverage region depends
on the card's foil style.
"""
import math
import os
from PIL import Image, ImageChops, ImageDraw, ImageFilter

MASK_SIZE = 512
# Regular-holo art window in card-face UV, measured from original std masks.
WINDOW_RECT = (0.17, 0.09, 0.83, 0.50)

STYLES = ("full", "window", "reverse")

_SIN_LUT = [int(127.5 + 127.5 * math.sin(i * 2 * math.pi / 256)) for i in range(256)]


def _engraving(lum: Image.Image, cycles: float = 70.0, angle_deg: float = 80.0,
               lum_cycles: float = 5.0) -> Image.Image:
    """Sine grating with luminance-modulated phase (engraved-swirl field)."""
    w, h = lum.size
    rad = math.radians(angle_deg)
    step = cycles * 256.0 / w
    gx = [int(step * math.cos(rad) * x) for x in range(w)]
    gy = [int(step * math.sin(rad) * y) for y in range(h)]
    klut = [int(lum_cycles * 256.0 / 255.0 * v) for v in range(256)]
    lum_bytes = lum.tobytes()
    out = bytearray(w * h)
    i = 0
    for y in range(h):
        base = gy[y]
        row = lum_bytes[i:i + w]
        for x in range(w):
            out[i] = _SIN_LUT[(gx[x] + base + klut[row[x]]) & 255]
            i += 1
    return Image.frombytes("L", (w, h), bytes(out))


def _saturation(art: Image.Image) -> Image.Image:
    r, g, b = art.split()
    mx = ImageChops.lighter(ImageChops.lighter(r, g), b)
    mn = ImageChops.darker(ImageChops.darker(r, g), b)
    return ImageChops.subtract(mx, mn)


def _print_gate(lum: Image.Image, sat: Image.Image) -> Image.Image:
    """0 where near-white print (text/borders) should knock the foil out."""
    from_white = lum.point(lambda v: 255 if v <= 200 else max(0, 255 - (v - 200) * 6))
    sat_rescue = sat.point(lambda v: min(255, v * 4))
    gate = ImageChops.lighter(from_white, sat_rescue)
    return gate.filter(ImageFilter.GaussianBlur(1.2))


def _region(style: str, size) -> Image.Image:
    if style == "full":
        return Image.new("L", size, 255)
    w, h = size
    box = (int(WINDOW_RECT[0] * w), int(WINDOW_RECT[1] * h),
           int(WINDOW_RECT[2] * w), int(WINDOW_RECT[3] * h))
    win = Image.new("L", size, 0)
    ImageDraw.Draw(win).rectangle(box, fill=255)
    win = win.filter(ImageFilter.GaussianBlur(2))
    return win if style == "window" else ImageChops.invert(win)


def generate_mask(art_path: str, style: str = "full") -> Image.Image:
    """Card art PNG -> RGBA foil mask in the original wp_ texture layout."""
    if style not in STYLES:
        raise ValueError(f"style must be one of {STYLES}, got {style!r}")
    art = Image.open(art_path).convert("RGB").resize(
        (MASK_SIZE, MASK_SIZE), Image.LANCZOS)
    lum = art.convert("L")
    lum_soft = lum.filter(ImageFilter.GaussianBlur(3))
    sat = _saturation(art)

    grating = _engraving(lum_soft)
    # Thin the sine into engraving lines (original masks are ~40% duty cycle).
    grating = grating.point(lambda v: min(255, max(0, (v - 120) * 2)))
    gate = _print_gate(lum, sat)
    region = _region(style, art.size)

    # Foil rides ink density: strong over dark/saturated print, faint on light.
    amp_a = lum_soft.point(lambda v: min(255, 40 + (255 - v)))
    amp_g = lum_soft.point(lambda v: min(255, 40 + (255 - v)))

    alpha = ImageChops.multiply(grating, gate)
    alpha = ImageChops.multiply(alpha, amp_a)
    alpha = ImageChops.multiply(alpha, region)

    # Original masks keep G ~= 0 wherever A ~= 0 (the shader reads the pattern
    # and the coverage from different channels) -- gate green identically.
    green = ImageChops.multiply(grating, amp_g)
    green = ImageChops.multiply(green, gate)
    green = ImageChops.multiply(green, region)

    zero = Image.new("L", art.size, 0)
    return Image.merge("RGBA", (zero, green, zero, alpha))


def generate_mask_png(art_path: str, out_path: str, style: str = "full") -> bool:
    """Generate and save a mask; returns False (and logs) on failure."""
    try:
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        generate_mask(art_path, style).save(out_path)
        return True
    except Exception as e:
        import logging
        logging.error(f"[FoilGen] Failed to generate mask for {art_path}: {e}")
        return False
