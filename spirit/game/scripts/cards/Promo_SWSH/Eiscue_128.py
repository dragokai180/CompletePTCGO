from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='df85701f-4c03-5974-a16e-f96f00c7f105',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Eiscue.Name',
    display_name='Eiscue',
    searchable_by=['Eiscue', 'Basic', 'Eiscue'],
    subtypes=['Basic'],
    collector_number=128,
    set_code='Promo_SWSH',
    regulation_mark='E',
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    attributes={200790: {'type': 'string', 'value': 'SWSH128'}},
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=875,
    abilities=[
        Attack(
            title='Ice Bonus',
            game_text='Discard a Water Energy card from your hand. If you do, draw 3 cards.',
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Headbutt Bounce',
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
        ),
    ],
)
