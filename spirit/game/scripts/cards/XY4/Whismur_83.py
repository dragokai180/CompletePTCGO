from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f18d2292-427b-5803-b147-0731be9892d2',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Whismur.Name',
    display_name='Whismur',
    searchable_by=['Whismur', 'Basic', 'Whismur'],
    subtypes=['Basic'],
    collector_number=83,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=293,
    abilities=[
        Attack(
            title='Screaming Fit',
            game_text='Both Active Pokémon are now Confused.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
