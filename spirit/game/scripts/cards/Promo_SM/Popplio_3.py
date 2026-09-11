from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6ac215f7-8681-5a3a-af23-de2169d5920a',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Popplio.Name',
    display_name='Popplio',
    searchable_by=['Popplio', 'Basic', 'Popplio'],
    subtypes=['Basic'],
    collector_number=3,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=728,
    abilities=[
        Attack(
            title='Sing',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
    ],
)
