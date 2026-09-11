from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c3f30c40-7658-5bf0-a09c-62fa0a4739e4',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Greavard.Name',
    display_name='Greavard',
    searchable_by=['Greavard', 'Basic', 'Greavard'],
    subtypes=['Basic'],
    collector_number=105,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=971,
    abilities=[
        Attack(
            title='Underworld Stroll',
            game_text='Your opponent reveals their hand. Choose a Supporter card you find there and put it on the bottom of their deck.',
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
        Attack(
            title='Sharp Fang',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
