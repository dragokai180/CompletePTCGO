from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="6889a587-ae58-5528-a6a3-2cf50ece087c",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swoobat.Name",
    display_name="Swoobat",
    searchable_by=["Swoobat","Stage 1","Swoobat"],
    subtypes=["Stage 1"],
    collector_number=65,
    set_code="BW11",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Woobat.Name",
    abilities=[
        Attack(
            title="Energy Gift",
            game_text="Flip a coin. If heads, search your deck for 2 Psychic Energy cards and attach them to your Pokémon in any way you like. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Heart Stamp",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
        ),
    ],
)
