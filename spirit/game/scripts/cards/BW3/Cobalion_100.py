from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import blazing_claws, dark_clamp, energy_press, return_to_six

card = PokemonCardDef(
    guid="a689caad-6c2a-581d-bba5-5c54e027176f",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cobalion.Name",
    display_name="Cobalion",
    searchable_by=["Cobalion","Basic","Cobalion"],
    subtypes=["Basic"],
    collector_number=100,
    set_code="BW3",
    rarity=Rarities.RareUltra,
    hp=120,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    abilities=[
        Attack(
            title="Energy Press",
            game_text="Does 20 more damage for each Energy attached to the Defending Pokémon.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=energy_press,
        ),
        Attack(
            title="Iron Breaker",
            game_text="The Defending Pokémon can't attack during your opponent's next turn.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=dark_clamp,
        ),
    ],
)
