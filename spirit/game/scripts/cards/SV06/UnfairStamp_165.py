from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import shuffle_hand_into_deck_draw


def _unfair_stamp_condition(board, player_id, card=None) -> bool:
    return bool(board.turn_state.pokemon_lost_last_turn(player_id))


card = ItemCardDef(
    guid="dddc7f9b-b389-4ca0-9d00-1c36e4474e31",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UnfairStamp.Name",
    display_name="Unfair Stamp",
    searchable_by=["Unfair Stamp", "Item", "ACE SPEC", "UnfairStamp"],
    subtypes=["Item", "ACE SPEC"],
    collector_number=165,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Ace,
    condition=_unfair_stamp_condition,
    effect=shuffle_hand_into_deck_draw(5, opponent_n=2),
)

