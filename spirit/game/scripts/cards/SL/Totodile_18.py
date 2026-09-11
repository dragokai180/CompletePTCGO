from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4bad9923-e07f-5f10-870f-037926a878ab',
    key='SL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Totodile.Name',
    display_name='Totodile',
    searchable_by=['Totodile', 'Basic', 'Totodile'],
    subtypes=['Basic'],
    collector_number=18,
    set_code='SL',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=158,
    abilities=[
        Attack(
            title='Water Gun',
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
        Attack(
            title='Bite',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
