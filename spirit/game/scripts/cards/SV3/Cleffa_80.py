from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d572bd46-f55f-5524-a5f8-0bc9550a3598',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cleffa.Name',
    display_name='Cleffa',
    searchable_by=['Cleffa', 'Basic', 'Cleffa'],
    subtypes=['Basic'],
    collector_number=80,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=173,
    abilities=[
        Attack(
            title='Grasping Draw',
            game_text='Draw cards until you have 7 cards in your hand.',
            cost={},
            effect=standard_attack,
        ),
    ],
)
