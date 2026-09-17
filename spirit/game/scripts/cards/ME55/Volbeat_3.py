from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f7483bb3-097a-535d-bce1-3a8cb1cb5f42',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Volbeat.Name',
    display_name='Volbeat',
    searchable_by=['Volbeat', 'Basic', 'Volbeat'],
    subtypes=['Basic'],
    collector_number=3,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=313,
    abilities=[
        Attack(
            title='Luring Glow',
            game_text="Switch in 1 of your opponent's Benched Pokémon to the Active Spot.",
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Bug Buzz',
            cost={PokemonTypes.COLORLESS: 3},
            damage=90,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
