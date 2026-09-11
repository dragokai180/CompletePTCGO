from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c1e549a4-a9c4-57a5-b095-650fcfdbfbb6',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Rockruff.Name',
    display_name='Rockruff',
    searchable_by=['Rockruff', 'Basic', 'Rockruff'],
    subtypes=['Basic'],
    collector_number=116,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=744,
    abilities=[
        Attack(
            title='Bite',
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
        ),
    ],
)
