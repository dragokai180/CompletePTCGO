from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5eabe58f-6097-547a-9ccd-10e1745da52e',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Starly.Name',
    display_name='Starly',
    searchable_by=['Starly', 'Basic', 'Starly'],
    subtypes=['Basic'],
    collector_number=125,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=396,
    abilities=[
        Attack(
            title='Call for Pals',
            game_text='Search your deck for as many Starly as you like and put them onto your Bench. Shuffle your deck afterward.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
