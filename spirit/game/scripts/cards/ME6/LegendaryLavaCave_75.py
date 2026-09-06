from spirit.game.data_utils import StadiumCardDef, def_for
from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import ability_lock_passive
from spirit.game.session.effects import is_evolution_pokemon

DISPLAY_NAME = "Legendary Lava Cave"


def _partner(board, player_id, card):
    """The other printing of Legendary Lava Cave in hand, if any."""
    hand = board.find_player_area(player_id, "hand")
    for other in (hand.children if hand else []):
        if other.entity_id == card.entity_id:
            continue
        if other.archetype_id == card.archetype_id:
            continue
        definition = def_for(other.archetype_id)
        if getattr(definition, "display_name", None) == DISPLAY_NAME:
            return other
    return None


def _playable(board, player_id, card):
    """Needs a different printing of Legendary Lava Cave in hand."""
    return _partner(board, player_id, card) is not None


card = StadiumCardDef(
    guid="07dffeea-b3ef-5904-a741-44e83dcecad6",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LegendaryLavaCave.Name",
    display_name=DISPLAY_NAME,
    searchable_by=["Legendary Lava Cave","Stadium","LegendaryLavaCave"],
    subtypes=["Stadium"],
    collector_number=75,
    set_code="ME6",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    condition=_playable,
    companion=_partner,
    passive=ability_lock_passive(lambda p, c: is_evolution_pokemon(p)),
)
