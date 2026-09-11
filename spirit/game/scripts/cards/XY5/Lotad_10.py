from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='82e3653d-a61a-582a-ba92-112cbe68a7e6',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Lotad.Name',
    display_name='Lotad',
    searchable_by=['Lotad', 'Basic', 'Lotad'],
    subtypes=['Basic'],
    collector_number=10,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=270,
    abilities=[
        Attack(
            title='Beat',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
