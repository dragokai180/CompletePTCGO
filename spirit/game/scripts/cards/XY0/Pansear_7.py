from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e69822d0-2a61-5da3-9f1d-6450f8c57fc0',
    key='XY0',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pansear.Name',
    display_name='Pansear',
    searchable_by=['Pansear', 'Basic', 'Pansear'],
    subtypes=['Basic'],
    collector_number=7,
    set_code='XY0',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=513,
    abilities=[
        Attack(
            title='Collect',
            game_text='Draw a card.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Fury Swipes',
            game_text='Flip 3 coins. This attack does 10 damage times the number of heads.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
