from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='537f78bf-a2c2-5a04-8b4a-c487e1c3bf7c',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Houndour.Name',
    display_name='Houndour',
    searchable_by=['Houndour', 'Basic', 'Houndour'],
    subtypes=['Basic'],
    collector_number=132,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=228,
    abilities=[
        Attack(
            title='Bite',
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
        ),
        Attack(
            title='Darkness Fang',
            cost={PokemonTypes.DARKNESS: 3},
            damage=70,
        ),
    ],
)
