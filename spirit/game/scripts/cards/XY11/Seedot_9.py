from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2c68a175-d1c7-5ef8-84fe-1fcf1619f744',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Seedot.Name',
    display_name='Seedot',
    searchable_by=['Seedot', 'Basic', 'Seedot'],
    subtypes=['Basic'],
    collector_number=9,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=273,
    abilities=[
        Attack(
            title='Bide',
            game_text="Flip a coin. If heads, if this Pokémon would be Knocked Out by damage from an attack during your opponent's next turn, it is not Knocked Out and its remaining HP becomes 10 instead.",
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
    ],
)
