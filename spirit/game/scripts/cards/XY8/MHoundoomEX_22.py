from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='743c618a-6fdb-5fc9-952a-28a41e076bb2',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MHoundoomEX.Name',
    display_name='M Houndoom-EX',
    searchable_by=['M Houndoom-EX', 'MEGA', 'EX', 'MHoundoomEX'],
    subtypes=['MEGA', 'EX'],
    collector_number=22,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=210,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.HoundoomEX.Name',
    family_id=229,
    abilities=[
        Attack(
            title='Inferno Fang',
            game_text='You may discard all Fire Energy attached to this Pokémon. If you do, this attack does 80 more damage.',
            cost={PokemonTypes.FIRE: 2},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
