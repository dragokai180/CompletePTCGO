from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9fb91925-4165-50e3-9f0d-abba7e1b0af5',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bronzor.Name',
    display_name='Bronzor',
    searchable_by=['Bronzor', 'Basic', 'Bronzor'],
    subtypes=['Basic'],
    collector_number=144,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=436,
    abilities=[
        Attack(
            title='Mirror Draw',
            game_text='Draw cards until you have the same number of cards in your hand as your opponent.',
            cost={PokemonTypes.METAL: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Speed Dive',
            cost={PokemonTypes.METAL: 2},
            damage=30,
        ),
    ],
)
