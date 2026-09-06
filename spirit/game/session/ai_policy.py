"""Rule-based main-turn policy for AIPlayer.

Picks one legal action from a compute_legal_actions target_map. Prompt
targeting inside effects still uses the existing AIPlayer first-choice
defaults; this module only decides the main-phase play.
"""

from typing import Any, Dict, List, Optional, Tuple

from spirit.game.attributes import (
    AttrID,
    CLIENT_SPECIAL_CONDITION_NAMES,
    SpecialConditions,
    TrainerType,
)
from spirit.game.data_utils import ABILITIES_BY_ID, Activations
from spirit.game.models.board import PokemonEntity
from spirit.game.session.constants import SelectionKind
from spirit.game.session.legal_actions import (
    ACTION_ATTACH_TOOL,
    ACTION_EVOLVE,
    ACTION_PLAY_ENERGY,
    ACTION_PLAY_POKEMON,
    ACTION_PLAY_STADIUM,
    ACTION_RETREAT,
    ACTION_USE_ABILITY,
    ACTION_USE_ATTACK,
    ACTION_USE_TRAINER,
    energy_provided_count,
)
from spirit.game.session.passives import effective_max_hp, effective_retreat_cost

# Pause between AI main-phase plays so a human opponent can see each one.
AI_ACTION_DELAY_SECONDS = 0.8

_LOW_HP_FRACTION = 0.30

_IMMOBILIZING = {
    CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.ASLEEP],
    CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.PARALYZED],
}


def choose_action(
    session: Any, player_id: str, target_map: List[Dict[str, Any]],
) -> Optional[Tuple[Dict[str, Any], List[str]]]:
    """Pick (target_map_entry, target_ids) or None to end the turn."""
    if not target_map:
        return None

    by_desc: Dict[str, List[Dict[str, Any]]] = {}
    for entry in target_map:
        by_desc.setdefault(_description(entry), []).append(entry)

    play = by_desc.get(ACTION_PLAY_POKEMON)
    if play:
        return play[0], []

    for desc in (ACTION_EVOLVE, ACTION_PLAY_ENERGY, ACTION_ATTACH_TOOL):
        entries = by_desc.get(desc)
        if entries:
            entry = entries[0]
            return entry, _prefer_active_target(session, player_id, entry)

    stadium = by_desc.get(ACTION_PLAY_STADIUM)
    if stadium:
        return stadium[0], []

    ability = _pick_ability(
        by_desc.get(ACTION_USE_ABILITY) or [],
        has_attack=bool(by_desc.get(ACTION_USE_ATTACK)),
    )
    if ability is not None:
        return ability, []

    trainer = _pick_trainer(session, by_desc.get(ACTION_USE_TRAINER) or [])
    if trainer is not None:
        return trainer, []

    retreat = by_desc.get(ACTION_RETREAT)
    if retreat and _should_retreat(session, player_id, target_map):
        entry = retreat[0]
        return entry, _retreat_targets(session, player_id, entry)

    attacks = by_desc.get(ACTION_USE_ATTACK)
    if attacks:
        return max(attacks, key=_attack_damage), []

    return None


def _description(entry: Dict[str, Any]) -> str:
    return (entry.get("selectableAction") or {}).get("description") or ""


def _action_id(entry: Dict[str, Any]) -> str:
    return (entry.get("selectableAction") or {}).get("actionID") or ""


def _first_valid(entry: Dict[str, Any]) -> List[str]:
    infos = entry.get("targetInfoLst") or []
    if not infos:
        return []
    return list(infos[0].get("validTargets") or [])


def _prefer_active_target(session, player_id: str, entry: Dict[str, Any]) -> List[str]:
    valid = _first_valid(entry)
    if not valid:
        return []
    active = session.board_state.active_pokemon(player_id)
    if active is not None and active.entity_id in valid:
        return [active.entity_id]
    return [valid[0]]


def _pick_ability(entries: List[Dict[str, Any]], has_attack: bool) -> Optional[Dict[str, Any]]:
    for entry in entries:
        ability = ABILITIES_BY_ID.get(_action_id(entry))
        if ability is None:
            continue
        if getattr(ability, "activation", None) != Activations.ONCE_PER_TURN:
            continue
        if getattr(ability, "ends_turn", False) and has_attack:
            continue
        return entry
    return None


def _pick_trainer(session, entries: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
    items: List[Dict[str, Any]] = []
    others: List[Dict[str, Any]] = []
    for entry in entries:
        card = session.board_state.get_entity(entry.get("entityID"))
        ttype = card.get_attribute(AttrID.TRAINER_TYPE) if card is not None else None
        if ttype == TrainerType.ITEM.value:
            items.append(entry)
        else:
            others.append(entry)
    chosen = items or others
    return chosen[0] if chosen else None


def _attack_damage(entry: Dict[str, Any]) -> int:
    ability = ABILITIES_BY_ID.get(_action_id(entry))
    damage = getattr(ability, "damage", 0) or 0
    try:
        return int(damage)
    except (TypeError, ValueError):
        return 0


def _should_retreat(session, player_id: str, target_map: List[Dict[str, Any]]) -> bool:
    board = session.board_state
    active = board.active_pokemon(player_id)
    if active is None:
        return False

    opp = board.active_pokemon(session._opponent_id(player_id))
    opp_hp = opp.get_attribute(AttrID.HP, 0) if opp is not None else 0
    if any(_description(e) == ACTION_USE_ATTACK and _attack_damage(e) >= opp_hp
           for e in target_map):
        return False

    conditions = active.get_attribute(AttrID.SPECIAL_CONDITIONS) or []
    if any(c in _IMMOBILIZING for c in conditions):
        return True

    max_hp = effective_max_hp(board, active) or 1
    current = active.get_attribute(AttrID.HP, 0)
    if current / max_hp >= _LOW_HP_FRACTION:
        return False
    bench = board.find_player_area(player_id, "bench")
    if bench is None:
        return False
    return any(
        isinstance(child, PokemonEntity)
        and child.get_attribute(AttrID.HP, 0) > current
        for child in bench.children
    )


def _healthiest_id(session, entity_ids: List[str]) -> Optional[str]:
    best_id = None
    best_hp = -1
    for eid in entity_ids:
        entity = session.board_state.get_entity(eid)
        if entity is None:
            continue
        hp = entity.get_attribute(AttrID.HP, 0)
        if hp > best_hp:
            best_hp = hp
            best_id = eid
    return best_id


def _retreat_targets(session, player_id: str, entry: Dict[str, Any]) -> List[str]:
    infos = entry.get("targetInfoLst") or []
    by_kind = {info.get("name"): info for info in infos}
    bench_ids = list((by_kind.get(SelectionKind.RETREAT_NEW_ACTIVE.value) or {})
                     .get("validTargets") or [])
    energy_ids = list((by_kind.get(SelectionKind.RETREAT_COST_ENTITY_LIST.value) or {})
                      .get("validTargets") or [])

    new_active_id = _healthiest_id(session, bench_ids)
    targets = [new_active_id] if new_active_id else []

    active = session.board_state.active_pokemon(player_id)
    cost = effective_retreat_cost(session.board_state, active) if active is not None else 0
    paid = 0
    for eid in energy_ids:
        if paid >= cost:
            break
        energy = session.board_state.get_entity(eid)
        if energy is None:
            continue
        targets.append(eid)
        paid += energy_provided_count(energy, session.board_state)
    return targets
