from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='805fd15d-e506-5c64-9b06-5dc796bfe34d',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Drifloon.Name',
    display_name='Drifloon',
    searchable_by=['Drifloon', 'Basic', 'Drifloon'],
    subtypes=['Basic'],
    collector_number=73,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=425,
    abilities=[
        Attack(
            title='Float Up',
            game_text='You may shuffle this Pokémon and all attached cards into your deck.',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
