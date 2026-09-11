from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1e3aba23-2d6d-57e0-994b-5bdcb2ebc8cd',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Zorua.Name',
    display_name='Zorua',
    searchable_by=['Zorua', 'Basic', 'Zorua'],
    subtypes=['Basic'],
    collector_number=72,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=570,
    abilities=[
        Attack(
            title='Scratch',
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
        ),
        Attack(
            title='Nasty Plot',
            game_text='Search your deck for a card and put it into your hand. Shuffle your deck afterward.',
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
