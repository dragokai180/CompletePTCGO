from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6995334e-5766-534e-96ad-bdfaa4e183a6',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.VenusaurVMAX.Name',
    display_name='Venusaur VMAX',
    searchable_by=['Venusaur VMAX', 'VMAX', 'VenusaurVMAX'],
    subtypes=['VMAX'],
    collector_number=102,
    set_code='Promo_SWSH',
    regulation_mark='E',
    rarity=Rarities.RarePromo,
    hp=330,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.VMAX,
    retreat_cost=4,
    attributes={200790: {'type': 'string', 'value': 'SWSH102'}},
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.VenusaurV.Name',
    family_id=3,
    abilities=[
        Attack(
            title='Forest Storm',
            game_text='This attack does 30 damage for each Grass Energy attached to all of your Pokémon.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='G-Max Bloom',
            game_text='Heal 30 damage from this Pokémon.',
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2},
            damage=210,
            effect=standard_attack,
        ),
    ],
)
