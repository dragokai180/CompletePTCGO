from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5dfc6b84-d5cb-52d0-88dd-8a444ee8620a',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sewaddle.Name',
    display_name='Sewaddle',
    searchable_by=['Sewaddle', 'Basic', 'Sewaddle'],
    subtypes=['Basic'],
    collector_number=5,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=540,
    abilities=[
        Attack(
            title='Nap',
            game_text='Heal 20 damage from this Pokémon.',
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Bug Bite',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
