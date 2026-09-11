from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8d4c9998-4172-5df3-9675-9b2301efd224',
    key='XY12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MSlowbroEX.Name',
    display_name='M Slowbro-EX',
    searchable_by=['M Slowbro-EX', 'MEGA', 'EX', 'MSlowbroEX'],
    subtypes=['MEGA', 'EX'],
    collector_number=27,
    set_code='XY12',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.SlowbroEX.Name',
    family_id=80,
    abilities=[
        Attack(
            title='Loll Roll Spin',
            game_text="This Pokémon is now Confused. During your next turn, this Pokémon's Loll Roll Spin attack does 100 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.WATER: 3},
            damage=100,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
