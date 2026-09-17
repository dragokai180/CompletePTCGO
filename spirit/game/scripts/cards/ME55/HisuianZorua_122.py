from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4abe813f-6d9c-5677-bad3-4ab9d2aa4e77',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.HisuianZorua.Name',
    display_name='Hisuian Zorua',
    searchable_by=['Hisuian Zorua', 'Basic', 'HisuianZorua'],
    subtypes=['Basic'],
    collector_number=122,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=570,
    abilities=[
        Attack(
            title='Scratch',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
