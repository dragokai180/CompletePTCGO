from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import deluge, deluge_condition, hydro_pump, powder_snow, reflect_energy

card = PokemonCardDef(
    guid="ba1586d8-1226-54c7-9bf3-3a604f0eb75a",
    key="PROMO_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meloetta.Name",
    display_name="Meloetta",
    searchable_by=["Meloetta","Basic","Meloetta"],
    subtypes=["Basic"],
    collector_number=68,
    set_code="PROMO_BW",
    rarity=Rarities.RarePromo,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    abilities=[
        Attack(
            title="Sing",
            game_text="The Defending Pokémon is now Asleep.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=powder_snow,
        ),
        Attack(
            title="Psyburn",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)
