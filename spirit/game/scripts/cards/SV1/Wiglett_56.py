from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='cb0862c4-3dcb-5ec4-b193-6f20eff93f4d',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Wiglett.Name',
    display_name='Wiglett',
    searchable_by=['Wiglett', 'Basic', 'Wiglett'],
    subtypes=['Basic'],
    collector_number=56,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=960,
    abilities=[
        Attack(
            title='Dig a Little',
            game_text="Flip a coin. If heads, discard the top card of your opponent's deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Ram',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
