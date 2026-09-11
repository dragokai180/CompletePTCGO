from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='647befd6-4d46-5a38-9e91-1b77f303fe98',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.LaprasGX.Name',
    display_name='Lapras-GX',
    searchable_by=['Lapras-GX', 'Basic', 'GX', 'LaprasGX'],
    subtypes=['Basic', 'GX'],
    collector_number=35,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=190,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=131,
    abilities=[
        Attack(
            title='Collect',
            game_text='Draw 3 cards.',
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Blizzard Burn',
            game_text="This Pokémon can't attack during your next turn.",
            cost={PokemonTypes.WATER: 3},
            damage=160,
            effect=standard_attack,
        ),
        Attack(
            title='Ice Beam-GX',
            game_text="Your opponent's Active Pokémon is now Paralyzed. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=standard_attack,
            gx=True,
        ),
    ],
)
