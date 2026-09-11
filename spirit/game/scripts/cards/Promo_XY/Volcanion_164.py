from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e9dd8f19-3486-5dcc-a02f-c1da284a4bc2',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Volcanion.Name',
    display_name='Volcanion',
    searchable_by=['Volcanion', 'Basic', 'Volcanion'],
    subtypes=['Basic'],
    collector_number=164,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=721,
    abilities=[
        Attack(
            title='Concentrated Fire',
            game_text='Flip a coin for each Fire Energy attached to this Pokémon. This attack does 50 damage times the number of heads.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Combustion Impact',
            game_text='Your opponent switches his or her Active Pokémon with 1 of his or her Benched Pokémon.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 3},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
