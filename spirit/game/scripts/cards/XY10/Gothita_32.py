from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a34b8d60-ffc5-535c-9f7c-8e594e0d06e8',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gothita.Name',
    display_name='Gothita',
    searchable_by=['Gothita', 'Basic', 'Gothita'],
    subtypes=['Basic'],
    collector_number=32,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=574,
    abilities=[
        Attack(
            title='Psybeam',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
