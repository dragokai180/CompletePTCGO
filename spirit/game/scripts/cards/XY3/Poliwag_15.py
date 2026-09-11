from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='19ae782f-68dc-5c29-ad44-dee2e9755a10',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Poliwag.Name',
    display_name='Poliwag',
    searchable_by=['Poliwag', 'Basic', 'Poliwag'],
    subtypes=['Basic'],
    collector_number=15,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=60,
    abilities=[
        Attack(
            title='Rain Splash',
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
        Attack(
            title='Spiral Current',
            game_text="Your opponent's Active Pokémon is now Confused. That Pokémon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
