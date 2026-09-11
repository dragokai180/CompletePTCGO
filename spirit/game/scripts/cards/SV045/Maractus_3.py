from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b08f5efe-0dc0-5127-a20a-c5386e4b9a92',
    key='SV045',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Maractus.Name',
    display_name='Maractus',
    searchable_by=['Maractus', 'Basic', 'Maractus'],
    subtypes=['Basic'],
    collector_number=3,
    set_code='SV045',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=556,
    abilities=[
        Attack(
            title='Double Draw',
            game_text='Draw 2 cards.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Pin Missile',
            game_text='Flip 4 coins. This attack does 30 damage for each heads.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
