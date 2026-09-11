from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4246b1e2-5ad9-55f7-b589-7a39344f7f7e',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Panpour.Name',
    display_name='Panpour',
    searchable_by=['Panpour', 'Basic', 'Panpour'],
    subtypes=['Basic'],
    collector_number=37,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=515,
    abilities=[
        Attack(
            title='Wave Splash',
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
        Attack(
            title='Water Splash',
            game_text='Flip a coin. If heads, this attack does 20 more damage.',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
