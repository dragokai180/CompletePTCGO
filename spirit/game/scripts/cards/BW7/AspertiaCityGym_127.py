from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = StadiumCardDef(
    guid="325e1feb-7c9c-53cc-bb9a-290e604ea12c",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AspertiaCityGym.Name",
    display_name="Aspertia City Gym",
    searchable_by=["Aspertia City Gym","Stadium","AspertiaCityGym"],
    subtypes=["Stadium"],
    collector_number=127,
    set_code="BW7",
    rarity=Rarities.Uncommon,
    passive=bw_trainer_passive('Aspertia City Gym'),
    ability=bw_stadium_ability('Aspertia City Gym'),
    abilities=bw_stadium_triggers('Aspertia City Gym')
)
