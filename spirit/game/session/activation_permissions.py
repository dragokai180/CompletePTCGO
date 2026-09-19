"""Public resource prerequisites shared by action menus and execution.

These checks govern ACTIVATING an effect, never playing a Stadium or attaching
a Tool. Private searches need a nonempty deck, not a server-visible match.
Card-specific conditions still handle timing, locks, and specialized targets.
"""
import re
from functools import lru_cache

from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes
from spirit.game.data_utils import def_for
from spirit.game.session.effects import (
    is_basic_energy, is_energy_card, is_stadium_card, is_basic_pokemon,
    full_stack, is_pokemon_card,
)
from spirit.game.session.passives import (
    effective_bench_capacity, effective_max_hp, effective_pokemon_types,
    evolution_blocked, healing_blocked,
)


def _cards(board, pid, zone):
    area = board.find_player_area(pid, zone)
    return list(area.children) if area is not None else []


def _damaged(board, pokemon):
    return pokemon is not None and pokemon.get_attribute(AttrID.HP, 0) < effective_max_hp(board, pokemon)


def _healable(board, pokemon):
    return _damaged(board, pokemon) and not healing_blocked(board, pokemon)


def _typed_energy(card, ptype, *, basic=False):
    from spirit.game.card_effects.pokemon import energy_provides_type
    return (is_basic_energy(card) if basic else is_energy_card(card)) and energy_provides_type(card, ptype.value)


@lru_cache(maxsize=4096)
def _text(raw):
    from spirit.game.card_effects.standard_era import _norm
    return _norm(raw)


def _filtered_pokemon(board, pid, source, phrase):
    """Resolve a printed public donor/target phrase, without examining a deck."""
    other = next((p for p in board.player_ids if p != pid), None)
    owner = other if "opponent" in phrase else pid
    pool = list(board.pokemon_in_play(owner)) if owner else []
    if 'this pokémon' in phrase or phrase.strip() == 'it':
        pool = [source] if source else []
    elif 'active' in phrase:
        pool = [board.active_pokemon(owner)] if owner else []
    elif 'benched' in phrase or 'bench' in phrase:
        pool = _cards(board, owner, 'bench') if owner else []
    elif 'your' not in phrase:
        pool += list(board.pokemon_in_play(other)) if other else []
    pool = [p for p in pool if p is not None]
    if 'other pokémon' in phrase:
        pool = [p for p in pool if p is not source]
    typed = re.search(r'(grass|fire|water|lightning|psychic|fighting|darkness|metal|fairy|dragon) pokémon', phrase)
    if typed:
        ptype = getattr(PokemonTypes, typed.group(1).upper()).value
        pool = [p for p in pool if ptype in effective_pokemon_types(board, p)]
    if 'basic pokémon' in phrase:
        pool = [p for p in pool if is_basic_pokemon(p)]
    if 'pokémon-ex' in phrase:
        from spirit.game.card_effects.bw_era import _pokemon_ex
        pool = [p for p in pool if _pokemon_ex(p)]
    for name in ('Wormadam', 'Deoxys', "Team Rocket's", 'Team Magma'):
        if name.lower() in phrase:
            pool = [p for p in pool if name in getattr(def_for(p.archetype_id), 'display_name', '')]
    if 'rapid strike pokémon' in phrase:
        pool = [p for p in pool if 'Rapid Strike' in (getattr(def_for(p.archetype_id), 'subtypes', []) or [])]
    return pool


def _transfer_allowed(board, pid, source, text):
    # These are transfers, not attachments from a private search or the hand.
    match = re.search(r'\bmove (.+?) (?:from|attached to) (.+?) to (.+?)(?:\.|$)', text)
    if not match:
        return True
    what, donor_phrase, target_phrase = match.groups()
    if 'pokémon' not in target_phrase or not any(
            word in donor_phrase for word in ('pokémon', 'wormadam', 'deoxys')):
        return True
    donors = _filtered_pokemon(board, pid, source, donor_phrase)
    targets = _filtered_pokemon(board, pid, source, target_phrase)
    if 'damage counter' in what:
        donors = [p for p in donors if _damaged(board, p)]
    elif 'energy' in what:
        from spirit.game.card_effects.bw_era import _energy_phrase_predicate
        predicate = _energy_phrase_predicate(what)
        donors = [p for p in donors if any(predicate(e) for e in board.attached_energies(p))]
    else:
        return True
    return any(d is not t for d in donors for t in targets)


def _stadium_allowed(board, pid, source, name):
    hand, deck = _cards(board, pid, 'hand'), _cards(board, pid, 'deck')
    discard, bench = _cards(board, pid, 'discard'), _cards(board, pid, 'bench')
    own = board.pokemon_in_play(pid)
    opponent = next((p for p in board.player_ids if p != pid), None)
    if name == 'Tropical Beach':
        return bool(deck) and len(hand) < 7
    if name == 'Pokémon Center':
        return any(_healable(board, p) for p in bench)
    if name == 'Champions Festival':
        return len(own) >= 6 and any(_healable(board, p) for p in own)
    if name == 'Twist Mountain':
        return len(bench) < effective_bench_capacity(board, pid) and any(
            c.get_attribute(AttrID.STAGE) == PokemonStage.RESTORED.value for c in hand)
    if name == 'Battle City':
        return bool(deck)
    if name in {'Giant Hearth', 'Viridian Forest'}:
        return bool(deck and hand)
    if name in {'Burned Tower', 'Training Court'}:
        return any(is_basic_energy(c) for c in discard)
    if name == 'Mt. Coronet':
        return any(_typed_energy(c, PokemonTypes.METAL) for c in discard)
    if name == 'Levincia':
        return any(_typed_energy(c, PokemonTypes.LIGHTNING, basic=True) for c in discard)
    if name == 'Cycling Road':
        return bool(deck) and any(is_basic_energy(c) for c in hand)
    if name in {'Heat Factory ◇', 'Scorched Earth'}:
        types = (PokemonTypes.FIRE, PokemonTypes.FIGHTING) if name == 'Scorched Earth' else (PokemonTypes.FIRE,)
        return bool(deck) and any(_typed_energy(c, t) for c in hand for t in types)
    if name == 'Moonlit Hill':
        return any(_typed_energy(c, PokemonTypes.PSYCHIC, basic=True) for c in hand) \
            and any(_healable(board, p) for p in own)
    if name == 'Lavender Town':
        return bool(opponent and _cards(board, opponent, 'hand'))
    if name == 'Mystery Garden':
        psychic = sum(PokemonTypes.PSYCHIC.value in effective_pokemon_types(board, p) for p in own)
        # The discarded Energy leaves hand BEFORE the draw-until comparison.
        return bool(deck) and any(is_energy_card(c) for c in hand) and len(hand) - 1 < psychic
    if name == 'Grand Tree':
        state = getattr(board, 'turn_state', None)
        return bool(deck and state and state.turn_number > 2 and any(
            p.get_attribute(AttrID.STAGE) == PokemonStage.BASIC.value
            and state.may_evolve_target(p.entity_id) and not evolution_blocked(board, pid, p)
            for p in own))
    return True


def public_activation_allowed(ability, board, pid, source):
    """Reject missing public resources even when a callback is absent/partial.

    This is not a general 'would anything change?' simulator: an optional
    branch may fail, a coin may be tails, and a hidden search may find nothing.
    Those remain legal. Only the explicitly recognized prerequisites apply.
    """
    text = _text(ability.game_text)
    title = ability.title
    from spirit.game.card_effects.hand_entry import hand_entry_allowed
    entry_allowed = hand_entry_allowed(board, pid, source, ability, text)
    if entry_allowed is not None:
        return entry_allowed
    definition = def_for(source.archetype_id) if source is not None else None
    if source is not None and is_stadium_card(source):
        if not _stadium_allowed(board, pid, source, getattr(definition, 'display_name', '')):
            return False
    hand, deck = _cards(board, pid, 'hand'), _cards(board, pid, 'deck')
    opponent = next((p for p in board.player_ids if p != pid), None)

    # Inline payment handlers are not exempt from MENU prerequisites.
    from spirit.game.card_effects.bw_era import (
        _ability_hand_discard_cost, _ability_attached_energy_discard_cost,
    )
    cost = _ability_hand_discard_cost(text)
    if cost and cost[0] is not None and sum(cost[1](c) for c in hand) < cost[0]:
        return False
    cost = _ability_attached_energy_discard_cost(text)
    if cost and sum(cost[1](e) for e in board.attached_energies(source)) < cost[0]:
        return False
    if not _transfer_allowed(board, pid, source, text):
        return False

    if title in {'Evidence Gathering', 'Primate Wisdom'}:
        return bool(hand and deck)
    if title in {'Scornful Storm', 'Wicked Ruler'}:
        return bool(opponent and len(_cards(board, opponent, 'hand')) > 4)
    if title == 'Weed Out':
        return len(_cards(board, pid, 'bench')) > 3
    if title in {'Stance Change', 'Schooling'}:
        wanted = 'Aegislash' if title == 'Stance Change' else 'Wishiwashi-GX'
        return any(getattr(def_for(c.archetype_id), 'display_name', '') == wanted for c in hand)
    if title == 'Unseen Flash':
        return sum(_typed_energy(c, PokemonTypes.LIGHTNING) for c in hand) >= 2
    if title in {'Hurricane Charge', 'Pyro Dance'}:
        types = (PokemonTypes.WATER, PokemonTypes.LIGHTNING) if title == 'Hurricane Charge' else (PokemonTypes.FIRE, PokemonTypes.FIGHTING)
        return any(_typed_energy(c, t, basic=title == 'Pyro Dance') for c in hand for t in types)
    if title in {'Busybody Nurse', 'Happiness Supplement'}:
        active = board.active_pokemon(pid)
        return bool(active and active.get_attribute(AttrID.SPECIAL_CONDITIONS))
    if title == 'Boisterous Wind':
        active = board.active_pokemon(opponent) if opponent else None
        return bool(active and board.attached_energies(active))
    if title == 'Teleport Room':
        area = board.find_global_area('activeStadium')
        return bool(area and area.children)
    if title == 'Toxic Wetland':
        area = board.find_global_area('activeStadium')
        if not area or not area.children:
            return False
    if title == 'Toxic Powder' and not any(
            getattr(def_for(c.archetype_id), 'display_name', '') == 'Ancient Booster Energy Capsule'
            for c in full_stack(source)[1:]):
        return False
    if title == 'Shocking Light':
        from spirit.game.card_effects.bw_era import _pokemon_ex
        return bool(opponent and any(_pokemon_ex(p) for p in board.pokemon_in_play(opponent)))
    if title == 'Ancient Wing':
        return bool(opponent and any(
            any(is_pokemon_card(c) for c in full_stack(p)[1:])
            for p in board.pokemon_in_play(opponent)))
    if title == 'Tag Transport':
        active = board.active_pokemon(pid)
        return bool(active and 'TAG TEAM' in (getattr(def_for(active.archetype_id), 'subtypes', []) or [])
                    and _cards(board, pid, 'bench'))
    if title in {'Second Sight', 'Mischievous Trick', 'Shuffle Dance', 'Scampering Tail'}:
        if title == 'Second Sight':
            return bool(deck or (opponent and _cards(board, opponent, 'deck')))
        owner = pid if title == 'Mischievous Trick' else opponent
        return bool(owner and _cards(board, owner, 'deck'))
    if title in {'Dimension Transfer', 'Wondrous Gift', 'Snack Search', "Mermaid's Call", 'Voraciousness'}:
        from spirit.game.session.effects import is_item_card
        discard = _cards(board, pid, 'discard')
        if title in {'Dimension Transfer', 'Wondrous Gift'}:
            return any(is_item_card(c) for c in discard)
        if title == 'Snack Search':
            return bool(discard)
        wanted = "Misty's Favor" if title == "Mermaid's Call" else 'Leftovers'
        return any(getattr(def_for(c.archetype_id), 'display_name', '') == wanted for c in discard)

    if re.search(r"(?:look at your opponent's hand|opponent reveal(?:s)? (?:their|his or her) hand|(?:from|in) your opponent's hand)", text):
        if not opponent or not _cards(board, opponent, 'hand'):
            return False
        if "onto your opponent's bench" in text and len(_cards(board, opponent, 'bench')) >= effective_bench_capacity(board, opponent):
            return False

    # Explicit multi-zone effects cannot be reduced to a deck-only check.
    if title == 'Legacy Star':
        return bool(deck or _cards(board, pid, 'discard'))
    if title in {'Mind Hat', 'Seething Currents'}:
        return bool(hand or (opponent and _cards(board, opponent, 'hand')))
    if title == 'Pitch a Pyukumuku':
        # This card replenishes even an empty deck before drawing.
        return source in hand

    search = re.search(r'\bsearch(?:es)? (?:your|their|his or her) deck', text)
    if search:
        prefix = text[:search.start()]
        replenishes = re.search(r'(?:put|shuffle).+\bdeck\b', prefix)
        if not deck and not replenishes:
            return False
        if re.search(r'(?:onto|on) (?:your|their) bench', text):
            if len(_cards(board, pid, 'bench')) >= effective_bench_capacity(board, pid):
                return False

    inspection = re.search(
        r'(?:look at|reveal|discard) the (?:top|bottom) (?:\d+ cards?|card) of '
        r"(your opponent's|your|their) deck", text)
    if inspection:
        owner = opponent if inspection.group(1) == "your opponent's" else pid
        if not owner or not _cards(board, owner, 'deck'):
            return False

    # Draw effects with no independent benefit need something to draw.
    # A shuffle-and-draw may first refill an empty deck from the hand.
    draw = re.search(r'\bdraw(?:s)? (?:(?:up to )?\d+ cards?|a card|cards until)', text)
    if draw and not re.search(r'choose (?:1|one):|\b(?:attach|heal|damage)\b', text):
        prefix = text[:draw.start()]
        refills_from_hand = re.search(r'shuffle .+hand.+(?:deck|bottom)', prefix)
        if not deck and not (refills_from_hand and hand):
            return False
        until = re.search(r'draw cards until (?:you|they) have (\d+) cards', text)
        if until:
            cost = _ability_hand_discard_cost(text)
            paid = (len(hand) if cost[0] is None else cost[0]) if cost else 0
            if len(hand) - paid >= int(until.group(1)):
                return False

    # Healing-only effects: damage on the wrong side/type/spot is not a target.
    # Mysterious Potion has an independent tails damage branch; do not gate it.
    heal = re.search(r'\bheal (?:\d+|all) damage from (.+?)(?:\.|$)', text)
    if heal and not any(phrase in text for phrase in ('if tails', 'draw', 'search', 'special condition')):
        targets = _filtered_pokemon(board, pid, source, heal.group(1))
        if 'has any energy attached' in text:
            targets = [p for p in targets if board.attached_energies(p)]
        typed_energy = re.search(r'has any (grass|fire|water|lightning|psychic|fighting|darkness|metal|fairy) energy attached', text)
        if typed_energy:
            ptype = getattr(PokemonTypes, typed_energy.group(1).upper())
            targets = [p for p in targets if any(_typed_energy(e, ptype) for e in board.attached_energies(p))]
        if not any(_healable(board, p) for p in targets):
            return False
    return True
