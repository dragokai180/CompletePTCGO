from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5f2a0a76-d83a-5c7f-8f5f-d2ed5b935185',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Drilbur.Name',
    display_name='Drilbur',
    searchable_by=['Drilbur', 'Basic', 'Drilbur'],
    subtypes=['Basic'],
    collector_number=89,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=529,
    abilities=[
        Attack(
            title='Fury Swipes',
            game_text='Flip 3 coins. This attack does 10 damage times the number of heads.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
