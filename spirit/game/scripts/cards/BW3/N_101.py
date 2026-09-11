from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = SupporterCardDef(
    guid="4a1cbb25-f185-595d-813d-edc372b9adc6",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.N.Name",
    display_name="N",
    searchable_by=["N","Supporter","N"],
    subtypes=["Supporter"],
    collector_number=101,
    set_code="BW3",
    rarity=Rarities.RareUltra,
    effect=bw_trainer_effect
)
