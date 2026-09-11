from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = ItemCardDef(
    guid="42205f50-1152-5e54-bffa-40dd6aba0712",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MaxPotion.Name",
    display_name="Max Potion",
    searchable_by=["Max Potion","Item","MaxPotion"],
    subtypes=["Item"],
    collector_number=121,
    set_code="BW9",
    rarity=Rarities.RareSecret,
    effect=bw_trainer_effect
)
