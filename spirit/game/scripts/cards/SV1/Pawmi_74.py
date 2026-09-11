from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d5d4a814-debd-5903-b7df-1cb1b08d2d9c',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pawmi.Name',
    display_name='Pawmi',
    searchable_by=['Pawmi', 'Basic', 'Pawmi'],
    subtypes=['Basic'],
    collector_number=74,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=921,
    abilities=[
        Attack(
            title='Light Punch',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title='Zap Kick',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
