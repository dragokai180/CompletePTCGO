from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = SupporterCardDef(
    guid="ba47b87e-6a16-59ac-8381-7dcd97bf7c94",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Ghetsis.Name",
    display_name="Ghetsis",
    searchable_by=["Ghetsis","Supporter","Ghetsis","Team Plasma"],
    subtypes=["Supporter","Team Plasma"],
    collector_number=101,
    set_code="BW9",
    rarity=Rarities.RareHolo,
    effect=bw_trainer_effect
)
