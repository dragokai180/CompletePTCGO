from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5d793e35-766f-5455-8e09-650c8f06cb9f',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Remoraid.Name',
    display_name='Remoraid',
    searchable_by=['Remoraid', 'Basic', 'Remoraid'],
    subtypes=['Basic'],
    collector_number=33,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=223,
    abilities=[
        Attack(
            title='Sprinkle Water',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
