from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d57298fb-7f96-52dc-9e32-6878f8f17dc6',
    key='SL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Litten.Name',
    display_name='Litten',
    searchable_by=['Litten', 'Basic', 'Litten'],
    subtypes=['Basic'],
    collector_number=15,
    set_code='SL',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=725,
    abilities=[
        Attack(
            title='Live Coal',
            cost={PokemonTypes.FIRE: 1},
            damage=20,
        ),
    ],
)
