from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='19443795-9720-5374-9c00-0e78358b6fe3',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Fennekin.Name',
    display_name='Fennekin',
    searchable_by=['Fennekin', 'Basic', 'Fennekin'],
    subtypes=['Basic'],
    collector_number=14,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=653,
    abilities=[
        Attack(
            title='Ember',
            game_text='Discard an Energy from this Pokémon.',
            cost={PokemonTypes.FIRE: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
