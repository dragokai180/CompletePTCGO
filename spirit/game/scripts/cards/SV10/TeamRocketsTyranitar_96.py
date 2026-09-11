from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="452d4aa6-8b9c-5dd8-877e-877550c43266",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsTyranitar.Name",
    display_name="Team Rocket's Tyranitar",
    searchable_by=["Team Rocket's Tyranitar", "Stage 2", "TeamRocketsTyranitar"],
    subtypes=["Stage 2"],
    collector_number=96,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsPupitar.Name",
    family_id=246,
    abilities=[
        Ability(
            title="Sand Stream",
            game_text="During Pokémon Checkup, if this Pokémon is in the Active Spot, put 2 damage counters on each of your opponent's Basic Pokémon.",
            effect=standard_ability,
            trigger=Triggers.BETWEEN_TURNS,
        ),
        Attack(
            title="Demolition Tackle",
            game_text="Discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=180,
            effect=standard_attack,
        ),
    ],
)
