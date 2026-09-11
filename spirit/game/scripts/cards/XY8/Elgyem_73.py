from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='efd8c7aa-05b8-5bd4-be06-03bb2b2724a1',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Elgyem.Name',
    display_name='Elgyem',
    searchable_by=['Elgyem', 'Basic', 'Elgyem'],
    subtypes=['Basic'],
    collector_number=73,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=605,
    abilities=[
        Attack(
            title='Psych Up',
            game_text="During your next turn, this Pokémon's Psych Up attack does 20 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
