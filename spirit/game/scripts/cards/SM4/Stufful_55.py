from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='23257b47-73e4-59a4-b9f1-6b69d84fe0d8',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Stufful.Name',
    display_name='Stufful',
    searchable_by=['Stufful', 'Basic', 'Stufful'],
    subtypes=['Basic'],
    collector_number=55,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=759,
    abilities=[
        Attack(
            title='Flop',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
