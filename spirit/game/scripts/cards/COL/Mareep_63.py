from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b492f69e-d32e-5eb4-9d0c-6386ff85137d',
    key='COL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Mareep.Name',
    display_name='Mareep',
    searchable_by=['Mareep', 'Basic', 'Mareep'],
    subtypes=['Basic'],
    collector_number=63,
    set_code='COL',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=179,
    abilities=[
        Attack(
            title='Static Shock',
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
        ),
    ],
)
