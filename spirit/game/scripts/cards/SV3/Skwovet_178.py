from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='309b7f6e-a253-5ca6-baaf-727a3dcc38d7',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Skwovet.Name',
    display_name='Skwovet',
    searchable_by=['Skwovet', 'Basic', 'Skwovet'],
    subtypes=['Basic'],
    collector_number=178,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=819,
    abilities=[
        Attack(
            title='Nicked Nibble',
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Gentle Slap',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
