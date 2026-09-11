from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='70c9d4f8-452e-55ff-b998-d0c7ab0ef321',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Skrelp.Name',
    display_name='Skrelp',
    searchable_by=['Skrelp', 'Basic', 'Skrelp'],
    subtypes=['Basic'],
    collector_number=52,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=690,
    abilities=[
        Attack(
            title='Hook',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)
