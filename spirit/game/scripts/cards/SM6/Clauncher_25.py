from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c761bbfc-d665-5afd-84cb-22ba80cfcfbb',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Clauncher.Name',
    display_name='Clauncher',
    searchable_by=['Clauncher', 'Basic', 'Clauncher'],
    subtypes=['Basic'],
    collector_number=25,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=692,
    abilities=[
        Attack(
            title='Water Gun',
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)
