from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_pokemon_card


def sacred_ash_condition(board, player_id):
    discard = board.find_player_area(player_id, "discard")
    if discard is None:
        return False
    return any(is_pokemon_card(c) for c in discard.children)


async def sacred_ash(ctx):
    """Shuffle up to 5 Pokémon from your discard pile into your deck (errata)."""
    pokemon = [c for c in ctx.discard_pile() if is_pokemon_card(c)]
    if not pokemon:
        return
    picks = await ctx.choose_cards(
        pokemon, min(5, len(pokemon)), minimum=1,
        prompt="Choose up to 5 Pokémon to shuffle into your deck.",
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
