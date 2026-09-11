from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = ItemCardDef(
    guid="9db709ce-a606-5210-9ce4-1f99b8591184",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperiorEnergyRetrieval.Name",
    display_name="Superior Energy Retrieval",
    searchable_by=["Superior Energy Retrieval","Item","SuperiorEnergyRetrieval"],
    subtypes=["Item"],
    collector_number=103,
    set_code="BW9",
    rarity=Rarities.Uncommon,
    effect=bw_trainer_effect
)
