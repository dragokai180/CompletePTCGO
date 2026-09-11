from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='24bef80e-7d94-5e60-9f26-64d46e56a5c3',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Espurr.Name',
    display_name='Espurr',
    searchable_by=['Espurr', 'Basic', 'Espurr'],
    subtypes=['Basic'],
    collector_number=59,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=677,
    abilities=[
        Attack(
            title='Perplexing Eyes',
            game_text="The Defending Pokémon's Weakness is now Psychic until the end of your next turn. (The amount of Weakness doesn't change.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
