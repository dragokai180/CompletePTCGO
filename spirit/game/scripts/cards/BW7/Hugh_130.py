from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = SupporterCardDef(
    guid="e65008f5-1b43-5b61-b244-d159baf7db68",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Hugh.Name",
    display_name="Hugh",
    searchable_by=["Hugh","Supporter","Hugh"],
    subtypes=["Supporter"],
    collector_number=130,
    set_code="BW7",
    rarity=Rarities.Uncommon,
    effect=bw_trainer_effect
)
