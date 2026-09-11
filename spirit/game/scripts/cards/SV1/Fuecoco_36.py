from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5d74fe19-125f-5fc4-a38d-889d117df56e',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Fuecoco.Name',
    display_name='Fuecoco',
    searchable_by=['Fuecoco', 'Basic', 'Fuecoco'],
    subtypes=['Basic'],
    collector_number=36,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=909,
    abilities=[
        Attack(
            title='Gnaw',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title='Combustion',
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
