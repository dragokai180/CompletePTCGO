from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='96d0420c-0ce6-5c5b-8766-d0f0c81a1619',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Noibat.Name',
    display_name='Noibat',
    searchable_by=['Noibat', 'Basic', 'Noibat'],
    subtypes=['Basic'],
    collector_number=100,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
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
            title='Ram',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title='Destructive Sound',
            game_text='Your opponent reveals their hand. Discard all Item cards you find there.',
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
    ],
)
