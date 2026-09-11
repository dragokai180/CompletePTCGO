from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='dd942474-d313-59c9-960d-81d0136fa6f1',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Seel.Name',
    display_name='Seel',
    searchable_by=['Seel', 'Basic', 'Seel'],
    subtypes=['Basic'],
    collector_number=86,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=86,
    abilities=[
        Attack(
            title='Chilly',
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
    ],
)
