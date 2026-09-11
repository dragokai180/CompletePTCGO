from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3041fa1c-df62-5bac-99c8-3879d7a0c013',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Drifloon.Name',
    display_name='Drifloon',
    searchable_by=['Drifloon', 'Basic', 'Drifloon'],
    subtypes=['Basic'],
    collector_number=46,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.COLORLESS,
    resistance_amount=20,
    family_id=425,
    abilities=[
        Attack(
            title='Minimize',
            game_text="During your opponent's next turn, any damage done to Drifloon by attacks is reduced by 20 (after applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Pull',
            game_text="Flip a coin. If heads, switch the Defending Pokémon with 1 of your opponent's Benched Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
