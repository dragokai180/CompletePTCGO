from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='443e96e8-6f76-5122-93ad-ad7b3f6be423',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pineco.Name',
    display_name='Pineco',
    searchable_by=['Pineco', 'Basic', 'Pineco'],
    subtypes=['Basic'],
    collector_number=4,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=204,
    abilities=[
        Attack(
            title='Rollout',
            cost={PokemonTypes.GRASS: 2},
            damage=30,
        ),
    ],
)
