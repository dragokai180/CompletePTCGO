from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='cb62e152-5aa8-5adc-8518-1b60cca2bb5e',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pumpkaboo.Name',
    display_name='Pumpkaboo',
    searchable_by=['Pumpkaboo', 'Basic', 'Pumpkaboo'],
    subtypes=['Basic'],
    collector_number=77,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=710,
    abilities=[
        Attack(
            title='Seed Bomb',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
        Attack(
            title='Reckless Charge',
            game_text='This Pokémon also does 20 damage to itself.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=standard_attack,
        ),
    ],
)
