"""Lysandre {*} (SM - Forbidden Light 110/131).

Supporter, Prism Star.

  "For each of your Fire Pokemon in play, put a card from your opponent's
   discard pile in the Lost Zone."

Unrelated to Boss's Orders despite sharing a character: this is its own
card name, so it is deliberately NOT in rules.EXCLUSIVE_NAME_GROUPS, and
the display name it carries -- "Lysandre {*}", the client's Prism Star
convention -- keeps it clear of the plain "Lysandre" that group names. A
deck may hold this alongside 4 Boss's Orders, or alongside 4 Lysandre.

The count is my Fire Pokemon in play, including the Active and anything
evolved. Girafarig (SM8 94) does the same thing for a flat 2, so the move
itself lives in lost_zone_from_opponent_discard, which takes either a
number or a callable.

The Prism Star rules themselves need nothing here: is_prism_star reads
the subtype, discard_area_name already routes this card to the Lost Zone
when it is played, and rules.py already caps it at 1 per name in a deck.
"""

from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities, PokemonTypes
from spirit.game.card_effects.support_common import lost_zone_from_opponent_discard
from spirit.game.session.effects import is_pokemon_of_type


def _my_fire_count(ctx) -> int:
    return sum(1 for p in ctx.my_pokemon_in_play()
               if is_pokemon_of_type(p, PokemonTypes.FIRE))


def _fire_in_play(board, player_id) -> bool:
    return any(is_pokemon_of_type(p, PokemonTypes.FIRE)
               for p in board.pokemon_in_play(player_id))


def _lysandre_condition(board, player_id) -> bool:
    opponent = next((p for p in board.player_ids if p != player_id), None)
    if opponent is None or not _fire_in_play(board, player_id):
        return False
    discard = board.find_player_area(opponent, "discard")
    return bool(discard and discard.children)


lysandre_prism_star = lost_zone_from_opponent_discard(_my_fire_count)


card = SupporterCardDef(
    guid="89bf6e51-6769-5f5b-b1b4-f0aec5c9ea0c",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LysandrePrismStar.Name",
    display_name="Lysandre {*}",
    searchable_by=["Lysandre", "Supporter", "Prism Star"],
    subtypes=["Supporter", "Prism Star"],
    collector_number=110,
    set_code="SM6",
    rarity=Rarities.Prism,
    effect=lysandre_prism_star,
    condition=_lysandre_condition,
)
