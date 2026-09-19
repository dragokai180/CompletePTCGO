from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='98c9b6f1-4894-51f9-ab5b-e163870c8c40',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.DeoxysVMAX.Name',
    display_name='Deoxys VMAX',
    searchable_by=['Deoxys VMAX', 'VMAX', 'DeoxysVMAX'],
    subtypes=['VMAX'],
    collector_number=267,
    set_code='Promo_SWSH',
    regulation_mark='F',
    rarity=Rarities.RarePromo,
    hp=330,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    attributes={200790: {'type': 'string', 'value': 'SWSH267'}},
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.DeoxysV.Name',
    family_id=386,
    abilities=[
        Ability(
            title='Protective DNA',
            game_text="All of your Pokémon take 30 less damage from attacks from your opponent's Pokémon VSTAR (after applying Weakness and Resistance).",
            passive=standard_passive("All of your Pokémon take 30 less damage from attacks from your opponent's Pokémon VSTAR (after applying Weakness and Resistance)."),
        ),
        Attack(
            title='Max Drain',
            game_text='Heal 30 damage from this Pokémon.',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=160,
            effect=standard_attack,
        ),
    ],
)

from spirit.game.card_effects.swsh_promos import configure_promo
configure_promo(card)
