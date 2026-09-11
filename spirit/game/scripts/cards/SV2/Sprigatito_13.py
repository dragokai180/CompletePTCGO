from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b159a236-ee2a-5e1a-8839-5b875093a3c7',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sprigatito.Name',
    display_name='Sprigatito',
    searchable_by=['Sprigatito', 'Basic', 'Sprigatito'],
    subtypes=['Basic'],
    collector_number=13,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=906,
    abilities=[
        Attack(
            title='Dig Claws',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
