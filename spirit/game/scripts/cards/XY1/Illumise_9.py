from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='543b8b9b-5aae-5cad-81ee-b7da55ac07ac',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Illumise.Name',
    display_name='Illumise',
    searchable_by=['Illumise', 'Basic', 'Illumise'],
    subtypes=['Basic'],
    collector_number=9,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=314,
    abilities=[
        Attack(
            title='Pheromotion',
            game_text='Search your deck for a Grass Pokémon, reveal it, and put it into your hand. Shuffle your deck afterward.',
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Quick Attack',
            game_text='Flip a coin. If heads, this attack does 20 more damage.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
