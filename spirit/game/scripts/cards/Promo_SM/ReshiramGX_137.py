from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d406bd43-81a2-5c6c-9a3a-bf65d2018e56',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.ReshiramGX.Name',
    display_name='Reshiram-GX',
    searchable_by=['Reshiram-GX', 'Basic', 'GX', 'ReshiramGX'],
    subtypes=['Basic', 'GX'],
    collector_number=137,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=643,
    abilities=[
        Attack(
            title='Flame Charge',
            game_text='Search your deck for up to 2 Fire Energy cards and attach them to this Pokémon. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Scorching Column',
            game_text="Your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.FIRE: 3, PokemonTypes.COLORLESS: 1},
            damage=110,
            effect=standard_attack,
        ),
        Attack(
            title='Vermilion-GX',
            game_text="You may attach up to 5 Fire Energy cards from your hand to your Pokémon in any way you like. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIRE: 3, PokemonTypes.COLORLESS: 1},
            damage=180,
            effect=standard_attack,
            gx=True,
        ),
    ],
)
