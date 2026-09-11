from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2c776188-d9f4-53a1-8a3f-4c96c0577da4',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Treecko.Name',
    display_name='Treecko',
    searchable_by=['Treecko', 'Basic', 'Treecko'],
    subtypes=['Basic'],
    collector_number=6,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=252,
    abilities=[
        Attack(
            title='Quick Attack',
            game_text='Flip a coin. If heads, this attack does 10 more damage.',
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
