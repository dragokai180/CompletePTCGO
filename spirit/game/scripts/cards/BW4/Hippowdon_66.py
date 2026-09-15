from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import shadow_punch, sinister_hand, sinister_hand_condition
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="ba4ef585-38a0-5e41-8351-92e2b87bf692",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hippowdon.Name",
    display_name="Hippowdon",
    searchable_by=["Hippowdon","Stage 1","Hippowdon"],
    subtypes=["Stage 1"],
    collector_number=66,
    set_code="BW4",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.LIGHTNING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Hippopotas.Name",
    abilities=[
        Attack(
            title="Sand Bazooka",
            game_text="You may move 1 Energy attached to this Pokémon to 1 of your Benched Pokémon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Rock Tumble",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=shadow_punch,
        ),
    ],
)
