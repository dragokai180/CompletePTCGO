from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b2b92270-c790-599c-b262-72775f489da0',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.VenusaurV.Name',
    display_name='Venusaur V',
    searchable_by=['Venusaur V', 'Basic', 'V', 'VenusaurV'],
    subtypes=['Basic', 'V'],
    collector_number=100,
    set_code='Promo_SWSH',
    regulation_mark='E',
    rarity=Rarities.RarePromo,
    hp=220,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    attributes={200790: {'type': 'string', 'value': 'SWSH100'}},
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=3,
    abilities=[
        Attack(
            title='Leaf Drain',
            game_text='Heal 30 damage from this Pokémon.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=standard_attack,
        ),
        Attack(
            title='Double-Edge',
            game_text='This Pokémon also does 30 damage to itself.',
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=190,
            effect=standard_attack,
        ),
    ],
)
