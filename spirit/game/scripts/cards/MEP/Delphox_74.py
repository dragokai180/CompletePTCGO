from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="6d2c6ed7-7f6f-5a1b-aebb-201fccd26f19",
    key="MEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Delphox.Name",
    display_name="Delphox",
    searchable_by=["Delphox", "Stage 2", "Delphox"],
    subtypes=["Stage 2"],
    collector_number=74,
    set_code="MEP",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Braixen.Name",
    abilities=[
        Ability(
            title="Flaring Magic",
            game_text="Once during your turn, you may discard a Basic [ [Fire] ] Energy card from your hand in order to use this Ability. Draw cards until you have 7 cards in your hand.",
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
            usable_from="hand",
        ),
        Attack(
            title="Energized Storm",
            game_text="This attack does 30 damage for each Energy attached to all Pokémon.",
            cost={PokemonTypes.FIRE: 2},
            damage=30,
            damage_operator="x",
            effect=standard_attack,
        ),
    ],
)
