"""Printings intentionally excluded from the playable/collectible catalog."""

# Anniversary novelty cards explicitly marked unusable at official tournaments.
EXCLUDED_SWSH_PROMOS = frozenset({132, 135, 136, 137, 138, 144})


def excluded_print(set_code, number):
    if str(set_code).upper() not in {'PROMO_SWSH', 'SWSHP'}:
        return False
    value = str(number).upper().removeprefix('SWSH')
    return value.isdigit() and int(value) in EXCLUDED_SWSH_PROMOS
