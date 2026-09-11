from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5b84415f-043f-5737-b83c-2bf57d8617ef',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Smoliv.Name',
    display_name='Smoliv',
    searchable_by=['Smoliv', 'Basic', 'Smoliv'],
    subtypes=['Basic'],
    collector_number=20,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=928,
    abilities=[
        Attack(
            title='Tackle',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
