from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = ItemCardDef(
    guid="cd12e318-73dd-53d2-ad1f-0b39c092ff6a",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Revive.Name",
    display_name="Revive",
    searchable_by=["Revive","Item","Revive"],
    subtypes=["Item"],
    collector_number=102,
    set_code="BW1",
    rarity=Rarities.Uncommon,
    effect=bw_trainer_effect
)
