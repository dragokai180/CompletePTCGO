from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9b2d8924-f631-53c2-ae67-5468bfefc1be',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Seel.Name',
    display_name='Seel',
    searchable_by=['Seel', 'Basic', 'Seel'],
    subtypes=['Basic'],
    collector_number=15,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=86,
    abilities=[
        Attack(
            title='Icy Snow',
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)
