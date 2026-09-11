from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a1033261-4a71-5215-bea4-3b9eb2eacec7',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Duskull.Name',
    display_name='Duskull',
    searchable_by=['Duskull', 'Basic', 'Duskull'],
    subtypes=['Basic'],
    collector_number=38,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=355,
    abilities=[
        Attack(
            title='Revival',
            game_text="Put a Basic Pokémon from your opponent's discard pile onto his or her Bench.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Sneaky Placement',
            game_text="Put 1 damage counter on your opponent's Active Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
    ],
)
