from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import deluge, deluge_condition, hydro_pump, powder_snow, reflect_energy

card = PokemonCardDef(
    guid="c18031e2-3ff3-5dd4-87dd-71e893b8f281",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ducklett.Name",
    display_name="Ducklett",
    searchable_by=["Ducklett","Basic","Ducklett"],
    subtypes=["Basic"],
    collector_number=35,
    set_code="BW5",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    abilities=[
        Attack(
            title="Water Pulse",
            game_text="The Defending Pokémon is now Asleep.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=powder_snow,
        ),
    ],
)
