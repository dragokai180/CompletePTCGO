from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1c26439f-614b-542b-bf39-c002f95e6ed3',
    key='XY12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Hitmonchan.Name',
    display_name='Hitmonchan',
    searchable_by=['Hitmonchan', 'Basic', 'Hitmonchan'],
    subtypes=['Basic'],
    collector_number=62,
    set_code='XY12',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=107,
    abilities=[
        Attack(
            title='Jab',
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
        ),
        Attack(
            title='Special Punch',
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
        ),
    ],
)
