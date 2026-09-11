from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = ItemCardDef(
    guid="0637d02a-8e9a-52f7-a3b6-1cd99c680ff1",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperScoopUp.Name",
    display_name="Super Scoop Up",
    searchable_by=["Super Scoop Up","Item","SuperScoopUp"],
    subtypes=["Item"],
    collector_number=103,
    set_code="BW1",
    rarity=Rarities.Uncommon,
    effect=bw_trainer_effect
)
