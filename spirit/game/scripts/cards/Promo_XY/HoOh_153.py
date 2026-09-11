from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='03cad2ae-d04f-5fba-89a1-9090832badd5',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.HoOh.Name',
    display_name='Ho-Oh',
    searchable_by=['Ho-Oh', 'Basic', 'HoOh'],
    subtypes=['Basic'],
    collector_number=153,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=250,
    abilities=[
        Attack(
            title='Stoke',
            game_text='Flip a coin. If heads, search your deck for up to 2 Fire Energy cards and attach them to this Pokémon. Shuffle your deck afterward.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Fire Wing',
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)
