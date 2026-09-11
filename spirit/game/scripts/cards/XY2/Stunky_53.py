from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='dcbcc37a-f07d-53b2-be4f-1d3417edcb09',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Stunky.Name',
    display_name='Stunky',
    searchable_by=['Stunky', 'Basic', 'Stunky'],
    subtypes=['Basic'],
    collector_number=53,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=434,
    abilities=[
        Attack(
            title='Smokescreen',
            game_text="If the Defending Pokémon tries to attack during your opponent's next turn, your opponent flips a coin. If tails, that attack does nothing.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Slash',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
