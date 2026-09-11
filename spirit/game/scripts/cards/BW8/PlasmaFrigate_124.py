from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = StadiumCardDef(
    guid="892bd555-cbe9-5221-b731-11585b08773b",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PlasmaFrigate.Name",
    display_name="Plasma Frigate",
    searchable_by=["Plasma Frigate","Stadium","PlasmaFrigate"],
    subtypes=["Stadium"],
    collector_number=124,
    set_code="BW8",
    rarity=Rarities.Uncommon,
    passive=bw_trainer_passive('Plasma Frigate'),
    ability=bw_stadium_ability('Plasma Frigate'),
    abilities=bw_stadium_triggers('Plasma Frigate')
)
