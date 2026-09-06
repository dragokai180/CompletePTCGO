from spirit.game.data_utils import StadiumCardDef, Ability, Activations
from spirit.game.attributes import Rarities


def academy_at_night_condition(board, player_id, stadium):
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and bool(hand.children)


async def academy_at_night(ctx):
    """Put a card from your hand on top of your deck."""
    hand = ctx.hand()
    if not hand:
        return
    picks = await ctx.choose_cards(
        hand, 1, minimum=1,
        prompt="Choose a card to put on top of your deck.",
    )
    if picks:
        await ctx.put_on_top_of_deck(picks[0])


card = StadiumCardDef(
    guid="c5538035-2fd0-5cdc-b85e-64955907d873",
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AcademyatNight.Name",
    display_name="Academy at Night",
    searchable_by=["Academy at Night","Stadium","AcademyatNight"],
    subtypes=["Stadium"],
    collector_number=54,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    ability=Ability(
        title="Academy at Night",
        game_text="Once during each player's turn, that player may put a card from their hand on top of their deck.",
        activation=Activations.ONCE_PER_TURN,
        effect=academy_at_night,
        condition=academy_at_night_condition,
    ),
)
