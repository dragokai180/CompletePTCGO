from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6c07ed9e-9286-5f90-baf5-7a070e8e6107',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Psyduck.Name',
    display_name='Psyduck',
    searchable_by=['Psyduck', 'Basic', 'Psyduck'],
    subtypes=['Basic'],
    collector_number=54,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=54,
    abilities=[
        Attack(
            title='Overthink',
            game_text="During your opponent's next turn, whenever they flip a coin, treat it as tails.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Water Gun',
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)
