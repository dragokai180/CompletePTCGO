from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='70ca16fb-b31d-5913-8a29-a2957bd86b4e',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.YveltalEX.Name',
    display_name='Yveltal-EX',
    searchable_by=['Yveltal-EX', 'Basic', 'EX', 'YveltalEX'],
    subtypes=['Basic', 'EX'],
    collector_number=79,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=717,
    abilities=[
        Attack(
            title='Evil Ball',
            game_text='This attack does 20 more damage times the amount of Energy attached to both Active Pokémon.',
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Y Cyclone',
            game_text='Move an Energy from this Pokémon to 1 of your Benched Pokémon.',
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=standard_attack,
        ),
    ],
)
