from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack, flip_damage
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="d406af99-4832-5040-8262-b6ee1344db1f",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Whimsicott.Name",
    display_name="Whimsicott",
    searchable_by=["Whimsicott","Stage 1","Whimsicott"],
    subtypes=["Stage 1"],
    collector_number=15,
    set_code="BW7",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cottonee.Name",
    abilities=[
        Attack(
            title="Fluffy Tag",
            game_text="Switch this Pokémon with 1 of your Benched Pokémon. During your next turn, the attacks of that Pokémon do 40 more damage to the Active Pokémon (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Stun Spore",
            game_text="Flip a coin. If heads, the Defending Pokémon is now Paralyzed.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)
