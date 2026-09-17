from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0b4c9808-58ae-5704-9aef-2e06ed8d110c',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name',
    display_name='Pikachu',
    searchable_by=['Pikachu', 'Basic', 'Pikachu'],
    subtypes=['Basic'],
    collector_number=50,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=25,
    abilities=[
        Attack(
            title='Satisfied Spark',
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
