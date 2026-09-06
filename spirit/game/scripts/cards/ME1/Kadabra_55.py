from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities


async def psychic_draw(ctx):
    """Once during your turn, when you play this Pokémon from your hand to
    evolve 1 of your Pokémon, you may use this Ability. Draw 2 cards."""
    if await ctx.ask_yes_no("Draw 2 cards?"):
        await ctx.draw_cards(2)

card = PokemonCardDef(
    guid="5d429cb0-be48-55c0-8965-718e53057b83",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kadabra.Name",
    display_name="Kadabra",
    searchable_by=["Kadabra","Stage 1","Kadabra"],
    subtypes=["Stage 1"],
    collector_number=55,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Abra.Name",
    family_id=63,
    abilities=[
        Ability(
            title="Psychic Draw",
            game_text="Once during your turn, when you play this Pokémon from your hand to evolve 1 of your Pokémon, you may use this Ability. Draw 2 cards.",
            trigger=Triggers.ON_EVOLVE,
            effect=psychic_draw,
        ),
        Attack(
            title="Super Psy Bolt",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
        ),
    ],
)
