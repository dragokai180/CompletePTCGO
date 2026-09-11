from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='849da797-6d6b-5fad-bdf7-b406a6701921',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.GarchompEX.Name',
    display_name='Garchomp-EX',
    searchable_by=['Garchomp-EX', 'Basic', 'EX', 'GarchompEX'],
    subtypes=['Basic', 'EX'],
    collector_number=9,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=170,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    family_id=445,
    abilities=[
        Attack(
            title='Dual Chop',
            game_text='Flip 2 coins. This attack does 30 damage times the number of heads.',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Power Blast',
            game_text='Discard an Energy attached to this Pokémon.',
            cost={PokemonTypes.WATER: 1, PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
