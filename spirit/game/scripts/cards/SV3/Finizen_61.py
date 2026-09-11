from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c10bbb42-506e-5c19-a194-d2b447f02d38',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Finizen.Name',
    display_name='Finizen',
    searchable_by=['Finizen', 'Basic', 'Finizen'],
    subtypes=['Basic'],
    collector_number=61,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=963,
    abilities=[
        Attack(
            title='Tail Smack',
            cost={PokemonTypes.WATER: 2},
            damage=30,
        ),
    ],
)
