from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='300c3344-1df1-54e2-9441-fb3dbd59248e',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dialga.Name',
    display_name='Dialga',
    searchable_by=['Dialga', 'Basic', 'Dialga'],
    subtypes=['Basic'],
    collector_number=77,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=483,
    abilities=[
        Attack(
            title='Metal Claw',
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title='Time Freeze',
            game_text="Your opponent can't play any Pokémon from his or her hand to evolve the Defending Pokémon during his or her next turn.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
