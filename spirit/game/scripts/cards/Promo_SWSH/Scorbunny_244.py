from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='de4d3687-827f-5fbf-9bb0-7fe3ad65fc9a',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Scorbunny.Name',
    display_name='Scorbunny',
    searchable_by=['Scorbunny', 'Basic', 'Scorbunny'],
    subtypes=['Basic'],
    collector_number=244,
    set_code='Promo_SWSH',
    regulation_mark='E',
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    attributes={200790: {'type': 'string', 'value': 'SWSH244'}},
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=813,
    abilities=[
        Attack(
            title='Flaring Dash',
            game_text='Flip a coin until you get tails. For each heads, draw a card.',
            cost={PokemonTypes.FIRE: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Flare',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)

from spirit.game.card_effects.swsh_promos import configure_promo
configure_promo(card)
