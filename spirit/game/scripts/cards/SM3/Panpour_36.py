from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d7befe04-82f9-514b-b576-5a92fde9e7aa',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Panpour.Name',
    display_name='Panpour',
    searchable_by=['Panpour', 'Basic', 'Panpour'],
    subtypes=['Basic'],
    collector_number=36,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=515,
    abilities=[
        Attack(
            title='Water Gun',
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)
