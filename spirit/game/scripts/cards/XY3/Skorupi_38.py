from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='061dd2e9-0096-57f8-8d76-6de1a96a73fa',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Skorupi.Name',
    display_name='Skorupi',
    searchable_by=['Skorupi', 'Basic', 'Skorupi'],
    subtypes=['Basic'],
    collector_number=38,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=451,
    abilities=[
        Attack(
            title='Poison Sting',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Pierce',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
