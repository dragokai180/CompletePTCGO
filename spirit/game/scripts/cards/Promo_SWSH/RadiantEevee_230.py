from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='13276fb0-d93f-5c41-84a2-a1097327598e',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.RadiantEevee.Name',
    display_name='Radiant Eevee',
    searchable_by=['Radiant Eevee', 'Basic', 'Radiant', 'RadiantEevee'],
    subtypes=['Basic', 'Radiant'],
    collector_number=230,
    set_code='Promo_SWSH',
    regulation_mark='F',
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    attributes={200790: {'type': 'string', 'value': 'SWSH230'}},
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=133,
    abilities=[
        Attack(
            title='Twinkle Gathering',
            game_text='Search your deck for a number of cards up to the number of different types of Pokémon you have in play and put them into your hand. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Boost Dash',
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
        ),
    ],
)

from spirit.game.card_effects.swsh_promos import configure_promo
configure_promo(card)
