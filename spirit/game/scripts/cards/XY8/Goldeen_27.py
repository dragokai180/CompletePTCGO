from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c00ec746-3d79-5098-b25e-8b8757237d18',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Goldeen.Name',
    display_name='Goldeen',
    searchable_by=['Goldeen', 'Basic', 'Goldeen'],
    subtypes=['Basic'],
    collector_number=27,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=118,
    abilities=[
        Attack(
            title='Reckless Charge',
            game_text='This Pokémon does 10 damage to itself.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
