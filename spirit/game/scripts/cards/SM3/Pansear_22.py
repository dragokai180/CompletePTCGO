from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d0c5e583-974e-56ac-bd36-bf900b63b306',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pansear.Name',
    display_name='Pansear',
    searchable_by=['Pansear', 'Basic', 'Pansear'],
    subtypes=['Basic'],
    collector_number=22,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=513,
    abilities=[
        Attack(
            title='Flare',
            cost={PokemonTypes.FIRE: 1},
            damage=10,
        ),
    ],
)
