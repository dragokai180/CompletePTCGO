from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d1dc84ef-6ed5-5ef8-af56-5651a8484ce5',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Hoppip.Name',
    display_name='Hoppip',
    searchable_by=['Hoppip', 'Basic', 'Hoppip'],
    subtypes=['Basic'],
    collector_number=3,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=187,
    abilities=[
        Attack(
            title='Splash',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
