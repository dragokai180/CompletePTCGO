from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='08f12d37-3f2e-528f-8d8d-07ebdf0941e7',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.GengarEX.Name',
    display_name='Gengar-EX',
    searchable_by=['Gengar-EX', 'Basic', 'EX', 'GengarEX'],
    subtypes=['Basic', 'EX'],
    collector_number=34,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=94,
    abilities=[
        Attack(
            title='Night Attack',
            game_text="Put 3 damage counters on 1 of your opponent's Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Dark Corridor',
            game_text="Your opponent's Active Pokémon is now Poisoned. Switch this Pokémon with 1 of your Benched Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
