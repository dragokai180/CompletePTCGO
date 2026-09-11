from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = SupporterCardDef(
    guid="e6192c06-9992-544d-b2a1-de32994d1037",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Ghetsis.Name",
    display_name="Ghetsis",
    searchable_by=["Ghetsis","Supporter","Ghetsis"],
    subtypes=["Supporter"],
    collector_number=115,
    set_code="BW9",
    rarity=Rarities.RareUltra,
    effect=bw_trainer_effect
)
