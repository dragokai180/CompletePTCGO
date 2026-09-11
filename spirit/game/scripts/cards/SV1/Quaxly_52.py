from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='040f5bb4-8573-562d-8ab5-d48019f81a21',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Quaxly.Name',
    display_name='Quaxly',
    searchable_by=['Quaxly', 'Basic', 'Quaxly'],
    subtypes=['Basic'],
    collector_number=52,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=912,
    abilities=[
        Attack(
            title='Pound',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title='Kick',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
