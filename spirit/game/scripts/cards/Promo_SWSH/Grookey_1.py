from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d1e391bf-cd0d-5256-b74d-4a85f1fe3edb',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Grookey.Name',
    display_name='Grookey',
    searchable_by=['Grookey', 'Basic', 'Grookey'],
    subtypes=['Basic'],
    collector_number=1,
    set_code='Promo_SWSH',
    regulation_mark='D',
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    attributes={200790: {'type': 'string', 'value': 'SWSH001'}},
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=810,
    abilities=[
        Attack(
            title='Branch Poke',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
