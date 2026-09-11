from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c1eb99c9-b0d7-51d6-ac70-1c7c96520c11',
    key='XY12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Ponyta.Name',
    display_name='Ponyta',
    searchable_by=['Ponyta', 'Basic', 'Ponyta'],
    subtypes=['Basic'],
    collector_number=19,
    set_code='XY12',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=77,
    abilities=[
        Attack(
            title='Smash Kick',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title='Flame Tail',
            cost={PokemonTypes.FIRE: 2},
            damage=30,
        ),
    ],
)
