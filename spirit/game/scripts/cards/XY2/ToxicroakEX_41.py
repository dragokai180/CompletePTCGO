from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ecc7dfe1-f2bb-53e4-90cc-a1b39368e9f8',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.ToxicroakEX.Name',
    display_name='Toxicroak-EX',
    searchable_by=['Toxicroak-EX', 'Basic', 'EX', 'ToxicroakEX'],
    subtypes=['Basic', 'EX'],
    collector_number=41,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=454,
    abilities=[
        Attack(
            title='Triple Poison',
            game_text="Your opponent's Active Pokémon is now Poisoned. Put 3 damage counters instead of 1 on that Pokémon between turns.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
        Attack(
            title='Smash Uppercut',
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
