from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6f51448f-6b43-540b-ab00-e3ddbdeb063f',
    key='XY6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Binacle.Name',
    display_name='Binacle',
    searchable_by=['Binacle', 'Basic', 'Binacle'],
    subtypes=['Basic'],
    collector_number=38,
    set_code='XY6',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=688,
    abilities=[
        Attack(
            title='Sand Attack',
            game_text="If the Defending Pokémon tries to attack during your opponent's next turn, your opponent flips a coin. If tails, that attack does nothing.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Mud-Slap',
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)
