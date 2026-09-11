from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='22aead2d-ce14-537e-b49e-7b9d7b3815fb',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Clauncher.Name',
    display_name='Clauncher',
    searchable_by=['Clauncher', 'Basic', 'Clauncher'],
    subtypes=['Basic'],
    collector_number=23,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=692,
    abilities=[
        Attack(
            title='Bubble',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Crabhammer',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
