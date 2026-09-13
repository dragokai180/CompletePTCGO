"""Public-information gates for conditional Trainer draw effects."""
from spirit.game.card_effects.support_common import draw_until_condition
from spirit.game.card_effects.trainers import deck_nonempty, _other_player, _bench_pokemon
from spirit.game.data_utils import def_for, is_pokemon_v


def _cynthia_limit(board, player_id):
    state = getattr(board, "turn_state", None)
    return 8 if state and state.pokemon_lost_last_turn(player_id) else 5


def _ariana_limit(board, player_id):
    pokemon = board.pokemon_in_play(player_id)
    return 8 if pokemon and all(
        (getattr(def_for(p.archetype_id), "display_name", "") or "").startswith("Team Rocket's ")
        for p in pokemon
    ) else 5


cynthias_ambition_condition = draw_until_condition(_cynthia_limit)
ariana_condition = draw_until_condition(_ariana_limit)


def honey_condition(board, player_id):
    opponent = _other_player(board, player_id)
    return bool(opponent) and deck_nonempty(board, player_id) and any(
        is_pokemon_v(p.archetype_id)
        for p in _bench_pokemon(board, opponent)
    )
