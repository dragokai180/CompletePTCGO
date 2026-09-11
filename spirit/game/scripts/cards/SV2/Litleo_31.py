from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='bfc8d2c4-56e9-56e9-9a85-f56f609e70df',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Litleo.Name',
    display_name='Litleo',
    searchable_by=['Litleo', 'Basic', 'Litleo'],
    subtypes=['Basic'],
    collector_number=31,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=667,
    abilities=[
        Attack(
            title='Blazing Destruction',
            game_text='Discard a Stadium in play.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Live Coal',
            cost={PokemonTypes.FIRE: 1},
            damage=10,
        ),
    ],
)
