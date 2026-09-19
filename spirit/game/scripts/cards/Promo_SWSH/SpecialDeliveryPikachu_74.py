from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d9761df9-476d-5687-a548-10ee0bb9d47a',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.SpecialDeliveryPikachu.Name',
    display_name='Special Delivery Pikachu',
    searchable_by=['Special Delivery Pikachu', 'Basic', 'SpecialDeliveryPikachu'],
    subtypes=['Basic'],
    collector_number=74,
    set_code='Promo_SWSH',
    regulation_mark='D',
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    attributes={200790: {'type': 'string', 'value': 'SWSH074'}},
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=25,
    abilities=[
        Attack(
            title='Happy Delivery',
            game_text='Search your deck for an Item card, reveal it, and put it into your hand. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Electro Ball',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
