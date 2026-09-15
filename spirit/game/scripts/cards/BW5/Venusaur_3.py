from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_ability, bw_legacy_attack, bw_legacy_passive, bw_stadium_ability, bw_stadium_triggers, bw_tool_abilities, bw_trainer_effect, bw_trainer_passive
from spirit.game.card_effects.bw10 import shadow_punch, sinister_hand, sinister_hand_condition

card = PokemonCardDef(
    guid="acb34ee7-0325-5cc7-bef9-3afb2ac4a890",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Venusaur.Name",
    display_name="Venusaur",
    searchable_by=["Venusaur","Stage 2","Venusaur"],
    subtypes=["Stage 2"],
    collector_number=3,
    set_code="BW5",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ivysaur.Name",
    abilities=[
        Ability(
            title="Floral Fragrance",
            game_text="Once during your turn (before your attack), you may search your deck for a Pokémon, reveal it, and put it into your hand. Shuffle your deck afterward.",
            activation=Activations.ONCE_PER_TURN,
            effect=bw_legacy_ability,
        ),
        Attack(
            title="Poison Powder",
            game_text="The Defending Pokémon is now Poisoned.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=bw_legacy_attack,
        ),
    ],
)
