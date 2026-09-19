from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='096f7e10-f13d-59ae-a3eb-b3d3b45adb19',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.SpecialDeliveryCharizard.Name',
    display_name='Special Delivery Charizard',
    searchable_by=['Special Delivery Charizard', 'Stage 2', 'SpecialDeliveryCharizard'],
    subtypes=['Stage 2'],
    collector_number=75,
    set_code='Promo_SWSH',
    regulation_mark='D',
    rarity=Rarities.RarePromo,
    hp=160,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    attributes={200790: {'type': 'string', 'value': 'SWSH075'}},
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name',
    family_id=4,
    abilities=[
        Attack(
            title='Happy Delivery',
            game_text='Search your deck for up to 2 Item cards, reveal them, and put them into your hand. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Flamethrower',
            game_text='Discard an Energy from this Pokémon.',
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=standard_attack,
        ),
    ],
)
