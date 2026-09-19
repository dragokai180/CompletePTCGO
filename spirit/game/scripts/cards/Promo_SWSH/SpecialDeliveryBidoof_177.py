from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='16da5676-8364-527e-8bfd-21a3e56f8565',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.SpecialDeliveryBidoof.Name',
    display_name='Special Delivery Bidoof',
    searchable_by=['Special Delivery Bidoof', 'Basic', 'SpecialDeliveryBidoof'],
    subtypes=['Basic'],
    collector_number=177,
    set_code='Promo_SWSH',
    regulation_mark='E',
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    attributes={200790: {'type': 'string', 'value': 'SWSH177'}},
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=399,
    abilities=[
        Attack(
            title='Happy Delivery',
            game_text='Search your deck for an Item card, reveal it, and put it into your hand. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Rock Smash',
            game_text='Flip a coin. If heads, this attack does 30 more damage.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
