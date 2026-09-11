from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a9c98a31-4f44-58c1-8ec3-46ac398db226',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Druddigon.Name',
    display_name='Druddigon',
    searchable_by=['Druddigon', 'Basic', 'Druddigon'],
    subtypes=['Basic'],
    collector_number=157,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    family_id=621,
    abilities=[
        Attack(
            title='Drag Off',
            game_text="Switch 1 of your opponent's Benched Pokémon with their Active Pokémon. This attack does 30 damage to the new Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
        Attack(
            title='Dragon Tail',
            game_text='Flip 2 coins. This attack does 100 damage for each heads.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
