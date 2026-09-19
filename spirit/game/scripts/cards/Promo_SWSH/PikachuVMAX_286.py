from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='68265202-92ed-5bfd-84bd-1e4b713c5d34',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.PikachuVMAX.Name',
    display_name='Pikachu VMAX',
    searchable_by=['Pikachu VMAX', 'VMAX', 'PikachuVMAX'],
    subtypes=['VMAX'],
    collector_number=286,
    set_code='Promo_SWSH',
    regulation_mark='F',
    rarity=Rarities.RarePromo,
    hp=310,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    attributes={200790: {'type': 'string', 'value': 'SWSH286'}},
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.PikachuV.Name',
    family_id=25,
    abilities=[
        Attack(
            title='Tail Charge',
            game_text='Attach up to 3 Lightning Energy cards from your discard pile to 1 of your Pokémon.',
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='G-Max Thunder',
            cost={PokemonTypes.LIGHTNING: 3, PokemonTypes.COLORLESS: 1},
            damage=250,
        ),
    ],
)

from spirit.game.card_effects.swsh_promos import configure_promo
configure_promo(card)
