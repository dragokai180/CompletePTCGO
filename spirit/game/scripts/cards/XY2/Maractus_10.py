from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b6328748-aa4a-51c6-aab5-9e51b2c31d3a',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Maractus.Name',
    display_name='Maractus',
    searchable_by=['Maractus', 'Basic', 'Maractus'],
    subtypes=['Basic'],
    collector_number=10,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=556,
    abilities=[
        Attack(
            title='Exciting Shake',
            game_text="During your next turn, flip 6 coins instead of 2 for this Pokémon's Prickly Needles attack.",
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Prickly Needles',
            game_text='Flip 2 coins. This attack does 20 damage times the number of heads.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
