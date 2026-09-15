from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="603f202a-f24f-54de-b1dc-52d659d1e4df",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zorua.Name",
    display_name="Zorua",
    searchable_by=["Zorua","Basic","Zorua"],
    subtypes=["Basic"],
    collector_number=89,
    set_code="BW11",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    abilities=[
        Attack(
            title="Ascension",
            game_text="Search your deck for a card that evolves from this Pokémon and put it onto this Pokémon. (This counts as evolving this Pokémon.) Shuffle your deck afterward.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Scratch",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
