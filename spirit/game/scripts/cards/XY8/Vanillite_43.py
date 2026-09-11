from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='788570eb-eb2c-571a-93cf-c71ad094c14c',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Vanillite.Name',
    display_name='Vanillite',
    searchable_by=['Vanillite', 'Basic', 'Vanillite'],
    subtypes=['Basic'],
    collector_number=43,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=582,
    abilities=[
        Attack(
            title='Stiffen',
            game_text="During your opponent's next turn, any damage done to this Pokémon by attacks is reduced by 20 (after applying Weakness and Resistance).",
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Icy Snow',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
