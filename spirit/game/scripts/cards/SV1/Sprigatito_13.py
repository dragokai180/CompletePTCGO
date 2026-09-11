from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='30347dc0-c90f-5fb3-901c-215d619e7bd3',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sprigatito.Name',
    display_name='Sprigatito',
    searchable_by=['Sprigatito', 'Basic', 'Sprigatito'],
    subtypes=['Basic'],
    collector_number=13,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=906,
    abilities=[
        Attack(
            title='Scratch',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title='Leafage',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
