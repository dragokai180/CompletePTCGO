from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = ItemCardDef(
    guid="ad0ea3bd-0688-5e4b-9262-ba4ee3a0d232",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ColressMachine.Name",
    display_name="Colress Machine",
    searchable_by=["Colress Machine","Item","ColressMachine"],
    subtypes=["Item"],
    collector_number=119,
    set_code="BW8",
    rarity=Rarities.Uncommon,
    effect=bw_trainer_effect
)
