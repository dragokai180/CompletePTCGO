from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='27725213-5b5a-54a3-bb00-1290c9a78c44',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Finneon.Name',
    display_name='Finneon',
    searchable_by=['Finneon', 'Basic', 'Finneon'],
    subtypes=['Basic'],
    collector_number=18,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=456,
    abilities=[
        Attack(
            title='Pound',
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)
