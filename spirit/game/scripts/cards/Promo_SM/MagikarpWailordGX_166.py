from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c606914f-e510-5a5f-865a-eba28f06f6f6',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MagikarpWailordGX.Name',
    display_name='Magikarp & Wailord-GX',
    searchable_by=['Magikarp & Wailord-GX', 'Basic', 'TAG TEAM', 'GX', 'MagikarpWailordGX'],
    subtypes=['Basic', 'TAG TEAM', 'GX'],
    collector_number=166,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=300,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=129,
    abilities=[
        Attack(
            title='Super Splash',
            cost={PokemonTypes.WATER: 5},
            damage=180,
        ),
        Attack(
            title='Towering Splash-GX',
            game_text="If this Pokémon has at least 7 extra Water Energy attached to it (in addition to this attack's cost), this attack does 100 damage to each of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.) (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            effect=standard_attack,
            gx=True,
        ),
    ],
)
