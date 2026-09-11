from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7608800c-fea6-53f5-89da-3137d3fda38d',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Shroomish.Name',
    display_name='Shroomish',
    searchable_by=['Shroomish', 'Basic', 'Shroomish'],
    subtypes=['Basic'],
    collector_number=15,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=285,
    abilities=[
        Attack(
            title='Spore',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
