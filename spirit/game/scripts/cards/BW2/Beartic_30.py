from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_ability, bw_legacy_attack, bw_legacy_passive, bw_stadium_ability, bw_stadium_triggers, bw_tool_abilities, bw_trainer_effect, bw_trainer_passive
from spirit.game.card_effects.bw10 import blazing_claws, dark_clamp, energy_press, return_to_six, shadow_punch, sinister_hand, sinister_hand_condition

card = PokemonCardDef(
    guid="d2e81213-884a-5faf-869c-f299128fe61b",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beartic.Name",
    display_name="Beartic",
    searchable_by=["Beartic","Stage 1","Beartic"],
    subtypes=["Stage 1"],
    collector_number=30,
    set_code="BW2",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cubchoo.Name",
    abilities=[
        Attack(
            title="Sheer Cold",
            game_text="The Defending Pokémon can't attack during your opponent's next turn.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=dark_clamp,
        ),
        Attack(
            title="Icicle Crash",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=shadow_punch,
        ),
    ],
)
