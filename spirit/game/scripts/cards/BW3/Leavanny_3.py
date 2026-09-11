from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import acrobatics, swift_dive
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="62b16c8a-312e-536a-b551-b3478d04b37b",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Leavanny.Name",
    display_name="Leavanny",
    searchable_by=["Leavanny","Stage 2","Leavanny"],
    subtypes=["Stage 2"],
    collector_number=3,
    set_code="BW3",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Swadloon.Name",
    abilities=[
        Ability(
            title="Leaf Tailor",
            game_text="Each of your Pokémon that has any Energy attached to it has no Weakness.",
            passive=bw_legacy_passive("Each of your Pokémon that has any Energy attached to it has no Weakness."),
        ),
        Attack(
            title="Cutting Arm",
            game_text="Flip 2 coins. This attack does 20 more damage for each heads.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=acrobatics,
        ),
    ],
)
