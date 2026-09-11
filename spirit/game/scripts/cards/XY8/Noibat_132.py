from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='61585493-b07d-54d0-9b6f-cc302bb2b88b',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Noibat.Name',
    display_name='Noibat',
    searchable_by=['Noibat', 'Basic', 'Noibat'],
    subtypes=['Basic'],
    collector_number=132,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=714,
    abilities=[
        Attack(
            title='Mysterious Beam',
            game_text="Flip a coin. If heads, discard an Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Gust',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
