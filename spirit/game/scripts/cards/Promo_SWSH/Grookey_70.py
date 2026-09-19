from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c7400e1a-c911-51f2-bbf9-bc7b6dab7c5c',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Grookey.Name',
    display_name='Grookey',
    searchable_by=['Grookey', 'Basic', 'Grookey'],
    subtypes=['Basic'],
    collector_number=70,
    set_code='Promo_SWSH',
    regulation_mark='D',
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    attributes={200790: {'type': 'string', 'value': 'SWSH070'}},
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=810,
    abilities=[
        Attack(
            title='Full On',
            game_text='Flip a coin. If tails, this attack does nothing.',
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
