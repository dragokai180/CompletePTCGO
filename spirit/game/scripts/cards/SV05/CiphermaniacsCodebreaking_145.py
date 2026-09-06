from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities


async def ciphermaniacs_codebreaking(ctx):
    """Search your deck for 2 cards, shuffle, then put those cards on top
    in any order (first pick = new top)."""
    deck_cards = list(ctx.deck())
    picks = await ctx.choose_cards(
        deck_cards, 2, minimum=2, ordered=True,
        prompt="Choose 2 cards to put on top of your deck, in order.",
        display_cards=deck_cards,
    )
    await ctx.shuffle_deck()
    for card in reversed(picks):
        await ctx.put_on_top_of_deck(card)


def _deck_has_two(board, player_id):
    deck = board.find_player_area(player_id, "deck")
    return bool(deck) and len(deck.children) >= 2


card = SupporterCardDef(
    guid="b0efc669-e8cb-5f04-a80c-b7f107ab8e26",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CiphermaniacsCodebreaking.Name",
    display_name="Ciphermaniac's Codebreaking",
    searchable_by=["Ciphermaniac's Codebreaking", "Supporter", "CiphermaniacsCodebreaking"],
    subtypes=["Supporter"],
    collector_number=145,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    effect=ciphermaniacs_codebreaking,
    condition=_deck_has_two,
)
