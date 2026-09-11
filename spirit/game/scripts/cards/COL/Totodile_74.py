from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f3944e54-075a-5739-a3ab-a627937b3de0',
    key='COL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Totodile.Name',
    display_name='Totodile',
    searchable_by=['Totodile', 'Basic', 'Totodile'],
    subtypes=['Basic'],
    collector_number=74,
    set_code='COL',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=158,
    abilities=[
        Attack(
            title='Aqua Tail',
            game_text='Flip a coin for each Water Energy attached to Totodile. This attack does 30 damage plus 20 more damage for each heads.',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
