from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='61192e43-549f-5165-bd0c-b46a2a0000b5',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Clauncher.Name',
    display_name='Clauncher',
    searchable_by=['Clauncher', 'Basic', 'Clauncher'],
    subtypes=['Basic'],
    collector_number=33,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=692,
    abilities=[
        Attack(
            title='Double Pincers',
            game_text='Flip 2 coins. This attack does 10 damage times the number of heads.',
            cost={PokemonTypes.WATER: 1},
            damage=10,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
