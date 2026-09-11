from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2675dd2b-2434-5014-999d-d3d2b8d501d3',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Mareep.Name',
    display_name='Mareep',
    searchable_by=['Mareep', 'Basic', 'Mareep'],
    subtypes=['Basic'],
    collector_number=66,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=179,
    abilities=[
        Attack(
            title='Static Shock',
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
        ),
        Attack(
            title='Electro Ball',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)
