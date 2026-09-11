from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="2a927def-f2f1-5099-b7e7-882686349d68",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Purrloin.Name",
    display_name="Purrloin",
    searchable_by=["Purrloin","Basic","Purrloin"],
    subtypes=["Basic"],
    collector_number=90,
    set_code="BW7",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    abilities=[
        Attack(
            title="Captivate",
            game_text="Flip a coin. If heads, switch 1 of your opponent's Benched Pokémon with the Defending Pokémon.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=bw_legacy_attack,
        ),
    ],
)
