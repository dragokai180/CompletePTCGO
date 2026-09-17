from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='24ba7665-7d33-515b-8e39-47c1944aef91',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Exeggcute.Name',
    display_name='Exeggcute',
    searchable_by=['Exeggcute', 'Basic', 'Exeggcute'],
    subtypes=['Basic'],
    collector_number=1,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=102,
    abilities=[
        Attack(
            title='Hypnosis',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
