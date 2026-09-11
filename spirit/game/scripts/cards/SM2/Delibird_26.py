from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='fed0f65d-a804-5bd2-aaa7-ad767c82c65a',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Delibird.Name',
    display_name='Delibird',
    searchable_by=['Delibird', 'Basic', 'Delibird'],
    subtypes=['Basic'],
    collector_number=26,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=225,
    abilities=[
        Attack(
            title='All the Presents',
            game_text='Flip a coin until you get tails. For each heads, you may search your deck for a card and put it into your hand. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Surprise Attack',
            game_text='Flip a coin. If tails, this attack does nothing.',
            cost={PokemonTypes.WATER: 1},
            damage=40,
            effect=standard_attack,
        ),
    ],
)
