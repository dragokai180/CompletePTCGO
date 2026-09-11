from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='cd7bce08-5173-57b5-9e78-af5dc991f4bc',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Purrloin.Name',
    display_name='Purrloin',
    searchable_by=['Purrloin', 'Basic', 'Purrloin'],
    subtypes=['Basic'],
    collector_number=56,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=509,
    abilities=[
        Attack(
            title='Fake Out',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
