from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import deluge, deluge_condition, hydro_pump, powder_snow, reflect_energy

card = PokemonCardDef(
    guid="408c31b6-2d08-5bd9-b828-e3187abe3037",
    key="DV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dratini.Name",
    display_name="Dratini",
    searchable_by=["Dratini","Basic","Dratini"],
    subtypes=["Basic"],
    collector_number=2,
    set_code="DV",
    rarity=Rarities.RareHolo,
    hp=40,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DRAGON,
    abilities=[
        Attack(
            title="Hypnotic Gaze",
            game_text="The Defending Pokémon is now Asleep.",
            cost={PokemonTypes.GRASS: 1},
            effect=powder_snow,
        ),
        Attack(
            title="Tail Whap",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
        ),
    ],
)
