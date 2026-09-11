from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4f734449-1138-5247-971b-c43f654f4ca5',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cyndaquil.Name',
    display_name='Cyndaquil',
    searchable_by=['Cyndaquil', 'Basic', 'Cyndaquil'],
    subtypes=['Basic'],
    collector_number=40,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=155,
    abilities=[
        Attack(
            title='Hammer In',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
