from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='641f3590-575f-54d1-8359-96c56bb0d295',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Fennekin.Name',
    display_name='Fennekin',
    searchable_by=['Fennekin', 'Basic', 'Fennekin'],
    subtypes=['Basic'],
    collector_number=25,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=653,
    abilities=[
        Attack(
            title='Firebreathing',
            game_text='Flip a coin. If heads, this attack does 30 more damage.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
