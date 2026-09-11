from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0256f5bf-d510-55ac-b163-175d42aed348',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Magmar.Name',
    display_name='Magmar',
    searchable_by=['Magmar', 'Basic', 'Magmar'],
    subtypes=['Basic'],
    collector_number=10,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=126,
    abilities=[
        Attack(
            title='Ram',
            cost={PokemonTypes.FIRE: 1},
            damage=10,
        ),
        Attack(
            title='Ember',
            game_text='Discard a Fire Energy attached to this Pokémon.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
