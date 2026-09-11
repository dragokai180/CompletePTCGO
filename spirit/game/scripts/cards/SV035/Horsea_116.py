from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='50a62828-e569-52d2-adcf-490d6128a5a2',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Horsea.Name',
    display_name='Horsea',
    searchable_by=['Horsea', 'Basic', 'Horsea'],
    subtypes=['Basic'],
    collector_number=116,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=116,
    abilities=[
        Attack(
            title='Rain Splash',
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
        Attack(
            title='Sharp Fin',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)
