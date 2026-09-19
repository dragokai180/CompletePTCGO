from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f8b908a1-281e-5d51-90d4-676b7154995a',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Moltres.Name',
    display_name='Moltres',
    searchable_by=['Moltres', 'Basic', 'Moltres'],
    subtypes=['Basic'],
    collector_number=185,
    set_code='Promo_SWSH',
    regulation_mark='F',
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    attributes={200790: {'type': 'string', 'value': 'SWSH185'}},
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=146,
    abilities=[
        Attack(
            title='Inferno Wings',
            game_text="If this Pokémon has any damage counters on it, this attack does 70 more. This attack's damage isn't affected by Weakness.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
