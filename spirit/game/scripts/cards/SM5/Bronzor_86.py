from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='485eaaab-eb73-5753-b9d6-ac6b153d1d67',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bronzor.Name',
    display_name='Bronzor',
    searchable_by=['Bronzor', 'Basic', 'Bronzor'],
    subtypes=['Basic'],
    collector_number=86,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=436,
    abilities=[
        Attack(
            title='Hypnosis',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.METAL: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Spinning Attack',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
