from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='67715c56-4511-5262-8458-8a2c9339b6c8',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Chikorita.Name',
    display_name='Chikorita',
    searchable_by=['Chikorita', 'Basic', 'Chikorita'],
    subtypes=['Basic'],
    collector_number=5,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=152,
    abilities=[
        Attack(
            title='Synthesis',
            game_text='Search your deck for a Grass Energy card and attach it to 1 of your Pokémon. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Razor Leaf',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
