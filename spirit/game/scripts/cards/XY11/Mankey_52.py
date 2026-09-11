from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f51ebb74-9244-59d5-a1ca-f868eafe0e1e',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Mankey.Name',
    display_name='Mankey',
    searchable_by=['Mankey', 'Basic', 'Mankey'],
    subtypes=['Basic'],
    collector_number=52,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=56,
    abilities=[
        Attack(
            title='Focus Energy',
            game_text="During your next turn, this Pokémon's Flop attack's base damage is 50.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Flop',
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
    ],
)
