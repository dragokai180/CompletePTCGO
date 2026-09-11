from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0ffa7d69-f0e6-57ee-a024-d3c4fd5ca21b',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Wiglett.Name',
    display_name='Wiglett',
    searchable_by=['Wiglett', 'Basic', 'Wiglett'],
    subtypes=['Basic'],
    collector_number=58,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=960,
    abilities=[
        Attack(
            title='Rain Splash',
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)
