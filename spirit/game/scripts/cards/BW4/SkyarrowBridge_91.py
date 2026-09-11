from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = StadiumCardDef(
    guid="eef9d804-c6b4-51c2-bdfa-36e5d22b410b",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SkyarrowBridge.Name",
    display_name="Skyarrow Bridge",
    searchable_by=["Skyarrow Bridge","Stadium","SkyarrowBridge"],
    subtypes=["Stadium"],
    collector_number=91,
    set_code="BW4",
    rarity=Rarities.Uncommon,
    passive=bw_trainer_passive('Skyarrow Bridge'),
    ability=bw_stadium_ability('Skyarrow Bridge'),
    abilities=bw_stadium_triggers('Skyarrow Bridge')
)
