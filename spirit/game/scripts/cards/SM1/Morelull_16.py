from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='637d3b7d-2c7c-5816-a7dc-26970e1bed75',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Morelull.Name',
    display_name='Morelull',
    searchable_by=['Morelull', 'Basic', 'Morelull'],
    subtypes=['Basic'],
    collector_number=16,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=755,
    abilities=[
        Attack(
            title='Flickering Spores',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Ram',
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
    ],
)
