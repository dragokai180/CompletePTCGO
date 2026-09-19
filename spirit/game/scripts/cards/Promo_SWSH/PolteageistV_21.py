from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d4456e35-c3f9-58a0-8cc5-2624f0e79deb',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.PolteageistV.Name',
    display_name='Polteageist V',
    searchable_by=['Polteageist V', 'Basic', 'V', 'PolteageistV'],
    subtypes=['Basic', 'V'],
    collector_number=21,
    set_code='Promo_SWSH',
    regulation_mark='D',
    rarity=Rarities.RarePromo,
    hp=170,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    attributes={200790: {'type': 'string', 'value': 'SWSH021'}},
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=855,
    abilities=[
        Ability(
            title='Teapot of Surprises',
            game_text="If this Pokémon is in the Active Spot and is damaged by an opponent's attack (even if it is Knocked Out), choose a random card from your opponent's hand. Your opponent reveals that card and puts it on the bottom of their deck.",
            passive=standard_passive("If this Pokémon is in the Active Spot and is damaged by an opponent's attack (even if it is Knocked Out), choose a random card from your opponent's hand. Your opponent reveals that card and puts it on the bottom of their deck."),
        ),
        Attack(
            title='Mind Bend',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=standard_attack,
        ),
    ],
)

from spirit.game.card_effects.swsh_promos import configure_promo
configure_promo(card)
