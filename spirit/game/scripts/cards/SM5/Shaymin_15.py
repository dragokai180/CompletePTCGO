from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='07600d7c-4553-5fd7-8c2f-d1919c13bab4',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Shaymin.Name',
    display_name='Shaymin',
    searchable_by=['Shaymin', 'Basic', 'Shaymin'],
    subtypes=['Basic'],
    collector_number=15,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=492,
    abilities=[
        Attack(
            title='Coax',
            game_text='Search your deck for up to 3 Basic Pokémon of different types and put them onto your Bench. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Soothing Scent',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
