from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5e7bf95d-b23a-5eab-a522-799538d8dd27',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Deerling.Name',
    display_name='Deerling',
    searchable_by=['Deerling', 'Basic', 'Deerling'],
    subtypes=['Basic'],
    collector_number=8,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=585,
    abilities=[
        Attack(
            title='Find a Friend',
            game_text='Search your deck for a Pokémon, reveal it, and put it into your hand. Shuffle your deck afterward.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
