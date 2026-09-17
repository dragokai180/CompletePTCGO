from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b87b2f2f-4aea-596f-bf39-935cff70907a',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Kangaskhan.Name',
    display_name='Kangaskhan',
    searchable_by=['Kangaskhan', 'Basic', 'Kangaskhan'],
    subtypes=['Basic'],
    collector_number=114,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Common,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=115,
    abilities=[
        Attack(
            title='Rage',
            game_text='This attack does 10 more damage for each damage counter on this Pokémon.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Mega Punch',
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
