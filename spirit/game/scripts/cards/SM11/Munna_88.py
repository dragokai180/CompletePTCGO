from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4fc8bdeb-2538-5d6a-b8a1-f93ec9f94e71',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Munna.Name',
    display_name='Munna',
    searchable_by=['Munna', 'Basic', 'Munna'],
    subtypes=['Basic'],
    collector_number=88,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=517,
    abilities=[
        Attack(
            title='Future Sight',
            game_text="Look at the top 4 cards of either player's deck and put them back in any order.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
