from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6ce8c6a3-5f21-5f1a-9996-b7808559cb9b',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Feebas.Name',
    display_name='Feebas',
    searchable_by=['Feebas', 'Basic', 'Feebas'],
    subtypes=['Basic'],
    collector_number=22,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=349,
    abilities=[
        Attack(
            title='Surprise Attack',
            game_text='Flip a coin. If tails, this attack does nothing.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
