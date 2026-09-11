from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import aura_of_the_land, knock_back, shadow_punch, sinister_hand, sinister_hand_condition

card = PokemonCardDef(
    guid="496416e3-c795-541d-91b1-6e668551880a",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vullaby.Name",
    display_name="Vullaby",
    searchable_by=["Vullaby","Basic","Vullaby"],
    subtypes=["Basic"],
    collector_number=73,
    set_code="BW5",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    abilities=[
        Attack(
            title="Whirlwind",
            game_text="Your opponent switches the Defending Pokémon with 1 of his or her Benched Pokémon.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
            effect=knock_back,
        ),
    ],
)
