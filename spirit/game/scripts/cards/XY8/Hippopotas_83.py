from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6bd3990c-1414-5b17-8fda-b6ad96f89d7d',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Hippopotas.Name',
    display_name='Hippopotas',
    searchable_by=['Hippopotas', 'Basic', 'Hippopotas'],
    subtypes=['Basic'],
    collector_number=83,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=449,
    abilities=[
        Attack(
            title='Nose Jet',
            game_text="If the Defending Pokémon tries to attack during your opponent's next turn, your opponent flips a coin. If tails, that attack does nothing.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
