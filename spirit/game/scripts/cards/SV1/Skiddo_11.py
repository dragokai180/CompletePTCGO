from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5dc1bf5f-df8c-5297-9e44-ace78fa79e48',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Skiddo.Name',
    display_name='Skiddo',
    searchable_by=['Skiddo', 'Basic', 'Skiddo'],
    subtypes=['Basic'],
    collector_number=11,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=672,
    abilities=[
        Attack(
            title='Vine Whip',
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
        Attack(
            title='Smash Kick',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
