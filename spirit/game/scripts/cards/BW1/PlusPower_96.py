from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = ItemCardDef(
    guid="15ba7894-6949-50f2-ae3f-976e87d8615f",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PlusPower.Name",
    display_name="PlusPower",
    searchable_by=["PlusPower","Item","PlusPower"],
    subtypes=["Item"],
    collector_number=96,
    set_code="BW1",
    rarity=Rarities.Uncommon,
    effect=bw_trainer_effect
)
