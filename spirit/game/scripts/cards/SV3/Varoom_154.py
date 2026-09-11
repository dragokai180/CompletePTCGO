from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3f867b88-8b5b-517e-a55c-117f7eb1c645',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Varoom.Name',
    display_name='Varoom',
    searchable_by=['Varoom', 'Basic', 'Varoom'],
    subtypes=['Basic'],
    collector_number=154,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=965,
    abilities=[
        Attack(
            title='Spinning Draw',
            game_text='Draw a card.',
            cost={PokemonTypes.METAL: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
