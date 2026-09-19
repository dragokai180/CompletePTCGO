from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c83b6e5a-4eb4-5f0c-85ab-7de76d6a85e9',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Zacian.Name',
    display_name='Zacian',
    searchable_by=['Zacian', 'Basic', 'Zacian'],
    subtypes=['Basic'],
    collector_number=33,
    set_code='Promo_SWSH',
    regulation_mark='D',
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    attributes={200790: {'type': 'string', 'value': 'SWSH033'}},
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=888,
    abilities=[
        Attack(
            title='Crunch',
            game_text="Flip a coin. If heads, discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            effect=standard_attack,
        ),
        Attack(
            title='Metal Blade',
            game_text='Discard 3 Energy from this Pokémon.',
            cost={PokemonTypes.METAL: 3, PokemonTypes.COLORLESS: 1},
            damage=190,
            effect=standard_attack,
        ),
    ],
)
