from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="bac07b27-a8de-5b7b-9f16-08f64ef53cb2",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rampardosex.Name",
    display_name="Rampardos ex",
    searchable_by=["Rampardos ex", "Stage 2", "ex", "Rampardosex"],
    subtypes=["Stage 2", "ex"],
    collector_number=45,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=330,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cranidos.Name",
    family_id=408,
    abilities=[
        Ability(
            title="Destructive Headbutting",
            game_text="Once during your turn, if this Pokémon is in the Active Spot, you may use this Ability. Flip a coin. If heads, discard an Energy from your opponent's Active Pokémon.",
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title="Rowdy Hammer",
            game_text="During your next turn, attacks used by this Pokémon do 150 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).",
            cost={PokemonTypes.FIGHTING: 2},
            damage=150,
            effect=standard_attack,
        ),
    ],
)
