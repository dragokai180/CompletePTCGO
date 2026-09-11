from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6caf3e64-c24f-57a2-9f21-c878cd5f2171',
    key='XY0',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Panpour.Name',
    display_name='Panpour',
    searchable_by=['Panpour', 'Basic', 'Panpour'],
    subtypes=['Basic'],
    collector_number=11,
    set_code='XY0',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=515,
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
