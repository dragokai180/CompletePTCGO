from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d155d25d-3de9-5fff-ab1a-bc061dcb5e51',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Nosepass.Name',
    display_name='Nosepass',
    searchable_by=['Nosepass', 'Basic', 'Nosepass'],
    subtypes=['Basic'],
    collector_number=107,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=299,
    abilities=[
        Attack(
            title='Iron Collecting',
            game_text='Put up to 2 Basic Metal Energy cards from your discard pile into your hand.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Rolling Tackle',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
