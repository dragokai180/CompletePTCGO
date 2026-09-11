from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3bab4820-d1c5-583a-837d-3cb88c762f51',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Poliwag.Name',
    display_name='Poliwag',
    searchable_by=['Poliwag', 'Basic', 'Poliwag'],
    subtypes=['Basic'],
    collector_number=30,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=60,
    abilities=[
        Attack(
            title='Water Gun',
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
        Attack(
            title='Hydro Pump',
            game_text='This attack does 10 more damage times the amount of Water Energy attached to this Pokémon.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
