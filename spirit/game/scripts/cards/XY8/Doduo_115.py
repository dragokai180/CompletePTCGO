from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='02a34259-9805-5963-a54c-3531e9d0bb16',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Doduo.Name',
    display_name='Doduo',
    searchable_by=['Doduo', 'Basic', 'Doduo'],
    subtypes=['Basic'],
    collector_number=115,
    set_code='XY8',
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
    family_id=84,
    abilities=[
        Attack(
            title='Simultaneous Peck',
            game_text='Flip 2 coins. If either of them is tails, this attack does nothing.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Doduo Delivery',
            game_text='Draw 2 cards.',
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
    ],
)
