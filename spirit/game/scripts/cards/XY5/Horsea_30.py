from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='185003df-ae82-512f-8d8e-2ff4d62d6b34',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Horsea.Name',
    display_name='Horsea',
    searchable_by=['Horsea', 'Basic', 'Horsea'],
    subtypes=['Basic'],
    collector_number=30,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=116,
    abilities=[
        Attack(
            title='Bubble',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
    ],
)
