from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9019df64-108e-5f41-a333-ee0c6e7b8df6',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tarountula.Name',
    display_name='Tarountula',
    searchable_by=['Tarountula', 'Basic', 'Tarountula'],
    subtypes=['Basic'],
    collector_number=17,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=917,
    abilities=[
        Attack(
            title='Hook',
            cost={PokemonTypes.GRASS: 2},
            damage=40,
        ),
    ],
)
