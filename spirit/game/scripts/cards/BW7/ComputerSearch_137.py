from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = ItemCardDef(
    guid="f827aa15-b0c6-58a2-8fcb-21f1ccff73ac",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ComputerSearch.Name",
    display_name="Computer Search",
    searchable_by=["Computer Search","Item","ACE SPEC","ComputerSearch"],
    subtypes=["Item","ACE SPEC"],
    collector_number=137,
    set_code="BW7",
    rarity=Rarities.Ace,
    effect=bw_trainer_effect
)
