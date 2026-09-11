from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d8801d07-dfba-5877-aa8f-0f0c225462fd',
    key='SV045',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Woobat.Name',
    display_name='Woobat',
    searchable_by=['Woobat', 'Basic', 'Woobat'],
    subtypes=['Basic'],
    collector_number=32,
    set_code='SV045',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=527,
    abilities=[
        Attack(
            title='Reckless Charge',
            game_text='This Pokémon also does 10 damage to itself.',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
