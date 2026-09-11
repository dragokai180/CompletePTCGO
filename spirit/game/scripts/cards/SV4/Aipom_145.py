from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4097cefb-6d36-5501-88a9-dd2c154e4b5d',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Aipom.Name',
    display_name='Aipom',
    searchable_by=['Aipom', 'Basic', 'Aipom'],
    subtypes=['Basic'],
    collector_number=145,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=190,
    abilities=[
        Attack(
            title='Filch',
            game_text='Draw a card.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Smack',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
