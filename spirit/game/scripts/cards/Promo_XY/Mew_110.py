from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ec0d792a-3173-545e-a062-eb7c2f738676',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Mew.Name',
    display_name='Mew',
    searchable_by=['Mew', 'Basic', 'Mew'],
    subtypes=['Basic'],
    collector_number=110,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=151,
    abilities=[
        Attack(
            title='Clairvoyance',
            game_text='Your opponent reveals his or her hand.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Psychic',
            game_text="This attack does 10 more damage for each Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
