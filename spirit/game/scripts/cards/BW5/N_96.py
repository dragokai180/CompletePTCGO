from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = SupporterCardDef(
    guid="247658b0-6681-579f-9276-f9b4c8afcada",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.N.Name",
    display_name="N",
    searchable_by=["N","Supporter","N"],
    subtypes=["Supporter"],
    collector_number=96,
    set_code="BW5",
    rarity=Rarities.Uncommon,
    effect=bw_trainer_effect
)
