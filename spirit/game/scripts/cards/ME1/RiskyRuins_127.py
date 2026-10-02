from spirit.game.data_utils import StadiumCardDef, Ability, Triggers
from spirit.game.attributes import AttrID, PokemonTypes, Rarities
from spirit.game.session.effects import is_basic_pokemon


async def risky_ruins_watch(ctx):
    """Whenever any player puts a Basic non-Darkness Pokémon onto their Bench
    during their turn, place 2 damage counters on that Pokémon."""
    pokemon = ctx.benched_pokemon
    if pokemon is None or not is_basic_pokemon(pokemon):
        return
    if ctx.session.turn_state.active_player_id != ctx.benching_player_id:
        return
    types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
    if PokemonTypes.DARKNESS.value in types:
        return
    await ctx.deal_damage(20, target=pokemon, apply_modifiers=False,
                          as_counters=True)


card = StadiumCardDef(
    guid="34f2d480-4d64-528e-a379-c5728742136c",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RiskyRuins.Name",
    display_name="Risky Ruins",
    searchable_by=["Risky Ruins","Stadium","RiskyRuins"],
    subtypes=["Stadium"],
    collector_number=127,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    abilities=[
        Ability(
            title="Risky Ruins",
            game_text="Whenever any player puts a Basic non-Darkness Pokémon onto their Bench during their turn, place 2 damage counters on that Pokémon.",
            trigger=Triggers.ON_POKEMON_BENCHED,
            effect=risky_ruins_watch,
        ),
    ],
)
