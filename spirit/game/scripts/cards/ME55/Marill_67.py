from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='66b1dfd1-a0a7-5dcb-838e-ebb5bc8444c7',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Marill.Name',
    display_name='Marill',
    searchable_by=['Marill', 'Basic', 'Marill'],
    subtypes=['Basic'],
    collector_number=67,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=183,
    abilities=[
        Attack(
            title='Tackle',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
