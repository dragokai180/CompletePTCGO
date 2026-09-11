from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='87f871fb-64f1-5d06-aeb0-10399c950cd6',
    key='HF',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Psyduck.Name',
    display_name='Psyduck',
    searchable_by=['Psyduck', 'Basic', 'Psyduck'],
    subtypes=['Basic'],
    collector_number=11,
    set_code='HF',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=54,
    abilities=[
        Attack(
            title='Headache',
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
    ],
)
