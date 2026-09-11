from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='57149b23-d8f5-54f4-b9c2-11fa8d1a1989',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Skitty.Name',
    display_name='Skitty',
    searchable_by=['Skitty', 'Basic', 'Skitty'],
    subtypes=['Basic'],
    collector_number=113,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=300,
    abilities=[
        Attack(
            title='Charm',
            game_text="During your opponent's next turn, any damage done by attacks from the Defending Pokémon is reduced by 20 (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Tail Smack',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
