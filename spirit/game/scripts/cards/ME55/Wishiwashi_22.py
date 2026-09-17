from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='edff681d-76f9-50a6-8a4f-0068751c0a0e',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Wishiwashi.Name',
    display_name='Wishiwashi',
    searchable_by=['Wishiwashi', 'Basic', 'Wishiwashi'],
    subtypes=['Basic'],
    collector_number=22,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=746,
    abilities=[
        Ability(
            title='Counterattack Grouping',
            game_text="If your Wishiwashi or Wishiwashi ex is in the Active Spot and is damaged by an attack from your opponent's Pokémon (even if your Pokémon is Knocked Out), place 3 damage counters on the Attacking Pokémon.",
            effect=standard_ability,
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
        ),
        Attack(
            title='Surprise Attack',
            game_text='Flip a coin. If tails, this attack does nothing.',
            cost={PokemonTypes.WATER: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
