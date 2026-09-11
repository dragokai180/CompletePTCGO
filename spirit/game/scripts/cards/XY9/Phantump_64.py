from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='be722d9d-b3e2-56c6-8ebd-02ee849b954a',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Phantump.Name',
    display_name='Phantump',
    searchable_by=['Phantump', 'Basic', 'Phantump'],
    subtypes=['Basic'],
    collector_number=64,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=708,
    abilities=[
        Attack(
            title='Ascension',
            game_text='Search your deck for a card that evolves from this Pokémon and put it onto this Pokémon. (This counts as evolving this Pokémon.) Shuffle your deck afterward.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
