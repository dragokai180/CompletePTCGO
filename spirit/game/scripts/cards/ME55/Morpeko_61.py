from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c1afc124-3d7a-5f64-8874-dd02475e9244',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Morpeko.Name',
    display_name='Morpeko',
    searchable_by=['Morpeko', 'Basic', 'Morpeko'],
    subtypes=['Basic'],
    collector_number=61,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=877,
    abilities=[
        Attack(
            title='Select a Snack',
            game_text='Discard the top 3 cards of your deck and put 1 of them into your hand.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Slap',
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
