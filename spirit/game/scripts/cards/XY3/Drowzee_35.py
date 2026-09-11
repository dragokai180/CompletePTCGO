from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='242a8992-2fdb-57bf-8e56-8915dd4da213',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Drowzee.Name',
    display_name='Drowzee',
    searchable_by=['Drowzee', 'Basic', 'Drowzee'],
    subtypes=['Basic'],
    collector_number=35,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=96,
    abilities=[
        Attack(
            title='Sinister Suggestion',
            game_text='Whenever your opponent flips a coin during his or her next turn, treat it as tails.',
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Psyshot',
            cost={PokemonTypes.PSYCHIC: 2},
            damage=20,
        ),
    ],
)
