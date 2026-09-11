from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = SupporterCardDef(
    guid="a5fe7301-9ce8-5306-9878-561618f00324",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Cilan.Name",
    display_name="Cilan",
    searchable_by=["Cilan","Supporter","Cilan"],
    subtypes=["Supporter"],
    collector_number=86,
    set_code="BW4",
    rarity=Rarities.Uncommon,
    effect=bw_trainer_effect
)
