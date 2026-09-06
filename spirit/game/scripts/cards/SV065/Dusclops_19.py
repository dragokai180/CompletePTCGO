from spirit.game.data_utils import PokemonCardDef, Ability, Attack, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def cursed_blast_5(ctx):
    """Once during your turn: place 5 damage counters, then KO yourself."""
    candidates = ctx.opponent_pokemon_in_play()
    if not candidates:
        return
    target = await ctx.choose_pokemon(candidates, "Choose a Pokémon")
    if target is None:
        return
    await ctx.place_damage_counters(5, [target])
    await ctx.knock_out(ctx.source)


card = PokemonCardDef(
    guid="c3f02fa4-c197-4521-acfe-9755bbbed11a",
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dusclops.Name",
    display_name="Dusclops",
    searchable_by=["Dusclops", "Stage 1", "Dusclops"],
    subtypes=["Stage 1"],
    collector_number=19,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Duskull.Name",
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=355,
    abilities=[
        Ability(
            title="Cursed Blast",
            game_text=(
                "Once during your turn, you may put 5 damage counters on 1 of "
                "your opponent's Pokémon. If you use this Ability, this Pokémon "
                "is Knocked Out."
            ),
            activation=Activations.ONCE_PER_TURN,
            effect=cursed_blast_5,
        ),
        Attack(
            title="Will-O-Wisp",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=50,
        ),
    ],
)

