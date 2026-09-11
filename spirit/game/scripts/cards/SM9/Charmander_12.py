from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c9f8ea93-6806-5596-b6fb-3c874683fcd0',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Charmander.Name',
    display_name='Charmander',
    searchable_by=['Charmander', 'Basic', 'Charmander'],
    subtypes=['Basic'],
    collector_number=12,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=4,
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
