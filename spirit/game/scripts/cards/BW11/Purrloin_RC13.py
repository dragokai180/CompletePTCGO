from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="5275a0d4-ba4d-5bd5-9317-a865f7936c86",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Purrloin.Name",
    display_name="Purrloin",
    searchable_by=["Purrloin","Basic","Purrloin"],
    subtypes=["Basic"],
    collector_number=13,
    set_code="BW11",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    abilities=[
        Attack(
            title="Captivate",
            game_text="Flip a coin. If heads, switch 1 of your opponent's Benched Pokémon with the Defending Pokémon.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=bw_legacy_attack,
        ),
    ],
)
