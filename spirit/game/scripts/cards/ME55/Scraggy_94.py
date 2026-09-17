from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='91cfa735-c8ba-5e52-8d4d-b0803a3032af',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Scraggy.Name',
    display_name='Scraggy',
    searchable_by=['Scraggy', 'Basic', 'Scraggy'],
    subtypes=['Basic'],
    collector_number=94,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=559,
    abilities=[
        Attack(
            title='Nitpick',
            game_text='Your opponent shuffles their hand into their deck and draws 4 cards.',
            cost={PokemonTypes.DARKNESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Corkscrew Punch',
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
