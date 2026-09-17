from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='877e4b7d-0ad8-5302-9ff6-de9f536d7292',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Toxel.Name',
    display_name='Toxel',
    searchable_by=['Toxel', 'Basic', 'Toxel'],
    subtypes=['Basic'],
    collector_number=58,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=848,
    abilities=[
        Attack(
            title='Ram',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
