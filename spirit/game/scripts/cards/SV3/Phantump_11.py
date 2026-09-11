from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c8e997be-7067-5aa3-8cc1-889824a9ce90',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Phantump.Name',
    display_name='Phantump',
    searchable_by=['Phantump', 'Basic', 'Phantump'],
    subtypes=['Basic'],
    collector_number=11,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=708,
    abilities=[
        Attack(
            title='Branch Poke',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
