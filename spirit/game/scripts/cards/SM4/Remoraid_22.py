from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3a1b7945-ae56-51b0-8e5f-5b11d9d0ae0a',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Remoraid.Name',
    display_name='Remoraid',
    searchable_by=['Remoraid', 'Basic', 'Remoraid'],
    subtypes=['Basic'],
    collector_number=22,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=223,
    abilities=[
        Attack(
            title='Water Gun',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
