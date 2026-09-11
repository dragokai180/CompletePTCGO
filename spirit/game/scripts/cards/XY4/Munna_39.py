from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='967c15b0-2fa9-5c58-84a9-8eb0c29057e8',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Munna.Name',
    display_name='Munna',
    searchable_by=['Munna', 'Basic', 'Munna'],
    subtypes=['Basic'],
    collector_number=39,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=517,
    abilities=[
        Attack(
            title='See Through',
            game_text='Your opponent reveals his or her hand.',
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Double Headbutt',
            game_text='Flip 2 coins. This attack does 20 damage times the number of heads.',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
