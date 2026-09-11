from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a40a9e5c-20df-53b0-b120-5b5075cb972c',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dhelmise.Name',
    display_name='Dhelmise',
    searchable_by=['Dhelmise', 'Basic', 'Dhelmise'],
    subtypes=['Basic'],
    collector_number=20,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=781,
    abilities=[
        Attack(
            title='Sea Creeper Net',
            game_text='Search your deck for a Basic Pokémon and put it onto your Bench. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Spinning Attack',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)
