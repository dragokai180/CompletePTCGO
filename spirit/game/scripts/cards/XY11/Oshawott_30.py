from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='46bd61e6-ce16-5750-b984-1d9bffdfad37',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Oshawott.Name',
    display_name='Oshawott',
    searchable_by=['Oshawott', 'Basic', 'Oshawott'],
    subtypes=['Basic'],
    collector_number=30,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=501,
    abilities=[
        Attack(
            title='Water Gun',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
