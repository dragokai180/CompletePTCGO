from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='45584802-e690-57cf-82ac-12be9d4d1298',
    key='XY6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bagon.Name',
    display_name='Bagon',
    searchable_by=['Bagon', 'Basic', 'Bagon'],
    subtypes=['Basic'],
    collector_number=55,
    set_code='XY6',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    family_id=371,
    abilities=[
        Attack(
            title='Leer',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Almost Flight',
            game_text='This Pokémon does 10 damage to itself.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
