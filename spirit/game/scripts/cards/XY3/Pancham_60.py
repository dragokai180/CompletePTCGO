from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ea41de95-7791-5199-97bc-781e93a52e19',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pancham.Name',
    display_name='Pancham',
    searchable_by=['Pancham', 'Basic', 'Pancham'],
    subtypes=['Basic'],
    collector_number=60,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=674,
    abilities=[
        Attack(
            title='Comet Punch',
            game_text='Flip 4 coins. This attack does 10 damage times the number of heads.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
