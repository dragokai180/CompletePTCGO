from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='272a086a-1307-508c-b232-bb3b52cb7340',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Druddigon.Name',
    display_name='Druddigon',
    searchable_by=['Druddigon', 'Basic', 'Druddigon'],
    subtypes=['Basic'],
    collector_number=83,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    family_id=621,
    abilities=[
        Attack(
            title='Proud Fang',
            game_text='If your opponent has any Pokémon BREAK in play, this attack does 60 more damage.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Giga Claw',
            game_text='Flip 2 coins. If both of them are tails, this attack does nothing.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
