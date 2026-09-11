from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='37e66ea9-8063-5370-9ca7-bb0e230b2c65',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MewtwoEX.Name',
    display_name='Mewtwo-EX',
    searchable_by=['Mewtwo-EX', 'Basic', 'EX', 'MewtwoEX'],
    subtypes=['Basic', 'EX'],
    collector_number=62,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=150,
    abilities=[
        Attack(
            title='Shatter Shot',
            game_text='This attack does 30 damage times the amount of Psychic Energy attached to this Pokémon.',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Damage Change',
            game_text="Switch all damage counters on this Pokémon with those on your opponent's Active Pokémon.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
