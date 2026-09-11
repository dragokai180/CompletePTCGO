from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e9e4d801-30d3-53e3-8e65-06ad41a5b728',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Espurr.Name',
    display_name='Espurr',
    searchable_by=['Espurr', 'Basic', 'Espurr'],
    subtypes=['Basic'],
    collector_number=58,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=677,
    abilities=[
        Attack(
            title='Scratch',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
