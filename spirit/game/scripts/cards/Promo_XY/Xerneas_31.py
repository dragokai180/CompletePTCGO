from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b6757a74-b697-5942-97b3-2a8332d6e9b8',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Xerneas.Name',
    display_name='Xerneas',
    searchable_by=['Xerneas', 'Basic', 'Xerneas'],
    subtypes=['Basic'],
    collector_number=31,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=716,
    abilities=[
        Attack(
            title='Aurora Gain',
            game_text="During your opponent's next turn, this Pokémon has no weakness.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=standard_attack,
        ),
        Attack(
            title='Light of Life',
            game_text='If your opponent has Yveltal (including Yveltal-EX) in play, this attack does 40 more damage.',
            cost={PokemonTypes.FAIRY: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
