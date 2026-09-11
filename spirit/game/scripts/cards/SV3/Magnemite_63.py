from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4899d165-57bd-5d2b-9873-b6a86c9a5442',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Magnemite.Name',
    display_name='Magnemite',
    searchable_by=['Magnemite', 'Basic', 'Magnemite'],
    subtypes=['Basic'],
    collector_number=63,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=81,
    abilities=[
        Attack(
            title='Ram',
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
        ),
        Attack(
            title='Speed Ball',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
