from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import opponent_prizes_low


async def special_red_card(ctx):
    """Your opponent shuffles their hand and puts it on the bottom of their
    deck. If they put any cards on the bottom of their deck in this way, they
    draw 3 cards."""
    moved = await ctx.hand_to_bottom_of_deck(ctx.opponent_id)
    if moved > 0:
        await ctx.draw_cards(3, player_id=ctx.opponent_id)


card = ItemCardDef(
    guid="4e8d59dd-a91a-5f93-8a84-542bdc58d6a7",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SpecialRedCard.Name",
    display_name="Special Red Card",
    searchable_by=["Special Red Card","Item","SpecialRedCard"],
    subtypes=["Item"],
    collector_number=82,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    effect=special_red_card,
    condition=opponent_prizes_low,
)
