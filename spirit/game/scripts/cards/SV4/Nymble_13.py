from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e29a5d09-68a4-5860-8c0f-e661dc3f7b50',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Nymble.Name',
    display_name='Nymble',
    searchable_by=['Nymble', 'Basic', 'Nymble'],
    subtypes=['Basic'],
    collector_number=13,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=919,
    abilities=[
        Attack(
            title='Gnaw',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
