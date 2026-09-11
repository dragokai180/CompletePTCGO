from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = ItemCardDef(
    guid="05396c65-9f46-518e-a9db-9173574366f0",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TownMap.Name",
    display_name="Town Map",
    searchable_by=["Town Map","Item","TownMap"],
    subtypes=["Item"],
    collector_number=136,
    set_code="BW7",
    rarity=Rarities.Uncommon,
    effect=bw_trainer_effect
)
