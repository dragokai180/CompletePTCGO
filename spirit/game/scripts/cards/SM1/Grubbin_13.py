from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b7075f0b-94b1-568d-b025-e5726b8f6458',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Grubbin.Name',
    display_name='Grubbin',
    searchable_by=['Grubbin', 'Basic', 'Grubbin'],
    subtypes=['Basic'],
    collector_number=13,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=736,
    abilities=[
        Attack(
            title='Vice Grip',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
