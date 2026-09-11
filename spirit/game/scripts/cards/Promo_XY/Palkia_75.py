from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='31423115-7a86-5916-bac8-e2065fb9af70',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Palkia.Name',
    display_name='Palkia',
    searchable_by=['Palkia', 'Basic', 'Palkia'],
    subtypes=['Basic'],
    collector_number=75,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=484,
    abilities=[
        Attack(
            title='Wave Splash',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title='Cross Slicer',
            game_text="Your opponent can't attach Energy from his or her hand to the Defending Pokémon during his or her next turn.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
