from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f3149358-6159-5f46-ba2b-0cd4a48e2d26',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Geodude.Name',
    display_name='Geodude',
    searchable_by=['Geodude', 'Basic', 'Geodude'],
    subtypes=['Basic'],
    collector_number=45,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=74,
    abilities=[
        Attack(
            title='Rollout',
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
        Attack(
            title='Flail',
            game_text='This attack does 10 damage times the number of damage counters on this Pokémon.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
