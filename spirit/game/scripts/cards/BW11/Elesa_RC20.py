from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities, AttrID
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = SupporterCardDef(
    guid="15aac43c-a084-596e-b0ec-0c846f138b1d",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Elesa.Name",
    display_name="Elesa",
    searchable_by=["Elesa","Supporter","Elesa"],
    subtypes=["Supporter"],
    # Original client slots 116..140 hold Radiant Collection RC1..RC25.
    collector_number=135,
    attributes={AttrID.CARD_NUMBER_TEXT.value: {"type": "string", "value": "RC20"}},
    set_code="BW11",
    rarity=Rarities.Common,
    effect=bw_trainer_effect
)
