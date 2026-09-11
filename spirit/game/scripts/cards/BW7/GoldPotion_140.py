from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import heal_item, requires_damaged_pokemon

async def gold_potion(ctx):
    """Heal 90 damage from your Active Pokemon. You may play as many Item cards
    as you like during your turn (before your attack)."""
    await heal_item(90, scope="active")(ctx)
    # Unmatched clause: "You may play as many Item cards as you like during your turn (before your attack)."

card = ItemCardDef(
    guid="361a42e7-0c15-53e1-828d-f278212fe518",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GoldPotion.Name",
    display_name="Gold Potion",
    searchable_by=["Gold Potion","Item","ACE SPEC","GoldPotion"],
    subtypes=["Item","ACE SPEC"],
    collector_number=140,
    set_code="BW7",
    rarity=Rarities.Ace,
    effect=gold_potion,
    condition=requires_damaged_pokemon()
)
