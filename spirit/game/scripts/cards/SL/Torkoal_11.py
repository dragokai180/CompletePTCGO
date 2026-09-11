from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='336f27b5-7c42-50e0-bf14-c0c32c3be666',
    key='SL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Torkoal.Name',
    display_name='Torkoal',
    searchable_by=['Torkoal', 'Basic', 'Torkoal'],
    subtypes=['Basic'],
    collector_number=11,
    set_code='SL',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=324,
    abilities=[
        Attack(
            title='High-Pressure Heat',
            game_text="During your next turn, this Pokémon's High-Pressure Heat attack does 50 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Flamethrower',
            game_text='Discard an Energy from this Pokémon.',
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=standard_attack,
        ),
    ],
)
