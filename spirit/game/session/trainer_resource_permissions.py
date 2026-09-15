"""Public prerequisites for bespoke Trainers missing factory conditions.

Key by printed name so alternate arts and reprints share the same rule.
This supplements, rather than replaces, each definition's own condition.
Stadium placement, Tool attachment and future-turn modifiers are not gated
by whether their effect would immediately change the board.
"""
from spirit.game.attributes import AttrID, PokemonTypes, SpecialConditions
from spirit.game.data_utils import def_for
from spirit.game.session.activation_permissions import _cards, _damaged, _typed_energy
from spirit.game.session.passives import effective_bench_capacity, healing_blocked


DECK_SEARCH_NAMES = frozenset({
    'Poké Ball', 'Master Ball', 'Great Ball', 'Xtransceiver', 'Victory Cup',
    'Evolution Incense', 'Pokégear 3.0', 'Energy Loto', 'Irida', "Elesa's Sparkle",
    'Dawn', 'Dark Bell', 'Nest Ball', 'Capturing Aroma', 'Sonia', 'Café Master',
    'Ball Guy', 'Lance', 'Gordie', 'Peony', 'Arven', 'Bug Catching Set',
    "Colress's Tenacity", 'Crispin', 'Egg Incubator', 'Cover Fossil',
    'Plume Fossil', 'Root Fossil Lileep', 'Old Amber Aerodactyl', 'Piers',
    'Opal', 'Tool Box', 'Camping Gear', 'Boost Shake', "Trainers' Mail",
    'Digging Duo', 'Gutsy Pickaxe', 'Trekking Shoes', "Colress's Experiment",
    'Expedition Uniform', 'Adaman', 'Mirage Gate', 'Familiar Bell',
    'Wait and See Turbo',
})
DRAW_ONLY_NAMES = frozenset({
    'Professor Juniper', "Professor's Research", 'Hop', 'Barry', 'Dan',
    'Rotom Bike', 'League Staff', 'Milo', 'Allister', 'Carmine',
})
BENCH_SEARCH_NAMES = frozenset({
    'Nest Ball', 'Egg Incubator', 'Cover Fossil', 'Plume Fossil',
    'Root Fossil Lileep', 'Old Amber Aerodactyl',
})


def public_trainer_allowed(board, pid, source):
    definition = def_for(getattr(source, 'archetype_id', None))
    name = getattr(definition, 'display_name', '')
    if name in DECK_SEARCH_NAMES or name in DRAW_ONLY_NAMES:
        if not _cards(board, pid, 'deck'):
            return False
        if name in BENCH_SEARCH_NAMES:
            return len(_cards(board, pid, 'bench')) < effective_bench_capacity(board, pid)
        if name == 'Milo':
            return any(c is not source for c in _cards(board, pid, 'hand'))
        return True
    # Preserve independent branches: a Trainer can still resolve its second
    # effect when there are no cards to draw.
    if name in {'Blanche', 'Candela', 'Spark', "Gardenia's Vigor", 'Worker',
                'Avery', 'Aroma Lady', 'Choy', 'Zisu', 'Wallace', 'Lure Module',
                'Copycat', 'Judge', 'Marnie', "Lillie's Determination", 'Bruno', 'Kabu',
                'Agatha', 'Lucky Ice Pop', 'Spicy Seasoned Curry', 'Yell Horn',
                'Sidney', "Acerola's Premonition", 'Miss Fortune Sisters', 'Drone Rotom'}:
        deck = _cards(board, pid, 'deck')
        hand = [c for c in _cards(board, pid, 'hand') if c is not source]
        opponent = next((p for p in board.player_ids if p != pid), None)
        other_hand = _cards(board, opponent, 'hand') if opponent else []
        other_deck = _cards(board, opponent, 'deck') if opponent else []
        active = board.active_pokemon(pid)
        own = board.pokemon_in_play(pid)
        if name in {'Sidney', "Acerola's Premonition", 'Drone Rotom'}:
            return bool(other_hand or (name == 'Drone Rotom' and other_deck))
        if name == 'Miss Fortune Sisters':
            return bool(other_deck)
        if name == 'Lure Module':
            return bool(deck or other_deck)
        if name in {'Judge', 'Marnie'}:
            return bool(deck or hand or other_deck or other_hand)
        if name in {"Lillie's Determination", 'Bruno', 'Kabu'}:
            return bool(deck or hand)
        if name == 'Copycat':
            return bool(hand or (deck and other_hand))
        if name == 'Zisu':
            return bool(deck) and len(hand) < len(other_hand) + 1
        if name == 'Wallace':
            return bool(deck or other_deck)
        if name == 'Worker':
            stadium = board.find_global_area('activeStadium')
            return bool(deck or (stadium and stadium.children))
        if name == 'Avery':
            return bool(deck or (opponent and len(_cards(board, opponent, 'bench')) > 3))
        if name == 'Aroma Lady':
            return bool(deck or any(p.get_attribute(AttrID.SPECIAL_CONDITIONS) for p in own))
        if name == 'Choy':
            return bool(deck or other_hand)
        if name in {'Agatha', 'Lucky Ice Pop'}:
            return _damaged(board, active) and (name == 'Agatha' or not healing_blocked(board, active))
        if name in {'Spicy Seasoned Curry', 'Yell Horn'}:
            status = SpecialConditions.BURNED if name == 'Spicy Seasoned Curry' else SpecialConditions.CONFUSED
            targets = [active]
            if name == 'Yell Horn' and opponent:
                targets.append(board.active_pokemon(opponent))
            return any(p and (status not in (p.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])
                       or (name == 'Spicy Seasoned Curry' and _damaged(board, p))) for p in targets)
        if deck:
            return True
        if name == "Gardenia's Vigor":
            return bool(_cards(board, pid, 'bench')) and any(
                _typed_energy(c, PokemonTypes.GRASS) for c in hand)
        ptype = {'Blanche': PokemonTypes.WATER, 'Candela': PokemonTypes.FIRE, 'Spark': PokemonTypes.LIGHTNING}[name]
        return bool(_cards(board, pid, 'bench')) and any(
            _typed_energy(c, ptype) for c in _cards(board, pid, 'discard'))
    return True
