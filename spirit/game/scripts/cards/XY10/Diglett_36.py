from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3dd5ee6a-8dac-5174-9443-792070ca37f8',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Diglett.Name',
    display_name='Diglett',
    searchable_by=['Diglett', 'Basic', 'Diglett'],
    subtypes=['Basic'],
    collector_number=36,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=50,
    abilities=[
        Attack(
            title='Ram',
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
    ],
)
