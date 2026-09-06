from spirit.game.data_utils import StadiumCardDef, def_for
from spirit.game.attributes import Rarities
from spirit.game.session.passives import Passive

DISPLAY_NAME = "Legendary Ocean Trench"


def _partner(board, player_id, card):
    """The other printing of Legendary Ocean Trench in hand, if any."""
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
    """Needs a different printing of Legendary Ocean Trench in hand."""
    return _partner(board, player_id, card) is not None


class LegendaryOceanTrenchPassive(Passive):
    """Whenever any player's Pokemon is healed, double the amount healed."""

    stacking_key = "LegendaryOceanTrench"

    def heal_multiplier(self, target, carrier):
        return 2


card = StadiumCardDef(
    guid="c9dcb65c-3f28-5948-b7f8-2847eb84aade",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LegendaryOceanTrench.Name",
    display_name=DISPLAY_NAME,
    searchable_by=["Legendary Ocean Trench", "Stadium", "LegendaryOceanTrench"],
    subtypes=["Stadium"],
    collector_number=71,
    set_code="ME6",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    condition=_playable,
    companion=_partner,
    passive=LegendaryOceanTrenchPassive(),
)
