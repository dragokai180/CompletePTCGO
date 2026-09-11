from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ff13b1b3-6a40-553f-8fee-8a759138052d',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Toedscool.Name',
    display_name='Toedscool',
    searchable_by=['Toedscool', 'Basic', 'Toedscool'],
    subtypes=['Basic'],
    collector_number=25,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=948,
    abilities=[
        Attack(
            title='Spore',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Ram',
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
        ),
    ],
)
