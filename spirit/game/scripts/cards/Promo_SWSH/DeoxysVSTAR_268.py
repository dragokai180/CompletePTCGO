from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a0598c8e-fce9-5000-bc5e-a075de3a679d',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.DeoxysVSTAR.Name',
    display_name='Deoxys VSTAR',
    searchable_by=['Deoxys VSTAR', 'VSTAR', 'DeoxysVSTAR'],
    subtypes=['VSTAR'],
    collector_number=268,
    set_code='Promo_SWSH',
    regulation_mark='F',
    rarity=Rarities.RarePromo,
    hp=270,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.VSTAR,
    retreat_cost=2,
    attributes={200790: {'type': 'string', 'value': 'SWSH268'}},
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.DeoxysV.Name',
    family_id=386,
    abilities=[
        Attack(
            title='Psychic Javelin',
            game_text="This attack also does 60 damage to 1 of your opponent's Benched Pokémon V. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=190,
            effect=standard_attack,
        ),
        Attack(
            title='Star Force',
            game_text="This attack does 60 damage for each Energy attached to both Active Pokémon. (You can't use more than 1 VSTAR Power in a game.)",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=60,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)

from spirit.game.card_effects.swsh_promos import configure_promo
configure_promo(card)
