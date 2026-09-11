from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='77230816-eec5-52f0-bf28-084bb0180f79',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Minccino.Name',
    display_name='Minccino',
    searchable_by=['Minccino', 'Basic', 'Minccino'],
    subtypes=['Basic'],
    collector_number=87,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=572,
    abilities=[
        Attack(
            title='Tail Smack',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
