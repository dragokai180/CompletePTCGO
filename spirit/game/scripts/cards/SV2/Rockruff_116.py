from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='602b01c3-b0e7-5a67-b98a-4368865ef8e8',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Rockruff.Name',
    display_name='Rockruff',
    searchable_by=['Rockruff', 'Basic', 'Rockruff'],
    subtypes=['Basic'],
    collector_number=116,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=744,
    abilities=[
        Attack(
            title='Rock Throw',
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
        Attack(
            title='Bite',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)
