from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = ItemCardDef(
    guid="ee8f1352-2792-5a04-902a-cefd6892fc1a",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RandomReceiver.Name",
    display_name="Random Receiver",
    searchable_by=["Random Receiver","Item","RandomReceiver"],
    subtypes=["Item"],
    collector_number=138,
    set_code="BW8",
    rarity=Rarities.RareSecret,
    effect=bw_trainer_effect
)
