from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='bd6f3883-b4b2-5434-944b-4e704014d9ec',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pineco.Name',
    display_name='Pineco',
    searchable_by=['Pineco', 'Basic', 'Pineco'],
    subtypes=['Basic'],
    collector_number=4,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=204,
    abilities=[
        Attack(
            title='Ram',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
