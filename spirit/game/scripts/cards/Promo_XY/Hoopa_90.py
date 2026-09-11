from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='83338d69-3f72-59c7-9403-0f795cea3be9',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Hoopa.Name',
    display_name='Hoopa',
    searchable_by=['Hoopa', 'Basic', 'Hoopa'],
    subtypes=['Basic'],
    collector_number=90,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=720,
    abilities=[
        Attack(
            title='Summoning Draw',
            game_text='If Pikachu is on your Bench, draw 3 cards.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Double Spin',
            game_text='Flip 2 coins. This attack does 30 damage times the number of heads.',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
