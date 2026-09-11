from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='15ddb116-7f8a-5c63-9a73-80465b07093c',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Vanillite.Name',
    display_name='Vanillite',
    searchable_by=['Vanillite', 'Basic', 'Vanillite'],
    subtypes=['Basic'],
    collector_number=43,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=582,
    abilities=[
        Attack(
            title='Chilly',
            cost={PokemonTypes.WATER: 2},
            damage=40,
        ),
    ],
)
