from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = ItemCardDef(
    guid="055cc694-65da-5959-b0ea-53552a6d602c",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RandomReceiver.Name",
    display_name="Random Receiver",
    searchable_by=["Random Receiver","Item","RandomReceiver"],
    subtypes=["Item"],
    collector_number=99,
    set_code="BW5",
    rarity=Rarities.Uncommon,
    effect=bw_trainer_effect
)
