from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='968ba725-740a-5a88-8a22-82ab01fd526d',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Numel.Name',
    display_name='Numel',
    searchable_by=['Numel', 'Basic', 'Numel'],
    subtypes=['Basic'],
    collector_number=12,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=322,
    abilities=[
        Attack(
            title='Tackle',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title='Combustion',
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)
