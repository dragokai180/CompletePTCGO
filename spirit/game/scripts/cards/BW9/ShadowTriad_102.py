from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = SupporterCardDef(
    guid="459ba560-5f1b-5e37-8d5f-10648eb33d5d",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ShadowTriad.Name",
    display_name="Shadow Triad",
    searchable_by=["Shadow Triad","Supporter","ShadowTriad","Team Plasma"],
    subtypes=["Supporter","Team Plasma"],
    collector_number=102,
    set_code="BW9",
    rarity=Rarities.Uncommon,
    effect=bw_trainer_effect
)
