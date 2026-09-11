from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9b0e75a5-23cf-57a3-b19d-a60dde172480',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Wooper.Name',
    display_name='Wooper',
    searchable_by=['Wooper', 'Basic', 'Wooper'],
    subtypes=['Basic'],
    collector_number=88,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    resistance_type=PokemonTypes.LIGHTNING,
    resistance_amount=20,
    family_id=194,
    abilities=[
        Attack(
            title='Tail Whip',
            game_text="Flip a coin. If heads, the Defending Pokémon can't attack during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Watering',
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)
