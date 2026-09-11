from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import draw_until_effect

async def bicycle(ctx):
    """Draw cards until you have 4 cards in your hand. You may play as many
    Item cards as you like during your turn (before your attack)."""
    await draw_until_effect(4)(ctx)
    # Unmatched clause: "You may play as many Item cards as you like during your turn (before your attack)."

card = ItemCardDef(
    guid="729aa283-a8d0-54cf-b685-2ae687ca2562",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Bicycle.Name",
    display_name="Bicycle",
    searchable_by=["Bicycle","Item","Bicycle"],
    subtypes=["Item"],
    collector_number=117,
    set_code="BW8",
    rarity=Rarities.Uncommon,
    effect=bicycle
)
