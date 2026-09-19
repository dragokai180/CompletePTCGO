from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c9d66e34-130c-5001-a3a6-9b23628d9553',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.BlastoiseVMAX.Name',
    display_name='Blastoise VMAX',
    searchable_by=['Blastoise VMAX', 'VMAX', 'BlastoiseVMAX'],
    subtypes=['VMAX'],
    collector_number=103,
    set_code='Promo_SWSH',
    regulation_mark='E',
    rarity=Rarities.RarePromo,
    hp=330,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    attributes={200790: {'type': 'string', 'value': 'SWSH103'}},
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.BlastoiseV.Name',
    family_id=9,
    abilities=[
        Attack(
            title='Grand Falls',
            game_text='Search your deck for up to 3 Water Energy cards and attach them to your Benched Pokémon in any way you like. Then, shuffle your deck.',
            cost={PokemonTypes.WATER: 3},
            damage=120,
            effect=standard_attack,
        ),
        Attack(
            title='G-Max Bombard',
            game_text="This attack also does 30 damage to 2 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 4},
            damage=220,
            effect=standard_attack,
        ),
    ],
)

from spirit.game.card_effects.swsh_promos import configure_promo
configure_promo(card)
