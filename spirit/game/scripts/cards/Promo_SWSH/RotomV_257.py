from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f3a5ea8f-33e9-5170-824c-f55ef8e14733',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.RotomV.Name',
    display_name='Rotom V',
    searchable_by=['Rotom V', 'Basic', 'V', 'RotomV'],
    subtypes=['Basic', 'V'],
    collector_number=257,
    set_code='Promo_SWSH',
    regulation_mark='F',
    rarity=Rarities.RarePromo,
    hp=190,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    attributes={200790: {'type': 'string', 'value': 'SWSH257'}},
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=479,
    abilities=[
        Attack(
            title='Lost Hack',
            game_text="Put a Special Energy attached to 1 of your opponent's Pokémon in the Lost Zone.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Extreme Current',
            game_text='Discard an Energy from this Pokémon.',
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=standard_attack,
        ),
    ],
)
