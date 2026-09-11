from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8254e546-5e70-52f4-9c28-d6e00ca4b2e2',
    key='SV045',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.HeatRotom.Name',
    display_name='Heat Rotom',
    searchable_by=['Heat Rotom', 'Basic', 'HeatRotom'],
    subtypes=['Basic'],
    collector_number=13,
    set_code='SV045',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=479,
    abilities=[
        Attack(
            title='Heat Tackle',
            game_text='This Pokémon also does 40 damage to itself.',
            cost={PokemonTypes.FIRE: 2},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
