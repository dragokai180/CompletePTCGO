from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='62e4636a-f039-572e-9eac-2b27c5896d16',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Scatterbug.Name',
    display_name='Scatterbug',
    searchable_by=['Scatterbug', 'Basic', 'Scatterbug'],
    subtypes=['Basic'],
    collector_number=15,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=664,
    abilities=[
        Attack(
            title='Bug Bite',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
