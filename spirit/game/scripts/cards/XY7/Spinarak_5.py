from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d9c5033b-518b-5c31-bfaa-a834e9a8fe02',
    key='XY7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Spinarak.Name',
    display_name='Spinarak',
    searchable_by=['Spinarak', 'Basic', 'Spinarak'],
    subtypes=['Basic'],
    collector_number=5,
    set_code='XY7',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=167,
    abilities=[
        Attack(
            title='String Shot',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
