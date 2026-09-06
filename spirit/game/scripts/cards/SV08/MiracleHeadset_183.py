from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.card_effects.trainers import has_supporter_in_discard
from spirit.game.session.effects import is_supporter_card

card = ItemCardDef(
    guid="263e498a-542f-57ed-9fe5-193be15d1b63",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MiracleHeadset.Name",
    display_name="Miracle Headset",
    searchable_by=["Miracle Headset","Item","ACE SPEC","MiracleHeadset"],
    subtypes=["Item","ACE SPEC"],
    collector_number=183,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Ace,
    effect=recover_from_discard(
        is_supporter_card, count=2, minimum=0, reveal=False, to="hand",
        prompt="Choose up to 2 Supporter cards to put into your hand.",
    ),
    condition=has_supporter_in_discard,
)
