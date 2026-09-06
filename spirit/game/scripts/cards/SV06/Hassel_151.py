from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import deck_nonempty


def hassel_playable(board, player_id):
    if not board.turn_state.pokemon_lost_last_turn(player_id):
        return False
    return deck_nonempty(board, player_id)


async def hassel(ctx):
    """Look at the top 8 cards; put up to 3 into your hand, then shuffle."""
    top = ctx.deck_top(8)
    if not top:
        return
    picks = await ctx.choose_cards(
        top, 3, minimum=0,
        prompt="Choose up to 3 cards to put into your hand.",
        display_cards=top,
    )
    await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()


card = SupporterCardDef(
    guid="093fdb59-34d7-5225-a339-2eccd70df382",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Hassel.Name",
    display_name="Hassel",
    searchable_by=["Hassel","Supporter","Hassel"],
    subtypes=["Supporter"],
    collector_number=151,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    effect=hassel,
    condition=hassel_playable,
)
