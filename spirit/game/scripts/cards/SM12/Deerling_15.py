from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f1088840-edb6-5807-9808-4331727d0c00',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Deerling.Name',
    display_name='Deerling',
    searchable_by=['Deerling', 'Basic', 'Deerling'],
    subtypes=['Basic'],
    collector_number=15,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=585,
    abilities=[
        Attack(
            title='Tackle',
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
    ],
)
