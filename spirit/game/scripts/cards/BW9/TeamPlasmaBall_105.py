from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = ItemCardDef(
    guid="1b3890d6-4786-5fe6-aa3e-8afc54ada2e2",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamPlasmaBall.Name",
    display_name="Team Plasma Ball",
    searchable_by=["Team Plasma Ball","Item","TeamPlasmaBall"],
    subtypes=["Item","Team Plasma"],
    collector_number=105,
    set_code="BW9",
    rarity=Rarities.Uncommon,
    effect=bw_trainer_effect
)
