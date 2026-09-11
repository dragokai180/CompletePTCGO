from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6576c9f8-d833-54b4-8089-47b7d06a74f9',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.HoopaEX.Name',
    display_name='Hoopa-EX',
    searchable_by=['Hoopa-EX', 'Basic', 'EX', 'HoopaEX'],
    subtypes=['Basic', 'EX'],
    collector_number=85,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=720,
    abilities=[
        Attack(
            title='Hyperspace Ring',
            game_text='Search your deck for up to 2 Item cards, reveal them, and put them into your hand. Shuffle your deck afterward.',
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Wonder Trick',
            game_text='Your opponent switches his or her Active Pokémon with 1 of his or her Benched Pokémon.',
            cost={PokemonTypes.PSYCHIC: 3},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
