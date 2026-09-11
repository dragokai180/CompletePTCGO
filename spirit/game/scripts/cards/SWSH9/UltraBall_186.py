from spirit.game.card_effects.trainers import has_discard_cost, ultra_ball
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="fb774725-4a88-5dd0-888d-b53a1488c226",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UltraBall.Name",
    display_name="Ultra Ball",
    searchable_by=["Ultra Ball", "Item"],
    subtypes=["Item"],
    collector_number=186,
    set_code="SWSH9",
    rarity=Rarities.RareSecret,
    effect=ultra_ball,
    condition=has_discard_cost(2)
)
