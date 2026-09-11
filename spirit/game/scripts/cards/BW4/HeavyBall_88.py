from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = ItemCardDef(
    guid="6e193649-7d79-566c-99c8-8357c5da5d7f",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HeavyBall.Name",
    display_name="Heavy Ball",
    searchable_by=["Heavy Ball","Item","HeavyBall"],
    subtypes=["Item"],
    collector_number=88,
    set_code="BW4",
    rarity=Rarities.Uncommon,
    effect=bw_trainer_effect
)
