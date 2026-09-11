from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='06ac3dbd-dc58-5ced-8239-8ebcff2c2a8a',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Horsea.Name',
    display_name='Horsea',
    searchable_by=['Horsea', 'Basic', 'Horsea'],
    subtypes=['Basic'],
    collector_number=30,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=116,
    abilities=[
        Attack(
            title='Hook',
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
    ],
)
