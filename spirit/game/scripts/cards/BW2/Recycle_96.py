from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = ItemCardDef(
    guid="08517d71-90c7-5629-b4b2-7d3db1763e53",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Recycle.Name",
    display_name="Recycle",
    searchable_by=["Recycle","Item","Recycle"],
    subtypes=["Item"],
    collector_number=96,
    set_code="BW2",
    rarity=Rarities.Uncommon,
    effect=bw_trainer_effect
)
