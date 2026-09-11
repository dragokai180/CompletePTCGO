from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities

async def calculate(ctx):
    """Look at the top 4 cards of your deck and put them back on top of your
    deck in any order."""
    await ctx.reorder_deck_top(4)



card = PokemonCardDef(
    guid="11cca9f3-29ea-5187-932e-1386669eb05b",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beldum.Name",
    display_name="Beldum",
    searchable_by=["Beldum","Basic","Beldum"],
    subtypes=["Basic"],
    collector_number=50,
    set_code="BW9",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    abilities=[
        Attack(
            title="Calculate",
            game_text="Look at the top 4 cards of your deck and put them back on top of your deck in any order.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=calculate,
        ),
        Attack(
            title="Psypunch",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
