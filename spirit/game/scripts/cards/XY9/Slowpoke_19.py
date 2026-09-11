from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8c1eddcf-1111-5efa-9dc5-8e6d07b72fdc',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name',
    display_name='Slowpoke',
    searchable_by=['Slowpoke', 'Basic', 'Slowpoke'],
    subtypes=['Basic'],
    collector_number=19,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=79,
    abilities=[
        Attack(
            title='Headbutt',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title='Tail Lure',
            game_text='Search your deck for a Pokémon, reveal it, and put it into your hand. Shuffle your deck afterward.',
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
    ],
)
