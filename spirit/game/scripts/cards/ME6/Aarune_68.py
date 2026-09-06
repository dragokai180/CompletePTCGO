from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import AttrID, Rarities, TrainerType
from spirit.game.session.effects import is_supporter_card
from spirit.game.card_effects.support_common import search_to_hand


def _is_supporter_or_stadium(card):
    return is_supporter_card(card) or (
        card.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.STADIUM.value
    )


card = SupporterCardDef(
    guid="69904817-5d7e-507b-8a41-0ffbef16c203",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Aarune.Name",
    display_name="Aarune",
    searchable_by=["Aarune","Supporter","Aarune"],
    subtypes=["Supporter"],
    collector_number=68,
    set_code="ME6",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(
        _is_supporter_or_stadium, count=3, reveal=True,
        prompt="Choose up to 3 Supporter and Stadium cards.",
    ),
)
