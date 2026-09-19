from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9634f93c-792a-50ab-81be-b626f6b7e216',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bulbasaur.Name',
    display_name='Bulbasaur',
    searchable_by=['Bulbasaur', 'Basic', 'Bulbasaur'],
    subtypes=['Basic'],
    collector_number=303,
    set_code='Promo_SWSH',
    regulation_mark='F',
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    attributes={200790: {'type': 'string', 'value': 'SWSH303'}},
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=1,
    abilities=[
        Attack(
            title='Shake and Gather',
            game_text='Flip a coin until you get tails. For each heads, draw a card.',
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
    ],
)

from spirit.game.card_effects.swsh_promos import configure_promo
configure_promo(card)
