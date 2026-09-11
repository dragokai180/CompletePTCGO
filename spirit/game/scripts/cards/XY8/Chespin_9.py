from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='cc0d4a4a-088a-5349-a094-9cd0a6363362',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Chespin.Name',
    display_name='Chespin',
    searchable_by=['Chespin', 'Basic', 'Chespin'],
    subtypes=['Basic'],
    collector_number=9,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=650,
    abilities=[
        Attack(
            title='Tree Climb',
            game_text='Search your deck for a Grass Energy card, reveal it, and put it into your hand. Shuffle your deck afterward.',
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Seed Bomb',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
