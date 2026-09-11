from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2582889f-cceb-59f5-8124-db5d4f8de025',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Drifloon.Name',
    display_name='Drifloon',
    searchable_by=['Drifloon', 'Basic', 'Drifloon'],
    subtypes=['Basic'],
    collector_number=80,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=425,
    abilities=[
        Attack(
            title='Ram',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
