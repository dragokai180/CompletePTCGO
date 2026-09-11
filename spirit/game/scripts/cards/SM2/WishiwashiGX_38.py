from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='da7ea9c3-a0f9-5708-bc7a-aeb7a079209a',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.WishiwashiGX.Name',
    display_name='Wishiwashi-GX',
    searchable_by=['Wishiwashi-GX', 'Basic', 'GX', 'WishiwashiGX'],
    subtypes=['Basic', 'GX'],
    collector_number=38,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=210,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=746,
    abilities=[
        Attack(
            title='Water Gun',
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
        Attack(
            title='Torrential Vortex',
            game_text="Discard a Special Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=standard_attack,
        ),
        Attack(
            title='Blue Surge-GX',
            game_text="Move all Energy from this Pokémon to your Benched Pokémon in any way you like. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 2},
            damage=220,
            effect=standard_attack,
            gx=True,
        ),
    ],
)
