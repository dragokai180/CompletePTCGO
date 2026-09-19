from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='132c380c-e55e-5341-8bb4-cd6a1972abcb',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Oricorio.Name',
    display_name='Oricorio',
    searchable_by=['Oricorio', 'Basic', 'Fusion Strike', 'Oricorio'],
    subtypes=['Basic', 'Fusion Strike'],
    collector_number=210,
    set_code='Promo_SWSH',
    regulation_mark='E',
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    attributes={200790: {'type': 'string', 'value': 'SWSH210'}},
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=741,
    abilities=[
        Attack(
            title='Mixed Call',
            game_text='Search your deck for a Pokémon and a Supporter card, reveal them, and put them into your hand. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Razor Wing',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)

from spirit.game.card_effects.swsh_promos import configure_promo
configure_promo(card)
