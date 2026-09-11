from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import destructive_beam

card = PokemonCardDef(
    guid="f8043476-e986-576a-9e65-d9f17407a56b",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Trapinch.Name",
    display_name="Trapinch",
    searchable_by=["Trapinch","Basic","Trapinch"],
    subtypes=["Basic"],
    collector_number=83,
    set_code="BW7",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.LIGHTNING,
    abilities=[
        Attack(
            title="Smithereen Smash",
            game_text="Flip a coin. If heads, discard an Energy attached to the Defending Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=destructive_beam,
        ),
        Attack(
            title="Bite",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
