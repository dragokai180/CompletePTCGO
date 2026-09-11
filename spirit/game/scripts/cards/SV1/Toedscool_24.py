from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7f2627aa-947a-5cca-9998-67255802cb95',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Toedscool.Name',
    display_name='Toedscool',
    searchable_by=['Toedscool', 'Basic', 'Toedscool'],
    subtypes=['Basic'],
    collector_number=24,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=948,
    abilities=[
        Attack(
            title='Furious Kicks',
            game_text='Flip 3 coins. This attack does 10 damage for each heads.',
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
