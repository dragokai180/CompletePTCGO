from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e469ede7-1c85-5dd9-b0f0-ed2e7e8bb0e1',
    key='COL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Chikorita.Name',
    display_name='Chikorita',
    searchable_by=['Chikorita', 'Basic', 'Chikorita'],
    subtypes=['Basic'],
    collector_number=53,
    set_code='COL',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    family_id=152,
    abilities=[
        Attack(
            title='Nap',
            game_text='Remove 1 damage counter from Chikorita.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Reckless Charge',
            game_text='Chikorita does 10 damage to itself.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
