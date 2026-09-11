from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='43f1444c-8732-5e3b-b77c-bbc243329fdc',
    key='GUM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bulbasaur.Name',
    display_name='Bulbasaur',
    searchable_by=['Bulbasaur', 'Basic', 'Bulbasaur'],
    subtypes=['Basic'],
    collector_number=1,
    set_code='GUM',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=1,
    abilities=[
        Attack(
            title='Find a Friend',
            game_text='Search your deck for a Grass Pokémon, reveal it, and put it into your hand. Then, shuffle your deck.',
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
    ],
)
