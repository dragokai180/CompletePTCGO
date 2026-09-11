from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='548b8f9b-5d74-5839-9328-725b43901270',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Litleo.Name',
    display_name='Litleo',
    searchable_by=['Litleo', 'Basic', 'Litleo'],
    subtypes=['Basic'],
    collector_number=19,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=667,
    abilities=[
        Attack(
            title='Fire Mane',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
