from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b9b8d821-9e45-59c6-8a95-fa1a930f2a1b',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Zacian.Name',
    display_name='Zacian',
    searchable_by=['Zacian', 'Basic', 'Zacian'],
    subtypes=['Basic'],
    collector_number=106,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=888,
    abilities=[
        Attack(
            title='Hardened Blade',
            game_text='If this Pokémon has a Pokémon Tool attached, this attack does 40 more damage.',
            cost={PokemonTypes.METAL: 1},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Slashing Strike',
            game_text="During your next turn, this Pokémon can't use Slashing Strike",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=standard_attack,
            locks_next_turn=True,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
