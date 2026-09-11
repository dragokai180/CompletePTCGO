from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = StadiumCardDef(
    guid="05a72a5d-eebf-5d02-b466-482575223882",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.VirbankCityGym.Name",
    display_name="Virbank City Gym",
    searchable_by=["Virbank City Gym","Stadium","VirbankCityGym"],
    subtypes=["Stadium"],
    collector_number=126,
    set_code="BW8",
    rarity=Rarities.Uncommon,
    passive=bw_trainer_passive('Virbank City Gym'),
    ability=bw_stadium_ability('Virbank City Gym'),
    abilities=bw_stadium_triggers('Virbank City Gym')
)
