from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities, AttrID
from spirit.game.card_effects.bw10 import deluge, deluge_condition, hydro_pump, powder_snow, reflect_energy

card = PokemonCardDef(
    guid="2839ce74-3f61-5a74-a6e4-17813022e91c",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ralts.Name",
    display_name="Ralts",
    searchable_by=["Ralts","Basic","Ralts"],
    subtypes=["Basic"],
    # Original client slots 116..140 hold Radiant Collection RC1..RC25.
    collector_number=123,
    attributes={AttrID.CARD_NUMBER_TEXT.value: {"type": "string", "value": "RC8"}},
    set_code="BW11",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    abilities=[
        Attack(
            title="Hypnotic Gaze",
            game_text="The Defending Pokémon is now Asleep.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=powder_snow,
        ),
        Attack(
            title="Pound",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
