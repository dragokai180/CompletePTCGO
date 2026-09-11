from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d7835845-1f24-5a5d-8c46-6375b8a20f08',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Minun.Name',
    display_name='Minun',
    searchable_by=['Minun', 'Basic', 'Minun'],
    subtypes=['Basic'],
    collector_number=32,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=312,
    abilities=[
        Attack(
            title='Negative Discard',
            game_text='Put 2 basic Energy cards from your discard pile into your hand.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Static Shock',
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
        ),
    ],
)
