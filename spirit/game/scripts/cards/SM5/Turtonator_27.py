from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f02df417-b6a9-519a-9e47-38fa518110ca',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Turtonator.Name',
    display_name='Turtonator',
    searchable_by=['Turtonator', 'Basic', 'Turtonator'],
    subtypes=['Basic'],
    collector_number=27,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=776,
    abilities=[
        Attack(
            title='Searing Flame',
            game_text="Your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
            effect=standard_attack,
        ),
        Attack(
            title='Steam Artillery',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 3},
            damage=100,
        ),
    ],
)
