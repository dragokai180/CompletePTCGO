from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d4794fdf-7eb6-5f8a-b701-2d6c77e3b88c',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cetoddle.Name',
    display_name='Cetoddle',
    searchable_by=['Cetoddle', 'Basic', 'Cetoddle'],
    subtypes=['Basic'],
    collector_number=59,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=974,
    abilities=[
        Attack(
            title='Icicle',
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
        Attack(
            title='Sharp Fin',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)
