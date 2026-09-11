from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5ae2d69e-3737-5221-86bc-5b730f516c8b',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Buizel.Name',
    display_name='Buizel',
    searchable_by=['Buizel', 'Basic', 'Buizel'],
    subtypes=['Basic'],
    collector_number=28,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=418,
    abilities=[
        Attack(
            title='Water Gun',
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
        Attack(
            title='Quick Attack',
            game_text='Flip a coin. If heads, this attack does 20 more damage.',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
