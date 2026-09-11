from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='53e74a02-d486-5695-b878-5bc233fc0741',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Shellder.Name',
    display_name='Shellder',
    searchable_by=['Shellder', 'Basic', 'Shellder'],
    subtypes=['Basic'],
    collector_number=33,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=90,
    abilities=[
        Attack(
            title='Tackle',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
