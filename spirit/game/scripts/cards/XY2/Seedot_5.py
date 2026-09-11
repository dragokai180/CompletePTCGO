from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3e480498-4d3b-538f-a0c0-cfb27fb9ce21',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Seedot.Name',
    display_name='Seedot',
    searchable_by=['Seedot', 'Basic', 'Seedot'],
    subtypes=['Basic'],
    collector_number=5,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=273,
    abilities=[
        Attack(
            title='Call for Family',
            game_text='Search your deck for a Basic Pokémon and put it onto your Bench. Shuffle your deck afterward.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
