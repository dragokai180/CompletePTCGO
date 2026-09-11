from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2eec1c0d-b4a8-5251-9c41-0c20f0d073fd',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Snorunt.Name',
    display_name='Snorunt',
    searchable_by=['Snorunt', 'Basic', 'Snorunt'],
    subtypes=['Basic'],
    collector_number=31,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=361,
    abilities=[
        Attack(
            title='Chilly',
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
        Attack(
            title='Frost Breath',
            cost={PokemonTypes.WATER: 2},
            damage=20,
        ),
    ],
)
