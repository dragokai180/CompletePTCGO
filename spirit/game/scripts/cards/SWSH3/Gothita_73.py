from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def fortunate_eye(ctx):
    """Look at the top 5 cards of your opponent's deck and put them back in
    any order."""
    await ctx.reorder_deck_top(5, player_id=ctx.opponent_id)

card = PokemonCardDef(
    guid="9de00fec-28e5-5a73-a7cd-96cffa0f78d1",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gothita.Name",
    display_name="Gothita",
    searchable_by=["Gothita", "Basic", "Gothita"],
    subtypes=["Basic"],
    collector_number=73,
    set_code="SWSH3",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=574,
    abilities=[
        Attack(
            title="Fortunate Eye",
            game_text="Look at the top 5 cards of your opponent's deck and put them back in any order.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=fortunate_eye,
        ),
        Attack(
            title="Gentle Slap",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
