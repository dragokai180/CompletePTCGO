from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = SupporterCardDef(
    guid="159594b4-73d7-5ec8-a1f4-2144c651e3cd",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CedricJuniper.Name",
    display_name="Cedric Juniper",
    searchable_by=["Cedric Juniper","Supporter","CedricJuniper"],
    subtypes=["Supporter"],
    collector_number=110,
    set_code="BW11",
    rarity=Rarities.Uncommon,
    effect=bw_trainer_effect
)
