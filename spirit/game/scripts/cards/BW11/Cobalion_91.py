from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import blazing_claws, dark_clamp, energy_press, return_to_six

card = PokemonCardDef(
    guid="3adc46a7-ee73-57d5-b58d-826b6efb4299",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cobalion.Name",
    display_name="Cobalion",
    searchable_by=["Cobalion","Basic","Cobalion"],
    subtypes=["Basic"],
    collector_number=91,
    set_code="BW11",
    rarity=Rarities.RareHolo,
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
