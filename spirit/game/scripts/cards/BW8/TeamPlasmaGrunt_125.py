from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = SupporterCardDef(
    guid="2c39126b-92c3-5ab9-96a0-55801cdea99b",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamPlasmaGrunt.Name",
    display_name="Team Plasma Grunt",
    searchable_by=["Team Plasma Grunt","Supporter","TeamPlasmaGrunt"],
    subtypes=["Supporter","Team Plasma"],
    collector_number=125,
    set_code="BW8",
    rarity=Rarities.Uncommon,
    effect=bw_trainer_effect
)
