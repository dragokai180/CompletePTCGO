from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='940b8253-3e10-53bc-820d-1056af4ce51e',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pinsir.Name',
    display_name='Pinsir',
    searchable_by=['Pinsir', 'Basic', 'Pinsir'],
    subtypes=['Basic'],
    collector_number=6,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=127,
    abilities=[
        Attack(
            title='Roof Fling',
            game_text="Flip a coin. If heads, put your opponent's Active Pokémon and all cards attached to it into your opponent's hand.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
        Attack(
            title='Guillotine',
            cost={PokemonTypes.GRASS: 2},
            damage=50,
        ),
    ],
)
