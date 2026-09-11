from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='873778e3-a127-5ab7-b995-1511612e930e',
    key='GUM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Morelull.Name',
    display_name='Morelull',
    searchable_by=['Morelull', 'Basic', 'Morelull'],
    subtypes=['Basic'],
    collector_number=3,
    set_code='GUM',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=755,
    abilities=[
        Attack(
            title='Sleep Spore',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
