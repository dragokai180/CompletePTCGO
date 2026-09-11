from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='840e608f-c8e0-548f-8210-b6275727cbff',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Wiglett.Name',
    display_name='Wiglett',
    searchable_by=['Wiglett', 'Basic', 'Wiglett'],
    subtypes=['Basic'],
    collector_number=52,
    set_code='SV4',
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
            title='Vibration',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
