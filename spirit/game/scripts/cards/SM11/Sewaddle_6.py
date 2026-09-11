from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4ed4bf35-aa40-593f-aadb-3270031625f5',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sewaddle.Name',
    display_name='Sewaddle',
    searchable_by=['Sewaddle', 'Basic', 'Sewaddle'],
    subtypes=['Basic'],
    collector_number=6,
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
        Attack(
            title='Multiply',
            game_text='Search your deck for up to 2 Sewaddle and put them onto your Bench. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Gnaw',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
