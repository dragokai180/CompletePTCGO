from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c6705b6c-7a1b-551c-adb9-0de1c15e920a',
    key='SL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Shroomish.Name',
    display_name='Shroomish',
    searchable_by=['Shroomish', 'Basic', 'Shroomish'],
    subtypes=['Basic'],
    collector_number=4,
    set_code='SL',
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
            title='Absorb',
            game_text='Heal 20 damage from this Pokémon.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
