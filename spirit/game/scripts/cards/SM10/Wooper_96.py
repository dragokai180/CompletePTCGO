from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='86ff7ea8-819c-5a32-aaaf-9832b6cb4af2',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Wooper.Name',
    display_name='Wooper',
    searchable_by=['Wooper', 'Basic', 'Wooper'],
    subtypes=['Basic'],
    collector_number=96,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=194,
    abilities=[
        Attack(
            title='Mud Bomb',
            cost={PokemonTypes.WATER: 2},
            damage=30,
        ),
    ],
)
