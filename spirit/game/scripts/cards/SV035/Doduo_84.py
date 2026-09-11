from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d93031f3-5da5-5fd0-a247-64097d7fc39c',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Doduo.Name',
    display_name='Doduo',
    searchable_by=['Doduo', 'Basic', 'Doduo'],
    subtypes=['Basic'],
    collector_number=84,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=84,
    abilities=[
        Attack(
            title='Reckless Charge',
            game_text='This Pokémon also does 10 damage to itself.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
