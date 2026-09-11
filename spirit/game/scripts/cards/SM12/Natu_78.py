from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='23852def-8394-50f6-8c0f-aab0f1734a11',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Natu.Name',
    display_name='Natu',
    searchable_by=['Natu', 'Basic', 'Natu'],
    subtypes=['Basic'],
    collector_number=78,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=177,
    abilities=[
        Attack(
            title='Future Sight',
            game_text="Look at the top 4 cards of either player's deck and put them back in any order.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
    ],
)
