from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='eb56504f-927a-53ac-849a-61cbb5a8c074',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Remoraid.Name',
    display_name='Remoraid',
    searchable_by=['Remoraid', 'Basic', 'Remoraid'],
    subtypes=['Basic'],
    collector_number=31,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=223,
    abilities=[
        Attack(
            title='Wild River',
            game_text='Switch this Pokémon with 1 of your Benched Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Water Gun',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
