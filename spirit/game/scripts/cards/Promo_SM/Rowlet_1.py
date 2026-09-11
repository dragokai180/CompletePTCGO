from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='021be855-441f-53b5-86e9-ea55c93ad927',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Rowlet.Name',
    display_name='Rowlet',
    searchable_by=['Rowlet', 'Basic', 'Rowlet'],
    subtypes=['Basic'],
    collector_number=1,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=722,
    abilities=[
        Attack(
            title='Fury Attack',
            game_text='Flip 3 coins. This attack does 10 damage for each heads.',
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
