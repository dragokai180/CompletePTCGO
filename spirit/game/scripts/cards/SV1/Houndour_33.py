from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d8df2430-b25d-5c8f-ade8-b0ef0f09b570',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Houndour.Name',
    display_name='Houndour',
    searchable_by=['Houndour', 'Basic', 'Houndour'],
    subtypes=['Basic'],
    collector_number=33,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=228,
    abilities=[
        Attack(
            title='Bite',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title='Flare',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
