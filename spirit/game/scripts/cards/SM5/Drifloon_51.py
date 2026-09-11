from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a66a2b28-9d1f-5ea7-826a-e7fe7b752cdd',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Drifloon.Name',
    display_name='Drifloon',
    searchable_by=['Drifloon', 'Basic', 'Drifloon'],
    subtypes=['Basic'],
    collector_number=51,
    set_code='SM5',
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
    family_id=425,
    abilities=[
        Attack(
            title='Creepy Wind',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Hang Down',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
