from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='68d47672-e023-5454-9246-f58cc5280929',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Carvanha.Name',
    display_name='Carvanha',
    searchable_by=['Carvanha', 'Basic', 'Carvanha'],
    subtypes=['Basic'],
    collector_number=46,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=318,
    abilities=[
        Attack(
            title='Sharp Fang',
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
    ],
)
