from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="b85c6e68-45bb-5ac4-baaf-e4c12894f08f",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Palpitoad.Name",
    display_name="Palpitoad",
    searchable_by=["Palpitoad","Stage 1","Palpitoad"],
    subtypes=["Stage 1"],
    collector_number=41,
    set_code="BW11",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tympole.Name",
    abilities=[
        Attack(
            title="Mud Shot",
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
        Attack(
            title="Round",
            game_text="Does 20 damage times the number of your Pokémon that have the Round attack.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            damage_operator="x",
            effect=bw_legacy_attack,
        ),
    ],
)
