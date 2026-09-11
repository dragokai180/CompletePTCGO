from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c9d3eb28-07dd-5b42-ae2a-e1e2e954b327',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Karrablast.Name',
    display_name='Karrablast',
    searchable_by=['Karrablast', 'Basic', 'Karrablast'],
    subtypes=['Basic'],
    collector_number=8,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=588,
    abilities=[
        Attack(
            title='Peck',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title='Headbutt',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
