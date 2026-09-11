from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='65f85e12-a07d-5e24-b7ac-69c859138ba1',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Zigzagoon.Name',
    display_name='Zigzagoon',
    searchable_by=['Zigzagoon', 'Basic', 'Zigzagoon'],
    subtypes=['Basic'],
    collector_number=167,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=263,
    abilities=[
        Attack(
            title='Headbutt Bounce',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title='Claw Slash',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
