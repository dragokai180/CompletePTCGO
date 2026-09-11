from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import heal_item, requires_damaged_pokemon

async def potion(ctx):
    """Heal 30 damage from 1 of your Pokemon. You may play as many Item cards
    as you like during your turn (before your attack)."""
    await heal_item(30)(ctx)
    # Unmatched clause: "You may play as many Item cards as you like during your turn (before your attack)."

card = ItemCardDef(
    guid="7b1ba5c0-a429-58d1-87d7-b5d09a7548cd",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Potion.Name",
    display_name="Potion",
    searchable_by=["Potion","Item","Potion"],
    subtypes=["Item"],
    collector_number=132,
    set_code="BW7",
    rarity=Rarities.Common,
    effect=potion,
    condition=requires_damaged_pokemon()
)
