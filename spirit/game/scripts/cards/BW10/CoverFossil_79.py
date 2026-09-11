from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.bw10 import cover_fossil

card = ItemCardDef(
    guid="e482382e-c42b-5200-bb37-ad1e96179bff",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CoverFossil.Name",
    display_name="Cover Fossil",
    searchable_by=["Cover Fossil", "Item"],
    subtypes=["Item"],
    collector_number=79,
    set_code="BW10",
    rarity=Rarities.Uncommon,
    effect=cover_fossil
)
