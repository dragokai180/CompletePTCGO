from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2bc43b87-bbf0-553f-b9a0-aa2f2882fdeb',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sandshrew.Name',
    display_name='Sandshrew',
    searchable_by=['Sandshrew', 'Basic', 'Sandshrew'],
    subtypes=['Basic'],
    collector_number=75,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=27,
    abilities=[
        Attack(
            title='Double Scratch',
            game_text='Flip 2 coins. This attack does 10 damage times the number of heads.',
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Sand Tomb',
            game_text="The Defending Pokémon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
