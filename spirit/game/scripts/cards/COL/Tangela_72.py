from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c945ce8e-3765-525c-8d02-78b3e0b1de33',
    key='COL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tangela.Name',
    display_name='Tangela',
    searchable_by=['Tangela', 'Basic', 'Tangela'],
    subtypes=['Basic'],
    collector_number=72,
    set_code='COL',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    family_id=114,
    abilities=[
        Attack(
            title='Nutritional Support',
            game_text='Search your deck for a Grass Energy card and attach it to 1 of your Pokémon. Shuffle your deck afterward.',
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Poisonpowder',
            game_text='The Defending Pokémon is now Poisoned.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
