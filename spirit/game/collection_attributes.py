"""Client collection facets, separate from in-game rules and text search.

The native attribute filters read typed archetype attributes, not the Python
``subtypes`` list or ``searchable_by``. IDs/tag spelling are the client's wire
contract. Only recognized tags may enter 202200 (unknown tags log warnings).
"""
import json
from spirit.game.attributes import Rarities


TAG_SUBTYPES = {
    'Ultra Beast': 'UltraBeast', 'TAG TEAM': 'TAG',
    'Shining': 'ShinyPokemon', 'Shiny': 'ShinyPokemon',
    'Prism Star': 'PrismStar', 'V': 'V', 'VMAX': 'VMAX',
    'Single Strike': 'SingleStrike', 'Rapid Strike': 'RapidStrike',
    'Fusion Strike': 'FusionStrike', 'Yellow A': 'YellowA', 'League': 'League',
}
TEAM_SUBTYPES = {'Team Plasma': 0, 'Team Flare': 1, 'Team Aqua': 3, 'Team Magma': 4}


def collection_attributes(card, print_metadata=None):
    """Build filter attributes from this printing without changing its rules.

    Lowercase modern ``ex`` must NOT become historical Pokemon-EX. Full Art
    comes from print metadata, independently of whether foil is enabled; a
    full-card shiny material alone does not imply a full-art illustration.
    """
    subtypes = set(card.subtypes or ())
    tags = {tag for subtype, tag in TAG_SUBTYPES.items() if subtype in subtypes}
    if getattr(card, 'rarity', None) == Rarities.Shining:
        tags.add('ShinyPokemon')
    if subtypes & {'V', 'VMAX', 'VSTAR', 'V-UNION'}:
        tags.add('V')
    teams = {value for subtype, value in TEAM_SUBTYPES.items() if subtype in subtypes}
    # Double Crisis exports omit teams on its named Pokemon, Trainers and
    # special Energy. All 34 printings explicitly carry one of these teams.
    if getattr(card, 'set_code', '') == 'TATM':
        name = getattr(card, 'display_name', '') or ''
        if name.startswith('Team Aqua') or name in {'Aqua Diffuser', 'Double Aqua Energy'}:
            teams.add(3)
        if name.startswith('Team Magma') or name in {'Magma Pointer', 'Double Magma Energy'}:
            teams.add(4)
    full_art = bool((print_metadata or {}).get('full_art')) or 'Full Art' in subtypes
    result = {
        '201010': {'type': 'bool', 'value': 'EX' in subtypes},
        '201030': {'type': 'bool', 'value': 'LEGEND' in subtypes},
        '201000': {'type': 'bool', 'value': full_art},
    }
    if tags:
        result['202200'] = {'type': 'json', 'value': json.dumps(sorted(tags))}
    if teams:
        result['200360'] = {'type': 'json', 'value': json.dumps(sorted(teams))}
    if 'GX' in subtypes:
        gx_ids = [a.ability_id for a in getattr(card, 'abilities', ())
                  if getattr(a, 'gx', False) and a.ability_id]
        if gx_ids:
            result['202120'] = {'type': 'json', 'value': json.dumps(gx_ids)}
    return result
