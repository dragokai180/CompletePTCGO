from spirit.game.card_effects.support_common import requires_hand
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.bw10 import caitlin

card = SupporterCardDef(
    guid="0c2cf89d-b106-56ad-b7d6-aa9d046b34ae",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Caitlin.Name",
    display_name="Caitlin",
    searchable_by=["Caitlin", "Supporter"],
    subtypes=["Supporter"],
    collector_number=78,
    set_code="BW10",
    rarity=Rarities.Uncommon,
    condition=requires_hand(),
    effect=caitlin
)
