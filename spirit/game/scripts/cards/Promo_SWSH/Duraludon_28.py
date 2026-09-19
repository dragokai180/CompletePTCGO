from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f0cd1389-903f-5b32-b76f-4e08c77a2d84',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Duraludon.Name',
    display_name='Duraludon',
    searchable_by=['Duraludon', 'Basic', 'Duraludon'],
    subtypes=['Basic'],
    collector_number=28,
    set_code='Promo_SWSH',
    regulation_mark='D',
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    attributes={200790: {'type': 'string', 'value': 'SWSH028'}},
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=884,
    abilities=[
        Attack(
            title='Metal Claw',
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
        Attack(
            title='Steel Beam',
            game_text='This Pokémon also does 40 damage to itself.',
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 3},
            damage=150,
            effect=standard_attack,
        ),
    ],
)
