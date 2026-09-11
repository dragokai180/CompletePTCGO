from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='64ebe692-9f18-59ff-8900-9f75ad4dd1e9',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.KangaskhanGX.Name',
    display_name='Kangaskhan-GX',
    searchable_by=['Kangaskhan-GX', 'Basic', 'GX', 'KangaskhanGX'],
    subtypes=['Basic', 'GX'],
    collector_number=188,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=115,
    abilities=[
        Attack(
            title='Split Spiral Punch',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Enraged Strike',
            game_text="If your opponent's Active Pokémon is Confused, this attack does 80 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Familial Combo-GX',
            game_text="Draw 5 cards. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 3},
            damage=150,
            effect=standard_attack,
            gx=True,
        ),
    ],
)
