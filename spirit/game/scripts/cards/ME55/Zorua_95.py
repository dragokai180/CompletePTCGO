from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5b2b6609-6d52-5229-8834-1ed0da955262',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Zorua.Name',
    display_name='Zorua',
    searchable_by=['Zorua', 'Basic', 'Zorua'],
    subtypes=['Basic'],
    collector_number=95,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=570,
    abilities=[
        Attack(
            title='Darkness Fang',
            cost={PokemonTypes.DARKNESS: 2},
            damage=40,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
