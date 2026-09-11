from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import player_has_bench, switch as switch_effect

async def play_switch(ctx):
    """Switch your Active Pokemon with 1 of your Benched Pokemon. You may play
    as many Item cards as you like during your turn (before your attack)."""
    await switch_effect(ctx)
    # Unmatched clause: "You may play as many Item cards as you like during your turn (before your attack)."

card = ItemCardDef(
    guid="fa19c4be-76cf-5e0b-a6a4-571a70c6cf1b",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Switch.Name",
    display_name="Switch",
    searchable_by=["Switch","Item","Switch"],
    subtypes=["Item"],
    collector_number=104,
    set_code="BW1",
    rarity=Rarities.Common,
    effect=play_switch,
    condition=player_has_bench
)
