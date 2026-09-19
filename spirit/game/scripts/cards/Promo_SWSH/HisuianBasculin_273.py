from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ce555577-0962-50d8-87a0-c4dacebb8bc7',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.HisuianBasculin.Name',
    display_name='Hisuian Basculin',
    searchable_by=['Hisuian Basculin', 'Basic', 'HisuianBasculin'],
    subtypes=['Basic'],
    collector_number=273,
    set_code='Promo_SWSH',
    regulation_mark='F',
    rarity=Rarities.RarePromo,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    attributes={200790: {'type': 'string', 'value': 'SWSH273'}},
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=550,
    abilities=[
        Attack(
            title='Submerge Silently',
            game_text="You can use this attack only if you go second, and only during your first turn. During your opponent's next turn, prevent all damage done to this Pokémon by attacks.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Bite',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
