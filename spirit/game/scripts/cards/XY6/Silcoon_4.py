from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='28bba2f8-138d-5455-a1a7-19ebad3fef00',
    key='XY6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Silcoon.Name',
    display_name='Silcoon',
    searchable_by=['Silcoon', 'Stage 1', 'Silcoon'],
    subtypes=['Stage 1'],
    collector_number=4,
    set_code='XY6',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Wurmple.Name',
    family_id=265,
    abilities=[
        Attack(
            title='String Shot',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
