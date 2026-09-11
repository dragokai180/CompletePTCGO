from spirit.game.card_effects.trainers import has_discard_cost, ultra_ball
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="ae2d787c-a34f-502a-8453-0c0a9fa9fe13",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UltraBall.Name",
    display_name="Ultra Ball",
    searchable_by=["Ultra Ball", "Item"],
    subtypes=["Item"],
    collector_number=150,
    set_code="SWSH9",
    rarity=Rarities.Uncommon,
    effect=ultra_ball,
    condition=has_discard_cost(2)
)
