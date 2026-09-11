from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='55a6f948-3fe5-591b-accf-a4fb76440662',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Trapinch.Name',
    display_name='Trapinch',
    searchable_by=['Trapinch', 'Basic', 'Trapinch'],
    subtypes=['Basic'],
    collector_number=53,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=328,
    abilities=[
        Attack(
            title='Mountain Munch',
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Mud-Slap',
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
        ),
    ],
)
