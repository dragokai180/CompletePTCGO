from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7f524633-192f-54b7-b6a6-1ff4857a8c7c',
    key='SL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bulbasaur.Name',
    display_name='Bulbasaur',
    searchable_by=['Bulbasaur', 'Basic', 'Bulbasaur'],
    subtypes=['Basic'],
    collector_number=1,
    set_code='SL',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=1,
    abilities=[
        Attack(
            title='Razor Leaf',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
