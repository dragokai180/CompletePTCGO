from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c24d3fd2-a5ac-5116-8d08-938df178710c',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanMeowth.Name',
    display_name='Alolan Meowth',
    searchable_by=['Alolan Meowth', 'Basic', 'AlolanMeowth'],
    subtypes=['Basic'],
    collector_number=78,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=52,
    abilities=[
        Attack(
            title='Fury Swipes',
            game_text='Flip 3 coins. This attack does 10 damage for each heads.',
            cost={},
            damage=10,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
