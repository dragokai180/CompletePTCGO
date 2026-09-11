from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9ebd5aec-718f-5653-9822-620b506e1bb0',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Feebas.Name',
    display_name='Feebas',
    searchable_by=['Feebas', 'Basic', 'Feebas'],
    subtypes=['Basic'],
    collector_number=35,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=349,
    abilities=[
        Attack(
            title='Drawup Power',
            game_text='Search your deck for an Energy card, reveal it, and put it into your hand. Then, shuffle your deck.',
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
    ],
)
