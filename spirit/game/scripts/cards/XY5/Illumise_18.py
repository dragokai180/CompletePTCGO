from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='91e40882-8c6e-53a0-8e6f-ede7a26b6425',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Illumise.Name',
    display_name='Illumise',
    searchable_by=['Illumise', 'Basic', 'Illumise'],
    subtypes=['Basic'],
    collector_number=18,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=314,
    abilities=[
        Attack(
            title='Helping Hand',
            game_text='Search your deck for a basic Energy card and attach it to 1 of your Benched Pokémon. Shuffle your deck afterward.',
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Twirling Sign',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
