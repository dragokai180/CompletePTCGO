from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8d5a2c34-80f0-5aa6-b7c1-5b016e9109b6',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Corphish.Name',
    display_name='Corphish',
    searchable_by=['Corphish', 'Basic', 'Corphish'],
    subtypes=['Basic'],
    collector_number=24,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=341,
    abilities=[
        Attack(
            title='Crabhammer',
            cost={PokemonTypes.WATER: 2},
            damage=30,
        ),
    ],
)
