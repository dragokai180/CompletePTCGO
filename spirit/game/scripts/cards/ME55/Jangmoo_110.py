from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a5ec6871-c977-5de3-a5d9-37d1862f434f',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Jangmoo.Name',
    display_name='Jangmo-o',
    searchable_by=['Jangmo-o', 'Basic', 'Jangmoo'],
    subtypes=['Basic'],
    collector_number=110,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=782,
    abilities=[
        Attack(
            title='Screech',
            game_text='During your next turn, the Defending Pokémon takes 30 more damage from attacks (after applying Weakness and Resistance).',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Dragon Claw',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.FIGHTING: 1},
            damage=40,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
