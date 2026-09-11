from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2e93927f-78da-5979-aa70-c778a973e1de',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tentacool.Name',
    display_name='Tentacool',
    searchable_by=['Tentacool', 'Basic', 'Tentacool'],
    subtypes=['Basic'],
    collector_number=72,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=72,
    abilities=[
        Attack(
            title='Tingle',
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
        Attack(
            title='Watering',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
