from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8881824a-f161-5579-9993-ad817c8d145e',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Zigzagoon.Name',
    display_name='Zigzagoon',
    searchable_by=['Zigzagoon', 'Basic', 'Zigzagoon'],
    subtypes=['Basic'],
    collector_number=111,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=263,
    abilities=[
        Attack(
            title='Sand Attack',
            game_text="If the Defending Pokémon tries to attack during your opponent's next turn, your opponent flips a coin. If tails, that attack does nothing.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Headbutt',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
