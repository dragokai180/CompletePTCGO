from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = ItemCardDef(
    guid="56651494-fb94-5b38-9de7-64e8845b5336",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HypnotoxicLaser.Name",
    display_name="Hypnotoxic Laser",
    searchable_by=["Hypnotoxic Laser","Item","HypnotoxicLaser"],
    subtypes=["Item"],
    collector_number=123,
    set_code="BW8",
    rarity=Rarities.Uncommon,
    effect=bw_trainer_effect
)
