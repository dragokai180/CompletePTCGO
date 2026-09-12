from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = SupporterCardDef(
    guid="5a2ed0ca-d5bf-55bb-aa66-5924901e2bc3",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Colress.Name",
    display_name="Colress",
    searchable_by=["Colress","Supporter","Colress","Team Plasma"],
    subtypes=["Supporter","Team Plasma"],
    collector_number=135,
    set_code="BW8",
    rarity=Rarities.RareUltra,
    effect=bw_trainer_effect
)
