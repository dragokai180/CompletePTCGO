from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b8ca6a2d-d48d-579a-a6bd-99d4521856dd',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Toedscool.Name',
    display_name='Toedscool',
    searchable_by=['Toedscool', 'Basic', 'Toedscool'],
    subtypes=['Basic'],
    collector_number=118,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=948,
    abilities=[
        Attack(
            title='Smash Kick',
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
        Attack(
            title='Mud-Slap',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
