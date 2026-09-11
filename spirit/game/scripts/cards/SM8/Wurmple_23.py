from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='22b27a66-2119-5f5f-b1a6-13058bb4ab80',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Wurmple.Name',
    display_name='Wurmple',
    searchable_by=['Wurmple', 'Basic', 'Wurmple'],
    subtypes=['Basic'],
    collector_number=23,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=265,
    abilities=[
        Attack(
            title='Ram',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
