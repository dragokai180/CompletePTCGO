from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b7c88007-b26c-505b-bd9b-6880f3fb8047',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MrMime.Name',
    display_name='Mr. Mime',
    searchable_by=['Mr. Mime', 'Basic', 'MrMime'],
    subtypes=['Basic'],
    collector_number=97,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=122,
    abilities=[
        Ability(
            title='Bench Barrier',
            game_text='Prevent all damage done to your Benched Pokémon by attacks.',
            passive=standard_passive('Prevent all damage done to your Benched Pokémon by attacks.'),
        ),
        Attack(
            title='Juggling',
            game_text='Flip 4 coins. This attack does 10 damage times the number of heads.',
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
