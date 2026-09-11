from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='cbefbef1-dd51-5a72-8e6d-1e0031829cdf',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Spinarak.Name',
    display_name='Spinarak',
    searchable_by=['Spinarak', 'Basic', 'Spinarak'],
    subtypes=['Basic'],
    collector_number=9,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=167,
    abilities=[
        Attack(
            title='Spider Scram',
            game_text="Your opponent's Active Pokémon is now Paralyzed and Poisoned. Put this Pokémon and all cards attached to it in the Lost Zone.",
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Sting',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
