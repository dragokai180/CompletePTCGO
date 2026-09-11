from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='edd1fbcd-0456-5cfe-97af-433dd89623fe',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Swinub.Name',
    display_name='Swinub',
    searchable_by=['Swinub', 'Basic', 'Swinub'],
    subtypes=['Basic'],
    collector_number=19,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=220,
    abilities=[
        Attack(
            title='Gnaw',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
