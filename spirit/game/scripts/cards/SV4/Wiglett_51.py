from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a47d6256-7384-58eb-afca-de05976aa403',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Wiglett.Name',
    display_name='Wiglett',
    searchable_by=['Wiglett', 'Basic', 'Wiglett'],
    subtypes=['Basic'],
    collector_number=51,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=960,
    abilities=[
        Attack(
            title='Fury Headbutt',
            game_text='Flip 3 coins. This attack does 10 damage for each heads.',
            cost={PokemonTypes.WATER: 1},
            damage=10,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
