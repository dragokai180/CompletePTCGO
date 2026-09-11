from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ab71f31c-6557-5161-811a-cb3e03362f87',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Turtwig.Name',
    display_name='Turtwig',
    searchable_by=['Turtwig', 'Basic', 'Turtwig'],
    subtypes=['Basic'],
    collector_number=6,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=387,
    abilities=[
        Attack(
            title='Synthesis',
            game_text='Search your deck for a Grass Energy card and attach it to 1 of your Pokémon. Then, shuffle your deck.',
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Headbutt Bounce',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
