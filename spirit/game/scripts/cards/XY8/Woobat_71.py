from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='bb19e3a7-3bf2-5422-ba81-5abd8adb81c9',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Woobat.Name',
    display_name='Woobat',
    searchable_by=['Woobat', 'Basic', 'Woobat'],
    subtypes=['Basic'],
    collector_number=71,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=527,
    abilities=[
        Attack(
            title='Odor Sleuth',
            game_text='Flip a coin. If heads, put a card from your discard pile into your hand.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Psyshot',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)
