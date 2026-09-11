from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='01cff739-aee1-5c8e-8ac3-afdd146a1091',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bruxish.Name',
    display_name='Bruxish',
    searchable_by=['Bruxish', 'Basic', 'Bruxish'],
    subtypes=['Basic'],
    collector_number=38,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=779,
    abilities=[
        Attack(
            title='Gnash Teeth',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Synchronoise',
            game_text="This attack does 20 damage to each of your opponent's Benched Pokémon that shares a type with your opponent's Active Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
