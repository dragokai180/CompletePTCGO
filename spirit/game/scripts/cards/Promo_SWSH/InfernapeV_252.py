from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='65810524-b583-5519-8680-05ff26bff3b6',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.InfernapeV.Name',
    display_name='Infernape V',
    searchable_by=['Infernape V', 'Basic', 'V', 'InfernapeV'],
    subtypes=['Basic', 'V'],
    collector_number=252,
    set_code='Promo_SWSH',
    regulation_mark='F',
    rarity=Rarities.RarePromo,
    hp=200,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    attributes={200790: {'type': 'string', 'value': 'SWSH252'}},
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=392,
    abilities=[
        Attack(
            title='Meteor Punch',
            game_text='Flip a coin until you get tails. This attack does 30 damage for each heads.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Bright Flame',
            game_text='Discard 2 Energy from this Pokémon.',
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=standard_attack,
        ),
    ],
)
