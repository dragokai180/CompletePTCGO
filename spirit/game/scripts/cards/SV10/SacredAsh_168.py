from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_pokemon_card


def sacred_ash_condition(board, player_id):
    discard = board.find_player_area(player_id, "discard")
    if discard is None:
        return False
    return sum(1 for c in discard.children if is_pokemon_card(c)) >= 5


async def sacred_ash(ctx):
    """Shuffle 5 Pokémon from your discard pile into your deck."""
    pokemon = [c for c in ctx.discard_pile() if is_pokemon_card(c)]
    if len(pokemon) < 5:
        return
    picks = await ctx.choose_cards(
        pokemon, 5, minimum=5,
        prompt="Choose 5 Pokémon to shuffle into your deck.",
    )
    if picks:
        await ctx.shuffle_into_deck(picks)


card = ItemCardDef(
    guid="a4f32df7-7b7b-5e3e-af04-cec52991e47d",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SacredAsh.Name",
    display_name="Sacred Ash",
    searchable_by=["Sacred Ash", "Item", "SacredAsh"],
    subtypes=["Item"],
    collector_number=168,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    condition=sacred_ash_condition,
    effect=sacred_ash,
)
