from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1774b992-0ae5-54e4-99c7-45ab6e1e3a1d',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Rowlet.Name',
    display_name='Rowlet',
    searchable_by=['Rowlet', 'Basic', 'Rowlet'],
    subtypes=['Basic'],
    collector_number=13,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=722,
    abilities=[
        Attack(
            title='Razor Wing',
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
    ],
)
