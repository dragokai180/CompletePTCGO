from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6ab9a3c9-bf2a-579f-b1e1-5debe87754e7',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Glameow.Name',
    display_name='Glameow',
    searchable_by=['Glameow', 'Basic', 'Glameow'],
    subtypes=['Basic'],
    collector_number=93,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=431,
    abilities=[
        Attack(
            title='Act Cute',
            game_text='Your opponent puts a card from his or her hand on the bottom of his or her deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Scratch',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
