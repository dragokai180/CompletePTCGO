from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5009d595-d4b0-5d2b-8cbe-8f85447cc50a',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name',
    display_name='Eevee',
    searchable_by=['Eevee', 'Basic', 'Eevee'],
    subtypes=['Basic'],
    collector_number=95,
    set_code='Promo_SWSH',
    regulation_mark='D',
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    attributes={200790: {'type': 'string', 'value': 'SWSH095'}},
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=133,
    abilities=[
        Attack(
            title='First Step',
            game_text='Draw a card.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Tail Whap',
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
        ),
    ],
)
