from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='28af70d8-f49e-56f7-b8e2-043f939c3711',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Darumaka.Name',
    display_name='Darumaka',
    searchable_by=['Darumaka', 'Basic', 'Darumaka'],
    subtypes=['Basic'],
    collector_number=34,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=554,
    abilities=[
        Attack(
            title='Headbutt',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title='Surprise Attack',
            game_text='Flip a coin. If tails, this attack does nothing.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=standard_attack,
        ),
    ],
)
