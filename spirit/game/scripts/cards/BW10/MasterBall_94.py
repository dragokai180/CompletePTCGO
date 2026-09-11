from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.bw10 import master_ball

card = ItemCardDef(
    guid="c44dca6a-27da-56f3-89bc-3e49607496ea",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MasterBall.Name",
    display_name="Master Ball",
    searchable_by=["Master Ball", "Item", "ACE SPEC"],
    subtypes=["Item", "ACE SPEC"],
    collector_number=94,
    set_code="BW10",
    rarity=Rarities.Ace,
    effect=master_ball
)
