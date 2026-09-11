from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ee13b7f5-d977-5b96-830e-27bb0c1a72cc',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Drowzee.Name',
    display_name='Drowzee',
    searchable_by=['Drowzee', 'Basic', 'Drowzee'],
    subtypes=['Basic'],
    collector_number=50,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=96,
    abilities=[
        Attack(
            title='Mumble',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
        Attack(
            title='Focused Wish',
            game_text='Flip a coin. If heads, this attack does 20 more damage.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
