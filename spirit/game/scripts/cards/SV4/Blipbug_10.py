from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='54621d73-51a8-5f47-b1ff-94559d27ab0b',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Blipbug.Name',
    display_name='Blipbug',
    searchable_by=['Blipbug', 'Basic', 'Blipbug'],
    subtypes=['Basic'],
    collector_number=10,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=824,
    abilities=[
        Attack(
            title='Surprise Attack',
            game_text='Flip a coin. If tails, this attack does nothing.',
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
