from spirit.game.data_utils import StadiumCardDef, Ability, Activations
from spirit.game.attributes import AttrID, PokemonTypes, Rarities
from spirit.game.card_effects.trainers import player_has_bench


def _is_water(pokemon):
    types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
    return PokemonTypes.WATER.value in types


def surfing_beach_condition(board, player_id, stadium=None):
    if not player_has_bench(board, player_id):
        return False
    active = board.active_pokemon(player_id)
    if active is None or not _is_water(active):
        return False
    bench = board.find_player_area(player_id, "bench")
    return bool(bench) and any(_is_water(p) for p in bench.children)


async def surfing_beach(ctx):
    """Switch your Active Water Pokémon with 1 of your Benched Water Pokémon."""
    bench = [p for p in ctx.my_bench() if _is_water(p)]
    if not bench:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose a Benched Water Pokémon to switch into the Active Spot"
    )
    if target is not None:
        await ctx.switch_active(ctx.player_id, target)


SURFING_BEACH_ABILITY = Ability(
    title="Surfing Beach",
    game_text="Once during each player's turn, that player may switch their Active Water Pokémon with 1 of their Benched Water Pokémon.",
    activation=Activations.ONCE_PER_TURN,
    effect=surfing_beach,
    condition=surfing_beach_condition,
)


card = StadiumCardDef(
    guid="8ab8254b-5e01-51e5-83a7-737d9bb93f66",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SurfingBeach.Name",
    display_name="Surfing Beach",
    searchable_by=["Surfing Beach","Stadium","SurfingBeach"],
    subtypes=["Stadium"],
    collector_number=129,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    ability=SURFING_BEACH_ABILITY,
)
