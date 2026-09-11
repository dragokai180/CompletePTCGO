from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a4fc0ecf-5ec4-58d9-92ea-6a726cb2d01a',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sewaddle.Name',
    display_name='Sewaddle',
    searchable_by=['Sewaddle', 'Basic', 'Sewaddle'],
    subtypes=['Basic'],
    collector_number=7,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=540,
    abilities=[
        Ability(
            title='Swaddling Leaves',
            game_text='This Pokémon takes 10 less damage from attacks (after applying Weakness and Resistance).',
            passive=standard_passive('This Pokémon takes 10 less damage from attacks (after applying Weakness and Resistance).'),
        ),
        Attack(
            title='Surprise Attack',
            game_text='Flip a coin. If tails, this attack does nothing.',
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
