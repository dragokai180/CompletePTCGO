from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='cc342421-eeaa-588c-a93a-6ecdfacdddbc',
    key='COL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Teddiursa.Name',
    display_name='Teddiursa',
    searchable_by=['Teddiursa', 'Basic', 'Teddiursa'],
    subtypes=['Basic'],
    collector_number=73,
    set_code='COL',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=216,
    abilities=[
        Attack(
            title='Fake Tears',
            game_text="Flip a coin. If heads, your opponent can't play any Trainer cards from his or her hand during your opponent's next turn, and any damage done to Teddiursa by attack is reduced by 30 (after applying weakness and resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
