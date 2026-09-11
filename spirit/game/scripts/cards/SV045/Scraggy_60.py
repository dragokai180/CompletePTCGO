from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='cf68efe6-cb2b-5d7d-ba5a-c491606f4fc7',
    key='SV045',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Scraggy.Name',
    display_name='Scraggy',
    searchable_by=['Scraggy', 'Basic', 'Scraggy'],
    subtypes=['Basic'],
    collector_number=60,
    set_code='SV045',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=559,
    abilities=[
        Attack(
            title='Low Kick',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title='Headstrike',
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
