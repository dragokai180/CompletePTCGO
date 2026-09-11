from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='94c16d26-e9b4-5f51-8f77-252d2a85af41',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Froakie.Name',
    display_name='Froakie',
    searchable_by=['Froakie', 'Basic', 'Froakie'],
    subtypes=['Basic'],
    collector_number=39,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=656,
    abilities=[
        Attack(
            title='Bounce',
            game_text='Flip a coin. If heads, switch this Pokémon with 1 of your Benched Pokémon.',
            cost={PokemonTypes.WATER: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
