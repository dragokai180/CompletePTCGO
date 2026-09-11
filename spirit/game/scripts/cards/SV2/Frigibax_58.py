from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f51d184a-97f8-5a64-a908-78f2354b5e14',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Frigibax.Name',
    display_name='Frigibax',
    searchable_by=['Frigibax', 'Basic', 'Frigibax'],
    subtypes=['Basic'],
    collector_number=58,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=996,
    abilities=[
        Attack(
            title='Chilly',
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
        Attack(
            title='Bite',
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
