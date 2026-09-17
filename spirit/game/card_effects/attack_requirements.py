"""Printed attack prerequisites; effect clauses are not activation costs."""
import re
from functools import lru_cache

from spirit.game.attributes import AttrID, PokemonTypes
from spirit.game.data_utils import def_for
from spirit.game.session.passives import effective_max_hp, effective_pokemon_types


@lru_cache(maxsize=4096)
def requirements(raw):
    text = ' '.join((raw or '').replace('’', "'").lower().split())
    rules, unknown = [], []
    if "if you go second, you can't use this attack during your first turn" in text:
        rules.append(('not_second_first_turn', None))
    for match in re.finditer(r"you can use this attack only (?:if|when) (.+?)(?:\.|$)", text):
        clause = match.group(1)
        if clause == 'you have more prize cards remaining than your opponent':
            rules.append(('prize_margin', 1))
        elif m := re.fullmatch(r'you have at least (\d+) more prize cards remaining than your opponent', clause):
            rules.append(('prize_margin', int(m[1])))
        elif m := re.fullmatch(r"the total of both players' remaining prize cards is (\d+) or less", clause):
            rules.append(('prize_total', int(m[1])))
        elif m := re.fullmatch(r"your opponent has exactly (\d+) prize cards? remaining", clause):
            rules.append(('opponent_prizes', int(m[1])))
        elif re.fullmatch(r'you go second,? and only (?:on|during) your first turn', clause):
            rules.append(('second_first_turn', None))
        elif clause == 'this pokémon has any damage counters on it':
            rules.append(('own_damage', None))
        elif clause == "your opponent's active pokémon is affected by a special condition":
            rules.append(('defender_condition', None))
        elif m := re.fullmatch(r'you have (.+) pokémon on your bench', clause):
            words = tuple(re.split(r',? and |, ', m[1]))
            if all(word.upper() in PokemonTypes.__members__ for word in words):
                rules.append(('bench_types', words))
            else:
                unknown.append(clause)
        elif m := re.fullmatch(r'(this pokémon|your .+?) used (.+?) during your last turn', clause):
            rules.append(('previous_attack', (m[1], m[2])))
        elif m := re.fullmatch(r'you have (\d+) or more cards in (?:the|your) lost zone', clause):
            rules.append(('lost_zone', int(m[1])))
        else:
            unknown.append(clause)
    for match in re.finditer(
            r"if 1 of your pokémon used (.+?) during your last turn, this attack can't be used", text):
        rules.append(('not_previous_attack', match[1]))
    return tuple(rules), tuple(unknown)


def printed_attack_allowed(raw, board, player_id, source):
    rules, _ = requirements(raw)
    if not rules:
        return True
    state = getattr(board, 'turn_state', None)
    opponent = next((pid for pid in board.player_ids if pid != player_id), None)
    def cards(pid, zone):
        area = board.find_player_area(pid, zone) if pid is not None else None
        return list(area.children) if area is not None else []
    own_prizes, other_prizes = len(cards(player_id, 'prizePile')), len(cards(opponent, 'prizePile'))
    previous = getattr(state, 'attacks_prev_turn_by_player', {}).get(player_id, [])
    titles = getattr(state, 'attack_titles_prev_turn_by_player', {}).get(player_id, [])
    for kind, value in rules:
        if kind == 'prize_margin' and own_prizes - other_prizes < value:
            return False
        if kind == 'prize_total' and own_prizes + other_prizes > value:
            return False
        if kind == 'opponent_prizes' and other_prizes != value:
            return False
        if kind == 'second_first_turn' and (state is None or state.turn_number != 2):
            return False
        if kind == 'not_second_first_turn' and state is not None and state.turn_number == 2:
            return False
        if kind == 'own_damage' and (source is None or source.get_attribute(AttrID.HP, 0) >= effective_max_hp(board, source)):
            return False
        if kind == 'defender_condition':
            target = board.active_pokemon(opponent) if opponent else None
            if target is None or not target.get_attribute(AttrID.SPECIAL_CONDITIONS):
                return False
        if kind == 'bench_types':
            present = {t for p in cards(player_id, 'bench') for t in effective_pokemon_types(board, p)}
            if not all(getattr(PokemonTypes, word.upper()).value in present for word in value):
                return False
        if kind == 'not_previous_attack' and value in {t.casefold() for t in titles}:
            return False
        if kind == 'previous_attack':
            subject, title = value
            if not any(
                used_title.casefold() == title and (
                    source is not None and entity_id == source.entity_id
                    if subject == 'this pokémon' else
                    getattr(def_for(archetype_id), 'display_name', '').casefold() == subject.removeprefix('your ')
                ) for entity_id, archetype_id, used_title in previous
            ):
                return False
        if kind == 'lost_zone' and len(cards(player_id, 'lostZone')) < value:
            return False
    return True


def install_attack_requirement(attack):
    if getattr(attack.condition, '_printed_requirement', False) or not requirements(attack.game_text)[0]:
        return
    original = attack.condition
    def condition(board, player_id, source):
        return printed_attack_allowed(attack.game_text, board, player_id, source) and (
            original is None or bool(original(board, player_id, source)))
    condition._printed_requirement = True
    attack.condition = condition
