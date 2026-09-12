from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = StadiumCardDef(
    guid="b676ca51-b6cf-5d9f-8b1e-45a89cb027d4",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FrozenCity.Name",
    display_name="Frozen City",
    searchable_by=["Frozen City","Stadium","FrozenCity","Team Plasma"],
    subtypes=["Stadium","Team Plasma"],
    collector_number=100,
    set_code="BW9",
    rarity=Rarities.Uncommon,
    passive=bw_trainer_passive('Frozen City'),
    ability=bw_stadium_ability('Frozen City'),
    abilities=bw_stadium_triggers('Frozen City')
)
