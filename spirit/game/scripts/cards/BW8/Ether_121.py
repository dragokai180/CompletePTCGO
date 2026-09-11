from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = ItemCardDef(
    guid="6473890b-a3b0-5b3b-9d93-1a3e49321e7f",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Ether.Name",
    display_name="Ether",
    searchable_by=["Ether","Item","Ether"],
    subtypes=["Item"],
    collector_number=121,
    set_code="BW8",
    rarity=Rarities.Uncommon,
    effect=bw_trainer_effect
)
