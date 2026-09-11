from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='291afc15-377f-51db-8512-9c01cdd9fb77',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Nymble.Name',
    display_name='Nymble',
    searchable_by=['Nymble', 'Basic', 'Nymble'],
    subtypes=['Basic'],
    collector_number=14,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=919,
    abilities=[
        Attack(
            title='Flop',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
