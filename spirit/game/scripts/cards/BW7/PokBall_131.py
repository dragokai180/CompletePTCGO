from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_pokemon_card

async def poke_ball(ctx):
    """Flip a coin. If heads, search your deck for a Pokemon, reveal it, and
    put it into your hand. Shuffle your deck afterward. You may play as many
    Item cards as you like during your turn (before your attack)."""
    if (await ctx.flip_coins(1, "Poké Ball"))[0]:
        picks = await ctx.search_deck(
            is_pokemon_card, count=1, minimum=0,
            prompt="Choose a Pokémon to put into your hand.",
        )
        await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()
    # Unmatched clause: "You may play as many Item cards as you like during your turn (before your attack)."

card = ItemCardDef(
    guid="f097cce3-9f62-5b74-aa8e-cb2b53b007c0",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokBall.Name",
    display_name="Poké Ball",
    searchable_by=["Poké Ball","Item","PokBall"],
    subtypes=["Item"],
    collector_number=131,
    set_code="BW7",
    rarity=Rarities.Common,
    effect=poke_ball
)
