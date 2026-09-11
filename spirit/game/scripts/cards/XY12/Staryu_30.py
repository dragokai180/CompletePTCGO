from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f212b19f-cabc-5490-8c2c-710456ea46f6',
    key='XY12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Staryu.Name',
    display_name='Staryu',
    searchable_by=['Staryu', 'Basic', 'Staryu'],
    subtypes=['Basic'],
    collector_number=30,
    set_code='XY12',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=120,
    abilities=[
        Attack(
            title='Quick Blow',
            game_text='Flip a coin. If heads, this attack does 10 more damage.',
            cost={PokemonTypes.WATER: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
