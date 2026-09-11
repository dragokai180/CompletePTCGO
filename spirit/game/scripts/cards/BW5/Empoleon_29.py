from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_ability, bw_legacy_attack, bw_legacy_passive, bw_stadium_ability, bw_stadium_triggers, bw_tool_abilities, bw_trainer_effect, bw_trainer_passive

card = PokemonCardDef(
    guid="7fb80cb3-2500-57d9-a510-3a6895a1a8bd",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Empoleon.Name",
    display_name="Empoleon",
    searchable_by=["Empoleon","Stage 2","Empoleon"],
    subtypes=["Stage 2"],
    collector_number=29,
    set_code="BW5",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Prinplup.Name",
    abilities=[
        Ability(
            title="Diving Draw",
            game_text="Once during your turn (before your attack), you may discard 1 card from your hand. If you do, draw 2 cards.",
            activation=Activations.ONCE_PER_TURN,
            effect=bw_legacy_ability,
        ),
        Attack(
            title="Attack Command",
            game_text="Does 10 damage times the number of Pokémon in play (both yours and your opponent's).",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            damage_operator="x",
            effect=bw_legacy_attack,
        ),
    ],
)
