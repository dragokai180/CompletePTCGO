from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='aa3e2c53-e367-5685-8e2f-51c5f1cda887',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Fuecoco.Name',
    display_name='Fuecoco',
    searchable_by=['Fuecoco', 'Basic', 'Fuecoco'],
    subtypes=['Basic'],
    collector_number=23,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=909,
    abilities=[
        Attack(
            title='Live Coal',
            cost={PokemonTypes.FIRE: 1},
            damage=10,
        ),
        Attack(
            title='Ram',
            cost={PokemonTypes.FIRE: 2},
            damage=30,
        ),
    ],
)
