from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_pokemon_card

async def victory_cup(ctx):
    """Flip a coin. If heads, search your deck for a Pokemon, reveal it, and
    put it into your hand. Shuffle your deck afterward. You may play as many
    Item cards as you like during your turn (before your attack)."""
    if (await ctx.flip_coins(1, "Victory Cup"))[0]:
        picks = await ctx.search_deck(
            is_pokemon_card, count=1, minimum=0,
            prompt="Choose a Pokémon to put into your hand.",
        )
        await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()
    # Unmatched clause: "You may play as many Item cards as you like during your turn (before your attack)."

card = ItemCardDef(
    guid="cca8d164-4e24-5053-bd85-d712ecf4d3cb",
    key="PROMO_BW",
    name="com.direwolfdigital.cake.data.archetypes.trainer.VictoryCup.Name",
    display_name="Victory Cup",
    searchable_by=["Victory Cup","Item","VictoryCup"],
    subtypes=["Item"],
    collector_number=31,
    set_code="PROMO_BW",
    rarity=Rarities.RarePromo,
    effect=victory_cup
)
