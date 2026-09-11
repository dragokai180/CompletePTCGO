from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = ItemCardDef(
    guid="b8b699ef-ee96-5095-9f64-d356f12f6016",
    key="DV",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FirstTicket.Name",
    display_name="First Ticket",
    searchable_by=["First Ticket","Item","FirstTicket"],
    subtypes=["Item"],
    collector_number=19,
    set_code="DV",
    rarity=Rarities.Common,
    effect=bw_trainer_effect,
    condition=lambda board, player_id, card=None: False,
)
