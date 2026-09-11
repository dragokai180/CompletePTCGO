from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d1224c0e-d598-5aa9-af7b-b5763b8ae3c4',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cosmog.Name',
    display_name='Cosmog',
    searchable_by=['Cosmog', 'Basic', 'Cosmog'],
    subtypes=['Basic'],
    collector_number=99,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=789,
    abilities=[
        Attack(
            title='Ascension',
            game_text='Search your deck for a card that evolves from this Pokémon and put it onto this Pokémon to evolve it. Then, shuffle your deck.',
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
    ],
)
