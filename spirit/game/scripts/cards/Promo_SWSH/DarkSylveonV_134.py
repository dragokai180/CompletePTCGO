from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1584357c-5961-53fd-8a54-ebd6adaafb66',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.DarkSylveonV.Name',
    display_name='Dark Sylveon V',
    searchable_by=['Dark Sylveon V', 'Basic', 'V', 'DarkSylveonV'],
    subtypes=['Basic', 'V'],
    collector_number=134,
    set_code='Promo_SWSH',
    regulation_mark='E',
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    attributes={200790: {'type': 'string', 'value': 'SWSH134'}},
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=700,
    abilities=[
        Attack(
            title='Disarming Voice',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Tricky Ribbon',
            game_text="Choose a random card from your opponent's hand. Your opponent reveals that card and shuffles it into their deck.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
