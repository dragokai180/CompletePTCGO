from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3e741abd-b7ea-5ca1-a8c8-8652bd39e188',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Magmar.Name',
    display_name='Magmar',
    searchable_by=['Magmar', 'Basic', 'Magmar'],
    subtypes=['Basic'],
    collector_number=126,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=126,
    abilities=[
        Attack(
            title='Live Coal',
            cost={PokemonTypes.FIRE: 1},
            damage=10,
        ),
        Attack(
            title='Flare Combo',
            game_text='If Electabuzz is on your Bench, this attack does 80 more damage.',
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
