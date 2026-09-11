from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e5a0f417-98ce-541d-810e-09ee2aa0b575',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Krabby.Name',
    display_name='Krabby',
    searchable_by=['Krabby', 'Basic', 'Krabby'],
    subtypes=['Basic'],
    collector_number=13,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=98,
    abilities=[
        Attack(
            title='Vice Grip',
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
        Attack(
            title='Crabhammer',
            cost={PokemonTypes.WATER: 3},
            damage=50,
        ),
    ],
)
