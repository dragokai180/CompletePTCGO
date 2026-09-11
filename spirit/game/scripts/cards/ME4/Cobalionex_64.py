from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="d691a8ee-7fe7-53e9-8afd-2daa184d3635",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cobalionex.Name",
    display_name="Cobalion ex",
    searchable_by=["Cobalion ex", "Basic", "ex", "Cobalionex"],
    subtypes=["Basic", "ex"],
    collector_number=64,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=210,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=638,
    abilities=[
        Ability(
            title="Metal Road",
            game_text="Once during your turn, when this Pokémon moves from your Bench to the Active Spot, you may use this Ability. Move any amount of Metal Energy from your other Pokémon to this Pokémon.",
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title="Power Tackle",
            game_text="During your next turn, this Pokémon can't use attacks.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=standard_attack,
            locks_next_turn=True,
        ),
    ],
)
