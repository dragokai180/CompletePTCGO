from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import (
    heal_item,
    requires_damaged_active_with_energy,
)

card = ItemCardDef(
    guid="bf3c425b-900f-5db2-a666-62d98e1e4b1e",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.JumboIceCream.Name",
    display_name="Jumbo Ice Cream",
    searchable_by=["Jumbo Ice Cream", "Item", "JumboIceCream"],
    subtypes=["Item"],
    collector_number=91,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    effect=heal_item(80, scope="active"),
    condition=requires_damaged_active_with_energy(3),
)
