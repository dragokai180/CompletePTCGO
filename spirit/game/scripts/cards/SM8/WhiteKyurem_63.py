from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ee41f2c1-7713-530e-aa68-5063b1eebd24',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.WhiteKyurem.Name',
    display_name='White Kyurem',
    searchable_by=['White Kyurem', 'Basic', 'WhiteKyurem'],
    subtypes=['Basic'],
    collector_number=63,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=646,
    abilities=[
        Attack(
            title='Field Crush',
            game_text='If your opponent has a Stadium card in play, discard it.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Freezing Flames',
            game_text='If this Pokémon has any Fire Energy attached to it, this attack does 80 more damage.',
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
