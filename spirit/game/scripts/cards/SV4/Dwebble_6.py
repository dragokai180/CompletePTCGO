from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='250e0bd7-d390-5fda-8ba5-68530f7bb313',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dwebble.Name',
    display_name='Dwebble',
    searchable_by=['Dwebble', 'Basic', 'Dwebble'],
    subtypes=['Basic'],
    collector_number=6,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=557,
    abilities=[
        Attack(
            title='Beat',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
