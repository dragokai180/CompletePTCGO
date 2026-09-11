from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5ecd9542-57b2-5ffd-95c8-481f458e9d08',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Torkoal.Name',
    display_name='Torkoal',
    searchable_by=['Torkoal', 'Basic', 'Torkoal'],
    subtypes=['Basic'],
    collector_number=23,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=324,
    abilities=[
        Attack(
            title='Singe',
            game_text="Your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.FIRE: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Body Slam',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
