from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='84d6522b-651b-5a8a-99ad-1eade3614bb2',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cobalion.Name',
    display_name='Cobalion',
    searchable_by=['Cobalion', 'Basic', 'Cobalion'],
    subtypes=['Basic'],
    collector_number=74,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=638,
    abilities=[
        Attack(
            title='Quick Guard',
            game_text="Prevent all damage done to this Pokémon by attacks from Basic Pokémon during your opponent's next turn. This Pokémon can't use Quick Guard during your next turn.",
            cost={PokemonTypes.METAL: 1},
            effect=standard_attack,
            locks_next_turn=True,
        ),
        Attack(
            title='Revenge Blast',
            game_text='This attack does 30 more damage for each Prize card your opponent has taken.',
            cost={PokemonTypes.METAL: 2},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
