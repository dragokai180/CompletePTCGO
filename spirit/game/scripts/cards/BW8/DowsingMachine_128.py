from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = ItemCardDef(
    guid="b5f85814-dbe1-5495-bcda-cdee9d7f4442",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DowsingMachine.Name",
    display_name="Dowsing Machine",
    searchable_by=["Dowsing Machine","Item","ACE SPEC","DowsingMachine"],
    subtypes=["Item","ACE SPEC"],
    collector_number=128,
    set_code="BW8",
    rarity=Rarities.Ace,
    effect=bw_trainer_effect
)
