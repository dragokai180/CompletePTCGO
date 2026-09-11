from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='15f3f958-9578-5c2c-a443-fb35ce322fc9',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.GardevoirEX.Name',
    display_name='Gardevoir-EX',
    searchable_by=['Gardevoir-EX', 'Basic', 'EX', 'GardevoirEX'],
    subtypes=['Basic', 'EX'],
    collector_number=105,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=282,
    abilities=[
        Attack(
            title='Life Leap',
            game_text="Heal from this Pokémon the same amount of damage you did to your opponent's Active Pokémon.",
            cost={PokemonTypes.FAIRY: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Shining Wind',
            game_text="During your opponent's next turn, this Pokémon has no Weakness.",
            cost={PokemonTypes.FAIRY: 3},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
