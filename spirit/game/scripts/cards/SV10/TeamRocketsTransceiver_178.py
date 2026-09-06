from spirit.game.data_utils import ItemCardDef, def_for
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import deck_nonempty
from spirit.game.session.effects import is_supporter_card


def _is_team_rocket_supporter(card) -> bool:
    if not is_supporter_card(card):
        return False
    definition = def_for(card.archetype_id)
    name = getattr(definition, "display_name", "") or ""
    return "Team Rocket" in name


card = ItemCardDef(
    guid="1934bc4e-ceb9-5b0c-a787-b53a024a3dc2",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamRocketsTransceiver.Name",
    display_name="Team Rocket's Transceiver",
    searchable_by=["Team Rocket's Transceiver", "Item", "TeamRocketsTransceiver"],
    subtypes=["Item"],
    collector_number=178,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    condition=deck_nonempty,
    effect=search_to_hand(
        _is_team_rocket_supporter, count=1, minimum=0,
        prompt="Choose a Team Rocket Supporter to put into your hand.",
    ),
)
