"""Nest Ball (SM - Sun & Moon 123/149).

  "Search your deck for a Basic Pokemon and put it onto your Bench. Then,
   shuffle your deck."

Battle VIP Pass without the first-turn gate and for one Pokemon instead of
two. One difference on purpose: the space check reads
effective_bench_capacity rather than the flat BENCH_CAPACITY constant, so it
respects a Bench that Sky Field widened to 8 or Sudowoodo or Parallel City
narrowed. bench_pokemon() enforces the real capacity anyway, so the check is
about not offering a search whose result would silently fail to land.

The name uses the client's own key, which for this card carries no set
segment (...archetypes.trainercards.nestball.name) -- a third shape
alongside the ...trainer.<Name>.Name and <set>.trainercards.<name>_<set>_<n>
forms other cards here use.
"""

from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_basic_pokemon
from spirit.game.session.passives import effective_bench_capacity


async def nest_ball(ctx):
    """Search the deck for a Basic and bench it, then shuffle."""
    bench = ctx.board.find_player_area(ctx.player_id, "bench")
    space = (effective_bench_capacity(ctx.board, ctx.player_id)
             - len(bench.children)) if bench else 0
    if space <= 0:
        return
    picks = await ctx.search_deck(
        is_basic_pokemon, count=1, minimum=0,
        prompt="Choose a Basic Pokémon to put onto your Bench.",
    )
    for card in picks:
        await ctx.bench_pokemon(card)
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="2fb45df5-1462-5682-b672-8d8f943fcaa9",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.trainercards.nestball.name",
    display_name="Nest Ball",
    searchable_by=["Nest Ball", "Item", "NestBall"],
    subtypes=["Item"],
    collector_number=123,
    set_code="SM1",
    rarity=Rarities.Uncommon,
    effect=nest_ball,
)
