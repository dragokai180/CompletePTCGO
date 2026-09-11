from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='eba78726-1eff-5652-a08e-93729df8d18d',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Froakie.Name',
    display_name='Froakie',
    searchable_by=['Froakie', 'Basic', 'Froakie'],
    subtypes=['Basic'],
    collector_number=46,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=656,
    abilities=[
        Attack(
            title='Pound',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
