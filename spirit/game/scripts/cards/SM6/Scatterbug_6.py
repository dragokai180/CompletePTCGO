from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e89f38b7-eb50-56bb-99f4-ccd6aeaedfef',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Scatterbug.Name',
    display_name='Scatterbug',
    searchable_by=['Scatterbug', 'Basic', 'Scatterbug'],
    subtypes=['Basic'],
    collector_number=6,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=664,
    abilities=[
        Attack(
            title='Ultra Evolution',
            game_text='Flip a coin. If heads, search your deck for Vivillon and put it onto this Scatterbug to evolve it. Then, shuffle your deck.',
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
    ],
)
