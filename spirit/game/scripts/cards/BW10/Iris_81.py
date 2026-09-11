from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.bw10 import iris

card = SupporterCardDef(
    guid="6c18a227-5400-5a2d-b108-4713a501d512",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Iris.Name",
    display_name="Iris",
    searchable_by=["Iris", "Supporter"],
    subtypes=["Supporter"],
    collector_number=81,
    set_code="BW10",
    rarity=Rarities.Uncommon,
    effect=iris
)
