from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a44d0ef9-a383-5d02-b6a0-7bb0663b6a0e',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Drilbur.Name',
    display_name='Drilbur',
    searchable_by=['Drilbur', 'Basic', 'Drilbur'],
    subtypes=['Basic'],
    collector_number=118,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=529,
    abilities=[
        Attack(
            title='Dig Claws',
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
        ),
    ],
)
