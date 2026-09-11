from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='32783b63-f8ed-58e7-8178-b1ccd10a9c55',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bellsprout.Name',
    display_name='Bellsprout',
    searchable_by=['Bellsprout', 'Basic', 'Bellsprout'],
    subtypes=['Basic'],
    collector_number=1,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=69,
    abilities=[
        Attack(
            title='Vine Whip',
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
        Attack(
            title='Knock Off',
            game_text="Discard a random card from your opponent's hand.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
