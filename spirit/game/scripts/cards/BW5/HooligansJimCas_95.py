from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = SupporterCardDef(
    guid="95b4b0c5-f29c-58a8-947b-27f88890b72a",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HooligansJimCas.Name",
    display_name="Hooligans Jim & Cas",
    searchable_by=["Hooligans Jim & Cas","Supporter","HooligansJimCas"],
    subtypes=["Supporter"],
    collector_number=95,
    set_code="BW5",
    rarity=Rarities.Uncommon,
    effect=bw_trainer_effect
)
