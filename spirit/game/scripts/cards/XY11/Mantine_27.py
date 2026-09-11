from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5f42b244-b2e3-5479-8b77-6a02091f15e7',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Mantine.Name',
    display_name='Mantine',
    searchable_by=['Mantine', 'Basic', 'Mantine'],
    subtypes=['Basic'],
    collector_number=27,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=226,
    abilities=[
        Attack(
            title='Healing Wave',
            game_text='Discard as many cards as you like from your hand. Heal 10 damage from this Pokémon for each card you discarded in this way.',
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Dwindling Wave',
            game_text='This attack does 90 damage minus 10 damage for each damage counter on this Pokémon.',
            cost={PokemonTypes.WATER: 3},
            damage=90,
            damage_operator='-',
            effect=standard_attack,
        ),
    ],
)
