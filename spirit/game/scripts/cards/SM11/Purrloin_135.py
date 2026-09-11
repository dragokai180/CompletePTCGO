from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='107ff3f7-be0b-5bd6-b988-b28468037856',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Purrloin.Name',
    display_name='Purrloin',
    searchable_by=['Purrloin', 'Basic', 'Purrloin'],
    subtypes=['Basic'],
    collector_number=135,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=509,
    abilities=[
        Attack(
            title='Cleaning Up',
            game_text="Discard a Pokémon Tool card from 1 of your opponent's Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
