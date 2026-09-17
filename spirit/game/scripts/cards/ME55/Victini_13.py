from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='bc6d3c74-da97-59d2-b5dc-fed10508ddf9',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Victini.Name',
    display_name='Victini',
    searchable_by=['Victini', 'Basic', 'Victini'],
    subtypes=['Basic'],
    collector_number=13,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=494,
    abilities=[
        Attack(
            title='Call for Family',
            game_text='Search your deck for up to 2 Basic Pokémon and put them onto your Bench. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='V-Flame',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
