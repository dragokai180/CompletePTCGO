from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6fb33170-b187-5a53-b3d2-11f22e6f3241',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Shellos.Name',
    display_name='Shellos',
    searchable_by=['Shellos', 'Basic', 'Shellos'],
    subtypes=['Basic'],
    collector_number=28,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=422,
    abilities=[
        Attack(
            title='Rain Splash',
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)
