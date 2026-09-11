from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import creepy_wind, wind_blast

card = PokemonCardDef(
    guid="796d6606-2d03-5fad-8224-bd294a46853c",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Yamask.Name",
    display_name="Yamask",
    searchable_by=["Yamask","Basic","Yamask"],
    subtypes=["Basic"],
    collector_number=44,
    set_code="BW3",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    abilities=[
        Attack(
            title="Perplex",
            game_text="Flip a coin. If heads, the Defending Pokémon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            effect=creepy_wind,
        ),
    ],
)
