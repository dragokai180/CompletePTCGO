from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='92ca4b9b-f119-5e68-8bf7-197c149dfaa8',
    key='DM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Horsea.Name',
    display_name='Horsea',
    searchable_by=['Horsea', 'Basic', 'Horsea'],
    subtypes=['Basic'],
    collector_number=16,
    set_code='DM',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=116,
    abilities=[
        Attack(
            title='Hydro Pump',
            game_text='This attack does 10 more damage times the amount of Water Energy attached to this Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
