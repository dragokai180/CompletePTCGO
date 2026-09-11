from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='77e6c1a8-ccaa-5077-9228-18122ec96190',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.PalkiaGX.Name',
    display_name='Palkia-GX',
    searchable_by=['Palkia-GX', 'Basic', 'GX', 'PalkiaGX'],
    subtypes=['Basic', 'GX'],
    collector_number=20,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=484,
    abilities=[
        Attack(
            title='Spatial Control',
            game_text='Move any number of Energy from your Benched Pokémon to this Pokémon.',
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Hydro Pressure',
            game_text='This attack does 20 more damage times the amount of Water Energy attached to this Pokémon.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Zero Vanish-GX',
            game_text="Shuffle all Energy from each of your opponent's Pokémon into their deck. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=standard_attack,
            gx=True,
        ),
    ],
)
