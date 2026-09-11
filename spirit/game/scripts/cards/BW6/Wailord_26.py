from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="ef191cce-68f1-520c-9164-5f48e2ede195",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wailord.Name",
    display_name="Wailord",
    searchable_by=["Wailord","Stage 1","Wailord"],
    subtypes=["Stage 1"],
    collector_number=26,
    set_code="BW6",
    rarity=Rarities.RareHolo,
    hp=200,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wailmer.Name",
    abilities=[
        Attack(
            title="Water Cannon",
            game_text="Flip a coin. If heads, this attack does 30 damage times the amount of Water Energy attached to this Pokémon.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            damage_operator="x",
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Giant Wave",
            game_text="This Pokémon can't use Giant Wave during your next turn.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=bw_legacy_attack,
        ),
    ],
)
