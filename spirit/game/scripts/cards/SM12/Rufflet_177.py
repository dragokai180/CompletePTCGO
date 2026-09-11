from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5447b463-bb14-5d57-adf5-f239b90e1c57',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Rufflet.Name',
    display_name='Rufflet',
    searchable_by=['Rufflet', 'Basic', 'Rufflet'],
    subtypes=['Basic'],
    collector_number=177,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=627,
    abilities=[
        Attack(
            title='Fury Attack',
            game_text='Flip 3 coins. This attack does 10 damage for each heads.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
