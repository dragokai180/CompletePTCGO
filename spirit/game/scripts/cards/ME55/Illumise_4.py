from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='864f2490-0231-5373-8c73-de4a9cf470f3',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Illumise.Name',
    display_name='Illumise',
    searchable_by=['Illumise', 'Basic', 'Illumise'],
    subtypes=['Basic'],
    collector_number=4,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=314,
    abilities=[
        Ability(
            title='Supereffective Pheromones',
            game_text='If you have Volbeat in play, apply Weakness for both Active Pokémon as x3',
            passive=standard_passive('If you have Volbeat in play, apply Weakness for both Active Pokémon as x3'),
        ),
        Attack(
            title='Ram',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
