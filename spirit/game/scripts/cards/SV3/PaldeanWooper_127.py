from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='594ef717-3852-5c53-b2c3-b8dc2c3d2816',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.PaldeanWooper.Name',
    display_name='Paldean Wooper',
    searchable_by=['Paldean Wooper', 'Basic', 'PaldeanWooper'],
    subtypes=['Basic'],
    collector_number=127,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=194,
    abilities=[
        Attack(
            title='Flop',
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
