from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='eee6d599-5ca5-506f-9499-ee890af3b11a',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cosmog.Name',
    display_name='Cosmog',
    searchable_by=['Cosmog', 'Basic', 'Cosmog'],
    subtypes=['Basic'],
    collector_number=78,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=789,
    abilities=[
        Attack(
            title='Splash',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
