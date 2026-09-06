from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import requires_bench_space
from spirit.game.card_effects.trainers import deck_nonempty
from spirit.game.session.effects import is_basic_pokemon
from spirit.game.session.passives import effective_bench_capacity


def _precious_trolley_condition(board, player_id) -> bool:
    return deck_nonempty(board, player_id) and requires_bench_space(1)(board, player_id)


async def precious_trolley(ctx):
    """Search for any number of Basic Pokémon and put them onto your Bench."""
    space = effective_bench_capacity(ctx.board, ctx.player_id) - len(ctx.my_bench())
    if space <= 0:
        await ctx.shuffle_deck()
        return
    picks = await ctx.search_deck(
        is_basic_pokemon, count=space, minimum=0,
        prompt="Choose Basic Pokémon to put onto your Bench.",
    )
    for card in picks:
        await ctx.bench_pokemon(card)
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="4246a29d-05e4-5789-9529-e0c9110b89c9",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PreciousTrolley.Name",
    display_name="Precious Trolley",
    searchable_by=["Precious Trolley", "Item", "ACE SPEC", "PreciousTrolley"],
    subtypes=["Item", "ACE SPEC"],
    collector_number=185,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Ace,
    condition=_precious_trolley_condition,
    effect=precious_trolley,
)
