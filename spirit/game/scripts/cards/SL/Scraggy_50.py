from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='91a7db01-aa8a-5ad6-958b-96321c1d64bd',
    key='SL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Scraggy.Name',
    display_name='Scraggy',
    searchable_by=['Scraggy', 'Basic', 'Scraggy'],
    subtypes=['Basic'],
    collector_number=50,
    set_code='SL',
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
    family_id=559,
    abilities=[
        Attack(
            title='Call for Family',
            game_text='Search your deck for a Basic Pokémon and put it onto your Bench. Then, shuffle your deck.',
            cost={PokemonTypes.DARKNESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Headbutt',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
