from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5808ee84-fa44-5321-928d-2248803e3cf9',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Wailmer.Name',
    display_name='Wailmer',
    searchable_by=['Wailmer', 'Basic', 'Wailmer'],
    subtypes=['Basic'],
    collector_number=29,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=320,
    abilities=[
        Attack(
            title='Splash',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title='Surf',
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)
