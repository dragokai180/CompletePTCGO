from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import deck_nonempty
from spirit.game.session.effects import is_trainer_card


card = SupporterCardDef(
    guid="27759999-a630-5eba-b663-c21c5f64ad17",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamRocketsPetrel.Name",
    display_name="Team Rocket's Petrel",
    searchable_by=["Team Rocket's Petrel", "Supporter", "TeamRocketsPetrel"],
    subtypes=["Supporter"],
    collector_number=176,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    condition=deck_nonempty,
    effect=search_to_hand(
        is_trainer_card, count=1, minimum=0,
        prompt="Choose a Trainer card to put into your hand.",
    ),
)
