from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import aura_of_the_land, knock_back, shadow_punch, sinister_hand, sinister_hand_condition

card = PokemonCardDef(
    guid="989505f8-ca0b-54dc-a8c7-f4d19cfd545e",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Deino.Name",
    display_name="Deino",
    searchable_by=["Deino","Basic","Deino"],
    subtypes=["Basic"],
    collector_number=75,
    set_code="BW9",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    abilities=[
        Attack(
            title="Push Down",
            game_text="Your opponent switches the Defending Pokémon with 1 of his or her Benched Pokémon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=knock_back,
        ),
        Attack(
            title="Bite",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
