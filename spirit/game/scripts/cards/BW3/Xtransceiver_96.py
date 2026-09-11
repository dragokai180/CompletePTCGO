from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_supporter_card

async def xtransceiver(ctx):
    """Flip a coin. If heads, search your deck for a Supporter card, reveal it,
    and put it into your hand. Shuffle your deck afterward. You may play as
    many Item cards as you like during your turn (before your attack)."""
    if (await ctx.flip_coins(1, "Xtransceiver"))[0]:
        picks = await ctx.search_deck(
            is_supporter_card, count=1, minimum=0,
            prompt="Choose a Supporter card to put into your hand.",
        )
        await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()
    # Unmatched clause: "You may play as many Item cards as you like during your turn (before your attack)."

card = ItemCardDef(
    guid="366251ef-5691-5e67-bf80-4bf88b52fae6",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Xtransceiver.Name",
    display_name="Xtransceiver",
    searchable_by=["Xtransceiver","Item","Xtransceiver"],
    subtypes=["Item"],
    collector_number=96,
    set_code="BW3",
    rarity=Rarities.Uncommon,
    effect=xtransceiver
)
