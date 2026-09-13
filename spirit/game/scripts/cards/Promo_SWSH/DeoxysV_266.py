from spirit.game.card_effects.galleries import deoxys_psychic
from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3ba79d7f-1a0f-519a-8b2d-cd3b39261d73',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.DeoxysV.Name',
    display_name='Deoxys V',
    searchable_by=['Deoxys V', 'Basic', 'V', 'DeoxysV'],
    subtypes=['Basic', 'V'],
    collector_number=266,
    set_code='Promo_SWSH',
    regulation_mark='F',
    rarity=Rarities.RarePromo,
    hp=210,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    attributes={200790: {'type': 'string', 'value': 'SWSH266'}},
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=386,
    abilities=[
        Attack(
            title='Psychic',
            game_text="This attack does 30 more damage for each Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator='+',
            effect=deoxys_psychic,
        ),
        Attack(
            title='Power Edge',
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=140,
        ),
    ],
)
