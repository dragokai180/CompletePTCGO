from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6aadcbf6-b12a-57e7-96e7-fcaf000cc115',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Seedot.Name',
    display_name='Seedot',
    searchable_by=['Seedot', 'Basic', 'Seedot'],
    subtypes=['Basic'],
    collector_number=4,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=273,
    abilities=[
        Attack(
            title='Ram',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
