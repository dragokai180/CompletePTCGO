from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d913eb06-cd3f-5895-9dea-1c89b97e6b28',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Deino.Name',
    display_name='Deino',
    searchable_by=['Deino', 'Basic', 'Deino'],
    subtypes=['Basic'],
    collector_number=97,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=633,
    abilities=[
        Attack(
            title='Gnaw',
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
        ),
        Attack(
            title='Headbutt',
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
