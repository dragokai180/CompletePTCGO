from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = ItemCardDef(
    guid="6a490558-dc70-5aa3-80ea-a2f3747a9725",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Pokdex.Name",
    display_name="Pokédex",
    searchable_by=["Pokédex","Item","Pokdex"],
    subtypes=["Item"],
    collector_number=98,
    set_code="BW1",
    rarity=Rarities.Uncommon,
    effect=bw_trainer_effect
)
