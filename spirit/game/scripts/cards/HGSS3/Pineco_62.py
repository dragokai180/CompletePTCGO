from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2c69790c-f498-57e0-8136-6f66310d9db8',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pineco.Name',
    display_name='Pineco',
    searchable_by=['Pineco', 'Basic', 'Pineco'],
    subtypes=['Basic'],
    collector_number=62,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=204,
    abilities=[
        Attack(
            title='Rollout',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
