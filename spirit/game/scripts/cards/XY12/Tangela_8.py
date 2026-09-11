from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='35be01a7-43bb-5fe6-a99a-04c83b3a508f',
    key='XY12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tangela.Name',
    display_name='Tangela',
    searchable_by=['Tangela', 'Basic', 'Tangela'],
    subtypes=['Basic'],
    collector_number=8,
    set_code='XY12',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=114,
    abilities=[
        Attack(
            title='Bind',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Poison Powder',
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.GRASS: 3},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
