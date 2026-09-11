from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a02f868c-af86-5b44-9221-12a8368171e4',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Magnemite.Name',
    display_name='Magnemite',
    searchable_by=['Magnemite', 'Basic', 'Magnemite'],
    subtypes=['Basic'],
    collector_number=63,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=81,
    abilities=[
        Attack(
            title='Magnetic Switch',
            game_text='Switch this Pokémon with 1 of your Benched Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Electro Ball',
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
        ),
    ],
)
