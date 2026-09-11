from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c7de9f1b-2489-5cc9-ab13-11d39e343094',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Machop.Name',
    display_name='Machop',
    searchable_by=['Machop', 'Basic', 'Machop'],
    subtypes=['Basic'],
    collector_number=62,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=66,
    abilities=[
        Attack(
            title='Dual Chop',
            game_text='Flip 2 coins. This attack does 30 damage for each heads.',
            cost={PokemonTypes.FIGHTING: 2},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
