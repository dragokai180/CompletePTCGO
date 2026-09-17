from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e5d0de0e-8635-552d-b41e-98c12d947bfa',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Snorlax.Name',
    display_name='Snorlax',
    searchable_by=['Snorlax', 'Basic', 'Snorlax'],
    subtypes=['Basic'],
    collector_number=119,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Common,
    hp=160,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=143,
    abilities=[
        Ability(
            title='Good Sleep',
            game_text='If this Pokémon remains Asleep during Pokémon Checkup, heal all damage from this Pokémon.',
            effect=standard_ability,
            trigger=Triggers.BETWEEN_TURNS,
        ),
        Attack(
            title='Collapse',
            game_text='This Pokémon is now Asleep.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=130,
            effect=standard_attack,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
