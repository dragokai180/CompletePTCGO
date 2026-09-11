from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3a672028-3296-59f0-a6bd-f08ded551f84',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Foongus.Name',
    display_name='Foongus',
    searchable_by=['Foongus', 'Basic', 'Foongus'],
    subtypes=['Basic'],
    collector_number=12,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=590,
    abilities=[
        Ability(
            title='Play Ball',
            game_text='When you play this Pokémon from your hand onto your Bench, you may put 3 Poké Ball cards from your discard pile into your hand.',
            effect=standard_ability,
            trigger=Triggers.ON_PLAY,
        ),
        Attack(
            title='Ram',
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
    ],
)
