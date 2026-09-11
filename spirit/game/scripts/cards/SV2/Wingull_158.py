from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='751a555b-2959-5a79-bf1d-9fdc9d3d3f27',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Wingull.Name',
    display_name='Wingull',
    searchable_by=['Wingull', 'Basic', 'Wingull'],
    subtypes=['Basic'],
    collector_number=158,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=278,
    abilities=[
        Attack(
            title='Gust',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
